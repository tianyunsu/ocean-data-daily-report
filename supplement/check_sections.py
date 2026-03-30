import feishu_write_doc
secs = feishu_write_doc.SECTIONS
print(f"共 {len(secs)} 个方向")
for i, s in enumerate(secs):
    print(f"  {i+1}. {s['title']} - {len(s['items'])} 条")
