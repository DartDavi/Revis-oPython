# 5. Simulador de Rendimentos Crie uma função chamada calcular_juros que receba um 
# valor inicial, uma taxa de juros mensal e um número de meses. O programa deve usar um laço 
# de repetição dentro ou fora da função para calcular o crescimento do dinheiro mês a mês, 
# aplicando juros compostos. O programa deve imprimir o saldo ao final de cada mês. Se em 
# algum mês o saldo dobrar em relação ao valor inicial, o laço deve ser interrompido e uma 
# mensagem de "Meta Atingida antecipadamente!" deve ser exibida. 
def calcular_juros(valor_inicial, taxa_mensal, meses):
    saldo = valor_inicial

    for mes in range(1, meses + 1):
        saldo = saldo * (1 + taxa_mensal / 100)
        print(f"Mês {mes}: R$ {saldo:.2f}")

        if saldo >= 2 * valor_inicial:
            print("Meta Atingida antecipadamente!")
            break

    return saldo


valor = float(input("Valor inicial (R$): "))
taxa = float(input("Taxa de juros mensal (%): "))
qtd_meses = int(input("Número de meses: "))

saldo_final = calcular_juros(valor, taxa, qtd_meses)
print(f"Saldo final: R$ {saldo_final:.2f}")