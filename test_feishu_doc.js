/**
 * 飞书云文档创建测试脚本
 * 使用方法：
 * 1. 先设置环境变量（运行 set_feishu_env.ps1）
 * 2. 执行：node test_feishu_doc.js
 */

const https = require('https');

// 从环境变量读取配置
const appId = process.env.FEISHU_APP_ID;
const appSecret = process.env.FEISHU_APP_SECRET;
const folderToken = process.env.FEISHU_FOLDER_TOKEN || '';

console.log('=== 飞书云文档创建测试 ===\n');

// 检查环境变量
if (!appId || !appSecret) {
    console.log('❌ 错误：环境变量未设置');
    console.log('请先运行以下命令设置环境变量：');
    console.log('  .\\set_feishu_env.ps1');
    console.log('\n或手动设置：');
    console.log('  $env:FEISHU_APP_ID = "你的App ID"');
    console.log('  $env:FEISHU_APP_SECRET = "你的App Secret"');
    process.exit(1);
}

console.log('✓ 环境变量检查通过');
console.log(`  App ID: ${appId}`);
console.log(`  App Secret: ${appSecret.substring(0, 10)}...`);
if (folderToken) {
    console.log(`  Folder Token: ${folderToken}`);
}
console.log();

// 步骤1：获取 tenant_access_token
console.log('步骤1/3：获取访问令牌...');

const tokenData = JSON.stringify({
    app_id: appId,
    app_secret: appSecret
});

const tokenOptions = {
    hostname: 'open.feishu.cn',
    port: 443,
    path: '/open-apis/auth/v3/tenant_access_token/internal',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(tokenData)
    }
};

const tokenReq = https.request(tokenOptions, (tokenRes) => {
    let tokenBody = '';
    tokenRes.on('data', (chunk) => { tokenBody += chunk; });
    tokenRes.on('end', () => {
        try {
            const tokenJson = JSON.parse(tokenBody);
            const accessToken = tokenJson.tenant_access_token;
            const code = tokenJson.code;

            if (code !== 0) {
                console.log('❌ 获取令牌失败');
                console.log(`  错误码：${code}`);
                console.log(`  错误信息：${tokenJson.msg}`);
                return;
            }

            if (!accessToken) {
                console.log('❌ 未收到访问令牌');
                console.log(`  响应：${JSON.stringify(tokenJson)}`);
                return;
            }

            console.log('✓ 访问令牌获取成功');
            console.log(`  Token: ${accessToken.substring(0, 20)}...`);
            console.log();

            // 步骤2：创建文档
            console.log('步骤2/3：创建飞书文档...');

            const createData = {
                title: '测试文档 - 海洋AI日报',
                folder_token: folderToken
            };

            const createOptions = {
                hostname: 'open.feishu.cn',
                port: 443,
                path: '/open-apis/docx/v1/documents',
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${accessToken}`,
                    'Content-Type': 'application/json',
                    'Content-Length': Buffer.byteLength(JSON.stringify(createData))
                }
            };

            const createReq = https.request(createOptions, (createRes) => {
                let createBody = '';
                createRes.on('data', (chunk) => { createBody += chunk; });
                createRes.on('end', () => {
                    try {
                        const createJson = JSON.parse(createBody);
                        const documentId = createJson?.data?.document?.document_id;
                        const createCode = createJson.code;

                        if (createCode !== 0) {
                            console.log('❌ 创建文档失败');
                            console.log(`  错误码：${createCode}`);
                            console.log(`  错误信息：${createJson.msg}`);
                            return;
                        }

                        if (!documentId) {
                            console.log('❌ 未收到文档ID');
                            console.log(`  响应：${JSON.stringify(createJson)}`);
                            return;
                        }

                        const docUrl = `https://docs.feishu.cn/docx/${documentId}`;
                        console.log('✓ 文档创建成功！');
                        console.log(`  文档ID：${documentId}`);
                        console.log(`  文档URL：${docUrl}`);
                        console.log();

                        // 步骤3：添加文档内容
                        console.log('步骤3/3：添加文档内容...');

                        const blockData = {
                            children: [
                                {
                                    block_type: 1,
                                    paragraph: {
                                        elements: [
                                            {
                                                text_run: {
                                                    content: '这是由 WorkBuddy 自动创建的测试文档'
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    block_type: 1,
                                    paragraph: {
                                        elements: [
                                            {
                                                text_run: {
                                                    content: '海洋AI技术日报正在运行中...'
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    block_type: 13,
                                    heading_3: {
                                        style: {},
                                        elements: [
                                            {
                                                text_run: {
                                                    content: '测试成功！'
                                                }
                                            }
                                        ]
                                    }
                                }
                            ],
                            index: -1
                        };

                        const blockOptions = {
                            hostname: 'open.feishu.cn',
                            port: 443,
                            path: `/open-apis/docx/v1/documents/${documentId}/blocks/batch_create`,
                            method: 'POST',
                            headers: {
                                'Authorization': `Bearer ${accessToken}`,
                                'Content-Type': 'application/json',
                                'Content-Length': Buffer.byteLength(JSON.stringify(blockData))
                            }
                        };

                        const blockReq = https.request(blockOptions, (blockRes) => {
                            let blockBody = '';
                            blockRes.on('data', (chunk) => { blockBody += chunk; });
                            blockRes.on('end', () => {
                                try {
                                    const blockJson = JSON.parse(blockBody);
                                    console.log('✓ 文档内容添加成功');
                                    console.log();
                                    console.log('=== 测试完成 ===');
                                    console.log('🎉 恭喜！飞书云文档配置成功！');
                                    console.log(`📄 查看文档：${docUrl}`);
                                    console.log();
                                    console.log('现在您可以运行日报自动化任务了，文档将自动创建。');
                                } catch (e) {
                                    console.log('⚠️ 添加内容时出现错误（不影响文档创建）');
                                    console.log(`  错误：${e.message}`);
                                    console.log();
                                    console.log('=== 测试完成 ===');
                                    console.log('✓ 文档已创建，但内容添加可能失败');
                                    console.log(`📄 查看文档：${docUrl}`);
                                }
                            });
                        });

                        blockReq.on('error', (e) => {
                            console.log('⚠️ 添加内容请求失败（不影响文档创建）');
                            console.log(`  错误：${e.message}`);
                            console.log();
                            console.log('=== 测试完成 ===');
                            console.log('✓ 文档已创建，但内容添加可能失败');
                            console.log(`📄 查看文档：${docUrl}`);
                        });

                        blockReq.write(JSON.stringify(blockData));
                        blockReq.end();

                    } catch (e) {
                        console.log('❌ 解析创建结果失败');
                        console.log(`  错误：${e.message}`);
                        console.log(`  响应：${createBody}`);
                    }
                });
            });

            createReq.on('error', (e) => {
                console.log('❌ 创建文档请求失败');
                console.log(`  错误：${e.message}`);
            });

            createReq.write(JSON.stringify(createData));
            createReq.end();

        } catch (e) {
            console.log('❌ 解析令牌响应失败');
            console.log(`  错误：${e.message}`);
            console.log(`  响应：${tokenBody}`);
        }
    });
});

tokenReq.on('error', (e) => {
    console.log('❌ 获取令牌请求失败');
    console.log(`  错误：${e.message}`);
});

tokenReq.write(tokenData);
tokenReq.end();
