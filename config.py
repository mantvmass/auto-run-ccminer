import os

# banner function
def banner():
    os.system("@cls||clear")
    print("Created by.mobile-mining V2.1")
    print("---------------------------------------------------") 
    print("\033[96mสนับสนุนนักพัมนา\033[00m\n"
        + " กสิกรไทย: 0608905863\n"
        + "     LTC:  LTT2X57ervCMpfNva5uo1JBzT2UJVBiEZu\n"
        + "    DOGE:  DFwUqKS3j3RMMkqQF8z6kbYZ652M8VCFVs")
    print("---------------------------------------------------\n")






    
# def set_miner():
#     banner()
#     pool = None
#     wallet = None
#     password = None
#     cpu = None
#     try:
#         print("ตัวอย่าง: \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
#         pool = input("Pool[-o]: ")

#         print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.OMG-MINER\033[00m")
#         wallet = input("Wallet[-u]: ")

#         print("ตัวอย่าง: \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
#         password = input("Password[-p]: ")

#         print("\033[93m 0 ขึ้นไป หรือ เท่ากับจำนวณเธรดCPUท่าน เช็ค 'lscpu'\033[00m")
#         cpu = int(input("CPU[-t]: "))

#         if pool == "" or wallet == "":
#             raise Exception()
#         if password == "":
#             password = "x"
#         if cpu == "":
#             cpu = 1
#     except:
#         print("\nเกิดข้อผิดพลาด มีบางอย่างไม่ถุูกต้อง!")
#         time.sleep(2)
#         set_miner()
#     puts = {
#         'Pool': pool,
#         'Wallet': wallet,
#         'Pass': password,
#         'Cpu': cpu
#     }
#     with open("set-miner/miner.json", "w") as set:
#         json.dump(puts, set, indent=4)

