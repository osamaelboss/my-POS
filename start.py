#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مشغل نظام نقاط البيع العربي
Arabic POS System Launcher
"""

import os
import sys
import subprocess

def main():
    print("🚀 مرحباً بك في نظام نقاط البيع العربي")
    print("Welcome to Arabic POS System")
    print("=" * 50)
    
    # Check if we're in virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  تحتاج لتفعيل البيئة الافتراضية أولاً")
        print("You need to activate the virtual environment first")
        print()
        print("قم بتشغيل:")
        print("Run:")
        print("  source pos_env/bin/activate")
        print("  python start.py")
        return
    
    # Check requirements
    try:
        import tkinter
        import openpyxl
        import arabic_reshaper
        import bidi
        print("✅ جميع المتطلبات متوفرة")
        print("All requirements available")
    except ImportError as e:
        print(f"❌ مكتبة مفقودة: {e}")
        print(f"Missing library: {e}")
        print("جاري تثبيت المتطلبات...")
        print("Installing requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print()
    print("🎉 بدء تشغيل النظام...")
    print("Starting the system...")
    print()
    
    # Import and run main application
    try:
        from main import main as run_pos
        run_pos()
    except Exception as e:
        print(f"❌ خطأ في تشغيل النظام: {e}")
        print(f"Error running system: {e}")
        print()
        print("تأكد من:")
        print("Make sure:")
        print("1. تفعيل البيئة الافتراضية (Virtual environment activated)")
        print("2. تثبيت جميع المتطلبات (All requirements installed)")
        print("3. وجود جميع الملفات (All files present)")

if __name__ == "__main__":
    main()