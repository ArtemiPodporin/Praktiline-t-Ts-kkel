#0
n = int(input())
i = 2
while i * i <= n:
    if n % i == 0:
        print(i)
        break
    i += 1
if i * i > n:
    print(n) 


#22
print("Ma tahan kommi")
katsed = 0
while True:
    answer = input("Tahan kommi!")
    katsed += 1
    if answer.lower() == "kommid":
        print(f"Teil kommid kirjutakse kulus {katsed} katse.")
        break
