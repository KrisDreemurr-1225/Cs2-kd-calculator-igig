import time

def ask_for_again():
    while True:
        ask = input("Wanna try again? ").lower()
        if ask == "no":
            for i in range(1000):
                print("You made me feel sad :d")
        elif ask == "yes":
            print("Yay :D")
            break
        else:
            print("Think harder")

def calculate():
    while True:

        global kd

        kills = float(input("Enter your kills here! "))
        if kills == 0:
            print("No, u cant")
            break

        deaths = float(input("Enter your deaths here! "))
        if deaths == 0:
            print("No, you can't")
            break

        kd = kills/deaths

        print("-----ANALYSING YOUR AMAZING RESULT-----")
        time.sleep(2)

        print("Your kd is,", kd)
        break

kd = 0

print("Welcome to the kd-ratio calculator! Here, by typing ur stats, you will get your total kd! Enjoy!")

time.sleep(3)

while True:

    calculate()

    ask_for_again()


