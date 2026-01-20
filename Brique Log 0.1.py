vendas = []
preju = []
i = 0
lucrototal = 0
lucroestimado = 0
vendaestimada = 0
gastototal = 0
vendatotal = 0
prejutotal = 0

def cadastrar_produto():
  print(f"Cadastro do {i+1}° item")
  nome = input("Qual o nome do seu item? ")
  gasto = float(input("Quanto você gastou nele? "))
  log = input("Você teve algum gasto para entregar?(S/N)")
  if log.lower() in ["s", "sim", "ss"]:
    log_valor = float(input("Qual o valor gasto na entrega? "))
    gasto += log_valor
  tax = input("Você teve algum gasto para consertar e ou reformar?(S/N) ")
  if tax.lower() in ["s",  "sim", "ss"]:
      tax_valor = float(input("Qual o valor gasto no serviço? "))
      gasto += tax_valor
      
  option = input("Esse item configura qual das opções? \n1. Vendido\n2. Em estoque")
  if option == "1":
    status = 1
    venda = float(input("Por quanto você vendeu ele? "))
  elif option == "2":
      status = 2
      venda = float(input("Por quanto você pretende vender ele? "))
  else:
    print("Responsta inválida")
      
  lucro = venda - gasto
    
  ficha = {
    "nome": nome,
    "compra": gasto,
    "venda": venda,
    "lucro": lucro,
    "status": status
  }
  print(f"{nome} cadastrado com sucesso!")
  return ficha
  
while True:
  item_novo = cadastrar_produto()
  vendas.append(item_novo)
  i += 1
  continuar = input("Quer cadastrar um novo item? (S/N)")
  if continuar in ["n", "N", "não", "não"]:
    break
  
for item in vendas:
  gastototal += item["compra"]
  if item["status"] == 1:
    vendatotal += item["venda"]
    lucrototal += item["lucro"]
  elif item["status"] == 2:
    vendaestimada += item["venda"]
    lucroestimado += item["lucro"]
    
  if item["lucro"] <= 0:
    prejutotal += item["lucro"]
    preju.append(item["nome"])
  
print("="*30)
print("   RESUMO DE GASTOS/GANHOS   ")
print("="*30)
print("\nATÉ O MOMENTO -")
print(f"\nGastos totais: R${gastototal}")
print(f"Vendas realizadas: R${vendatotal}")
print(f"Lucro obtido: R${lucrototal}")
print("—"*15)
print("\nGANHOS ESTIMADOS -")
print(f"\nVendas à realizar: R${vendaestimada}")
print(f"Lucro estimado: R${lucroestimado}")

if prejutotal < 0:
  valor_bonito = prejutotal * -1
  nomes_colados = ", ".join(preju)
  print("! !"*15)
  print(f"O(s) seu(s) produto(s): {nomes_colados} teve ou tiveram um prejuízo de R${valor_bonito}")