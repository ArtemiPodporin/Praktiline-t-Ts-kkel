#0
p=0
while True:
    number = int(input("Sisestage number suurem kui 10: "))
    p+=1
    if number >= 10: 
        print("Õigesti")
        break
    else:
        print("Arv on liiga väike")
print("katsed",p)


#22
print("Ma tahan kommi")
katsed = 0
while True:
    answer = input("Tahan kommi!")
    katsed += 1
    if answer.lower() == "kommid":
        print(f"Teil kommid kirjutakse kulus {katsed} katse.")
        break
