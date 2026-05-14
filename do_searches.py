"""Search all 9 directions and save results to files."""
import subprocess
import os
import json
from datetime import datetime

SKILL_DIR = r'C:\Users\Administrator\.agents\skills\autoglm-websearch'
OUTPUT_DIR = r'C:\Users\Administrator\WorkBuddy\Claw\search_results'
os.makedirs(OUTPUT_DIR, exist_ok=True)

queries = {
    '1_ocean_ai': 'ocean artificial intelligence machine learning 2026 April',
    '2_ocean_digital_twin': 'ocean digital twin simulation 2026 April',
    '3_ocean_visualization': 'ocean visualization dashboard interactive 2026',
    '4_ocean_data_quality': 'ocean data quality control Argo QA/QC 2026 April',
    '5_ocean_data_processing': 'ocean data processing satellite Argo 2026 April',
    '6_ocean_data_management': 'ocean data sharing platform repository 2026 April',
    '7_open_cruise': 'open cruise ship time sharing expedition 2026 April',
    '8_ocean_data_center': 'ocean data center repository archive 2026 April',
    '9_tools_github': 'ocean Python GitHub xarray CMEMS Argo tool 2026 April',
}

results = {}
for key, query in queries.items():
    out_file = os.path.join(OUTPUT_DIR, f'{key}.txt')
    cmd = f'cd /d "{SKILL_DIR}" && python websearch.py "{query}" 2>&1'
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, timeout=60, encoding='utf-8', errors='replace')
        output = result.stdout + result.stderr
    except Exception as e:
        output = f'ERROR: {e}'
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(output)
    results[key] = output[:500]  # preview
    print(f'[{key}] Done ({len(output)} chars)')

print('\n=== SUMMARY ===')
for k, v in results.items():
    print(f'{k}: {v[:100]}...')
