import os, json, time
from config import banner
from multiprocessing import cpu_count
from progress.spinner import MoonSpinner

cpu_thread = cpu_count()

def presetOne(): # zergpool
    os.system("@cls||clear")
    print("[--Time Zone--]\n"
    ," [1] Default\n"
    ," [2] North America\n"
    ," [3] Europe\n"
    ," [4] Asia")
    try:
        option = int(input(">>> "))
        if option > 4 or option < 1:
            raise Exception()
        elif option == 1:
            pool = "stratum+tcp://verushash.mine.zergpool.com:3300"
        elif option == 2:
            pool = "stratum+tcp://verushash.na.mine.zergpool.com:3300"
        elif option == 3:
            pool = "stratum+tcp://verushash.eu.mine.zergpool.com:3300"
        elif option == 4:
            pool = "stratum+tcp://verushash.asia.mine.zergpool.com:3300"
    except:
        os.system("@cls||clear")
        print("เลือก 1 - 4 เท่านั้น!")
        time.sleep(2)

    coin = input("เหรียญที่จะรับ: ")
    if coin == "":
        coin = "VRSC"

    wallet = input(f"ที่อยู่กระเป๋า {coin.upper()} : ")
    if wallet == "":
        os.system("@cls||clear")
        print("ข้อมูลไม่ถูกต้อง่!")
        time.sleep(2)
    
    nameWorker = input("ชื่อคนงาน: ")
    if nameWorker == "":
        nameWorker = "poppy"
    
    push = {
        'Pool': pool,
        'Wallet': wallet,
        'Pass': f"c={coin.upper()},mc=VRSC,ID={nameWorker}",
        'Cpu': cpu_thread-1
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(push, set, indent=4)



def presetTwo(): # luckpool
    os.system("@cls||clear")
    print("[--Time Zone--]\n"
    ," [1] North America\n"
    ," [2] Europe\n"
    ," [3] Asia-Pacific")
    try:
        option = int(input(">>> "))
        if option > 3 or option < 1:
            raise Exception()
        elif option == 1:
            pool = "stratum+tcp://na.luckpool.net:3956"
        elif option == 2:
            pool = "stratum+tcp://eu.luckpool.net:3956"
        elif option == 3:
            pool = "stratum+tcp://ap.luckpool.net:3956"
    except:
        os.system("@cls||clear")
        print("เลือก 1 - 4 เท่านั้น!")
        time.sleep(2)

    coin = input("pass[-p]: ")
    if coin == "":
        coin = "x"

    wallet = input("ที่อยู่กระเป๋า VRSC : ")
    if wallet == "":
        os.system("@cls||clear")
        print("ข้อมูลไม่ถูกต้อง่!")
        time.sleep(2)
    
    nameWorker = input("ชื่อคนงาน: ")
    if nameWorker == "":
        nameWorker = "poppy"

    push = {
        'Pool': pool,
        'Wallet': wallet+"."+nameWorker,
        'Pass': coin,
        'Cpu': cpu_thread-1
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(push, set, indent=4)


def saveMiner():
    pass

def editMiner():
    pass


# setting function
def custom():
    banner()
    try:
        print("ตัวอย่าง: \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
        pool = input("[-o]: ")

        print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.OMG-MINER\033[00m")
        wallet = input("[-u]: ")

        print("ตัวอย่าง: \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
        password = input("[-p]: ")

        print(f"\033[93mตัวอย่าง: 0 > {cpu_thread}\033[00m")
        cpu = int(input("[-t]: "))
        
        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
    except:
        print("\nเกิดข้อผิดพลาด มีบางอย่างไม่ถุูกต้อง!")
        time.sleep(2)
        custom()
    push = {
        'Pool': pool,
        'Wallet': wallet,
        'Pass': password,
        'Cpu': cpu
    }
    with open("set-miner/miner.json", "w") as set:
        json.dump(push, set, indent=4)




def router(option):
    if option == 1:
        presetOne()
    elif option == 2:
        presetTwo()
    elif option == 3:
        saveMiner()
    elif option == 4:
        editMiner()
    elif option == 5:
        custom()




while True:
    # check path & main process
    os.system("@cls||clear")
    with MoonSpinner("กำลังทำงาน...") as bar:
            for i in range(100):
                time.sleep(0.05)
                bar.next()
    if os.path.exists("set-miner") == True:
        banner()
        print(f"[--เมนู--]  \033[0;37;44mCPU = {cpu_thread}\033[0;37;40m\n"
        ," [1] Preset Zergpool\n"
        ," [2] Preset Luckpool\n"
        ," [3] ที่บันทึกไว้\n"
        ," [4] แก้ไขการตั้งค่าปัจจุบัน\n"
        ," [5] กำหนดเอง\n"
        ," [0] ออก")
        try:
            option = int(input(">>> "))
            if option > 5:
                raise Exception()
            elif option == 0:
                break
            router(option)
        except:
            os.system("@cls||clear")
            print("เลือก 1 - 5 และ 0 เท่านั้น!")
            time.sleep(2)

    else:
        os.system("mkdir set-miner")

