import requests, os, json, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y年%m月%d日')
date_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

print(f'== 目标日期: {yesterday} ({date_str}) ==')

# ======== 第三步：飞书云文档 ========
print('\n[第三步] 飞书云文档...')
app_id = os.environ.get('FEISHU_APP_ID')
app_secret = os.environ.get('FEISHU_APP_SECRET')
folder_token = os.environ.get('FEISHU_FOLDER_TOKEN', '')
doc_url = None

if not app_id or not app_secret:
    print('警告：飞书应用配置未设置（FEISHU_APP_ID/FEISHU_APP_SECRET），跳过飞书文档创建')
else:
    try:
        token_resp = requests.post(
            'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
            json={'app_id': app_id, 'app_secret': app_secret}, timeout=10)
        access_token = token_resp.json().get('tenant_access_token')
        if not access_token:
            print(f'警告：获取 tenant_access_token 失败: {token_resp.json()}')
        else:
            headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
            doc_title = f'海洋AI技术日报 · {yesterday}'
            create_payload = {'title': doc_title, 'folder_token': folder_token}
            create_resp = requests.post(
                'https://open.feishu.cn/open-apis/docx/v1/documents',
                headers=headers, json=create_payload, timeout=10)
            doc_data = create_resp.json()
            document_id = doc_data.get('data', {}).get('document', {}).get('document_id')
            doc_url = f'https://docs.feishu.cn/docx/{document_id}' if document_id else None
            if doc_url:
                print(f'飞书文档创建成功：{doc_url}')
            else:
                print(f'飞书文档创建失败: {doc_data}')
    except Exception as e:
        print(f'警告：飞书文档创建异常: {e}')

# ======== 第四步：飞书机器人消息 ========
print('\n[第四步] 飞书机器人消息推送...')
webhook_url = os.environ.get('FEISHU_WEBHOOK_URL')
if not webhook_url:
    print('警告：飞书 Webhook 未配置（FEISHU_WEBHOOK_URL），跳过消息推送')
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
                    {'tag': 'div', 'text': {'tag': 'lark_md',
                        'content': '**今日涵盖主题：**\n🤖 海洋人工智能 | 🔄 数字孪生 | 📊 可视化 | ✅ 数据质量 | ⚙️ 数据处理 | 🗄️ 数据管理与共享 | 🚢 开放航次/船时共享'}},
                    {'tag': 'hr'},
                    {'tag': 'div', 'text': {'tag': 'lark_md',
                        'content': f'📄 **完整简报（飞书文档）：**\n{doc_url if doc_url else "文档创建失败，请查看本地文件"}'}},
                    {'tag': 'hr'},
                    {'tag': 'note', 'elements': [{'tag': 'plain_text', 'content': '由 WorkBuddy 自动生成 · 每日09:00推送'}]}
                ]
            }
        }
        resp = requests.post(webhook_url, json=card_content, timeout=10)
        print(f'飞书消息推送结果：{resp.json()}')
    except Exception as e:
        print(f'警告：飞书消息推送异常: {e}')

# ======== 第五步：邮件发送 ========
print('\n[第五步] 发送邮件...')
sender = os.environ.get('REPORT_EMAIL_SENDER')
password = os.environ.get('REPORT_EMAIL_PASSWORD')
smtp_server = os.environ.get('REPORT_EMAIL_SMTP', 'smtp.163.com')
smtp_port = int(os.environ.get('REPORT_EMAIL_SMTP_PORT', '465'))

if not sender or not password:
    print('警告：邮件配置未设置（REPORT_EMAIL_SENDER/REPORT_EMAIL_PASSWORD），跳过邮件发送')
else:
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'海洋AI技术日报 · {yesterday}'
        msg['From'] = sender
        msg['To'] = 'sutiany@163.com'
        doc_link_html = (f'<p style="margin:10px 0">📄 <a href="{doc_url}" style="color:#2e86c1">'
                         f'点击查看飞书云文档版本</a></p>') if doc_url else ''
        html_path = f'C:/Users/Administrator/WorkBuddy/Claw/daily_reports/海洋AI简报_{date_str}.html'
        with open(html_path, 'r', encoding='utf-8') as f:
            html_body = f.read()
        html_body = html_body.replace('<body>', f'<body>{doc_link_html}')
        msg.attach(MIMEText(html_body, 'html', 'utf-8'))
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender, password)
            server.sendmail(sender, ['sutiany@163.com'], msg.as_string())
        print('邮件发送成功')
    except Exception as e:
        print(f'警告：邮件发送异常: {e}')

print('\n== 所有步骤执行完毕 ==')
