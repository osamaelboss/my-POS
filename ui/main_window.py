# -*- coding: utf-8 -*-
"""
Main Application Window
Central hub for the POS system with navigation to all modules
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from utils.arabic_support import (
    create_arabic_label, create_arabic_button, format_arabic_text,
    get_arabic_font_config
)

class MainWindow:
    def __init__(self, root, db_manager):
        self.root = root
        self.db_manager = db_manager
        
        self.setup_main_window()
        self.create_widgets()
        self.update_alerts()
    
    def setup_main_window(self):
        """Configure main window"""
        self.root.title("نظام نقاط البيع والمخزون")
        self.root.geometry("1200x800")
        self.root.state('zoomed' if self.root.tk.call('tk', 'windowingsystem') == 'win32' else 'normal')
        
        # Configure colors
        self.root.configure(bg='#f5f5f5')
        
        # Configure styles
        style = ttk.Style()
        style.theme_use('clam')
    
    def create_widgets(self):
        """Create main window widgets"""
        # Header frame
        header_frame = tk.Frame(self.root, bg='#2196f3', height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Title
        title_label = create_arabic_label(
            header_frame,
            "نظام نقاط البيع والمخزون",
            font=get_arabic_font_config(20, "bold"),
            bg='#2196f3',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f5f5f5')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left sidebar for navigation
        self.create_sidebar(main_frame)
        
        # Right content area
        self.create_content_area(main_frame)
        
        # Status bar
        self.create_status_bar()
    
    def create_sidebar(self, parent):
        """Create navigation sidebar"""
        sidebar_frame = tk.Frame(parent, bg='#ffffff', width=250, relief=tk.RAISED, bd=1)
        sidebar_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10))
        sidebar_frame.pack_propagate(False)
        
        # Sidebar title
        sidebar_title = create_arabic_label(
            sidebar_frame,
            "القوائم الرئيسية",
            font=get_arabic_font_config(16, "bold"),
            bg='#ffffff',
            fg='#333333'
        )
        sidebar_title.pack(pady=(20, 30))
        
        # Navigation buttons
        nav_buttons = [
            ("المبيعات والفواتير", self.open_sales, "#4caf50"),
            ("إدارة المنتجات", self.open_products, "#ff9800"),
            ("إدارة العملاء", self.open_customers, "#2196f3"),
            ("إدارة الموردين", self.open_suppliers, "#9c27b0"),
            ("التقارير", self.open_reports, "#f44336"),
            ("البحث السريع", self.open_search, "#607d8b"),
            ("الإعدادات", self.open_settings, "#795548")
        ]
        
        for text, command, color in nav_buttons:
            btn = create_arabic_button(
                sidebar_frame,
                text,
                command=command,
                font=get_arabic_font_config(12, "bold"),
                bg=color,
                fg='white',
                width=20,
                pady=10
            )
            btn.pack(pady=5, padx=20, fill=tk.X)
    
    def create_content_area(self, parent):
        """Create main content area"""
        content_frame = tk.Frame(parent, bg='#f5f5f5')
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Welcome section
        welcome_frame = tk.Frame(content_frame, bg='#ffffff', relief=tk.RAISED, bd=1)
        welcome_frame.pack(fill=tk.X, pady=(0, 20))
        
        welcome_title = create_arabic_label(
            welcome_frame,
            "مرحباً بك في نظام نقاط البيع",
            font=get_arabic_font_config(18, "bold"),
            bg='#ffffff',
            fg='#333333'
        )
        welcome_title.pack(pady=20)
        
        # Quick stats section
        self.create_quick_stats(content_frame)
        
        # Alerts section
        self.create_alerts_section(content_frame)
        
        # Quick actions section
        self.create_quick_actions(content_frame)
    
    def create_quick_stats(self, parent):
        """Create quick statistics section"""
        stats_frame = tk.Frame(parent, bg='#ffffff', relief=tk.RAISED, bd=1)
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        stats_title = create_arabic_label(
            stats_frame,
            "إحصائيات سريعة",
            font=get_arabic_font_config(14, "bold"),
            bg='#ffffff',
            fg='#333333'
        )
        stats_title.pack(pady=(15, 10))
        
        # Stats grid
        stats_grid = tk.Frame(stats_frame, bg='#ffffff')
        stats_grid.pack(pady=(0, 15))
        
        # Get statistics
        try:
            products_count = len(self.db_manager.get_products())
            customers_count = len(self.db_manager.get_customers())
            daily_sales = self.db_manager.get_daily_sales_report()
            daily_total = sum(float(sale.get('الإجمالي', 0) or 0) for sale in daily_sales)
            low_stock_count = len(self.db_manager.get_low_stock_products())
        except Exception as e:
            products_count = customers_count = daily_total = low_stock_count = 0
        
        stats_data = [
            ("إجمالي المنتجات", products_count, "#4caf50"),
            ("إجمالي العملاء", customers_count, "#2196f3"),
            ("مبيعات اليوم", f"{daily_total:.2f} ج.م", "#ff9800"),
            ("مخزون منخفض", low_stock_count, "#f44336")
        ]
        
        for i, (label, value, color) in enumerate(stats_data):
            col = i % 2
            row = i // 2
            
            stat_frame = tk.Frame(stats_grid, bg=color, padx=20, pady=15)
            stat_frame.grid(row=row, column=col, padx=10, pady=5, sticky='ew')
            
            value_label = tk.Label(
                stat_frame,
                text=str(value),
                font=get_arabic_font_config(16, "bold"),
                bg=color,
                fg='white'
            )
            value_label.pack()
            
            label_label = create_arabic_label(
                stat_frame,
                label,
                font=get_arabic_font_config(10),
                bg=color,
                fg='white'
            )
            label_label.pack()
        
        # Configure grid weights
        stats_grid.columnconfigure(0, weight=1)
        stats_grid.columnconfigure(1, weight=1)
    
    def create_alerts_section(self, parent):
        """Create alerts section for low stock and expiring products"""
        alerts_frame = tk.Frame(parent, bg='#ffffff', relief=tk.RAISED, bd=1)
        alerts_frame.pack(fill=tk.X, pady=(0, 20))
        
        alerts_title = create_arabic_label(
            alerts_frame,
            "التنبيهات",
            font=get_arabic_font_config(14, "bold"),
            bg='#ffffff',
            fg='#333333'
        )
        alerts_title.pack(pady=(15, 10))
        
        # Alerts content
        self.alerts_content = tk.Frame(alerts_frame, bg='#ffffff')
        self.alerts_content.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
    
    def create_quick_actions(self, parent):
        """Create quick actions section"""
        actions_frame = tk.Frame(parent, bg='#ffffff', relief=tk.RAISED, bd=1)
        actions_frame.pack(fill=tk.BOTH, expand=True)
        
        actions_title = create_arabic_label(
            actions_frame,
            "إجراءات سريعة",
            font=get_arabic_font_config(14, "bold"),
            bg='#ffffff',
            fg='#333333'
        )
        actions_title.pack(pady=(15, 20))
        
        # Quick action buttons
        actions_grid = tk.Frame(actions_frame, bg='#ffffff')
        actions_grid.pack(expand=True)
        
        quick_actions = [
            ("فاتورة جديدة", self.new_invoice, "#4caf50"),
            ("منتج جديد", self.new_product, "#ff9800"),
            ("عميل جديد", self.new_customer, "#2196f3"),
            ("تقرير يومي", self.daily_report, "#f44336")
        ]
        
        for i, (text, command, color) in enumerate(quick_actions):
            col = i % 2
            row = i // 2
            
            btn = create_arabic_button(
                actions_grid,
                text,
                command=command,
                font=get_arabic_font_config(12, "bold"),
                bg=color,
                fg='white',
                width=15,
                pady=15
            )
            btn.grid(row=row, column=col, padx=20, pady=10)
        
        # Configure grid weights
        actions_grid.columnconfigure(0, weight=1)
        actions_grid.columnconfigure(1, weight=1)
    
    def create_status_bar(self):
        """Create status bar"""
        self.status_bar = tk.Frame(self.root, bg='#e0e0e0', height=30)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_bar.pack_propagate(False)
        
        # Current time
        self.time_label = tk.Label(
            self.status_bar,
            text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            font=get_arabic_font_config(10),
            bg='#e0e0e0',
            fg='#333333'
        )
        self.time_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # License status
        try:
            license_info = self.db_manager.get_license_info()
            if license_info:
                expiry_date = license_info.get('expiry_date', '')
                if expiry_date:
                    days_left = (datetime.strptime(expiry_date, '%Y-%m-%d') - datetime.now()).days
                    license_text = f"الترخيص ينتهي خلال {days_left} يوم"
                else:
                    license_text = "الترخيص نشط"
            else:
                license_text = "غير مرخص"
        except:
            license_text = "غير مرخص"
        
        self.license_label = create_arabic_label(
            self.status_bar,
            license_text,
            font=get_arabic_font_config(10),
            bg='#e0e0e0',
            fg='#333333'
        )
        self.license_label.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # Update time every second
        self.update_time()
    
    def update_time(self):
        """Update time display"""
        self.time_label.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.root.after(1000, self.update_time)
    
    def update_alerts(self):
        """Update alerts display"""
        # Clear existing alerts
        for widget in self.alerts_content.winfo_children():
            widget.destroy()
        
        try:
            # Low stock alerts
            low_stock = self.db_manager.get_low_stock_products()
            if low_stock:
                alert_frame = tk.Frame(self.alerts_content, bg='#ffebee')
                alert_frame.pack(fill=tk.X, pady=2)
                
                create_arabic_label(
                    alert_frame,
                    f"⚠️ {len(low_stock)} منتج بمخزون منخفض",
                    font=get_arabic_font_config(11, "bold"),
                    bg='#ffebee',
                    fg='#d32f2f'
                ).pack(anchor=tk.E, padx=10, pady=5)
            
            # Expiring products alerts
            expiring = self.db_manager.get_expiring_products()
            if expiring:
                alert_frame = tk.Frame(self.alerts_content, bg='#fff3e0')
                alert_frame.pack(fill=tk.X, pady=2)
                
                create_arabic_label(
                    alert_frame,
                    f"⏰ {len(expiring)} منتج قارب على الانتهاء",
                    font=get_arabic_font_config(11, "bold"),
                    bg='#fff3e0',
                    fg='#f57c00'
                ).pack(anchor=tk.E, padx=10, pady=5)
            
            # If no alerts
            if not low_stock and not expiring:
                create_arabic_label(
                    self.alerts_content,
                    "✅ لا توجد تنبيهات",
                    font=get_arabic_font_config(11),
                    bg='#ffffff',
                    fg='#4caf50'
                ).pack(anchor=tk.E, padx=10, pady=10)
                
        except Exception as e:
            create_arabic_label(
                self.alerts_content,
                "خطأ في تحميل التنبيهات",
                font=get_arabic_font_config(11),
                bg='#ffffff',
                fg='#f44336'
            ).pack(anchor=tk.E, padx=10, pady=10)
    
    # Navigation methods
    def open_sales(self):
        """Open sales management"""
        messagebox.showinfo("قريباً", "وحدة المبيعات قيد التطوير")
    
    def open_products(self):
        """Open product management"""
        messagebox.showinfo("قريباً", "وحدة إدارة المنتجات قيد التطوير")
    
    def open_customers(self):
        """Open customer management"""
        messagebox.showinfo("قريباً", "وحدة إدارة العملاء قيد التطوير")
    
    def open_suppliers(self):
        """Open supplier management"""
        messagebox.showinfo("قريباً", "وحدة إدارة الموردين قيد التطوير")
    
    def open_reports(self):
        """Open reports"""
        messagebox.showinfo("قريباً", "وحدة التقارير قيد التطوير")
    
    def open_search(self):
        """Open search"""
        messagebox.showinfo("قريباً", "وحدة البحث قيد التطوير")
    
    def open_settings(self):
        """Open settings"""
        messagebox.showinfo("قريباً", "وحدة الإعدادات قيد التطوير")
    
    # Quick action methods
    def new_invoice(self):
        """Create new invoice"""
        messagebox.showinfo("قريباً", "فاتورة جديدة قيد التطوير")
    
    def new_product(self):
        """Add new product"""
        messagebox.showinfo("قريباً", "إضافة منتج جديد قيد التطوير")
    
    def new_customer(self):
        """Add new customer"""
        messagebox.showinfo("قريباً", "إضافة عميل جديد قيد التطوير")
    
    def daily_report(self):
        """Show daily report"""
        messagebox.showinfo("قريباً", "التقرير اليومي قيد التطوير")