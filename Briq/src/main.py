# main.py

from produto import cadastrar_produto
from calculos import calcular_resumo

produtos = []
indice = 1

while True:
    produtos.append(cadastrar_produto(indice))
    indice += 1

    if input("Cadastrar novo item? (S/N) ").lower() in ["n", "nao", "não"]:
        break

resumo = calcular_resumo(produtos)

print("\n=== RESUMO ===")
print(f"Gasto total: R$ {resumo['gasto_total']:.2f}")
print(f"Vendas realizadas: R$ {resumo['venda_total']:.2f}")
print(f"Lucro obtido: R$ {resumo['lucro_total']:.2f}")
print(f"Vendas estimadas: R$ {resumo['venda_estimada']:.2f}")
print(f"Lucro estimado: R$ {resumo['lucro_estimado']:.2f}")

if resumo["prejuizos"]:
    print("Itens com prejuízo:", ", ".join(resumo["prejuizos"]))