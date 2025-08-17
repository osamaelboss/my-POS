#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكريبت إنشاء نظام نقاط البيع العربي
Script to create Arabic POS System files
"""

import os

def create_directory_structure():
    """إنشاء هيكل المجلدات"""
    directories = [
        'database',
        'ui', 
        'utils'
    ]
    
    for dir_name in directories:
        os.makedirs(dir_name, exist_ok=True)
        print(f"✅ تم إنشاء مجلد: {dir_name}")

def create_requirements():
    """إنشاء ملف requirements.txt"""
    content = """openpyxl
Pillow
python-barcode
reportlab
arabic-reshaper
python-bidi"""
    
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ تم إنشاء: requirements.txt")

def create_main_launcher():
    """إنشاء ملف التشغيل الرئيسي"""
    content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("🚀 تشغيل نظام نقاط البيع العربي")
print("=" * 40)

# Test imports
try:
    print("⏳ فحص المكتبات...")
    import tkinter as tk
    import openpyxl
    import arabic_reshaper
    import bidi
    print("✅ جميع المكتبات متوفرة")
except Exception as e:
    print(f"❌ خطأ: {e}")
    print("جاري تثبيت المكتبات...")
    import subprocess
    import sys
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ تم تثبيت المكتبات")

# Test database
try:
    print("⏳ فحص قاعدة البيانات...")
    from database.excel_manager import ExcelManager
    db = ExcelManager()
    print("✅ قاعدة البيانات جاهزة")
except Exception as e:
    print(f"❌ خطأ في قاعدة البيانات: {e}")
    exit(1)

print("🎉 كل شيء جاهز!")
print("⏳ بدء تشغيل النظام...")

# Run main application
try:
    import main
    main.main()
except Exception as e:
    print(f"❌ خطأ في تشغيل النظام: {e}")
    print("تفاصيل الخطأ:")
    import traceback
    traceback.print_exc()
'''
    
    with open('تشغيل_النظام.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ تم إنشاء: تشغيل_النظام.py")

def create_windows_launcher():
    """إنشاء ملف تشغيل Windows"""
    content = '''@echo off
chcp 65001 >nul
echo ============================================
echo        نظام نقاط البيع العربي
echo        Arabic POS System  
echo ============================================
echo.

python تشغيل_النظام.py
pause'''
    
    with open('تشغيل.bat', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ تم إنشاء: تشغيل.bat")

def create_setup_instructions():
    """إنشاء تعليمات الإعداد"""
    content = '''🚀 تعليمات إعداد نظام نقاط البيع العربي

===============================================

📋 خطوات التشغيل:

1️⃣ في Windows:
   - اضغط مرتين على: تشغيل.bat
   - أو افتح Command Prompt واكتب: python تشغيل_النظام.py

2️⃣ في Linux/Mac:
   - افتح Terminal واكتب: python3 تشغيل_النظام.py

===============================================

🔐 التفعيل:

- كلمة المرور: password
- اختر مدة الترخيص: 30 يوم

===============================================

📁 ملفات البيانات:

ستجد ملفات Excel في مجلد "data" بعد التشغيل:
- Products.xlsx (المنتجات)
- Customers.xlsx (العملاء) 
- Sales.xlsx (المبيعات)
- وغيرها...

===============================================

✅ النظام جاهز للاستخدام!'''
    
    with open('تعليمات_التشغيل.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ تم إنشاء: تعليمات_التشغيل.txt")

def main():
    """الدالة الرئيسية"""
    print("🔧 بدء إنشاء نظام نقاط البيع العربي...")
    print("=" * 50)
    
    # إنشاء المجلدات
    create_directory_structure()
    
    # إنشاء الملفات الأساسية
    create_requirements()
    create_main_launcher()
    create_windows_launcher()
    create_setup_instructions()
    
    print("\n" + "=" * 50)
    print("🎉 تم إنشاء النظام بنجاح!")
    print("📁 الملفات التي تم إنشاؤها:")
    print("   - requirements.txt")
    print("   - تشغيل_النظام.py") 
    print("   - تشغيل.bat")
    print("   - تعليمات_التشغيل.txt")
    print("   - مجلدات: database, ui, utils")
    print("\n⚠️ ملاحظة: ستحتاج لإضافة باقي ملفات الكود!")
    print("📞 راجع الملفات الأخرى المطلوبة في قائمة_الملفات_المطلوبة.txt")

if __name__ == "__main__":
    main()