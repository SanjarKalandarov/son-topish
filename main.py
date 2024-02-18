import random
import math



def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Kattaroq son ayting:", end="")
        elif taxmin > tasodifiy_son:
            print("Kichikroq son ayting:", end="")
        else:
            print("Yutdingiz!")
            break
            return taxminlar
            print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")

def men_oylagan_sonni_top(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
        )
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar


def play(x=10):
    yana=True
    while True:
        taxminlar_user=sontop(x)
        taxminlar_pc=men_oylagan_sonni_top(x)
        if taxminlar_user>taxminlar_pc:

            print("men Yutdim")

        elif taxminlar_user<taxminlar_pc:
            print("siz Yutdingiz")
        else:
            print("durrang")

            yana=input("Yana o'ynaysizmi? ha(1)/yo'q(0)")

play()