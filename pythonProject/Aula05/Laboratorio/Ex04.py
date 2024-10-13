valorCompra = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

valorTotal = 0
desconto = 0
if parcelas == 1:
    desconto = valorCompra * (10/100)
    valorTotal = valorCompra - desconto

    parcela = valorTotal / parcelas
    if valorCompra > 5000:
        desconto = valorCompra * (15 / 100)
        valorTotal = valorCompra - desconto

        parcela = valorTotal / parcelas
elif parcelas == 2 or parcelas == 3:
    desconto = valorCompra * (5 / 100)
    valorTotal = valorCompra - desconto

    parcela = valorTotal / parcelas
    if valorCompra > 5000:
        desconto = valorCompra * (10 / 100)
        valorTotal = valorCompra - desconto

        parcela = valorTotal / parcelas
elif parcelas > 3:
    desconto = 0
    valorTotal = valorCompra - desconto

    parcela = valorTotal / parcelas
    if valorCompra > 5000:
        desconto = valorCompra * (5 / 100)
        valorTotal = valorCompra - desconto

        parcela = valorTotal / parcelas

print("Desconto total:", "%.2f" % desconto)
print("Valor final da compra com desconto:", "%.2f" % valorTotal)
print("Cada parcela será de:", "%.2f" % parcela)
