// 更深层QA：检查是否有问题字符/空文本框
const fs = require('fs');
const JSZip = require('./node_modules/jszip');

async function main() {
  const buf = fs.readFileSync('推动海洋经济高质量发展.pptx');
  const zip = await JSZip.loadAsync(buf);

  const slideFiles = Object.keys(zip.files)
    .filter(f => f.match(/^ppt\/slides\/slide\d+\.xml$/))
    .sort((a,b) => parseInt(a.match(/\d+/)[0]) - parseInt(b.match(/\d+/)[0]));

  let issues = [];

  for (const sf of slideFiles) {
    const xml = await zip.files[sf].async('string');
    const slideNum = parseInt(sf.match(/\d+/)[0]);

    // 检测 &amp;quot; （双重转义，会显示为 &quot;）
    if (xml.includes('&amp;quot;')) {
      issues.push(`Slide ${slideNum}: 含 &amp;quot; 双重转义`);
    }

    // 检测空文本框 <a:t></a:t>
    const emptyCount = (xml.match(/<a:t><\/a:t>/g) || []).length;
    if (emptyCount > 0) {
      issues.push(`Slide ${slideNum}: ${emptyCount} 个空文本段`);
    }
  }

  if (issues.length === 0) {
    console.log('✅ 未发现问题，内容正常');
  } else {
    console.log('⚠️  发现问题：');
    issues.forEach(i => console.log(' -', i));
  }
}

main().catch(e => console.error(e));
