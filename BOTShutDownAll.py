from colorama import init as colorama_init
import os
from colorama import Fore
import subprocess
from colorama import Style

def main():
    os.system('cls')
    colorama_init()
    print(f'{Fore.CYAN}')
    print('Shuting down following programs:')
    print(f'{Style.RESET_ALL}')
    print(f'{Fore.GREEN}')
    os.system("taskkill /f /im Code.exe")
    os.system("taskkill /f /im GitHubDesktop.exe")
    os.system("taskkill /f /im Postman.exe")
    os.system("taskkill /f /im discord.exe")
    os.system("taskkill /f /im steam.exe")
    os.system("taskkill /f /im stremio.exe")
    os.system("taskkill /f /im anki.exe")
    os.system("taskkill /f /im Taskmgr.exe")
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im firefox.exe")
    os.system("taskkill /f /im Skype.exe")
    os.system("taskkill /f /im msedge.exe")
    print(f'{Style.RESET_ALL}')
    

if __name__ == '__main__':
    main()