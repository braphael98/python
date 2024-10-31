numeros = [1,1,1,1,1,1]
soma = 0
try: 
    for numero in numeros:
        soma += numero
        print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    