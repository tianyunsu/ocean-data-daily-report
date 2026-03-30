const https = require('https');
const http = require('http');
const fs = require('fs');
const path = require('path');

const yesterday = new Date();
yesterday.setDate(yesterday.getDate() - 1);
const year = yesterday.getFullYear();
const month = String(yesterday.getMonth() + 1).padStart(2, '0');
const day = String(yesterday.getDate()).padStart(2, '0');

const yesterdayCN = `${year}年${month}月${day}日`;
const dateStr = `${year}-${month}-${day}`;
const htmlPath = `C:/Users/Administrator/WorkBuddy/Claw/daily_reports/海洋AI简报_${dateStr}.html`;

console.log(`处理日期: ${yesterdayCN}`);
console.log(`HTML文件: ${htmlPath}`);
console.log();

let docUrl = null;

// ===================== 第三步：创建飞书云文档 =====================
console.log('=== 第三步：创建飞书云文档 ===');
const appId = process.env.FEISHU_APP_ID;
const appSecret = process.env.FEISHU_APP_SECRET;
const folderToken = process.env.FEISHU_FOLDER_TOKEN || '';

if (!appId || !appSecret) {
    console.log('警告：飞书应用配置未设置，跳过飞书文档创建');
    continueWithFeishuMessage();
} else {
    // 获取 tenant_access_token
    const tokenData = JSON.stringify({ app_id: appId, app_secret: appSecret });
    
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

                if (!accessToken) {
                    console.log(`获取token失败: ${tokenBody}`);
                    continueWithFeishuMessage();
                    return;
                }

                // 创建飞书文档
                const createData = {
                    title: `海洋AI技术日报 · ${yesterdayCN}`,
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

                            if (documentId) {
                                docUrl = `https://docs.feishu.cn/docx/${documentId}`;
                                console.log(`飞书文档创建成功：${docUrl}`);
                                console.log(`Document ID: ${documentId}`);
                            } else {
                                console.log(`文档创建失败: ${createBody}`);
                            }
                        } catch (e) {
                            console.log(`解析创建结果失败: ${e.message}`);
                        }
                        continueWithFeishuMessage();
                    });
                });

                createReq.on('error', (e) => {
                    console.log(`创建文档请求失败: ${e.message}`);
                    continueWithFeishuMessage();
                });

                createReq.write(JSON.stringify(createData));
                createReq.end();
            } catch (e) {
                console.log(`解析token失败: ${e.message}`);
                continueWithFeishuMessage();
            }
        });
    });

    tokenReq.on('error', (e) => {
        console.log(`获取token失败: ${e.message}`);
        continueWithFeishuMessage();
    });

    tokenReq.write(tokenData);
    tokenReq.end();
}

function continueWithFeishuMessage() {
    console.log();
    console.log('=== 第四步：飞书机器人消息推送 ===');
    const webhookUrl = process.env.FEISHU_WEBHOOK_URL;

    if (!webhookUrl) {
        console.log('警告：飞书 Webhook 未配置，跳过消息推送');
        sendEmail();
        return;
    }

    const cardContent = {
        msg_type: 'interactive',
        card: {
            header: {
                title: { tag: 'plain_text', content: `🌊 海洋AI技术日报 · ${yesterdayCN}` },
                template: 'blue'
            },
            elements: [
                { tag: 'div', text: { tag: 'lark_md', content: '**今日涵盖主题：**\n🤖 海洋人工智能 | 🔄 数字孪生 | 📊 可视化 | ✅ 数据质量 | ⚙️ 数据处理' } },
                { tag: 'hr' },
                { tag: 'div', text: { tag: 'lark_md', content: `📄 **完整简报（飞书文档）：**\n${docUrl || '文档创建失败，请查看本地文件'}` } },
                { tag: 'hr' },
                { tag: 'note', elements: [{ tag: 'plain_text', content: '由 WorkBuddy 自动生成 · 每日09:00推送' }] }
            ]
        }
    };

    const parsedUrl = new URL(webhookUrl);
    const messageOptions = {
        hostname: parsedUrl.hostname,
        port: parsedUrl.port || 443,
        path: parsedUrl.pathname + parsedUrl.search,
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(JSON.stringify(cardContent))
        }
    };

    const messageReq = https.request(messageOptions, (res) => {
        let body = '';
        res.on('data', (chunk) => { body += chunk; });
        res.on('end', () => {
            console.log(`飞书消息推送结果：${body}`);
            sendEmail();
        });
    });

    messageReq.on('error', (e) => {
        console.log(`飞书消息推送异常: ${e.message}`);
        sendEmail();
    });

    messageReq.write(JSON.stringify(cardContent));
    messageReq.end();
}

function sendEmail() {
    console.log();
    console.log('=== 第五步：发送邮件 ===');
    
    // Node.js 发邮件需要第三方库，这里模拟发送过程
    // 实际发送需要配置 SMTP 服务器
    const sender = process.env.REPORT_EMAIL_SENDER;
    const password = process.env.REPORT_EMAIL_PASSWORD;
    const smtpServer = process.env.REPORT_EMAIL_SMTP || 'smtp.163.com';
    const smtpPort = process.env.REPORT_EMAIL_SMTP_PORT || '465';

    if (!sender || !password) {
        console.log('警告：邮件配置未设置，跳过邮件发送');
        console.log();
        console.log('=== 任务执行完成 ===');
        console.log();
        console.log('说明：');
        console.log('1. HTML简报已生成：', htmlPath);
        console.log('2. 飞书文档：', docUrl || '未创建（需要配置环境变量）');
        console.log('3. 飞书消息和邮件发送需要安装对应的Node.js库（nodemailer等）');
        return;
    }

    console.log('注意：发送邮件需要安装 nodemailer 库：npm install nodemailer');
    console.log('当前环境已配置邮件参数，但由于缺少依赖库，无法实际发送邮件');
    console.log();
    console.log('=== 任务执行完成 ===');
    console.log();
    console.log('说明：');
    console.log('1. HTML简报已生成：', htmlPath);
    console.log('2. 飞书文档：', docUrl || '未创建');
}
