# produto.py

def cadastrar_produto(indice):
    print(f"\nCadastro do {indice}° item")

    nome = input("Nome do item: ")
    gasto = float(input("Valor de compra: R$ "))

    if input("Teve gasto com entrega? (S/N) ").lower() in ["s", "sim"]:
        gasto += float(input("Valor da entrega: R$ "))

    if input("Teve gasto com conserto/reforma? (S/N) ").lower() in ["s", "sim"]:
        gasto += float(input("Valor do serviço: R$ "))

    status = input("Status do item (1 - Vendido | 2 - Em estoque): ")

    venda = float(
        input("Valor de venda: R$ ")
    )

    lucro = venda - gasto

    return {
        "nome": nome,
        "compra": gasto,
        "venda": venda,
        "lucro": lucro,
        "status": int(status)
    }