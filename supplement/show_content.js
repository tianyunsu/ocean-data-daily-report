const fs = require('fs');
const d = JSON.parse(fs.readFileSync('articles_content.json', 'utf8'));
console.log('=== ART1 MORE ===');
console.log(d.article1.text.slice(2000, 10000));
console.log('\n=== ART1 IMAGES ===');
console.log(JSON.stringify(d.article1.images, null, 2));
