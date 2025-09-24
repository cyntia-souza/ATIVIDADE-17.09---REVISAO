#Faça um programa que simule um caixa de supermercado. O programa deve solicitar o preço de vários produtos, 
#um por um. O programa deve parar de pedir preços quando o usuário digitar 0. No final, exiba o valor total da compra.
#O programa não deve aceitar valores negativos.


total_compra = 0

preco = float(input("Digite o valor do produto: "))

while preco != 0:
    total_compra = total_compra + preco

    preco = float(input("Digite o valor do produto (ou 0 para finalizar a compra): "))

print(f"O valor total da compra é: R${total_compra}")