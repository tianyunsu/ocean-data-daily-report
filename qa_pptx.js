// QA: 用JSZip读取pptx内容，验证每张幻灯片文字
const fs = require('fs');
const JSZip = require('./node_modules/jszip');

async function main() {
  const buf = fs.readFileSync('推动海洋经济高质量发展.pptx');
  const zip = await JSZip.loadAsync(buf);

  // 找所有幻灯片xml
  const slideFiles = Object.keys(zip.files)
    .filter(f => f.match(/^ppt\/slides\/slide\d+\.xml$/))
    .sort((a, b) => {
      const na = parseInt(a.match(/\d+/)[0]);
      const nb = parseInt(b.match(/\d+/)[0]);
      return na - nb;
    });

  console.log(`共发现 ${slideFiles.length} 张幻灯片\n`);

  for (const sf of slideFiles) {
    const xml = await zip.files[sf].async('string');
    // 提取所有<a:t>文本节点
    const texts = [];
    const re = /<a:t[^>]*>([^<]+)<\/a:t>/g;
    let m;
    while ((m = re.exec(xml)) !== null) {
      const t = m[1].trim();
      if (t) texts.push(t);
    }
    const slideNum = sf.match(/\d+/)[0];
    console.log(`[Slide ${slideNum.padStart(2,'0')}] 文本片段数: ${texts.length}`);
    // 打印前5个文本片段
    texts.slice(0, 6).forEach(t => console.log(`  · ${t.slice(0,60)}`));
    console.log('');
  }
}

main().catch(e => console.error(e));
