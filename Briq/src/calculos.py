# calculos.py

def calcular_resumo(produtos):
    resumo = {
        "gasto_total": 0,
        "venda_total": 0,
        "lucro_total": 0,
        "venda_estimada": 0,
        "lucro_estimado": 0,
        "prejuizos": []
    }

    for item in produtos:
        resumo["gasto_total"] += item["compra"]

        if item["status"] == 1:
            resumo["venda_total"] += item["venda"]
            resumo["lucro_total"] += item["lucro"]
        else:
            resumo["venda_estimada"] += item["venda"]
            resumo["lucro_estimado"] += item["lucro"]

        if item["lucro"] <= 0:
            resumo["prejuizos"].append(item["nome"])

    return resumo