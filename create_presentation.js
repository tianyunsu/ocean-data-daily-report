const PptxGenJS = require("pptxgenjs");

// 创建演示文稿
const pptx = new PptxGenJS();

// 设置幻灯片尺寸（16:9）
pptx.layout = 'LAYOUT_16x9';

// 党建风格配色方案
const colors = {
    primary: '#C8102E',       // 中国红（主色）
    secondary: '#FFD700',     // 金色（辅助色）
    dark: '#8B0000',           // 深红色
    light: '#FFF5E6',         // 浅米色背景
    white: '#FFFFFF',         // 白色
    text: '#333333',          // 深灰色文字
    accent: '#DC143C'         // 亮红色强调
};

// 字体设置
const fonts = {
    title: 'SimHei',          // 黑体（标题）
    body: 'Microsoft YaHei',  // 微软雅黑（正文）
    number: 'Arial'           // 数字字体
};

// ========== 第1页：封面 ==========
const slide1 = pptx.addSlide();
slide1.background = { color: colors.primary };

// 标题
slide1.addText('Google BigQuery', {
    x: 0.5, y: 1.5, w: 9, h: 1,
    fontSize: 48, bold: true, color: colors.white,
    fontFamily: fonts.title, align: 'center'
});

slide1.addText('数据质量检查调研报告', {
    x: 0.5, y: 2.5, w: 9, h: 1,
    fontSize: 44, bold: true, color: colors.white,
    fontFamily: fonts.title, align: 'center'
});

// 装饰线
slide1.addShape(pptx.ShapeType.line, {
    x: 3, y: 3.8, w: 4, h: 0,
    line: { color: colors.secondary, width: 3 }
});

// 日期和版本
slide1.addText('2026年3月13日', {
    x: 0.5, y: 4.5, w: 9, h: 0.5,
    fontSize: 20, color: colors.light,
    fontFamily: fonts.body, align: 'center'
});

slide1.addText('版本：v1.0', {
    x: 0.5, y: 5, w: 9, h: 0.5,
    fontSize: 18, color: colors.light,
    fontFamily: fonts.body, align: 'center'
});

// ========== 第2页：报告摘要 ==========
const slide2 = pptx.addSlide();
slide2.background = { color: colors.light };

slide2.addText('报告摘要', {
    x: 0.5, y: 0.3, w: 9, h: 0.8,
    fontSize: 36, bold: true, color: colors.primary,
    fontFamily: fonts.title
});

// 装饰条
slide2.addShape(pptx.ShapeType.rect, {
    x: 0.5, y: 1.1, w: 2.5, h: 0.08,
    fill: { color: colors.secondary }
});

const summary = [
    '本报告基于2024-2025年最新技术文档和实践案例',
    '系统梳理BigQuery数据质量检查的主要方法、工具和最佳实践',
    '涵盖官方原生工具、开源解决方案及自动化框架',
    '为数据工程师和数据分析师提供全面的数据质量管理参考'
];

summary.forEach((text, index) => {
    slide2.addText(`• ${text}`, {
        x: 0.8, y: 1.5 + index * 0.6, w: 8.4, h: 0.5,
        fontSize: 18, color: colors.text,
        fontFamily: fonts.body,
        bullet: false
    });
});

// ========== 第3页：核心发现 ==========
const slide3 = pptx.addSlide();
slide3.background = { color: colors.light };

slide3.addText('核心发现', {
    x: 0.5, y: 0.3, w: 9, h: 0.8,
    fontSize: 36, bold: true, color: colors.primary,
    fontFamily: fonts.title
});

slide3.addShape(pptx.ShapeType.rect, {
    x: 0.5, y: 1.1, w: 2.5, h: 0.08,
    fill: { color: colors.secondary }
});

// 三个核心工具
const tools = [
    { name: 'Dataplex Data Quality Scan', desc: 'Google官方原生工具，集成度高，自动化程度高' },
    { name: 'CloudDQ', desc: '开源声明式CLI工具，支持CI/CD，灵活性强' },
    { name: '自动化检查框架', desc: '多表自动化、异常检测、告警机制' }
];

tools.forEach((tool, index) => {
    const yPos = 1.5 + index * 1.3;

    // 工具名称背景
    slide3.addShape(pptx.ShapeType.rect, {
        x: 0.8, y: yPos, w: 8.4, h: 0.5,
        fill: { color: colors.primary },
        line: { color: colors.primary }
    });

    slide3.addText(tool.name, {
        x: 0.8, y: yPos, w: 8.4, h: 0.5,
        fontSize: 20, bold: true, color: colors.white,
        fontFamily: fonts.title, align: 'center'
    });

    slide3.addText(tool.desc, {
        x: 0.8, y: yPos + 0.6, w: 8.4, h: 0.6,
        fontSize: 16, color: colors.text,
        fontFamily: fonts.body, align: 'center'
    });
});

// ========== 第4页：数据质量检查维度 ==========
const slide4 = pptx.addSlide();
slide4.background = { color: colors.light };

slide4.addText('数据质量检查的六大维度', {
    x: 0.5, y: 0.3, w: 9, h: 0.8,
    fontSize: 36, bold: true, color: colors.primary,
    fontFamily: fonts.title
});

slide4.addShape(pptx.ShapeType.rect, {
    x: 0.5, y: 1.1, w: 3, h: 0.08,
    fill: { color: colors.secondary }
});

// 两列布局
const dimensions = [
    '完整性：必填字段空值率、记录数量一致性',
    '准确性：数据类型、数值范围、格式规范',
    '一致性：跨表关联、时间序列连续性',
    '唯一性：主键重复、唯一约束验证',
    '及时性：数据延迟、更新频率、SLA合规',
    '可信度：数据来源、血缘追溯、元数据'
];

dimensions.forEach((text, index) => {
    const col = index < 3 ? 0 : 4.5;
    const row = index < 3 ? index : index - 3;

    // 序号圆圈
    slide4.addShape(pptx.ShapeType.ellipse, {
        x: col + 0.8, y: 1.5 + row * 0.9, w: 0.4, h: 0.4,
        fill: { color: colors.primary }
    });

    slide4.addText((index + 1).toString(), {
        x: col + 0.8, y: 1.5 + row * 0.9, w: 0.4, h: 0.4,
        fontSize: 18, bold: true, color: colors.white,
        fontFamily: fonts.number, align: 'center'
    });

    // 内容
    slide4.addText(text, {
        x: col + 1.3, y: 1.5 + row * 0.9, w: 4, h: 0.5,
        fontSize: 16, color: colors.text,
        fontFamily: fonts.body
    });
});

// ========== 第5页：技术方案对比 ==========
const slide5 = pptx.addSlide();
slide5.background = { color: colors.light };

slide5.addText('技术实现方案对比', {
    x: 0.5, y: 0.3, w: 9, h: 0.8,
    fontSize: 36, bold: true, color: colors.primary,
    fontFamily: fonts.title
});

slide5.addShape(pptx.ShapeType.rect, {
    x: 0.5, y: 1.1, w: 2.5, h: 0.08,
    fill: { color: colors.secondary }
});

// 表格数据
const tableData = [
    [
        { text: '方案', options: { fontSize: 16, bold: true, color: colors.white } },
        { text: '优势', options: { fontSize: 16, bold: true, color: colors.white } },
        { text: '适用场景', options: { fontSize: 16, bold: true, color: colors.white } }
    ],
    [
        { text: 'Dataplex', options: { fontSize: 14, bold: true } },
        { text: '官方支持、集成度高', options: { fontSize: 14 } },
        { text: '企业级大规模部署', options: { fontSize: 14 } }
    ],
    [
        { text: 'CloudDQ', options: { fontSize: 14, bold: true } },
        { text: '开源免费、CI/CD友好', options: { fontSize: 14 } },
        { text: '中小型技术团队', options: { fontSize: 14 } }
    ],
    [
        { text: '自定义脚本', options: { fontSize: 14, bold: true } },
        { text: '灵活度高、完全可控', options: { fontSize: 14 } },
        { text: '特殊定制化需求', options: { fontSize: 14 } }
    ]
];

slide5.addTable(tableData, {
    x: 0.8, y: 1.5, w: 8.4, h: 3.5,
    colW: [2.5, 3.5, 2.4],
    border: { pt: 1, color: 'CCCCCC' },
    fill: { color: colors.primary },
    align: 'left',
    valign: 'middle',
    fontSize: 14,
    fontFace: fonts.body
});

// ========== 第6页：最佳实践 ==========
const slide6 = pptx.addSlide();
slide6.background = { color: colors.light };

slide6.addText('最佳实践建议', {
    x: 0.5, y: 0.3, w: 9, h: 0.8,
    fontSize: 36, bold: true, color: colors.primary,
    fontFamily: fonts.title
});

slide6.addShape(pptx.ShapeType.rect, {
    x: 0.5, y: 1.1, w: 2, h: 0.08,
    fill: { color: colors.secondary }
});

const practices = [
    {
        title: '分层检查策略',
        items: ['基础层：完整性、唯一性、数据类型', '业务层：业务逻辑、一致性', '高级层：异常检测、数据漂移']
    },
    {
        title: '优先级设置',
        items: ['P0：核心业务指标，立即告警', 'P1：重要业务指标，人工确认', 'P2：一般监控，记录日志']
    },
    {
        title: '自动化实施',
        items: ['定时检查：批处理任务', '告警机制：邮件、即时通讯', '可视化：数据质量仪表板']
    }
];

practices.forEach((practice, index) => {
    const yPos = 1.5 + index * 1.5;

    // 标题背景
    slide6.addShape(pptx.ShapeType.rect, {
        x: 0.8, y: yPos, w: 8.4, h: 0.5,
        fill: { color: colors.dark },
        line: { color: colors.dark }
    });

    slide6.addText(practice.title, {
        x: 0.8, y: yPos, w: 8.4, h: 0.5,
        fontSize: 18, bold: true, color: colors.white,
        fontFamily: fonts.title
    });

    practice.items.forEach((item, itemIndex) => {
        slide6.addText(`• ${item}`, {
            x: 1, y: yPos + 0.55 + itemIndex * 0.35, w: 8.2, h: 0.3,
            fontSize: 14, color: colors.text,
            fontFamily: fonts.body
        });
    });
});

// ========== 第7页：技术趋势 ==========
const slide7 = pptx.addSlide();
slide7.background = { color: colors.light };

slide7.addText('技术趋势与未来方向', {
    x: 0.5, y: 0.3, w: 9, h: 0.8,
    fontSize: 36, bold: true, color: colors.primary,
    fontFamily: fonts.title
});

slide7.addShape(pptx.ShapeType.rect, {
    x: 0.5, y: 1.1, w: 3, h: 0.08,
    fill: { color: colors.secondary }
});

const trends = [
    {
        title: 'AI驱动的数据质量',
        desc: '使用Gemini CLI生成数据质量规则，智能异常检测，自动化根因分析'
    },
    {
        title: '数据可观测性',
        desc: '全链路数据监控，实时数据指标追踪，智能告警和根因分析'
    },
    {
        title: 'Code-First工作流',
        desc: '支持Git版本控制，更好的CI/CD集成，可测试和可复现的数据质量规则'
    }
];

trends.forEach((trend, index) => {
    const yPos = 1.5 + index * 1.4;

    // 标题圆圈
    slide7.addShape(pptx.ShapeType.ellipse, {
        x: 0.8, y: yPos, w: 0.6, h: 0.6,
        fill: { color: colors.primary }
    });

    slide7.addText((index + 1).toString(), {
        x: 0.8, y: yPos, w: 0.6, h: 0.6,
        fontSize: 24, bold: true, color: colors.white,
        fontFamily: fonts.number, align: 'center'
    });

    slide7.addText(trend.title, {
        x: 1.5, y: yPos, w: 7.7, h: 0.5,
        fontSize: 20, bold: true, color: colors.dark,
        fontFamily: fonts.title
    });

    slide7.addText(trend.desc, {
        x: 1.5, y: yPos + 0.55, w: 7.7, h: 0.6,
        fontSize: 16, color: colors.text,
        fontFamily: fonts.body
    });
});

// ========== 第8页：实施路线图 ==========
const slide8 = pptx.addSlide();
slide8.background = { color: colors.light };

slide8.addText('实施路线图', {
    x: 0.5, y: 0.3, w: 9, h: 0.8,
    fontSize: 36, bold: true, color: colors.primary,
    fontFamily: fonts.title
});

slide8.addShape(pptx.ShapeType.rect, {
    x: 0.5, y: 1.1, w: 2, h: 0.08,
    fill: { color: colors.secondary }
});

const phases = [
    { name: '基础建设', time: '1-2个月', items: ['选择工具', '定义规则', '监控告警', '质量仪表板'] },
    { name: '自动化优化', time: '2-3个月', items: ['自动检查', 'CI/CD集成', '告警优化', '评分体系'] },
    { name: '智能化升级', time: '3-6个月', items: ['AI异常检测', '根因分析', '成本优化', '治理框架'] },
    { name: '持续改进', time: '持续进行', items: ['规则优化', '扩展监控', '团队意识', '最佳实践'] }
];

phases.forEach((phase, index) => {
    const col = (index % 2) * 4.5;
    const row = Math.floor(index / 2);

    // 阶段框
    slide8.addShape(pptx.ShapeType.rect, {
        x: col + 0.8, y: 1.5 + row * 2, w: 4.1, h: 1.8,
        fill: { color: colors.white },
        line: { color: colors.primary, width: 2 }
    });

    // 阶段名称
    slide8.addText(phase.name, {
        x: col + 0.8, y: 1.5 + row * 2, w: 4.1, h: 0.5,
        fontSize: 18, bold: true, color: colors.primary,
        fontFamily: fonts.title, align: 'center'
    });

    // 时间
    slide8.addText(phase.time, {
        x: col + 0.8, y: 1.95 + row * 2, w: 4.1, h: 0.4,
        fontSize: 14, color: colors.text,
        fontFamily: fonts.body, align: 'center'
    });

    // 分割线
    slide8.addShape(pptx.ShapeType.line, {
        x: col + 1, y: 2.35 + row * 2, w: 3.7, h: 0,
        line: { color: colors.secondary, width: 1 }
    });

    // 内容
    const itemsText = phase.items.join('  ');
    slide8.addText(itemsText, {
        x: col + 1, y: 2.45 + row * 2, w: 3.7, h: 0.7,
        fontSize: 12, color: colors.text,
        fontFamily: fonts.body, align: 'center'
    });
});

// ========== 第9页：总结与建议 ==========
const slide9 = pptx.addSlide();
slide9.background = { color: colors.light };

slide9.addText('总结与建议', {
    x: 0.5, y: 0.3, w: 9, h: 0.8,
    fontSize: 36, bold: true, color: colors.primary,
    fontFamily: fonts.title
});

slide9.addShape(pptx.ShapeType.rect, {
    x: 0.5, y: 1.1, w: 2, h: 0.08,
    fill: { color: colors.secondary }
});

// 关键要点
slide9.addText('关键要点', {
    x: 0.8, y: 1.5, w: 8.4, h: 0.5,
    fontSize: 22, bold: true, color: colors.dark,
    fontFamily: fonts.title
});

const keyPoints = [
    'Dataplex是官方推荐的企业级解决方案',
    'CloudDQ是优秀的开源替代方案',
    '数据质量检查需要体系化建设',
    'AI和可观测性是未来趋势'
];

keyPoints.forEach((point, index) => {
    slide9.addShape(pptx.ShapeType.rect, {
        x: 0.8, y: 2 + index * 0.6, w: 0.05, h: 0.5,
        fill: { color: colors.primary }
    });

    slide9.addText(point, {
        x: 1, y: 2 + index * 0.6, w: 8.2, h: 0.5,
        fontSize: 18, color: colors.text,
        fontFamily: fonts.body
    });
});

// 实施建议
slide9.addText('实施建议', {
    x: 0.8, y: 4.7, w: 8.4, h: 0.5,
    fontSize: 22, bold: true, color: colors.dark,
    fontFamily: fonts.title
});

const recommendations = [
    '从小规模试点开始，选择关键业务表实施',
    '建立数据质量文化，让数据质量成为团队的共同责任',
    '持续优化和改进，数据质量是一个持续的过程',
    '平衡成本和效果，选择合适的检查策略'
];

recommendations.forEach((rec, index) => {
    slide9.addShape(pptx.ShapeType.rect, {
        x: 0.8, y: 5.2 + index * 0.6, w: 0.05, h: 0.5,
        fill: { color: colors.secondary }
    });

    slide9.addText(rec, {
        x: 1, y: 5.2 + index * 0.6, w: 8.2, h: 0.5,
        fontSize: 16, color: colors.text,
        fontFamily: fonts.body
    });
});

// ========== 第10页：结束页 ==========
const slide10 = pptx.addSlide();
slide10.background = { color: colors.primary };

slide10.addText('谢谢观看', {
    x: 0.5, y: 2.5, w: 9, h: 1,
    fontSize: 56, bold: true, color: colors.white,
    fontFamily: fonts.title, align: 'center'
});

// 装饰线
slide10.addShape(pptx.ShapeType.line, {
    x: 3.5, y: 3.6, w: 3, h: 0,
    line: { color: colors.secondary, width: 3 }
});

slide10.addText('Google BigQuery 数据质量检查调研报告', {
    x: 0.5, y: 4, w: 9, h: 0.6,
    fontSize: 24, color: colors.light,
    fontFamily: fonts.body, align: 'center'
});

slide10.addText('2026年3月', {
    x: 0.5, y: 5, w: 9, h: 0.5,
    fontSize: 20, color: colors.light,
    fontFamily: fonts.body, align: 'center'
});

// 保存PPT
pptx.writeFile({ fileName: 'BigQuery数据质量检查调研报告.pptx' });

console.log('PPT创建成功！');
