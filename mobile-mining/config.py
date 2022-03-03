import os, json, requests

def versionApp():
    with open("version.json", encoding="utf-8") as read:
        load = read.read()
        loads = json.loads(load)
        return loads['version']

# banner function
def banner():
    url = "http://mobile-mining.tk/api/app_update/versionApp.php"
    receive = requests.get(url)
    s = receive.json()

    os.system("@cls||clear")
    print(f"Created by.mobile-mining V{versionApp()}")
    print("---------------------------------------------------") 
    print("\033[96mสนับสนุนนักพัมนา\033[00m\n"
        + " กสิกรไทย: 0608905863\n"
        + "     LTC:  LTT2X57ervCMpfNva5uo1JBzT2UJVBiEZu\n"
        + "    DOGE:  DFwUqKS3j3RMMkqQF8z6kbYZ652M8VCFVs")
    print("---------------------------------------------------")
    if versionApp() != s[0]:
        print(f"\n\033[1;31;40mมีเวอร์ชั่นใหม่กว่าคือ {s[0]} กรุณาอัพเดท!\033[0m\n")