#new_lnk.py
from win32com.shell import shell, shellcon
import subprocess
import winreg
import pythoncom
import os
from win32com.shell import shell
a=shell.SHGetSpecialFolderPath(0,shellcon.CSIDL_COMMON_STARTMENU)
def get_desktop():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
	return winreg.QueryValueEx(key, "Desktop")[0]
def create_shortcut(fname,lname):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink
    )
    shortcut.SetPath(fname)
    shortcut.SetDescription(os.path.basename(lname))
    shortcut.SetIconLocation(fname,0)
    persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
    persist_file.Save(lname,0)
fname = os.getcwd() + r"\\main.exe"
lnkname =  get_desktop() + "\\天气.lnk"
create_shortcut(fname, lnkname)
create_shortcut(os.getcwd() + "\\uninstall.exe", get_desktop() + "\\卸载.lnk")