const https = require('https');
const fs = require('fs');

const urls = [
  { url: 'https://mp.weixin.qq.com/s/0kjTWsbhrNyWKquDF5Tj6g', file: 'wx_article_1.html' },
  { url: 'https://mp.weixin.qq.com/s/ez-eFuUj350VzWZR5mvO3g', file: 'wx_article_2.html' }
];

function fetchUrl(urlStr, outputFile) {
  return new Promise((resolve, reject) => {
    const options = {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'zh-CN,zh;q=0.9'
      }
    };
    
    https.get(urlStr, options, (res) => {
      let data = '';
      // Handle redirect
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        console.log(`Redirecting to: ${res.headers.location}`);
        fetchUrl(res.headers.location, outputFile).then(resolve).catch(reject);
        return;
      }
      res.setEncoding('utf8');
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        fs.writeFileSync(outputFile, data, 'utf8');
        console.log(`Saved ${outputFile}, length: ${data.length}`);
        resolve(data);
      });
    }).on('error', reject);
  });
}

(async () => {
  for (const { url, file } of urls) {
    try {
      await fetchUrl(url, file);
    } catch(e) {
      console.error(`Failed: ${e.message}`);
    }
  }
})();
