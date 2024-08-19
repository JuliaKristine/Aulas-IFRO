par = []
impar = []
for i in range(10):
    print('Digite 10 números.')
    num = int(input(f"Digite um número : "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print("Números pares:", par)
print("Números ímpares:", impar)