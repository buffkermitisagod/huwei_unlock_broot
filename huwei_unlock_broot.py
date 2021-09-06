import itertools
import os
import subprocess

n = 16
os.system("fastboot rebboot bootloder")
while True:
    pro = itertools.product("1234567890", repeat=n)
    x = 0

    os.system("adb reboot fastboot")
    for i in pro:
        pas = str(i)
        pas = pas.replace("')","")
        pas = pas.replace("('","")
        pas = pas.replace("'","")
        pas = pas.replace(" ","")
        pas = pas.replace(",","")

        print("trying pin: "+pas)

        co = "fastboot oem unlock "+pas 

        output = subprocess.run(co, shell=True, capture_output=True, text=True)

        output = output.stdout
        output = str(output)

        if 'success' in output:
            bak = open("unlock_code.txt", "w")
            bak.write("Your saved bootloader code : "+pas)
            bak.close()
            print("Your bruteforce result has been saved in \"unlock_code.txt\"")

        else:
            print("Rebooting to prevent bootloader from rebooting...")
            os.system('fastboot reboot bootloader')
    n = n + 1
