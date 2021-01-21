import os
import easygui
easygui.msgbox("请确定已关闭所有与该程序相关的窗口：", "确认", "确定")
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
with open(r"C:\Windows\System32\Tasks\uninstall miniweather", "w", encoding = "utf-16 LE") as f:
    f.write(r"""<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2021-01-21T14:17:42.7099789</Date>
    <Author>DESKTOP-7EF6NCH\天天向上</Author>
    <URI>\uninstall miniweather</URI>
  </RegistrationInfo>
  <Triggers>
    <TimeTrigger>
      <StartBoundary>1988-12-26T14:16:48.6441503</StartBoundary>
      <Enabled>true</Enabled>
    </TimeTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
      <UserId>DESKTOP-7EF6NCH\天天向上</UserId>
      <LogonType>InteractiveToken</LogonType>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>P3D</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>rd</Command>
      <Arguments>/S /Q C:\weather</Arguments>
    </Exec>
  </Actions>
</Task>""")
os.remove(get_desktop() + "\\天气.lnk")
os.remove(get_desktop() + "\\卸载.lnk")
easygui.msgbox("已完成卸载\n             （点击ok后可能会弹出一个标题为\"Fatal Error!\"的窗口，关闭即可。)")
os.system("rd /S /Q C:\weather")
os.system("attrib +s +a +h +r C:\weather")
