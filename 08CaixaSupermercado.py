# 8. Caixa de Supermercado Faça um programa para registrar os itens da compra de um 
# cliente. O programa deve ler o preço e a quantidade de cada item continuamente. Se o preço 
# digitado for negativo, a compra é encerrada. Se o total da compra ultrapassar R$ 200,00, o 
# sistema deve aplicar um desconto de 10% sobre o total. Exiba o valor bruto, o valor do 
# desconto e o valor final a pagar. 
total = 0

preco = float(input("Preço do item (negativo para encerrar): R$ "))

while preco >= 0:
    quantidade = int(input("Quantidade: "))

    subtotal = preco * quantidade
    total += subtotal
    print(f"Subtotal do item: R$ {subtotal:.2f}")

    preco = float(input("Preço do item (negativo para encerrar): R$ "))

if total > 200:
    desconto = total * 0.10
else:
    desconto = 0

valor_final = total - desconto

print("\n--- Resumo da compra ---")
print(f"Valor bruto: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")