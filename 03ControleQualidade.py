# 3. Controle de Qualidade na Fábrica Em uma linha de produção, as peças passam por uma 
# balança. O operador informará o peso de   peças (pergunte ao usuário quantas peças serão 𝑁
# pesadas antes de iniciar). Sem utilizar listas, crie um programa que determine e exiba no final 
# qual foi o peso da peça mais pesada e qual foi o peso da peça mais leve que passou pela 
# esteira naquele lote. 
n = int(input("Quantas peças serão pesadas? "))

for i in range(1, n + 1):
    peso = float(input(f"Peso da peça {i} (kg): "))

    if i == 1:
        mais_pesada = peso
        menos_pesada = peso
    else:
        if peso > mais_pesada:
            mais_pesada = peso
        if peso < menos_pesada:
            menos_pesada = peso

print(f"Peça mais pesada: {mais_pesada:.2f}kg")
print(f"Mais leve: {menos_pesada:.2f}kg")