# 4. Votação de Síndico Um condomínio está elegendo o novo síndico. Existem três candidatos 
# (1 - Ana, 2 - João, 3 - Maria). Crie um programa que receba os votos dos moradores 
# indefinidamente, até que o número 0 seja digitado para encerrar a urna. O programa deve 
# rejeitar votos inválidos (números diferentes de 0, 1, 2 e 3), pedindo que o usuário digite 
# novamente. Ao fim, exiba o total de votos de cada candidato e quem foi o vencedor.
votos_ana = 0
votos_joao = 0
votos_maria = 0

voto = int(input("Digite seu voto (1-Ana, 2-João, 3-Maria, 0 para encerrar): "))

while voto != 0:
    if voto == 1:
        votos_ana += 1
    elif voto == 2:
        votos_joao += 1
    elif voto == 3:
        votos_maria += 1
    else:
        print("Voto inválido! Digite 1, 2, 3 ou 0 para encerrar.")

    voto = int(input("Digite seu voto (1-Ana, 2-João, 3-Maria, 0 para encerrar): "))

print("\n--- Resultado da votação ---")
print(f"Ana: {votos_ana} voto(s)")
print(f"João: {votos_joao} voto(s)")
print(f"Maria: {votos_maria} voto(s)")

maior = max(votos_ana, votos_joao, votos_maria)

if maior == 0:
    print("Nenhum voto foi registrado.")
else:
    empatados = (votos_ana == maior) + (votos_joao == maior) + (votos_maria == maior)

    if empatados == 1:
        if votos_ana == maior:
            print("Vencedor(a): Ana")
        elif votos_joao == maior:
            print("Vencedor(a): João")
        else:
            print("Vencedor(a): Maria")
    else:
        print("Empate entre:")
        if votos_ana == maior:
            print("- Ana")
        if votos_joao == maior:
            print("- João")
        if votos_maria == maior:
            print("- Maria")