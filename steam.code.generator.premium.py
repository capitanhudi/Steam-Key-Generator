from time import sleep
import random
import string
import os

letters = string.ascii_uppercase  # Letter array.
numArr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letterProb = 6  # Probability of next char going to be letter (letterProb / (numProb + letterProb))
numProb = 4  # Probability of next char going to be number (numProb / (numProb + letterProb))


def GetRandomLetter():
    return random.choice(letters)


def GetRandomNumber():
    return random.choice(numArr)


def GetRandomChar():
    x = round(random.random(), 3)
    if x < letterProb / (numProb + letterProb):
        return GetRandomLetter()
    else:
        return GetRandomNumber()


def GetRandomWord(length: float = 5):
    word = ""
    for i in range(length):
        word += GetRandomChar()
    return word


def PrintWithAnimation(value, speed: float = 0.1):
    for i in str(value):
        print(i, end="")
        sleep(speed)
    print("")


def CreateFile(name: str):
    fileCreated = False
    x = 0
    while not fileCreated:
        fname = name
        if x != 0:
            fname += "(x)".replace("x", str(x))

        try:
            return open(fname + ".txt", "x")
        except:
            x += 1


def GiveKeys(_file):
    x = input("Kaç tane key istiyon:")
    try:
        for i in range(int(x)): None
        PrintWithAnimation("Dosya oluşturuluyor...", 0.25)
        PrintWithAnimation("Dosya başarıyla oluşturuldu!")
        PrintWithAnimation("Dosya yazılıyor...", 0.25)
        for i in range(int(x)):
            key = GetRandomWord() + "-" + GetRandomWord() + "-" + GetRandomWord()+"\n"
            ff = open(_file, "a")
            ff.write(key)
            ff.close()
        PrintWithAnimation("Dosya başarıyla yazıldı!")
    except:
        print("SAYI GİR!!!")
        GiveKeys(_file)


PrintWithAnimation("By Hudi")
f = CreateFile(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') +"\SteamKodları")
GiveKeys(f.name)
PrintWithAnimation("Masaüstüne bak ;)")

input()
