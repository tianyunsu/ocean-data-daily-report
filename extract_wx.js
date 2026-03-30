const fs = require('fs');

function extractContent(htmlFile) {
  const html = fs.readFileSync(htmlFile, 'utf8');
  
  // Extract title
  let title = '';
  const titleMatch = html.match(/<h1[^>]*class="[^"]*rich_media_title[^"]*"[^>]*>([\s\S]*?)<\/h1>/i) ||
                     html.match(/<meta[^>]*property="og:title"[^>]*content="([^"]+)"/i) ||
                     html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  if (titleMatch) title = titleMatch[1].replace(/<[^>]+>/g, '').trim();

  // Extract main content area
  const contentMatch = html.match(/<div[^>]*id="js_content"[^>]*>([\s\S]*?)<\/div>\s*<\/div>/i) ||
                       html.match(/<div[^>]*class="[^"]*rich_media_content[^"]*"[^>]*>([\s\S]*?)<\/div>/i);
  
  let content = '';
  if (contentMatch) {
    content = contentMatch[1];
  } else {
    // fallback: get body content
    const bodyMatch = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
    if (bodyMatch) content = bodyMatch[1];
  }

  // Extract images
  const imgRegex = /<img[^>]*(?:data-src|src)="([^"]+)"[^>]*>/gi;
  const images = [];
  let imgMatch;
  while ((imgMatch = imgRegex.exec(content)) !== null) {
    const src = imgMatch[1];
    if (src && !src.includes('gif') && src.startsWith('http')) {
      images.push(src);
    }
  }

  // Clean HTML to text
  let text = content
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/<\/p>/gi, '\n')
    .replace(/<\/div>/gi, '\n')
    .replace(/<\/h[1-6]>/gi, '\n')
    .replace(/<\/li>/gi, '\n')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&ldquo;/g, '"')
    .replace(/&rdquo;/g, '"')
    .replace(/&#\d+;/g, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();

  return { title, text: text.slice(0, 15000), images: images.slice(0, 10) };
}

const art1 = extractContent('wx_article_1.html');
const art2 = extractContent('wx_article_2.html');

const result = { article1: art1, article2: art2 };
fs.writeFileSync('articles_content.json', JSON.stringify(result, null, 2), 'utf8');

console.log('=== Article 1 ===');
console.log('Title:', art1.title);
console.log('Images:', art1.images.length);
console.log('Text preview:\n', art1.text.slice(0, 2000));
console.log('\n=== Article 2 ===');
console.log('Title:', art2.title);
console.log('Images:', art2.images.length);
console.log('Text preview:\n', art2.text.slice(0, 2000));
