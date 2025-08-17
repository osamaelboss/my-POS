#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 تشغيل نظام نقاط البيع العربي
Run Arabic POS System
"""

import os
import sys
import subprocess

# إضافة مسار المشروع
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_path)

def check_and_setup():
    """فحص وإعداد البيئة"""
    print("🔧 فحص البيئة...")
    
    # فحص Python
    if sys.version_info < (3, 6):
        print("❌ تحتاج Python 3.6 أو أحدث")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # فحص البيئة الافتراضية
    venv_path = os.path.join(project_path, 'pos_env')
    if not os.path.exists(venv_path):
        print("⚠️ إنشاء البيئة الافتراضية...")
        subprocess.run([sys.executable, '-m', 'venv', venv_path])
    
    # تفعيل البيئة الافتراضية
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, 'Scripts', 'activate')
        python_exe = os.path.join(venv_path, 'Scripts', 'python.exe')
    else:  # Linux/Mac
        activate_script = os.path.join(venv_path, 'bin', 'activate')
        python_exe = os.path.join(venv_path, 'bin', 'python')
    
    # تثبيت المتطلبات
    requirements_file = os.path.join(project_path, 'requirements.txt')
    if os.path.exists(requirements_file):
        print("📦 تثبيت المتطلبات...")
        subprocess.run([python_exe, '-m', 'pip', 'install', '-r', requirements_file])
    
    return python_exe

def run_pos_system(python_exe):
    """تشغيل نظام نقاط البيع"""
    print("🎉 تشغيل النظام...")
    
    main_file = os.path.join(project_path, 'main.py')
    if not os.path.exists(main_file):
        print("❌ ملف main.py غير موجود")
        return False
    
    # تشغيل النظام
    try:
        subprocess.run([python_exe, main_file], cwd=project_path)
        return True
    except Exception as e:
        print(f"❌ خطأ في التشغيل: {e}")
        return False

def main():
    """الدالة الرئيسية"""
    print("=" * 60)
    print("🚀 مرحباً بك في نظام نقاط البيع العربي")
    print("   Welcome to Arabic POS System")
    print("=" * 60)
    
    try:
        # إعداد البيئة
        python_exe = check_and_setup()
        if not python_exe:
            print("❌ فشل في إعداد البيئة")
            input("اضغط Enter للخروج...")
            return
        
        print("✅ البيئة جاهزة")
        print()
        
        # تشغيل النظام
        success = run_pos_system(python_exe)
        
        if success:
            print("✅ تم إغلاق النظام بنجاح")
        else:
            print("❌ حدث خطأ في التشغيل")
            
    except KeyboardInterrupt:
        print("\n⚠️ تم إيقاف النظام بواسطة المستخدم")
    except Exception as e:
        print(f"❌ خطأ غير متوقع: {e}")
    
    print()
    input("اضغط Enter للخروج...")

if __name__ == "__main__":
    main()