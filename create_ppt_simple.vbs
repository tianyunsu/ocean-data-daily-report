' VBScript to create PowerPoint presentation
Set ppt = CreateObject("PowerPoint.Application")
ppt.Visible = True

Set pres = ppt.Presentations.Add

' Slide 1: Title
Set slide1 = pres.Slides.Add(1, 1)
slide1.Shapes(1).TextFrame.TextRange.Text = "树立和践行正确政绩观" & vbCrLf & "学习教育工作部署"
slide1.Shapes(1).TextFrame.TextRange.Font.Size = 54
slide1.Shapes(1).TextFrame.TextRange.Font.Bold = True
slide1.Shapes(1).TextFrame.TextRange.Font.Color.RGB = RGB(200, 16, 46)

' Slide 2: Background
Set slide2 = pres.Slides.Add(2, 2)
slide2.Shapes(1).TextFrame.TextRange.Text = "一、会议背景" & vbCrLf & vbCrLf & "自然资源部召开党组会议，深入学习贯彻习近平总书记关于树立和践行正确政绩观的重要论述和重要指示精神。" & vbCrLf & vbCrLf & "自然资源部第一海洋研究所召开党委（扩大）会议，动员部署全所开展树立和践行正确政绩观学习教育工作。"
slide2.Shapes(1).TextFrame.TextRange.Font.Size = 28

' Slide 3: Significance
Set slide3 = pres.Slides.Add(3, 2)
slide3.Shapes(1).TextFrame.TextRange.Text = "二、重要意义" & vbCrLf & vbCrLf & "- 贯彻落实党的二十届四中全会战略部署的重要举措" & vbCrLf & "- 践行党的根本宗旨、夯实党的执政根基的必然要求" & vbCrLf & "- 推进党和国家事业发展、全面从严治党的关键环节" & vbCrLf & "- 2026年党建工作的重要任务"
slide3.Shapes(1).TextFrame.TextRange.Font.Size = 26

' Slide 4: Requirements
Set slide4 = pres.Slides.Add(4, 2)
slide4.Shapes(1).TextFrame.TextRange.Text = "三、总要求" & vbCrLf & vbCrLf & "立党为公、为民造福、科学决策、真抓实干" & vbCrLf & vbCrLf & "- 坚持学查改一体推进" & vbCrLf & "- 结合学论述谋发展见行动活动" & vbCrLf & "- 确保学习教育取得实效" & vbCrLf & "- 将正确政绩观融入科研管理和科技创新全过程"
slide4.Shapes(1).TextFrame.TextRange.Font.Size = 26

' Slide 5: Tasks
Set slide5 = pres.Slides.Add(5, 2)
slide5.Shapes(1).TextFrame.TextRange.Text = "四、重点任务" & vbCrLf & vbCrLf & "- 深学细悟 - 把牢正确方向，深入学习领会习近平总书记重要论述精神" & vbCrLf & "- 联系实际 - 深挖细查问题，结合实际工作查找问题" & vbCrLf & "- 从严从实 - 推动整改整治，力戒形式主义"
slide5.Shapes(1).TextFrame.TextRange.Font.Size = 26

' Slide 6: Rectification
Set slide6 = pres.Slides.Add(6, 2)
slide6.Shapes(1).TextFrame.TextRange.Text = "五、整治重点" & vbCrLf & vbCrLf & "- 重点整治规划编制中的形式主义问题" & vbCrLf & "- 化解自然资源领域信访问题" & vbCrLf & "- 排查整改影响科研创新发展的突出问题" & vbCrLf & "- 解决群众反映强烈的急难愁盼问题"
slide6.Shapes(1).TextFrame.TextRange.Font.Size = 26

' Slide 7: Work Requirements
Set slide7 = pres.Slides.Add(7, 2)
slide7.Shapes(1).TextFrame.TextRange.Text = "六、工作要求" & vbCrLf & vbCrLf & "- 提高政治站位，深刻认识学习教育的重大意义" & vbCrLf & "- 精心组织实施，各级党组织负起政治责任" & vbCrLf & "- 坚持开门教育，广泛听取群众意见建议" & vbCrLf & "- 力戒形式主义，确保学习教育不偏不空、不走过场" & vbCrLf & "- 以正确政绩观引领自然资源工作提质量上水平" & vbCrLf & "- 以清廉务实作风推动十五五科研工作开好局"
slide7.Shapes(1).TextFrame.TextRange.Font.Size = 22

' Slide 8: End
Set slide8 = pres.Slides.Add(8, 1)
slide8.Shapes(1).TextFrame.TextRange.Text = "谢谢观看"
slide8.Shapes(1).TextFrame.TextRange.Font.Size = 72
slide8.Shapes(1).TextFrame.TextRange.Font.Bold = True
slide8.Shapes(1).TextFrame.TextRange.Font.Color.RGB = RGB(200, 16, 46)

' Save
pres.SaveAs "c:\Users\Administrator\WorkBuddy\Claw\树立和践行正确政绩观学习教育.pptx"
pres.Close
ppt.Quit

MsgBox "PPT created successfully!", 0, "Complete"
