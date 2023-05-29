def Fibonacci(n):
    if n<0:
        raise ValueError("n tem que ser maior do que zero")
    if n==0:
        return 0 
    if n==1:
        return 1 
    else:
        a,b = 0, 1 
        for _ in range(2, n + 1):
            a,b = b, a +b 
        return b    
numero = int(input("Digite o valor de n: "))
try:
    resultado = Fibonacci (numero)
    print(f"fibonacci{numero}: {resultado}")
except ValueError as error:
    print(error)
