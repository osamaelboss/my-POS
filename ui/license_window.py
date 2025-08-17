# -*- coding: utf-8 -*-
"""
License Activation Window
Handles license verification and activation
"""

import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
from datetime import datetime, timedelta

from utils.arabic_support import (
    create_arabic_label, create_arabic_button, create_arabic_entry,
    format_arabic_text, get_arabic_font_config
)

class LicenseWindow:
    def __init__(self, parent, db_manager, device_id):
        self.parent = parent
        self.db_manager = db_manager
        self.device_id = device_id
        self.window = None
        self.on_license_activated = None
        
        # Master password (in production, this should be more secure)
        self.master_password_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # "password"
    
    def show(self):
        """Show license activation window"""
        self.window = tk.Toplevel(self.parent)
        self.window.title("تفعيل البرنامج")
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        
        # Center the window
        self.window.transient(self.parent)
        self.window.grab_set()
        
        # Configure window
        self.window.configure(bg='#f0f0f0')
        
        self.create_widgets()
        
        # Focus on password entry
        self.password_entry.focus_set()
    
    def create_widgets(self):
        """Create window widgets"""
        main_frame = tk.Frame(self.window, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = create_arabic_label(
            main_frame,
            "النسخة غير مفعلة - برجاء إدخال كود التفعيل",
            font=get_arabic_font_config(16, "bold"),
            bg='#f0f0f0',
            fg='#d32f2f'
        )
        title_label.pack(pady=(0, 30))
        
        # Device ID display
        device_frame = tk.Frame(main_frame, bg='#f0f0f0')
        device_frame.pack(fill=tk.X, pady=(0, 20))
        
        create_arabic_label(
            device_frame,
            "معرف الجهاز:",
            font=get_arabic_font_config(12, "bold"),
            bg='#f0f0f0'
        ).pack(anchor=tk.E)
        
        device_id_label = tk.Label(
            device_frame,
            text=self.device_id,
            font=("Courier", 10),
            bg='#ffffff',
            relief=tk.SUNKEN,
            padx=10,
            pady=5
        )
        device_id_label.pack(fill=tk.X, pady=(5, 0))
        
        # Master password entry
        password_frame = tk.Frame(main_frame, bg='#f0f0f0')
        password_frame.pack(fill=tk.X, pady=(0, 20))
        
        create_arabic_label(
            password_frame,
            "كلمة مرور المطور:",
            font=get_arabic_font_config(12, "bold"),
            bg='#f0f0f0'
        ).pack(anchor=tk.E)
        
        self.password_entry = tk.Entry(
            password_frame,
            show="*",
            font=get_arabic_font_config(12),
            justify='center'
        )
        self.password_entry.pack(fill=tk.X, pady=(5, 0))
        self.password_entry.bind('<Return>', lambda e: self.verify_password())
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='#f0f0f0')
        buttons_frame.pack(fill=tk.X, pady=(20, 0))
        
        verify_btn = create_arabic_button(
            buttons_frame,
            "التحقق من كلمة المرور",
            command=self.verify_password,
            font=get_arabic_font_config(12, "bold"),
            bg='#4caf50',
            fg='white',
            padx=20,
            pady=10
        )
        verify_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        exit_btn = create_arabic_button(
            buttons_frame,
            "إغلاق البرنامج",
            command=self.exit_application,
            font=get_arabic_font_config(12, "bold"),
            bg='#f44336',
            fg='white',
            padx=20,
            pady=10
        )
        exit_btn.pack(side=tk.LEFT)
        
        # Status label
        self.status_label = create_arabic_label(
            main_frame,
            "",
            font=get_arabic_font_config(10),
            bg='#f0f0f0',
            fg='#666666'
        )
        self.status_label.pack(pady=(20, 0))
    
    def verify_password(self):
        """Verify master password"""
        entered_password = self.password_entry.get()
        
        if not entered_password:
            messagebox.showerror("خطأ", "برجاء إدخال كلمة المرور")
            return
        
        # Hash the entered password
        password_hash = hashlib.sha256(entered_password.encode()).hexdigest()
        
        if password_hash == self.master_password_hash:
            self.show_license_setup()
        else:
            messagebox.showerror("خطأ", "كلمة المرور غير صحيحة")
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus_set()
    
    def show_license_setup(self):
        """Show license setup interface"""
        # Clear current widgets
        for widget in self.window.winfo_children():
            widget.destroy()
        
        main_frame = tk.Frame(self.window, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = create_arabic_label(
            main_frame,
            "إعداد الترخيص",
            font=get_arabic_font_config(16, "bold"),
            bg='#f0f0f0',
            fg='#4caf50'
        )
        title_label.pack(pady=(0, 30))
        
        # Days selection
        days_frame = tk.Frame(main_frame, bg='#f0f0f0')
        days_frame.pack(fill=tk.X, pady=(0, 20))
        
        create_arabic_label(
            days_frame,
            "عدد أيام الترخيص:",
            font=get_arabic_font_config(12, "bold"),
            bg='#f0f0f0'
        ).pack(anchor=tk.E)
        
        # Days options
        self.selected_days = tk.IntVar(value=30)
        
        days_options = [
            (7, "أسبوع واحد (7 أيام)"),
            (30, "شهر واحد (30 يوم)"),
            (60, "شهرين (60 يوم)"),
            (90, "ثلاثة أشهر (90 يوم)"),
            (365, "سنة كاملة (365 يوم)")
        ]
        
        for days, text in days_options:
            rb = tk.Radiobutton(
                days_frame,
                text=format_arabic_text(text),
                variable=self.selected_days,
                value=days,
                font=get_arabic_font_config(11),
                bg='#f0f0f0',
                anchor='e'
            )
            rb.pack(anchor=tk.E, pady=2)
        
        # Custom days entry
        custom_frame = tk.Frame(main_frame, bg='#f0f0f0')
        custom_frame.pack(fill=tk.X, pady=(10, 20))
        
        self.custom_days_var = tk.IntVar()
        custom_rb = tk.Radiobutton(
            custom_frame,
            text=format_arabic_text("عدد مخصص من الأيام:"),
            variable=self.selected_days,
            value=0,  # 0 indicates custom
            font=get_arabic_font_config(11),
            bg='#f0f0f0',
            anchor='e',
            command=self.on_custom_selected
        )
        custom_rb.pack(anchor=tk.E)
        
        self.custom_entry = tk.Entry(
            custom_frame,
            textvariable=self.custom_days_var,
            font=get_arabic_font_config(12),
            justify='center',
            state='disabled',
            width=10
        )
        self.custom_entry.pack(anchor=tk.E, pady=(5, 0))
        
        # Buttons
        buttons_frame = tk.Frame(main_frame, bg='#f0f0f0')
        buttons_frame.pack(fill=tk.X, pady=(30, 0))
        
        activate_btn = create_arabic_button(
            buttons_frame,
            "تفعيل الترخيص",
            command=self.activate_license,
            font=get_arabic_font_config(12, "bold"),
            bg='#4caf50',
            fg='white',
            padx=20,
            pady=10
        )
        activate_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        cancel_btn = create_arabic_button(
            buttons_frame,
            "إلغاء",
            command=self.exit_application,
            font=get_arabic_font_config(12, "bold"),
            bg='#9e9e9e',
            fg='white',
            padx=20,
            pady=10
        )
        cancel_btn.pack(side=tk.LEFT)
    
    def on_custom_selected(self):
        """Enable custom days entry when selected"""
        if self.selected_days.get() == 0:
            self.custom_entry.config(state='normal')
            self.custom_entry.focus_set()
        else:
            self.custom_entry.config(state='disabled')
    
    def activate_license(self):
        """Activate license with selected days"""
        days = self.selected_days.get()
        
        if days == 0:  # Custom days
            days = self.custom_days_var.get()
            if days <= 0:
                messagebox.showerror("خطأ", "برجاء إدخال عدد أيام صحيح")
                return
        
        try:
            # Set license in database
            self.db_manager.set_license(self.device_id, days)
            
            # Calculate expiry date
            expiry_date = datetime.now() + timedelta(days=days)
            
            # Show success message
            success_message = f"""
تم تفعيل الترخيص بنجاح!

عدد الأيام: {days}
تاريخ الانتهاء: {expiry_date.strftime('%Y-%m-%d')}
معرف الجهاز: {self.device_id}
            """
            
            messagebox.showinfo("تم التفعيل", success_message)
            
            # Close license window and start main application
            self.window.destroy()
            if self.on_license_activated:
                self.on_license_activated()
                
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ في تفعيل الترخيص:\n{str(e)}")
    
    def exit_application(self):
        """Exit the application"""
        if messagebox.askokcancel("إغلاق", "هل تريد إغلاق البرنامج؟"):
            self.parent.quit()