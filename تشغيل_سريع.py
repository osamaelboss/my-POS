#!/usr/bin/env python3
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
    exit(1)

# Test database
try:
    print("⏳ فحص قاعدة البيانات...")
    from database.excel_manager import ExcelManager
    db = ExcelManager()
    print("✅ قاعدة البيانات جاهزة")
except Exception as e:
    print(f"❌ خطأ في قاعدة البيانات: {e}")
    exit(1)

# Test UI components
try:
    print("⏳ فحص واجهة المستخدم...")
    from utils.arabic_support import setup_arabic_font
    print("✅ واجهة المستخدم جاهزة")
except Exception as e:
    print(f"❌ خطأ في واجهة المستخدم: {e}")
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