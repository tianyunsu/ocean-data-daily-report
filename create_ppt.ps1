# PowerShell script to create PPTX using COM automation
# This script requires Microsoft PowerPoint to be installed

$ppt = New-Object -ComObject PowerPoint.Application
$ppt.Visible = $true

$pres = $ppt.Presentations.Add()

# 党建风格配色
$colors = @{
    primary = [System.Drawing.Color]::FromArgb(200, 16, 46)      # 中国红
    secondary = [System.Drawing.Color]::FromArgb(255, 215, 0)     # 金色
    dark = [System.Drawing.Color]::FromArgb(139, 0, 0)             # 深红色
    light = [System.Drawing.Color]::FromArgb(255, 245, 230)        # 浅米色
    white = [System.Drawing.Color]::FromArgb(255, 255, 255)        # 白色
}

# 第1页：封面
$slide1 = $pres.Slides.Add(1)
$slide1.Background.Fill.ForeColor.RGB = $colors.primary.ToArgb()

$title1 = $slide1.Shapes.AddTextbox(0, 100, 150, 800, 100)
$title1.TextFrame.TextRange.Text = "树立和践行正确政绩观"
$title1.TextFrame.TextRange.Font.Color.RGB = $colors.white.ToArgb()
$title1.TextFrame.TextRange.Font.Size = 60
$title1.TextFrame.TextRange.Font.Bold = $true
$title1.TextFrame.TextRange.Font.Name = "黑体"
$title1.TextFrame.TextRange.ParagraphFormat.Alignment = 2 # 居中

$title2 = $slide1.Shapes.AddTextbox(0, 100, 280, 800, 100)
$title2.TextFrame.TextRange.Text = "学习教育工作部署"
$title2.TextFrame.TextRange.Font.Color.RGB = $colors.white.ToArgb()
$title2.TextFrame.TextRange.Font.Size = 56
$title2.TextFrame.TextRange.Font.Bold = $true
$title2.TextFrame.TextRange.Font.Name = "黑体"
$title2.TextFrame.ParagraphFormat.Alignment = 2

$line = $slide1.Shapes.AddLine(200, 420, 600, 420)
$line.Line.ForeColor.RGB = $colors.secondary.ToArgb()
$line.Line.Weight = 3

$date = $slide1.Shapes.AddTextbox(0, 250, 480, 500, 50)
$date.TextFrame.TextRange.Text = "2026年3月"
$date.TextFrame.TextRange.Font.Color.RGB = $colors.light.ToArgb()
$date.TextFrame.TextRange.Font.Size = 24
$date.TextFrame.TextRange.Font.Name = "微软雅黑"
$date.ParagraphFormat.Alignment = 2

# 第2页：会议背景
$slide2 = $pres.Slides.Add(1)
$slide2.Background.Fill.ForeColor.RGB = $colors.light.ToArgb()

$title = $slide2.Shapes.AddTextbox(0, 50, 50, 900, 80)
$title.TextFrame.TextRange.Text = "一、会议背景"
$title.TextFrame.TextRange.Font.Color.RGB = $colors.primary.ToArgb()
$title.TextFrame.TextRange.Font.Size = 44
$title.TextFrame.TextRange.Font.Bold = $true
$title.TextFrame.TextRange.Font.Name = "黑体"

$line2 = $slide2.Shapes.AddLine(50, 140, 300, 140)
$line2.Line.ForeColor.RGB = $colors.secondary.ToArgb()
$line2.Line.Weight = 4

$content = @"
自然资源部召开党组会议，深入学习贯彻习近平总书记关于树立和践行正确政绩观的重要论述和重要指示精神，传达学习中办印发的《关于在全党开展树立和践行正确政绩观学习教育的通知》和中央党的建设工作领导小组会议精神。

自然资源部第一海洋研究所召开党委（扩大）会议，动员部署全所开展树立和践行正确政绩观学习教育工作。
"@

$textBox = $slide2.Shapes.AddTextbox(1, 80, 180, 840, 450)
$textBox.TextFrame.TextRange.Text = $content
$textBox.TextFrame.TextRange.Font.Color.RGB = 0x333333
$textBox.TextFrame.TextRange.Font.Size = 20
$textBox.TextFrame.TextRange.Font.Name = "微软雅黑"
$textBox.TextFrame.WordWrap = $true

# 第3页：重要意义
$slide3 = $pres.Slides.Add(1)
$slide3.Background.Fill.ForeColor.RGB = $colors.light.ToArgb()

$title3 = $slide3.Shapes.AddTextbox(0, 50, 50, 900, 80)
$title3.TextFrame.TextRange.Text = "二、重要意义"
$title3.TextFrame.TextRange.Font.Color.RGB = $colors.primary.ToArgb()
$title3.TextFrame.TextRange.Font.Size = 44
$title3.TextFrame.TextRange.Font.Bold = $true
$title3.TextFrame.TextRange.Font.Name = "黑体"

$line3 = $slide3.Shapes.AddLine(50, 140, 300, 140)
$line3.Line.ForeColor.RGB = $colors.secondary.ToArgb()
$line3.Line.Weight = 4

$points = @(
    "贯彻落实党的二十届四中全会战略部署的重要举措",
    "践行党的根本宗旨、夯实党的执政根基的必然要求",
    "推进党和国家事业发展、全面从严治党的关键环节",
    "2026年党建工作的重要任务"
)

$yPos = 180
foreach ($point in $points) {
    $bullet = $slide3.Shapes.AddTextbox(0, 80, $yPos, 840, 80)
    $bullet.TextFrame.TextRange.Text = "• " + $point
    $bullet.TextFrame.TextRange.Font.Color.RGB = 0x333333
    $bullet.TextFrame.TextRange.Font.Size = 22
    $bullet.TextFrame.TextRange.Font.Name = "微软雅黑"
    $yPos += 90
}

# 第4页：总要求
$slide4 = $pres.Slides.Add(1)
$slide4.Background.Fill.ForeColor.RGB = $colors.light.ToArgb()

$title4 = $slide4.Shapes.AddTextbox(0, 50, 50, 900, 80)
$title4.TextFrame.TextRange.Text = "三、总要求"
$title4.TextFrame.TextRange.Font.Color.RGB = $colors.primary.ToArgb()
$title4.TextFrame.TextRange.Font.Size = 44
$title4.TextFrame.TextRange.Font.Bold = $true
$title4.TextFrame.TextRange.Font.Name = "黑体"

$line4 = $slide4.Shapes.AddLine(50, 140, 300, 140)
$line4.Line.ForeColor.RGB = $colors.secondary.ToArgb()
$line4.Line.Weight = 4

$mainReq = $slide4.Shapes.AddTextbox(1, 150, 200, 700, 100)
$mainReq.TextFrame.TextRange.Text = "立党为公、为民造福、科学决策、真抓实干"
$mainReq.TextFrame.TextRange.Font.Color.RGB = $colors.primary.ToArgb()
$mainReq.TextFrame.TextRange.Font.Size = 32
$mainReq.TextFrame.TextRange.Font.Bold = $true
$mainReq.TextFrame.TextRange.Font.Name = "黑体"
$mainReq.ParagraphFormat.Alignment = 2

$subReqs = @(
    "坚持学查改一体推进",
    "结合'学论述谋发展见行动'活动",
    "确保学习教育取得实效",
    "将正确政绩观融入科研管理和科技创新全过程"
)

$yPos = 350
foreach ($req in $subReqs) {
    $item = $slide4.Shapes.AddTextbox(0, 150, $yPos, 700, 60)
    $item.TextFrame.TextRange.Text = "• " + $req
    $item.TextFrame.TextRange.Font.Color.RGB = 0x333333
    $item.TextFrame.TextRange.Font.Size = 20
    $item.TextFrame.TextRange.Font.Name = "微软雅黑"
    $item.ParagraphFormat.Alignment = 2
    $yPos += 70
}

# 第5页：重点任务
$slide5 = $pres.Slides.Add(1)
$slide5.Background.Fill.ForeColor.RGB = $colors.light.ToArgb()

$title5 = $slide5.Shapes.AddTextbox(0, 50, 50, 900, 80)
$title5.TextFrame.TextRange.Text = "四、重点任务"
$title5.TextFrame.TextRange.Font.Color.RGB = $colors.primary.ToArgb()
$title5.TextFrame.TextRange.Font.Size = 44
$title5.TextFrame.TextRange.Font.Bold = $true
$title5.TextFrame.TextRange.Font.Name = "黑体"

$line5 = $slide5.Shapes.AddLine(50, 140, 300, 140)
$line5.Line.ForeColor.RGB = $colors.secondary.ToArgb()
$line5.Line.Weight = 4

$tasks = @(
    @{
        title = "深学细悟"
        desc = "把牢正确方向，深入学习领会习近平总书记重要论述精神"
    },
    @{
        title = "联系实际"
        desc = "深挖细查问题，结合实际工作查找问题"
    },
    @{
        title = "从严从实"
        desc = "推动整改整治，力戒形式主义"
    }
)

$yPos = 180
foreach ($task in $tasks) {
    # 卡片背景
    $card = $slide5.Shapes.AddShape(1, 100, $yPos, 800, 110)
    $card.Fill.ForeColor.RGB = $colors.white.ToArgb()
    $card.Line.ForeColor.RGB = $colors.primary.ToArgb()
    $card.Line.Weight = 2

    # 标题
    $cardTitle = $slide5.Shapes.AddTextbox(0, 120, $yPos + 15, 760, 40)
    $cardTitle.TextFrame.TextRange.Text = $task.title
    $cardTitle.TextFrame.TextRange.Font.Color.RGB = $colors.primary.ToArgb()
    $cardTitle.TextFrame.TextRange.Font.Size = 24
    $cardTitle.TextFrame.TextRange.Font.Bold = $true
    $cardTitle.TextFrame.TextRange.Font.Name = "黑体"

    # 描述
    $cardDesc = $slide5.Shapes.AddTextbox(0, 120, $yPos + 60, 760, 40)
    $cardDesc.TextFrame.TextRange.Text = $task.desc
    $cardDesc.TextFrame.TextRange.Font.Color.RGB = 0x333333
    $cardDesc.TextFrame.TextRange.Font.Size = 18
    $cardDesc.TextFrame.TextRange.Font.Name = "微软雅黑"

    $yPos += 130
}

# 第6页：整治重点
$slide6 = $pres.Slides.Add(1)
$slide6.Background.Fill.ForeColor.RGB = $colors.light.ToArgb()

$title6 = $slide6.Shapes.AddTextbox(0, 50, 50, 900, 80)
$title6.TextFrame.TextRange.Text = "五、整治重点"
$title6.TextFrame.TextRange.Font.Color.RGB = $colors.primary.ToArgb()
$title6.TextFrame.TextRange.Font.Size = 44
$title6.TextFrame.TextRange.Font.Bold = $true
$title6.TextFrame.TextRange.Font.Name = "黑体"

$line6 = $slide6.Shapes.AddLine(50, 140, 300, 140)
$line6.Line.ForeColor.RGB = $colors.secondary.ToArgb()
$line6.Line.Weight = 4

$rectifications = @(
    "重点整治规划编制中的形式主义问题",
    "化解自然资源领域信访问题",
    "排查整改影响科研创新发展的突出问题",
    "解决群众反映强烈的急难愁盼问题"
)

$yPos = 180
foreach ($item in $rectifications) {
    $rect = $slide6.Shapes.AddTextbox(0, 80, $yPos, 840, 90)
    $rect.TextFrame.TextRange.Text = "• " + $item
    $rect.TextFrame.TextRange.Font.Color.RGB = 0x333333
    $rect.TextFrame.TextRange.Font.Size = 20
    $rect.TextFrame.TextRange.Font.Name = "微软雅黑"
    $yPos += 100
}

# 第7页：工作要求
$slide7 = $pres.Slides.Add(1)
$slide7.Background.Fill.ForeColor.RGB = $colors.light.ToArgb()

$title7 = $slide7.Shapes.AddTextbox(0, 50, 50, 900, 80)
$title7.TextFrame.TextRange.Font.Color.RGB = $colors.primary.ToArgb()
$title7.TextFrame.TextRange.Font.Size = 44
$title7.TextFrame.TextRange.Font.Bold = $true
$title7.TextFrame.TextRange.Font.Name = "黑体"
$title7.TextFrame.TextRange.Text = "六、工作要求"

$line7 = $slide7.Shapes.AddLine(50, 140, 300, 140)
$line7.Line.ForeColor.RGB = $colors.secondary.ToArgb()
$line7.Line.Weight = 4

$requirements = @(
    "提高政治站位，深刻认识学习教育的重大意义",
    "精心组织实施，各级党组织负起政治责任",
    "坚持开门教育，广泛听取群众意见建议",
    "力戒形式主义，确保学习教育不偏不空、不走过场",
    "以正确政绩观引领自然资源工作提质量上水平",
    "以清廉务实作风推动'十五五'科研工作开好局"
)

$yPos = 180
foreach ($req in $requirements) {
    $item = $slide7.Shapes.AddTextbox(0, 80, $yPos, 840, 75)
    $item.TextFrame.TextRange.Text = "• " + $req
    $item.TextFrame.TextRange.Font.Color.RGB = 0x333333
    $item.TextFrame.TextRange.Font.Size = 18
    $item.TextFrame.TextRange.Font.Name = "微软雅黑"
    $yPos += 85
}

# 第8页：结束页
$slide8 = $pres.Slides.Add(1)
$slide8.Background.Fill.ForeColor.RGB = $colors.primary.ToArgb()

$endTitle = $slide8.Shapes.AddTextbox(0, 100, 300, 800, 120)
$endTitle.TextFrame.TextRange.Text = "谢谢观看"
$endTitle.TextFrame.TextRange.Font.Color.RGB = $colors.white.ToArgb()
$endTitle.TextFrame.TextRange.Font.Size = 72
$endTitle.TextFrame.TextRange.Font.Bold = $true
$endTitle.TextFrame.TextRange.Font.Name = "黑体"
$endTitle.ParagraphFormat.Alignment = 2

$lineEnd = $slide8.Shapes.AddLine(250, 440, 550, 440)
$lineEnd.Line.ForeColor.RGB = $colors.secondary.ToArgb()
$lineEnd.Line.Weight = 3

$subTitle = $slide8.Shapes.AddTextbox(0, 200, 480, 600, 60)
$subTitle.TextFrame.TextRange.Text = "树立和践行正确政绩观学习教育"
$subTitle.TextFrame.TextRange.Font.Color.RGB = $colors.light.ToArgb()
$subTitle.TextFrame.TextRange.Font.Size = 28
$subTitle.TextFrame.TextRange.Font.Name = "微软雅黑"
$subTitle.ParagraphFormat.Alignment = 2

# 保存文件
$savePath = "c:\Users\Administrator\WorkBuddy\Claw\树立和践行正确政绩观学习教育.pptx"
$pres.SaveAs($savePath)
$pres.Close()
$ppt.Quit()

Write-Host "PPT已成功创建：$savePath"
