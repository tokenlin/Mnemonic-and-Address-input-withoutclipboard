import pyautogui
import sys
import time

print("助记词或地址输入-防剪切板木马")
print("版本号：v1.0.0")
print("开发者：cavin0405.eth")
print("twitter：@cavin0405")
print("")
print("")

def getMnemonicandAddressof(SN):    
    csvpath = 'SN_Mnemonic_Address_Remark.csv'
    with open(csvpath, mode="r") as fr:
        for line in fr:
            if line != "":
                _linelist = line.strip().split(",")
                if _linelist[0] == SN:
                    return _linelist[0], _linelist[1], _linelist[2] # SN, mnemonic, address

    return False, False, False

SN = input("请输入需要读取的序号：") 
inputlist = getMnemonicandAddressof(SN)
if inputlist[0] == False:
    print("########## 输入错误，退出！")
    sys.exit() 


mnemonicoraddress = input("读取助记词还是地址？（1-助记词；2-地址）：")
if mnemonicoraddress != '1' and mnemonicoraddress != '2':
    print("########## 输入错误，退出！")
    sys.exit() 
    
    
isformetamask = ''
if mnemonicoraddress == '1': # 助记词
    isformetamask = input("是否在Metamask的恢复页面上使用？（0-否；1-是）") 
    if isformetamask != '0' and isformetamask != '1':
        print("########## 输入错误，退出！")
        sys.exit()      


print("请把焦点放在第1个输入框上：")
time.sleep(3)

mnemonic = ''
address = ''


if inputlist[1] != False:
    mnemonic = inputlist[1]
if inputlist[2] != False:
    address = inputlist[2]


output = ''
if mnemonicoraddress == '1' and isformetamask == '0': # 助记词，不在小狐狸上
    output = mnemonic
elif mnemonicoraddress == '1' and isformetamask == '1': # 助记词，在小狐狸上
    output = mnemonic.replace(" ", "\t\t")
elif mnemonicoraddress == '2':
    output = address
else:
    print("########## 输入错误，退出！")
    sys.exit() 

pyautogui.write(output) # 不需要经过剪切板
print("########完成输入：", output)
time.sleep(60)
