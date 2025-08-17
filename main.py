#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arabic Desktop POS and Inventory Management System
Main Application Entry Point
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
from datetime import datetime, timedelta
import hashlib
import platform

from database.excel_manager import ExcelManager
from ui.main_window import MainWindow
from ui.license_window import LicenseWindow
from utils.arabic_support import setup_arabic_font

class POSApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide main window initially
        
        # Setup Arabic font and RTL support
        setup_arabic_font(self.root)
        
        # Initialize database manager
        self.db_manager = ExcelManager()
        
        # Check license before starting
        if self.check_license():
            self.start_main_application()
        else:
            self.show_license_window()
    
    def get_device_id(self):
        """Generate unique device ID based on system information"""
        system_info = f"{platform.node()}{platform.processor()}{platform.system()}"
        return hashlib.md5(system_info.encode()).hexdigest()
    
    def check_license(self):
        """Check if the application has a valid license"""
        try:
            license_data = self.db_manager.get_license_info()
            if not license_data:
                return False
            
            device_id = self.get_device_id()
            stored_device_id = license_data.get('device_id', '')
            expiry_date = license_data.get('expiry_date', '')
            
            # Check device ID match
            if device_id != stored_device_id:
                return False
            
            # Check expiry date
            if expiry_date:
                expiry = datetime.strptime(expiry_date, '%Y-%m-%d')
                if datetime.now() > expiry:
                    return False
            
            return True
        except Exception as e:
            print(f"License check error: {e}")
            return False
    
    def show_license_window(self):
        """Show license activation window"""
        license_window = LicenseWindow(self.root, self.db_manager, self.get_device_id())
        license_window.on_license_activated = self.start_main_application
        license_window.show()
    
    def start_main_application(self):
        """Start the main POS application"""
        self.root.deiconify()  # Show main window
        self.main_window = MainWindow(self.root, self.db_manager)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        """Handle application closing"""
        if messagebox.askokcancel("إغلاق", "هل تريد إغلاق البرنامج؟"):
            self.root.destroy()
    
    def run(self):
        """Run the application"""
        self.root.mainloop()

def main():
    """Main entry point"""
    try:
        app = POSApplication()
        app.run()
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ في تشغيل البرنامج:\n{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()