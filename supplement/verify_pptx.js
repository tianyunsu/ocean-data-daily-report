// 读取pptx文件做内容验证
const fs = require('fs');
const path = require('path');

// pptx本质是zip，用node内置能力验证
const pptxBuf = fs.readFileSync('推动海洋经济高质量发展.pptx');
console.log(`文件大小: ${(pptxBuf.length / 1024).toFixed(1)} KB`);

// Check magic bytes (PK zip header)
const magic = pptxBuf.slice(0, 4).toString('hex');
console.log(`文件头: ${magic} (应为 504b0304 = ZIP格式)`);

if (magic === '504b0304') {
  console.log('✅ 文件格式正确 (ZIP/PPTX)');
} else {
  console.log('❌ 文件格式异常');
}
