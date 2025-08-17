# -*- coding: utf-8 -*-
"""
Arabic Language Support Utilities
Handles RTL text display and Arabic font configuration
"""

import tkinter as tk
from tkinter import font
import arabic_reshaper
from bidi.algorithm import get_display
import platform

def setup_arabic_font(root):
    """Setup Arabic font for the application"""
    system = platform.system()
    
    if system == "Windows":
        arabic_fonts = ["Tahoma", "Arial Unicode MS", "Segoe UI"]
    elif system == "Linux":
        arabic_fonts = ["DejaVu Sans", "Liberation Sans", "Noto Sans Arabic"]
    else:  # macOS
        arabic_fonts = ["Arial Unicode MS", "Helvetica"]
    
    # Find available Arabic font
    available_fonts = font.families()
    selected_font = "Arial"  # Default fallback
    
    for arabic_font in arabic_fonts:
        if arabic_font in available_fonts:
            selected_font = arabic_font
            break
    
    # Configure default fonts
    root.option_add("*Font", f"{selected_font} 12")
    root.option_add("*Label.Font", f"{selected_font} 12")
    root.option_add("*Button.Font", f"{selected_font} 12 bold")
    root.option_add("*Entry.Font", f"{selected_font} 12")
    root.option_add("*Text.Font", f"{selected_font} 11")
    root.option_add("*Listbox.Font", f"{selected_font} 11")
    
    return selected_font

def format_arabic_text(text):
    """Format Arabic text for proper RTL display"""
    if not text:
        return ""
    
    try:
        # Reshape Arabic text
        reshaped_text = arabic_reshaper.reshape(str(text))
        # Apply bidirectional algorithm
        bidi_text = get_display(reshaped_text)
        return bidi_text
    except Exception as e:
        # Fallback to original text if formatting fails
        return str(text)

def create_arabic_label(parent, text, **kwargs):
    """Create a label with properly formatted Arabic text"""
    formatted_text = format_arabic_text(text)
    return tk.Label(parent, text=formatted_text, **kwargs)

def create_arabic_button(parent, text, command=None, **kwargs):
    """Create a button with properly formatted Arabic text"""
    formatted_text = format_arabic_text(text)
    return tk.Button(parent, text=formatted_text, command=command, **kwargs)

def create_arabic_entry(parent, **kwargs):
    """Create an entry widget optimized for Arabic input"""
    entry = tk.Entry(parent, **kwargs)
    # Set text direction to right-to-left
    entry.config(justify='right')
    return entry

def update_arabic_text(widget, text):
    """Update widget text with properly formatted Arabic"""
    formatted_text = format_arabic_text(text)
    widget.config(text=formatted_text)

class ArabicText(tk.Text):
    """Custom Text widget with Arabic support"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(wrap=tk.WORD)
        
        # Bind events for Arabic text handling
        self.bind('<KeyPress>', self.on_key_press)
    
    def on_key_press(self, event):
        """Handle Arabic text input"""
        # This can be extended for specific Arabic input handling
        pass
    
    def insert_arabic(self, index, text):
        """Insert Arabic text with proper formatting"""
        formatted_text = format_arabic_text(text)
        self.insert(index, formatted_text)
    
    def set_arabic_text(self, text):
        """Set the entire content with Arabic text"""
        self.delete(1.0, tk.END)
        formatted_text = format_arabic_text(text)
        self.insert(1.0, formatted_text)

def get_arabic_font_config(size=12, weight="normal"):
    """Get font configuration for Arabic text"""
    system = platform.system()
    
    if system == "Windows":
        font_family = "Tahoma"
    elif system == "Linux":
        font_family = "DejaVu Sans"
    else:  # macOS
        font_family = "Arial Unicode MS"
    
    return (font_family, size, weight)

def configure_arabic_widget(widget, **kwargs):
    """Configure widget for Arabic text display"""
    # Set font
    if 'font' not in kwargs:
        kwargs['font'] = get_arabic_font_config()
    
    # Set text alignment for RTL
    if hasattr(widget, 'config'):
        if isinstance(widget, (tk.Entry, tk.Text)):
            widget.config(justify='right', **kwargs)
        else:
            widget.config(**kwargs)
    
    return widget