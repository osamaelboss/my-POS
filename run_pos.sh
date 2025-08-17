#!/bin/bash
# Script to run Arabic POS System

echo "🚀 بدء تشغيل نظام نقاط البيع العربي..."
echo "Starting Arabic POS System..."

# Check if virtual environment exists
if [ ! -d "pos_env" ]; then
    echo "❌ البيئة الافتراضية غير موجودة. يجب تشغيل التثبيت أولاً"
    echo "Virtual environment not found. Please run installation first."
    exit 1
fi

# Activate virtual environment
echo "🔧 تفعيل البيئة الافتراضية..."
echo "Activating virtual environment..."
source pos_env/bin/activate

# Check if all required packages are installed
echo "✅ فحص المتطلبات..."
echo "Checking requirements..."
python -c "import tkinter, openpyxl, arabic_reshaper, bidi; print('✅ All packages available')"

if [ $? -ne 0 ]; then
    echo "❌ بعض المتطلبات مفقودة. جاري التثبيت..."
    echo "Some requirements missing. Installing..."
    pip install -r requirements.txt
fi

# Run the application
echo "🎉 تشغيل النظام..."
echo "Starting the system..."
python main.py