# 1. Calculadora de Frete de E-commerce Uma loja virtual precisa de um sistema para 
# calcular o valor do frete. Crie uma função que receba a distância em quilômetros e o tipo de 
# cliente ("Padrão" ou "VIP"). A regra é: R
#  15,00. 0,50𝑝𝑜𝑟 𝑘𝑚 𝑟𝑜𝑑𝑎𝑑𝑜.𝑆𝑒 𝑎 𝑑𝑖𝑠𝑡â𝑛𝑐𝑖𝑎 𝑓𝑜𝑟 𝑚𝑎𝑖𝑜𝑟 q𝑢𝑒 100 𝑘𝑚,ℎá 𝑢𝑚𝑎 𝑡𝑎𝑥𝑎 𝑓𝑖𝑥𝑎 𝑎𝑑𝑖𝑐𝑖𝑜𝑛𝑎𝑙 𝑑𝑒 𝑅
# Clientes VIP recebem 20% de desconto no valor final do frete. Peça para o usuário inserir os 
# dados e exiba o resultado utilizando a função criada. 
taxa_base = 15.00
valor_km = 0.50
taxa_adicional = 15.00

def calcular_frete(distancia, tipo_cliente):
    frete = taxa_base + valor_km * distancia

    if distancia > 100:
        frete += taxa_adicional

    if tipo_cliente == "VIP":
        frete *= 0.80

    return frete

distancia = float(input("Digite a distancia em km: "))
tipo = input("Tipo de cliente (Vip ou Padrão): ").upper().strip()

valor = calcular_frete(distancia, tipo)
print(f"valor do frete: R$ {valor:.2f}")