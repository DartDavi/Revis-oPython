# 6. Sistema de Tarifas de Táxi Crie duas funções distintas: tarifa_diurna(distancia) e 
# tarifa_noturna(distancia). A tarifa diurna cobra R  2,50 por 4,00𝑑𝑒𝑏𝑎𝑛𝑑𝑒𝑖𝑟𝑎𝑑𝑎𝑚𝑎𝑖𝑠𝑅
# km. A noturna cobra R  3,20 por km. O programa principal deve usar 6,00𝑑𝑒𝑏𝑎𝑛𝑑𝑒𝑖𝑟𝑎𝑑𝑎𝑚𝑎𝑖𝑠𝑅
# um laço para atender vários passageiros ao longo do turno de um motorista. Para cada 
# passageiro, pergunte se a corrida foi de dia (D) ou de noite (N) e a distância. Chame a função 
# adequada e some o valor para o caixa do motorista. O turno acaba quando a distância 
# informada for negativa. 
BANDEIRADA_DIURNA = 4.00
KM_DIURNO = 2.50
BANDEIRADA_NOTURNA = 6.00
KM_NOTURNO = 3.20


def tarifa_diurna(distancia):
    return BANDEIRADA_DIURNA + KM_DIURNO * distancia


def tarifa_noturna(distancia):
    return BANDEIRADA_NOTURNA + KM_NOTURNO * distancia


caixa = 0
corridas = 0

distancia = float(input("Distância da corrida em km (negativa para encerrar o turno): "))

while distancia >= 0:
    periodo = input("A corrida foi de dia (D) ou de noite (N)? ").strip().upper()

    while periodo != "D" and periodo != "N":
        print("Opção inválida! Digite D ou N.")
        periodo = input("A corrida foi de dia (D) ou de noite (N)? ").strip().upper()

    if periodo == "D":
        valor = tarifa_diurna(distancia)
    else:
        valor = tarifa_noturna(distancia)

    caixa += valor
    corridas += 1
    print(f"Valor da corrida: R$ {valor:.2f}")

    distancia = float(input("Distância da corrida em km (negativa para encerrar o turno): "))

print("\n--- Fim do turno ---")
print(f"Corridas realizadas: {corridas}")
print(f"Total no caixa: R$ {caixa:.2f}")