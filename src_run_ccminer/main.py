import os
import json
import time
import pip
from config import banner



# check import module
try:
    from progress.spinner import MoonSpinner
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.spinner import MoonSpinner

try:
    import requests
except ImportError:
    pip.main(['install', '--user', 'requests'])
    import requests





# install miner function 
def install():
    try:
        # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
        os.system("git clone https://github.com/mantvmass/ccminer_mmv")
        os.system("@cls||clear")
        print("\nกำลังติดตั้ง...\n")
    except:
        print("ติดตั้งไม่สำเร็จ!")


# run miner function
def run():
    banner()
    with open("set-miner/miner.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        miner = loads['MINER']
        nameMiner = loads['NAME']
        cpu = loads['CPU']

    if miner == "":
        print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
        return
   
        

    try:
        url = f"http://mobile-mining.tk/api/v1/get-read-specific.php?tag_name={miner}"
        receive = requests.get(url)
        s = receive.json()
        print("\033[1;34;40m")   
        print("TAG    =  ",s['tag_name'])
        print("WALLET =  ",s['wallet']+"."+nameMiner)
        print("POOL   =  ",s['pool'])
        print("PASS   =  ",s['password'])
        print("\033[00m\n")
        time.sleep(6)
        os.system(f"cd ccminer_mmv && ./ccminer -a verus -o {s['pool']} -u {s['wallet']}.{nameMiner} -p {s['password']} -t {cpu}")
    except:
        push = {'MINER': '','CPU': 1}
        with open("set-miner/miner.json", "w") as set:
            json.dump(push, set, indent=4)

    # print(s['id'])
    # print(s['tag_name'])
    # print(s['pool'])
    # print(s['wallet'])
    # print(s['password'])


while True:
    os.system("@cls||clear")
    with MoonSpinner("กำลังทำงาน...") as bar:
        for i in range(100):
            time.sleep(0.05)
            bar.next()
    if os.path.exists("ccminer_mmv") == False:
        install()
        break
    if os.path.exists("set-miner") == True:
        if os.path.isfile("set-miner/miner.json") == True:
            run()
            break
        else:
            os.system("@cls||clear")
            print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
    else:
        os.system("@cls||clear")
        print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")





























# import os, json, time, pip
# from config import banner



# # check import module
# try:
#     from progress.spinner import MoonSpinner
# except ImportError:
#     pip.main(['install', '--user', 'progress'])
#     from progress.spinner import MoonSpinner






# # install miner function 
# def install():
#     try:
#         # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
#         os.system("git clone https://github.com/mantvmass/ccminer_mmv")
#         os.system("@cls||clear")
#         print("ติดตั้งสำเร็จ")
#     except:
#         print("ติดตั้งไม่สำเร็จ!")


# # run miner function
# def run():
#     banner()
#     with open("set-miner/miner.json", encoding="utf-8") as set:
#         load = set.read()
#         loads = json.loads(load)
#         pool = loads['Pool']
#         wallet = loads['Wallet']
#         password = loads['Pass']
#         cpu = loads['Cpu']
#     if pool == "" or wallet == "":
#         print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
#         return
#     print("ccminer CPU3.7 for VerusHash v2.1 - 2.2 by Monkins1010 based on ccminer")
#     print("Originally based on Christian Buchner and Christian H. project")
#     os.system(f"cd ccminer_mmv && ./ccminer -a verus -o {pool} -u {wallet} -p {password} -t {cpu}")




# while True:
#     os.system("@cls||clear")
#     with MoonSpinner("กำลังทำงาน...") as bar:
#         for i in range(100):
#             time.sleep(0.05)
#             bar.next()
#     if os.path.exists("ccminer_mmv") == False:
#         install()
#         break
#     if os.path.exists("set-miner") == True:
#         if os.path.isfile("set-miner/miner.json") == True:
#             run()
#             break
#         else:
#             os.system("@cls||clear")
#             print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
#     else:
#         os.system("@cls||clear")
#         print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")