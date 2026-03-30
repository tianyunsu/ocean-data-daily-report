import subprocess, sys, os

script_dir = r"C:\Users\Administrator\.workbuddy\plugins\marketplaces\codebuddy-plugins-official\plugins\pptx\scripts\office"
pptx_file = r"C:\Users\Administrator\WorkBuddy\Claw\推动海洋经济高质量发展.pptx"

# Try to find python
python_exes = [
    r"C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe",
    r"C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe",
    r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\python.exe",
    r"C:\Python312\python.exe",
    r"C:\Python311\python.exe",
]
for p in python_exes:
    if os.path.exists(p):
        print(f"Found Python: {p}")
        break
