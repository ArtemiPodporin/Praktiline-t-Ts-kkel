#0
for i in range(100):
    number = int(input("Sisestage number: "))
    if number >= 10:
        print("Õigesti")
        break
    else:
        print("Arv on liiga väike")


#22
print("Ma tahan kommi")
katsed = 0
while True:
    answer = input("Tahan kommi!")
    katsed += 1
    if answer.lower() == "kommid":
        print(f"Teil kommid kirjutakse kulus {katsed} katse.")
        break
