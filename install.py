#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Installation Script for Arabic POS System
Installs required dependencies
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    
    try:
        # Upgrade pip first
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # Install requirements
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def create_desktop_shortcut():
    """Create desktop shortcut (Windows only)"""
    if os.name == 'nt':  # Windows
        try:
            import winshell
            from win32com.client import Dispatch
            
            desktop = winshell.desktop()
            path = os.path.join(desktop, "Arabic POS System.lnk")
            target = os.path.join(os.getcwd(), "main.py")
            wDir = os.getcwd()
            icon = target
            
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = sys.executable
            shortcut.Arguments = f'"{target}"'
            shortcut.WorkingDirectory = wDir
            shortcut.IconLocation = icon
            shortcut.save()
            
            print("✅ Desktop shortcut created!")
        except ImportError:
            print("⚠️ Could not create desktop shortcut (winshell not available)")
        except Exception as e:
            print(f"⚠️ Could not create desktop shortcut: {e}")

def main():
    """Main installation function"""
    print("=== Arabic POS System Installation ===")
    print()
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required!")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Install requirements
    if not install_requirements():
        print("❌ Installation failed!")
        sys.exit(1)
    
    # Create desktop shortcut
    create_desktop_shortcut()
    
    print()
    print("🎉 Installation completed successfully!")
    print()
    print("To run the application:")
    print(f"  python {os.path.join(os.getcwd(), 'main.py')}")
    print()
    print("Default master password: password")
    print()

if __name__ == "__main__":
    main()