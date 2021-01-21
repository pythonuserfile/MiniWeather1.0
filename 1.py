import ctypes, sys, os, time


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def admin_exe() :
    if is_admin():
        print("admin_exe函数内，以管理员权限运行")
        time.sleep(10)
        os.system("taskkill /im explorer.exe /f")
        time.sleep(100)
    else:
        if sys.version_info[0] == 3:
            print('admin_exe函数内，还没有管理员权限')
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            time.sleep(100)
                                                      


if __name__ == '__main__':
    print("admin_exe前")
    admin_exe()
    print("admin_exe后")
