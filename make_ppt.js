const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.title = '推动海洋经济高质量发展';

// ─── 配色 ───────────────────────────────────────────────────────────────────
const C = {
  deepBlue  : '0D2A4E',   // 深海蓝（深色背景）
  midBlue   : '1A4A7A',   // 中蓝（深色卡片/辅助）
  seaBlue   : '1F6BAE',   // 海蓝（强调色）
  accent    : '3AADCF',   // 青蓝（点睛色）
  lightBg   : 'F4F7FB',   // 浅灰蓝（内容页背景）
  cardBg    : 'FFFFFF',   // 白色卡片
  textDark  : '1A2A3A',   // 正文深色
  textMid   : '4A6080',   // 二级文字
  textLight : 'FFFFFF',   // 白色文字
  divider   : 'D8E4EF',   // 分隔线色
};

// ─── 辅助函数 ────────────────────────────────────────────────────────────────
// 左侧竖色条（装饰，不用线条）
function leftBar(slide, y, h, color) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.45, y, w: 0.06, h,
    fill: { color: color || C.accent },
    line: { color: color || C.accent, width: 0 }
  });
}

// 区块标题（带左彩条）
function sectionTitle(slide, text, y, color) {
  leftBar(slide, y, 0.38, color || C.accent);
  slide.addText(text, {
    x: 0.62, y, w: 9, h: 0.38,
    fontSize: 18, bold: true, color: C.deepBlue,
    fontFace: 'Microsoft YaHei', margin: 0, valign: 'middle'
  });
}

// 白色内容卡片
function card(slide, x, y, w, h, shadowOn) {
  slide.addShape(pres.shapes.RECTANGLE, {
    x, y, w, h,
    fill: { color: C.cardBg },
    line: { color: C.divider, width: 0.5 },
    shadow: shadowOn ? { type: 'outer', color: '000000', blur: 8, offset: 2, angle: 135, opacity: 0.08 } : undefined
  });
}

// 深色小标签
function tag(slide, text, x, y) {
  slide.addShape(pres.shapes.RECTANGLE, { x, y, w: 1.3, h: 0.26, fill: { color: C.seaBlue }, line: { color: C.seaBlue, width: 0 } });
  slide.addText(text, { x, y, w: 1.3, h: 0.26, fontSize: 10, color: C.textLight, bold: true, align: 'center', valign: 'middle', fontFace: 'Microsoft YaHei', margin: 0 });
}

// 页脚
function footer(slide, pageNum) {
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 5.35, w: 10, h: 0.275, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  slide.addText('推动海洋经济高质量发展  ·  《求是》2026年第6期', { x: 0.4, y: 5.36, w: 8, h: 0.25, fontSize: 9, color: 'AECDE8', fontFace: 'Microsoft YaHei', margin: 0 });
  slide.addText(`${pageNum}`, { x: 9.2, y: 5.36, w: 0.6, h: 0.25, fontSize: 9, color: 'AECDE8', align: 'right', fontFace: 'Microsoft YaHei', margin: 0 });
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 01 ── 封面
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.deepBlue };

  // 大海波浪装饰矩形（底部渐隐感）
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.0, w: 10, h: 1.625, fill: { color: C.midBlue, transparency: 60 }, line: { color: C.midBlue, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.6, w: 10, h: 1.025, fill: { color: C.midBlue, transparency: 30 }, line: { color: C.midBlue, width: 0 } });

  // 顶部细线装饰
  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.55, w: 1.2, h: 0.045, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });

  // 副标题标签
  s.addText('《求是》2026年第6期', { x: 0.5, y: 0.68, w: 5, h: 0.32, fontSize: 12, color: C.accent, fontFace: 'Microsoft YaHei', margin: 0 });

  // 主标题
  s.addText('推动海洋经济\n高质量发展', {
    x: 0.5, y: 1.15, w: 9, h: 1.9,
    fontSize: 46, bold: true, color: C.textLight,
    fontFace: 'Microsoft YaHei', margin: 0, lineSpacingMultiple: 1.2
  });

  // 来源说明
  s.addText([
    { text: '习近平总书记重要文章  ', options: { bold: true, color: 'E8F4FF' } },
    { text: '·  中共自然资源部党组署名文章', options: { color: 'AECDE8' } }
  ], { x: 0.5, y: 3.25, w: 9, h: 0.4, fontSize: 13, fontFace: 'Microsoft YaHei', margin: 0 });

  // 海洋图标装饰（用几何形状营造）
  s.addShape(pres.shapes.OVAL, { x: 7.8, y: 0.8, w: 1.8, h: 1.8, fill: { color: C.seaBlue, transparency: 80 }, line: { color: C.seaBlue, width: 0 } });
  s.addShape(pres.shapes.OVAL, { x: 8.3, y: 1.3, w: 1.2, h: 1.2, fill: { color: C.accent, transparency: 70 }, line: { color: C.accent, width: 0 } });

  // 底部说明
  s.addText('来源：新华社  |  自然资源部', { x: 0.5, y: 5.0, w: 9, h: 0.28, fontSize: 10, color: '6A9CC8', fontFace: 'Microsoft YaHei', margin: 0 });
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 02 ── 目录
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };

  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.9, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('目 录', { x: 0.5, y: 0.18, w: 9, h: 0.54, fontSize: 22, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  const items = [
    ['01', '战略高度', '海洋是国家发展的重要支撑与战略空间'],
    ['02', '历史成就', '新时代海洋经济发展的历史性突破'],
    ['03', '形势挑战', '国际竞争加剧与国内短板分析'],
    ['04', '五大思路', '创新·协同·产业·生态·合作'],
    ['05', '六项重点', '顶层设计到深度参与全球治理'],
    ['06', '重要意义', '向海图强，建设海洋强国'],
  ];

  items.forEach(([num, title, desc], i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = 0.45 + col * 4.85;
    const y = 1.1 + row * 1.38;

    card(s, x, y, 4.55, 1.18, true);
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: 0.5, h: 1.18, fill: { color: col === 0 ? C.seaBlue : C.midBlue }, line: { color: col === 0 ? C.seaBlue : C.midBlue, width: 0 } });
    s.addText(num, { x, y: y + 0.38, w: 0.5, h: 0.42, fontSize: 15, bold: true, color: C.textLight, align: 'center', fontFace: 'Microsoft YaHei', margin: 0 });
    s.addText(title, { x: x + 0.62, y: y + 0.12, w: 3.8, h: 0.38, fontSize: 15, bold: true, color: C.textDark, fontFace: 'Microsoft YaHei', margin: 0 });
    s.addText(desc, { x: x + 0.62, y: y + 0.56, w: 3.8, h: 0.48, fontSize: 10, color: C.textMid, fontFace: 'Microsoft YaHei', margin: 0 });
  });

  footer(s, 2);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 03 ── 章节封页：战略高度
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.deepBlue };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.5, w: 10, h: 1.125, fill: { color: C.midBlue, transparency: 50 }, line: { color: C.midBlue, width: 0 } });
  s.addText('01', { x: 0.5, y: 0.9, w: 3, h: 1.5, fontSize: 80, bold: true, color: C.seaBlue, fontFace: 'Arial Black', margin: 0, transparency: 60 });
  s.addText('战略高度', { x: 0.5, y: 1.8, w: 9, h: 0.8, fontSize: 36, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });
  s.addText('海洋是支撑未来发展的资源宝库和战略空间，是高质量发展战略要地', { x: 0.5, y: 2.75, w: 8.5, h: 0.5, fontSize: 14, color: 'AECDE8', fontFace: 'Microsoft YaHei', margin: 0 });
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 04 ── 海洋强国战略背景
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.75, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('海洋强国战略背景', { x: 0.45, y: 0.13, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  // 引用框
  s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y: 0.92, w: 9.1, h: 1.05, fill: { color: C.midBlue }, line: { color: C.midBlue, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y: 0.92, w: 0.07, h: 1.05, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addText('推进中国式现代化，必须高效开发利用海洋，推动海洋经济高质量发展，走出一条具有中国特色的向海图强之路。', {
    x: 0.65, y: 0.97, w: 8.7, h: 0.95,
    fontSize: 14, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0, italic: true
  });

  // 三列要点
  const points = [
    { title: '历史传承', body: '中华民族是最早利用海洋的民族之一。唐宋"海上丝绸之路"盛极一时，郑和七下西洋完成世界航海史上的壮举。' },
    { title: '新时代部署', body: '习近平总书记把海洋事业摆在党和国家发展全局重要位置，强调让海洋经济成为新的经济增长点。' },
    { title: '战略定位', body: '海洋是国家发展和综合实力的重要支撑，也是维护国家安全、参与全球治理的重要领域。' },
  ];
  points.forEach(({ title, body }, i) => {
    const x = 0.45 + i * 3.08;
    card(s, x, 2.18, 2.92, 2.9, true);
    s.addShape(pres.shapes.RECTANGLE, { x, y: 2.18, w: 2.92, h: 0.38, fill: { color: C.seaBlue }, line: { color: C.seaBlue, width: 0 } });
    s.addText(title, { x: x + 0.1, y: 2.18, w: 2.72, h: 0.38, fontSize: 13, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0, valign: 'middle' });
    s.addText(body, { x: x + 0.15, y: 2.65, w: 2.62, h: 2.3, fontSize: 11, color: C.textDark, fontFace: 'Microsoft YaHei', margin: 0 });
  });

  footer(s, 4);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 05 ── 章节封页：历史成就
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.deepBlue };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.5, w: 10, h: 1.125, fill: { color: C.midBlue, transparency: 50 }, line: { color: C.midBlue, width: 0 } });
  s.addText('02', { x: 0.5, y: 0.9, w: 3, h: 1.5, fontSize: 80, bold: true, color: C.seaBlue, fontFace: 'Arial Black', margin: 0, transparency: 60 });
  s.addText('历史成就', { x: 0.5, y: 1.8, w: 9, h: 0.8, fontSize: 36, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });
  s.addText('"十四五"期间海洋生产总值连续迈上9、10、11万亿元三个台阶', { x: 0.5, y: 2.75, w: 8.5, h: 0.5, fontSize: 14, color: 'AECDE8', fontFace: 'Microsoft YaHei', margin: 0 });
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 06 ── 海洋经济核心数据
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.75, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('海洋经济核心数据', { x: 0.45, y: 0.13, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  const stats = [
    { num: '11万亿+', label: '海洋生产总值', sub: '占GDP约8%' },
    { num: '~8%', label: '占国内生产总值', sub: '"十四五"时期' },
    { num: '70%', label: '新增海洋原油', sub: '占全国增量' },
    { num: '28%', label: '海洋药物品类', sub: '约占全球份额' },
  ];
  stats.forEach(({ num, label, sub }, i) => {
    const x = 0.45 + i * 2.28;
    card(s, x, 0.95, 2.1, 1.65, true);
    s.addShape(pres.shapes.RECTANGLE, { x, y: 0.95, w: 2.1, h: 0.08, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
    s.addText(num, { x: x + 0.1, y: 1.1, w: 1.9, h: 0.7, fontSize: 26, bold: true, color: C.seaBlue, fontFace: 'Arial', align: 'center', margin: 0 });
    s.addText(label, { x: x + 0.1, y: 1.82, w: 1.9, h: 0.36, fontSize: 11, bold: true, color: C.textDark, align: 'center', fontFace: 'Microsoft YaHei', margin: 0 });
    s.addText(sub, { x: x + 0.1, y: 2.2, w: 1.9, h: 0.28, fontSize: 9, color: C.textMid, align: 'center', fontFace: 'Microsoft YaHei', margin: 0 });
  });

  // 四大成就领域
  sectionTitle(s, '四大领域世界领先', 2.88);
  const leads = [
    ['船舶与海工装备', '产业规模全球第一'],
    ['海上风电', '产业规模全球第一'],
    ['海洋渔业', '产业规模全球第一'],
    ['海水淡化', '工程规模近300万吨/日'],
  ];
  leads.forEach(([title, desc], i) => {
    const x = 0.45 + i * 2.28;
    card(s, x, 3.3, 2.1, 1.7, false);
    s.addShape(pres.shapes.RECTANGLE, { x, y: 3.3, w: 2.1, h: 0.32, fill: { color: C.midBlue }, line: { color: C.midBlue, width: 0 } });
    s.addText(title, { x: x + 0.08, y: 3.3, w: 1.94, h: 0.32, fontSize: 11, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0, valign: 'middle' });
    s.addText(desc, { x: x + 0.08, y: 3.7, w: 1.94, h: 1.1, fontSize: 12, color: C.textDark, fontFace: 'Microsoft YaHei', margin: 0, valign: 'middle', align: 'center' });
  });

  footer(s, 6);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 07 ── 科技与生态成就
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.75, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('科技创新与生态保护成就', { x: 0.45, y: 0.13, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  // 左栏：科技成就
  card(s, 0.45, 0.9, 4.4, 4.2, true);
  s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y: 0.9, w: 4.4, h: 0.38, fill: { color: C.seaBlue }, line: { color: C.seaBlue, width: 0 } });
  s.addText('🔬 海洋科技创新', { x: 0.6, y: 0.9, w: 4.1, h: 0.38, fontSize: 14, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0, valign: 'middle' });

  const techItems = [
    '"梦想"号 ── 全球最大大洋钻探船建成入列',
    '"深海一号" ── 全球首座10万吨海上石油平台',
    '"蛟龙"号+"奋斗者"号 ── 完成首次北极载人深潜',
    '海洋能装备技术进入世界第一方阵',
    '崂山、汉江实验室全面运行',
  ];
  techItems.forEach((item, i) => {
    s.addShape(pres.shapes.OVAL, { x: 0.62, y: 1.44 + i * 0.6, w: 0.14, h: 0.14, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
    s.addText(item, { x: 0.85, y: 1.38 + i * 0.6, w: 3.85, h: 0.42, fontSize: 11, color: C.textDark, fontFace: 'Microsoft YaHei', margin: 0 });
  });

  // 右栏：生态成就
  card(s, 5.15, 0.9, 4.4, 4.2, true);
  s.addShape(pres.shapes.RECTANGLE, { x: 5.15, y: 0.9, w: 4.4, h: 0.38, fill: { color: C.midBlue }, line: { color: C.midBlue, width: 0 } });
  s.addText('🌊 生态保护与国际合作', { x: 5.3, y: 0.9, w: 4.1, h: 0.38, fontSize: 14, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0, valign: 'middle' });

  const ecoItems = [
    '大陆自然岸线保有率稳定在35%以上',
    '实施82个海洋生态保护修复工程项目',
    '"妈祖"系列预警报模型达国际先进水平',
    '与50多个国家和国际组织签署合作协议',
    '成为《BBNJ协定》首批签署国和缔约国',
  ];
  ecoItems.forEach((item, i) => {
    s.addShape(pres.shapes.OVAL, { x: 5.32, y: 1.44 + i * 0.6, w: 0.14, h: 0.14, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
    s.addText(item, { x: 5.55, y: 1.38 + i * 0.6, w: 3.85, h: 0.42, fontSize: 11, color: C.textDark, fontFace: 'Microsoft YaHei', margin: 0 });
  });

  footer(s, 7);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 08 ── 章节封页：形势挑战
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.deepBlue };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.5, w: 10, h: 1.125, fill: { color: C.midBlue, transparency: 50 }, line: { color: C.midBlue, width: 0 } });
  s.addText('03', { x: 0.5, y: 0.9, w: 3, h: 1.5, fontSize: 80, bold: true, color: C.seaBlue, fontFace: 'Arial Black', margin: 0, transparency: 60 });
  s.addText('形势与挑战', { x: 0.5, y: 1.8, w: 9, h: 0.8, fontSize: 36, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });
  s.addText('全球海洋竞争加剧，我国海洋经济发展面临复杂深刻变化', { x: 0.5, y: 2.75, w: 8.5, h: 0.5, fontSize: 14, color: 'AECDE8', fontFace: 'Microsoft YaHei', margin: 0 });
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 09 ── 外部挑战与内部短板
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.75, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('外部挑战与内部短板', { x: 0.45, y: 0.13, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  // 外部挑战（上半区）
  sectionTitle(s, '外部挑战', 0.88);
  const extChallenges = [
    { title: '国际竞争激烈', body: '沿海国家竞相出台蓝色经济战略，全球海洋治理体系加速重构，少数国家凭借技术优势主导规则制定。' },
    { title: '海上安全压力', body: '大国博弈、地缘冲突加剧，少数国家试图"以海制华"，设置技术壁垒，压缩我国海洋发展空间。' },
  ];
  extChallenges.forEach(({ title, body }, i) => {
    const x = 0.45 + i * 4.8;
    card(s, x, 1.35, 4.55, 1.45, true);
    s.addShape(pres.shapes.RECTANGLE, { x, y: 1.35, w: 0.06, h: 1.45, fill: { color: C.seaBlue }, line: { color: C.seaBlue, width: 0 } });
    s.addText(title, { x: x + 0.2, y: 1.42, w: 4.2, h: 0.35, fontSize: 13, bold: true, color: C.deepBlue, fontFace: 'Microsoft YaHei', margin: 0 });
    s.addText(body, { x: x + 0.2, y: 1.82, w: 4.2, h: 0.88, fontSize: 11, color: C.textMid, fontFace: 'Microsoft YaHei', margin: 0 });
  });

  // 内部短板（下半区）
  sectionTitle(s, '三大内部短板', 2.97);
  const intShorts = [
    { title: '科技成果供给偏弱', body: '高端仪器依赖进口，核心技术自给率低，成果转化率不高。' },
    { title: '产业核心竞争力不强', body: '传统产业大而不强，新兴产业规模尚小，缺乏国际竞争力的龙头企业。' },
    { title: '经济治理手段不足', body: '资源开发方式粗放，海洋金融产品单一，协同治理能力有待加强。' },
  ];
  intShorts.forEach(({ title, body }, i) => {
    const x = 0.45 + i * 3.1;
    card(s, x, 3.42, 2.92, 1.65, false);
    s.addShape(pres.shapes.RECTANGLE, { x, y: 3.42, w: 2.92, h: 0.06, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
    s.addText(title, { x: x + 0.12, y: 3.56, w: 2.68, h: 0.35, fontSize: 12, bold: true, color: C.deepBlue, fontFace: 'Microsoft YaHei', margin: 0 });
    s.addText(body, { x: x + 0.12, y: 3.95, w: 2.68, h: 0.96, fontSize: 10, color: C.textMid, fontFace: 'Microsoft YaHei', margin: 0 });
  });

  footer(s, 9);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 10 ── 章节封页：五大思路
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.deepBlue };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.5, w: 10, h: 1.125, fill: { color: C.midBlue, transparency: 50 }, line: { color: C.midBlue, width: 0 } });
  s.addText('04', { x: 0.5, y: 0.9, w: 3, h: 1.5, fontSize: 80, bold: true, color: C.seaBlue, fontFace: 'Arial Black', margin: 0, transparency: 60 });
  s.addText('五大发展思路', { x: 0.5, y: 1.8, w: 9, h: 0.8, fontSize: 36, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });
  s.addText('创新驱动·高效协同·产业更新·人海和谐·合作共赢', { x: 0.5, y: 2.75, w: 8.5, h: 0.5, fontSize: 14, color: C.accent, fontFace: 'Microsoft YaHei', margin: 0 });
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 11 ── 五大发展思路详解
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.75, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('五大发展思路', { x: 0.45, y: 0.13, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  const thoughts = [
    { num: '01', keyword: '创新驱动', color: '065A82', body: '尽快突破关键核心技术，推动海洋科技实现高水平自立自强' },
    { num: '02', keyword: '高效协同', color: '1A4A7A', body: '坚持陆海统筹、山海联动，增强协同发展合力' },
    { num: '03', keyword: '产业更新', color: '1F6BAE', body: '推动传统产业转型升级，大力发展海洋新兴产业，培育未来产业' },
    { num: '04', keyword: '人海和谐', color: '3AADCF', body: '统筹海洋资源开发和保护，建设可持续的海洋生态环境' },
    { num: '05', keyword: '合作共赢', color: '0D9488', body: '主动参与全球海洋治理，坚决维护我国领土主权和海洋权益' },
  ];

  thoughts.forEach(({ num, keyword, color, body }, i) => {
    const y = 0.9 + i * 0.87;
    s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y, w: 9.1, h: 0.72,
      fill: { color: i % 2 === 0 ? 'FFFFFF' : 'EEF4FB' },
      line: { color: C.divider, width: 0.5 }
    });
    // 序号圆角矩形
    s.addShape(pres.shapes.RECTANGLE, { x: 0.55, y: y + 0.1, w: 0.52, h: 0.52, fill: { color }, line: { color, width: 0 } });
    s.addText(num, { x: 0.55, y: y + 0.1, w: 0.52, h: 0.52, fontSize: 14, bold: true, color: 'FFFFFF', align: 'center', valign: 'middle', fontFace: 'Arial', margin: 0 });
    s.addText('更加注重' + keyword, { x: 1.2, y: y + 0.08, w: 2.2, h: 0.38, fontSize: 14, bold: true, color: C.deepBlue, fontFace: 'Microsoft YaHei', margin: 0 });
    s.addText(body, { x: 1.2, y: y + 0.38, w: 8.1, h: 0.3, fontSize: 10.5, color: C.textMid, fontFace: 'Microsoft YaHei', margin: 0 });
  });

  footer(s, 11);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 12 ── 章节封页：六项重点任务
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.deepBlue };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.5, w: 10, h: 1.125, fill: { color: C.midBlue, transparency: 50 }, line: { color: C.midBlue, width: 0 } });
  s.addText('05', { x: 0.5, y: 0.9, w: 3, h: 1.5, fontSize: 80, bold: true, color: C.seaBlue, fontFace: 'Arial Black', margin: 0, transparency: 60 });
  s.addText('六项重点任务', { x: 0.5, y: 1.8, w: 9, h: 0.8, fontSize: 36, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });
  s.addText('从顶层设计到全球治理，系统部署海洋经济高质量发展', { x: 0.5, y: 2.75, w: 8.5, h: 0.5, fontSize: 14, color: 'AECDE8', fontFace: 'Microsoft YaHei', margin: 0 });
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 13 ── 六项重点任务（上）1-3
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.75, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('六项重点任务（一）', { x: 0.45, y: 0.13, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  const tasks1 = [
    {
      num: '01', title: '加强顶层设计和政策支持',
      points: ['编制"十五五"海洋经济发展规划', '加大产业、科技、财税、金融政策支持', '鼓励引导社会资本积极参与']
    },
    {
      num: '02', title: '提高海洋科技自主创新能力',
      points: ['强化海洋战略科技力量', '培育海洋科技领军企业', '培育涉海专精特新中小企业']
    },
    {
      num: '03', title: '做强做优做大海洋产业',
      points: ['推动海上风电规范有序建设', '发展海洋生物医药和生物制品', '加强"数字海洋"建设', '推动海运业高质量发展']
    },
  ];

  tasks1.forEach(({ num, title, points }, i) => {
    const x = 0.45 + i * 3.1;
    card(s, x, 0.9, 2.92, 4.2, true);
    s.addShape(pres.shapes.RECTANGLE, { x, y: 0.9, w: 2.92, h: 0.5, fill: { color: C.seaBlue }, line: { color: C.seaBlue, width: 0 } });
    s.addText(num, { x: x + 0.12, y: 0.9, w: 0.42, h: 0.5, fontSize: 16, bold: true, color: C.accent, fontFace: 'Arial', margin: 0, valign: 'middle' });
    s.addText(title, { x: x + 0.55, y: 0.9, w: 2.25, h: 0.5, fontSize: 12, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0, valign: 'middle' });
    points.forEach((pt, j) => {
      s.addShape(pres.shapes.RECTANGLE, { x: x + 0.18, y: 1.6 + j * 0.72, w: 0.12, h: 0.12, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
      s.addText(pt, { x: x + 0.38, y: 1.55 + j * 0.72, w: 2.42, h: 0.58, fontSize: 11, color: C.textDark, fontFace: 'Microsoft YaHei', margin: 0 });
    });
  });

  footer(s, 13);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 14 ── 六项重点任务（下）4-6
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.75, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('六项重点任务（二）', { x: 0.45, y: 0.13, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  const tasks2 = [
    {
      num: '04', title: '加强主要海湾整体规划',
      points: ['有序推进沿海港口群优化整合', '支持重点港口绿色化转型', '支持重点港口数智化转型']
    },
    {
      num: '05', title: '加强海洋生态环境保护',
      points: ['加强海洋环境风险源头防范', '接续实施重点海域综合治理', '探索开展海洋碳汇核算']
    },
    {
      num: '06', title: '深度参与全球海洋治理',
      points: ['加强全球海洋科研调查合作', '推进防灾减灾国际合作', '推进"一带一路"国际港口联盟建设']
    },
  ];

  tasks2.forEach(({ num, title, points }, i) => {
    const x = 0.45 + i * 3.1;
    card(s, x, 0.9, 2.92, 4.2, true);
    s.addShape(pres.shapes.RECTANGLE, { x, y: 0.9, w: 2.92, h: 0.5, fill: { color: C.midBlue }, line: { color: C.midBlue, width: 0 } });
    s.addText(num, { x: x + 0.12, y: 0.9, w: 0.42, h: 0.5, fontSize: 16, bold: true, color: C.accent, fontFace: 'Arial', margin: 0, valign: 'middle' });
    s.addText(title, { x: x + 0.55, y: 0.9, w: 2.25, h: 0.5, fontSize: 12, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0, valign: 'middle' });
    points.forEach((pt, j) => {
      s.addShape(pres.shapes.RECTANGLE, { x: x + 0.18, y: 1.6 + j * 0.72, w: 0.12, h: 0.12, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
      s.addText(pt, { x: x + 0.38, y: 1.55 + j * 0.72, w: 2.42, h: 0.58, fontSize: 11, color: C.textDark, fontFace: 'Microsoft YaHei', margin: 0 });
    });
  });

  footer(s, 14);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 15 ── 章节封页：重要意义
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.deepBlue };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.18, h: 5.625, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 4.5, w: 10, h: 1.125, fill: { color: C.midBlue, transparency: 50 }, line: { color: C.midBlue, width: 0 } });
  s.addText('06', { x: 0.5, y: 0.9, w: 3, h: 1.5, fontSize: 80, bold: true, color: C.seaBlue, fontFace: 'Arial Black', margin: 0, transparency: 60 });
  s.addText('重要意义', { x: 0.5, y: 1.8, w: 9, h: 0.8, fontSize: 36, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });
  s.addText('向海图强，建设海洋强国，推动中国式现代化', { x: 0.5, y: 2.75, w: 8.5, h: 0.5, fontSize: 14, color: 'AECDE8', fontFace: 'Microsoft YaHei', margin: 0 });
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 16 ── 战略意义总结
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.lightBg };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.75, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addText('推动海洋经济高质量发展的战略意义', { x: 0.45, y: 0.13, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });

  const meanings = [
    { title: '拓展发展空间', body: '推动经济社会高质量发展，增强国家综合实力与战略纵深。', color: C.deepBlue },
    { title: '维护国家权益', body: '维护国家主权、安全、发展利益，捍卫领土主权和海洋权益。', color: C.midBlue },
    { title: '人海和谐发展', body: '统筹海洋资源开发与保护，推动构建海洋命运共同体。', color: C.seaBlue },
  ];

  meanings.forEach(({ title, body, color }, i) => {
    const x = 0.45 + i * 3.1;
    s.addShape(pres.shapes.RECTANGLE, { x, y: 0.95, w: 2.92, h: 2.4,
      fill: { color },
      line: { color, width: 0 },
      shadow: { type: 'outer', color: '000000', blur: 10, offset: 3, angle: 135, opacity: 0.12 }
    });
    s.addText(['0', '0', '0'][i] + (i + 1), { x: x + 0.15, y: 1.05, w: 0.5, h: 0.42, fontSize: 16, bold: true, color: C.accent, fontFace: 'Arial', margin: 0 });
    s.addText(title, { x: x + 0.15, y: 1.55, w: 2.62, h: 0.4, fontSize: 16, bold: true, color: 'FFFFFF', fontFace: 'Microsoft YaHei', margin: 0 });
    s.addText(body, { x: x + 0.15, y: 2.05, w: 2.62, h: 1.15, fontSize: 11, color: 'D0E8F5', fontFace: 'Microsoft YaHei', margin: 0 });
  });

  // 引用框
  s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y: 3.55, w: 9.1, h: 1.1, fill: { color: C.deepBlue }, line: { color: C.deepBlue, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y: 3.55, w: 0.07, h: 1.1, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addText('"十五五"时期是我国由海洋大国向海洋强国迈进的关键时期，必须增强忧患意识、底线思维，把海洋事业发展的战略主动权牢牢握在自己手里。', {
    x: 0.65, y: 3.6, w: 8.7, h: 1.0,
    fontSize: 12, color: 'D0E8F5', fontFace: 'Microsoft YaHei', margin: 0, italic: true
  });

  footer(s, 16);
}

// ═══════════════════════════════════════════════════════════════
// 幻灯片 17 ── 封底
// ═══════════════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.deepBlue };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.12, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 5.5, w: 10, h: 0.125, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });

  // 大圆装饰
  s.addShape(pres.shapes.OVAL, { x: 6.5, y: 0.5, w: 4.5, h: 4.5, fill: { color: C.midBlue, transparency: 70 }, line: { color: C.midBlue, width: 0 } });
  s.addShape(pres.shapes.OVAL, { x: 7.2, y: 1.2, w: 3.0, h: 3.0, fill: { color: C.seaBlue, transparency: 75 }, line: { color: C.seaBlue, width: 0 } });

  s.addText('向海图强', { x: 0.6, y: 1.1, w: 6, h: 1.1, fontSize: 48, bold: true, color: C.textLight, fontFace: 'Microsoft YaHei', margin: 0 });
  s.addText('建设海洋强国', { x: 0.6, y: 2.3, w: 6, h: 0.7, fontSize: 26, color: C.accent, fontFace: 'Microsoft YaHei', margin: 0 });

  s.addShape(pres.shapes.RECTANGLE, { x: 0.6, y: 3.2, w: 2.5, h: 0.04, fill: { color: C.accent }, line: { color: C.accent, width: 0 } });

  s.addText([
    { text: '来源：《求是》杂志2026年第6期\n', options: { color: 'AECDE8' } },
    { text: '习近平总书记重要文章  ·  中共自然资源部党组署名文章', options: { color: '7AAFD4' } }
  ], { x: 0.6, y: 3.45, w: 8, h: 0.8, fontSize: 11, fontFace: 'Microsoft YaHei', margin: 0 });
}

// ─── 写出文件 ───────────────────────────────────────────────────
pres.writeFile({ fileName: '推动海洋经济高质量发展.pptx' })
  .then(() => console.log('✅ PPT已生成：推动海洋经济高质量发展.pptx'))
  .catch(e => console.error('Error:', e));
