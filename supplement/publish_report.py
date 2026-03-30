import requests, os, json, smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y年%m月%d日')
date_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
html_path = f'C:/Users/Administrator/WorkBuddy/Claw/daily_reports/海洋AI简报_{date_str}.html'

print(f'处理日期: {yesterday}')
print(f'HTML文件: {html_path}')
print()

doc_url = None

# ========== 第三步：发布到飞书云文档 ==========
print('=== 第三步：创建飞书云文档 ===')
app_id = os.environ.get('FEISHU_APP_ID')
app_secret = os.environ.get('FEISHU_APP_SECRET')
folder_token = os.environ.get('FEISHU_FOLDER_TOKEN', '')

if not app_id or not app_secret:
    print('警告：飞书应用配置未设置，跳过飞书文档创建')
else:
    try:
        # 获取 tenant_access_token
        token_resp = requests.post('https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
            json={'app_id': app_id, 'app_secret': app_secret})
        token_data = token_resp.json()
        access_token = token_data.get('tenant_access_token')

        if not access_token:
            print(f'获取token失败: {token_data}')
        else:
            # 创建飞书文档
            headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
            doc_title = f'海洋AI技术日报 · {yesterday}'

            create_payload = {'title': doc_title}
            if folder_token:
                create_payload['folder_token'] = folder_token

            create_resp = requests.post(
                'https://open.feishu.cn/open-apis/docx/v1/documents',
                headers=headers,
                json=create_payload
            )
            doc_data = create_resp.json()
            document_id = doc_data.get('data', {}).get('document', {}).get('document_id')

            if document_id:
                doc_url = f'https://docs.feishu.cn/docx/{document_id}'
                print(f'飞书文档创建成功：{doc_url}')
                print(f'Document ID: {document_id}')
            else:
                print(f'文档创建失败: {doc_data}')
    except Exception as e:
        print(f'飞书文档创建异常: {str(e)}')

print()

# ========== 第四步：飞书机器人消息推送 ==========
print('=== 第四步：飞书机器人消息推送 ===')
webhook_url = os.environ.get('FEISHU_WEBHOOK_URL')

if not webhook_url:
    print('警告：飞书 Webhook 未配置，跳过消息推送')
else:
    try:
        card_content = {
            'msg_type': 'interactive',
            'card': {
                'header': {
                    'title': {'tag': 'plain_text', 'content': f'🌊 海洋AI技术日报 · {yesterday}'},
                    'template': 'blue'
                },
                'elements': [
                    {'tag': 'div', 'text': {'tag': 'lark_md', 'content': '**今日涵盖主题：**\n🤖 海洋人工智能 | 🔄 数字孪生 | 📊 可视化 | ✅ 数据质量 | ⚙️ 数据处理'}},
                    {'tag': 'hr'},
                    {'tag': 'div', 'text': {'tag': 'lark_md', 'content': f'📄 **完整简报（飞书文档）：**\n{doc_url if doc_url else "文档创建失败，请查看本地文件"}'}},
                    {'tag': 'hr'},
                    {'tag': 'note', 'elements': [{'tag': 'plain_text', 'content': '由 WorkBuddy 自动生成 · 每日09:00推送'}]}
                ]
            }
        }
        resp = requests.post(webhook_url, json=card_content)
        print(f'飞书消息推送结果：{resp.json()}')
    except Exception as e:
        print(f'飞书消息推送异常: {str(e)}')

print()

# ========== 第五步：发送邮件 ==========
print('=== 第五步：发送邮件 ===')
sender = os.environ.get('REPORT_EMAIL_SENDER')
password = os.environ.get('REPORT_EMAIL_PASSWORD')
smtp_server = os.environ.get('REPORT_EMAIL_SMTP', 'smtp.163.com')
smtp_port = int(os.environ.get('REPORT_EMAIL_SMTP_PORT', '465'))

if not sender or not password:
    print('警告：邮件配置未设置，跳过邮件发送')
else:
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'海洋AI技术日报 · {yesterday}'
        msg['From'] = sender
        msg['To'] = 'sutiany@163.com'

        doc_link_html = f'<p style="margin: 15px 0;"><strong>📄 <a href="{doc_url}" style="color: #0066cc;">点击查看飞书云文档版本</a></strong></p>' if doc_url else ''

        with open(html_path, 'r', encoding='utf-8') as f:
            html_body = f.read()

        # 在HTML头部插入飞书文档链接
        html_body = html_body.replace('<div class="content">', f'<div class="content">{doc_link_html}')

        msg.attach(MIMEText(html_body, 'html', 'utf-8'))

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender, password)
            server.sendmail(sender, ['sutiany@163.com'], msg.as_string())
        print('邮件发送成功')
    except Exception as e:
        print(f'邮件发送异常: {str(e)}')

print()
print('=== 任务执行完成 ===')
