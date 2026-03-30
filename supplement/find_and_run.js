// Python not available (Store stub), use Node.js implementation directly
console.log('Using Node.js implementation...');
runWithNode();

function runWithNode() {
  const https = require('https');
  const http = require('http');
  const fs = require('fs');
  const tls = require('tls');

  const appId = process.env.FEISHU_APP_ID;
  const appSecret = process.env.FEISHU_APP_SECRET;
  const webhookUrl = process.env.FEISHU_WEBHOOK_URL;
  const emailSender = process.env.REPORT_EMAIL_SENDER;
  const emailPass = process.env.REPORT_EMAIL_PASSWORD;

  const now = new Date();
  const yesterday = new Date(now - 86400000);
  const yy = yesterday.getFullYear();
  const mm = String(yesterday.getMonth()+1).padStart(2,'0');
  const dd = String(yesterday.getDate()).padStart(2,'0');
  const yesterdayStr = `${yy}年${mm}月${dd}日`;
  const dateStr = `${yy}-${mm}-${dd}`;

  console.log(`Target date: ${yesterdayStr}`);

  // Step 3: Feishu Doc
  console.log('\n[Step 3] Feishu Document...');
  let docUrl = null;

  if (!appId || !appSecret) {
    console.log('Warning: FEISHU_APP_ID/FEISHU_APP_SECRET not set, skipping Feishu doc');
    step4(docUrl);
    return;
  }

  const tokenBody = JSON.stringify({app_id: appId, app_secret: appSecret});
  const tokenReq = https.request({
    hostname: 'open.feishu.cn',
    path: '/open-apis/auth/v3/tenant_access_token/internal',
    method: 'POST',
    headers: {'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(tokenBody)}
  }, res => {
    let data = '';
    res.on('data', c => data += c);
    res.on('end', () => {
      try {
        const j = JSON.parse(data);
        const token = j.tenant_access_token;
        if (!token) { console.log('Failed to get token:', j); step4(null); return; }
        const folderToken = process.env.FEISHU_FOLDER_TOKEN || '';
        const docBody = JSON.stringify({title: `海洋AI技术日报 · ${yesterdayStr}`, folder_token: folderToken});
        const docReq = https.request({
          hostname: 'open.feishu.cn',
          path: '/open-apis/docx/v1/documents',
          method: 'POST',
          headers: {'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(docBody)}
        }, r2 => {
          let d2 = '';
          r2.on('data', c => d2 += c);
          r2.on('end', () => {
            try {
              const j2 = JSON.parse(d2);
              const docId = j2.data && j2.data.document && j2.data.document.document_id;
              docUrl = docId ? `https://docs.feishu.cn/docx/${docId}` : null;
              if (docUrl) console.log('Feishu doc created:', docUrl);
              else console.log('Feishu doc creation failed:', j2);
            } catch(e) { console.log('Parse error:', e.message); }
            step4(docUrl);
          });
        });
        docReq.on('error', e => { console.log('Doc request error:', e.message); step4(null); });
        docReq.write(docBody);
        docReq.end();
      } catch(e) { console.log('Token parse error:', e.message); step4(null); }
    });
  });
  tokenReq.on('error', e => { console.log('Token request error:', e.message); step4(null); });
  tokenReq.write(tokenBody);
  tokenReq.end();

  function step4(docUrl) {
    console.log('\n[Step 4] Feishu Webhook...');
    if (!webhookUrl) { console.log('Warning: FEISHU_WEBHOOK_URL not set, skipping'); step5(docUrl); return; }
    const docLine = docUrl ? docUrl : 'Doc creation failed, check local file';
    const card = {
      msg_type: 'interactive',
      card: {
        header: {title: {tag:'plain_text', content:`🌊 海洋AI技术日报 · ${yesterdayStr}`}, template:'blue'},
        elements: [
          {tag:'div', text:{tag:'lark_md', content:'**今日涵盖主题：**\n🤖 海洋人工智能 | 🔄 数字孪生 | 📊 可视化 | ✅ 数据质量 | ⚙️ 数据处理'}},
          {tag:'hr'},
          {tag:'div', text:{tag:'lark_md', content:`📄 **完整简报（飞书文档）：**\n${docLine}`}},
          {tag:'hr'},
          {tag:'note', elements:[{tag:'plain_text', content:'由 WorkBuddy 自动生成 · 每日09:00推送'}]}
        ]
      }
    };
    const wBody = JSON.stringify(card);
    const wUrl = new URL(webhookUrl);
    const wReq = https.request({
      hostname: wUrl.hostname,
      path: wUrl.pathname + wUrl.search,
      method: 'POST',
      headers: {'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(wBody)}
    }, r => {
      let d = '';
      r.on('data', c => d += c);
      r.on('end', () => { console.log('Feishu webhook result:', d); step5(docUrl); });
    });
    wReq.on('error', e => { console.log('Webhook error:', e.message); step5(docUrl); });
    wReq.write(wBody);
    wReq.end();
  }

  function step5(docUrl) {
    console.log('\n[Step 5] Email...');
    if (!emailSender || !emailPass) { console.log('Warning: REPORT_EMAIL_SENDER/REPORT_EMAIL_PASSWORD not set, skipping'); done(); return; }
    const smtpServer = process.env.REPORT_EMAIL_SMTP || 'smtp.163.com';
    const smtpPort = parseInt(process.env.REPORT_EMAIL_SMTP_PORT || '465');
    const htmlPath = `C:/Users/Administrator/WorkBuddy/Claw/daily_reports/海洋AI简报_${dateStr}.html`;
    let htmlBody = fs.readFileSync(htmlPath, 'utf8');
    const docLink = docUrl ? `<p style="margin:10px 0">📄 <a href="${docUrl}" style="color:#2e86c1">点击查看飞书云文档版本</a></p>` : '';
    htmlBody = htmlBody.replace('<body>', `<body>${docLink}`);
    const boundary = '----=_Part_' + Date.now();
    const subject = `=?UTF-8?B?${Buffer.from('海洋AI技术日报 · '+yesterdayStr).toString('base64')}?=`;
    const fromName = `=?UTF-8?B?${Buffer.from('海洋AI日报').toString('base64')}?=`;
    const msg = [
      `From: ${fromName} <${emailSender}>`,
      `To: sutiany@163.com`,
      `Subject: ${subject}`,
      `MIME-Version: 1.0`,
      `Content-Type: multipart/alternative; boundary="${boundary}"`,
      '',
      `--${boundary}`,
      `Content-Type: text/html; charset=utf-8`,
      `Content-Transfer-Encoding: base64`,
      '',
      Buffer.from(htmlBody).toString('base64'),
      '',
      `--${boundary}--`
    ].join('\r\n');

    const socket = tls.connect({host: smtpServer, port: smtpPort}, () => {
      let buf = '';
      let step = 0;
      socket.on('data', d => {
        buf += d.toString();
        const lines = buf.split('\r\n');
        buf = lines.pop();
        for (const line of lines) {
          if (!line) continue;
          const code = parseInt(line.substring(0,3));
          if (step===0 && code===220) { socket.write('EHLO localhost\r\n'); step=1; }
          else if (step===1 && (code===220||code===250)) {
            if (line.startsWith('250 ') || line.startsWith('220 ')) {
              socket.write(`AUTH LOGIN\r\n`); step=2;
            }
          }
          else if (step===2 && code===334) { socket.write(Buffer.from(emailSender).toString('base64')+'\r\n'); step=3; }
          else if (step===3 && code===334) { socket.write(Buffer.from(emailPass).toString('base64')+'\r\n'); step=4; }
          else if (step===4 && code===235) { socket.write(`MAIL FROM:<${emailSender}>\r\n`); step=5; }
          else if (step===5 && code===250) { socket.write(`RCPT TO:<sutiany@163.com>\r\n`); step=6; }
          else if (step===6 && code===250) { socket.write('DATA\r\n'); step=7; }
          else if (step===7 && code===354) { socket.write(msg+'\r\n.\r\n'); step=8; }
          else if (step===8 && code===250) { console.log('Email sent successfully'); socket.write('QUIT\r\n'); done(); }
          else if (code>=400) { console.log('SMTP error:', line); socket.destroy(); done(); }
        }
      });
      socket.on('error', e => { console.log('Socket error:', e.message); done(); });
    });
    socket.on('error', e => { console.log('TLS connect error:', e.message); done(); });
  }

  function done() {
    console.log('\n== All steps completed ==');
  }
}
