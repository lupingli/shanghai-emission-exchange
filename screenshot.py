#!/usr/bin/env python3
"""
上海环交所网站截图脚本
参考 novel-reader 的截图流程
"""

import sys
sys.path.insert(0, '/root/.openclaw/venvs/scrapling/lib/python3.11/site-packages')

from playwright.sync_api import sync_playwright
import os

# 项目路径
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_HTML = os.path.join(PROJECT_DIR, 'index.html')
SCREENSHOT_PATH = os.path.join(PROJECT_DIR, 'screenshot.png')

print("📸 开始截图上海环交所网站...")
print(f"📁 文件路径：{INDEX_HTML}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # 设置视口大小
    page.set_viewport_size({'width': 1920, 'height': 1080})
    
    # 访问本地 HTML 文件
    page.goto(f'file://{INDEX_HTML}', wait_until='networkidle')
    
    # 等待页面完全加载
    page.wait_for_timeout(2000)
    
    # 截图（整页）
    page.screenshot(path=SCREENSHOT_PATH, full_page=True)
    
    print(f"✅ 截图完成！")
    print(f"🖼️  保存位置：{SCREENSHOT_PATH}")
    
    browser.close()
