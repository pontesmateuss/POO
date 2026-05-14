contagem = {}


while True:
    entrada = input("Ano em que nasceu: ")
    if entrada == "":
        break

    ano = int(entrada)
    contagem[ano] = contagem.get(ano, 0) + 1
print("\n" + "-" * 48)
print(f"{'Censo dos Anos':^40}")
print("-" * 48)
 
if not contagem:
    print("Nenhum dado encontrado.")
else:
    print(f"{'Ano':<15} {'Pessoas':>10}")
    print("-" * 48)

    for ano in sorted(contagem):
        print(f"{ano:<15} {contagem[ano]:>10}")
    print("-" * 48)
    print(f"{'Total':<15} {sum(contagem.values()):>10}")
 

print("-" * 48)