@echo off
chcp 65001 >nul
echo ============================================
echo        نظام نقاط البيع العربي
echo        Arabic POS System  
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python غير مثبت
    echo ❌ Python is not installed
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "pos_env" (
    echo 🔧 إنشاء البيئة الافتراضية...
    echo 🔧 Creating virtual environment...
    python -m venv pos_env
)

REM Activate virtual environment and install requirements
echo 📦 تفعيل البيئة وتثبيت المتطلبات...
echo 📦 Activating environment and installing requirements...
call pos_env\Scripts\activate.bat
pip install -r requirements.txt

REM Run the application
echo.
echo 🚀 تشغيل النظام...
echo 🚀 Starting system...
echo.
python main.py

echo.
echo ✅ تم إغلاق النظام
echo ✅ System closed
pause