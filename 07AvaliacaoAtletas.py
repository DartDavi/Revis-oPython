# 7. Avaliação Física de Atletas Um preparador físico precisa avaliar o Índice de Massa 
# Corporal (IMC) de um grupo de atletas. Crie uma função que receba o peso e a altura, calcule 
# o IMC e retorne a classificação (Abaixo do peso, Normal, Sobrepeso, etc.). No programa 
# principal, faça um laço que pergunte os dados de vários atletas. O programa deve parar 
# quando o nome do atleta for "FIM". Ao final, exiba quantos atletas estão na categoria 
# "Normal".
def classificar_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


total_normal = 0

nome = input("Nome do atleta (ou FIM para encerrar): ").strip()

while nome.upper() != "FIM":
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    classificacao = classificar_imc(peso, altura)
    print(f"{nome}: {classificacao}")

    if classificacao == "Normal":
        total_normal += 1

    nome = input("Nome do atleta (ou FIM para encerrar): ").strip()

print(f"\nAtletas na categoria Normal: {total_normal}")