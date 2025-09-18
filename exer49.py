salario_bruto = float(input("Digite o salário bruto: R$ "))

if salario_bruto <= 1412.00:
    inss = salario_bruto * 0.075
elif salario_bruto <= 2666.68:
    inss = salario_bruto * 0.09
elif salario_bruto <= 4000.03:
    inss = salario_bruto * 0.12
elif salario_bruto <= 7786.02:
    inss = salario_bruto * 0.14
else:
    inss = 7786.02 * 0.14

base_irrf = salario_bruto - inss

if base_irrf <= 2112.00:
    irrf = 0
elif base_irrf <= 2826.65:
    irrf = base_irrf * 0.075 - 158.40
elif base_irrf <= 3751.05:
    irrf = base_irrf * 0.15 - 370.40
elif base_irrf <= 4664.68:
    irrf = base_irrf * 0.225 - 651.73
else:
    irrf = base_irrf * 0.275 - 884.96

salario_liquido = salario_bruto - inss - irrf
print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")