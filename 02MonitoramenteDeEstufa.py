# 2. Monitoramento de Temperatura em Estufa Um agricultor possui uma estufa e um sensor 
# de temperatura que faz leituras constantes. Escreva um programa que leia continuamente a 
# temperatura registrada (em graus Celsius) até que o usuário digite um valor de parada (por 
# exemplo, -99). Ao final, o programa deve exibir: 
# ●  A temperatura média do período. 
# ●  Quantas vezes a temperatura ultrapassou a marca de perigo (acima de 35°C).
parada = -99
limite_perigo = 35

soma = 0
quantidade = 0
acima_limite = 0

temp = float(input("Digite a temperatura em °C (-99 para encerrar): "))

while temp != parada:
    soma += temp
    quantidade += 1

    if temp > limite_perigo:
        acima_limite += 1

    temp = float(input("Digite a temperatura em °C (-99 para encerrar): "))

if quantidade > 0:
    media = soma / quantidade
    print(f"Temperatura média: {media:.2f} °C")
    print(f"Vezes acima de {limite_perigo} °C: {acima_limite}")
else:
    print("Nenhuma leitura foi registrada.")