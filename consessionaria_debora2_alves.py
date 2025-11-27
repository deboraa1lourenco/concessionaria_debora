print("--- BEM VINDO(A) A CONSESSIONÁRIA G&F ---")
print("Serviços oferecidos: Compra, venda e aluguel de caminhões")

print("\n=== CADASTRO DE CLIENTE ===")
cadastro_cliente = {}
cadastro_cliente["nome"] = input("Digite seu nome: ")
cadastro_cliente["telefone"] = int(input("Digite seu número de telefone para contato: "))
cadastro_cliente["saldo_inicial"] = float(input("Qual seu saldo inicial? "))

print("\n=== DADOS CADASTRADOS ===")
for chave, valor in cadastro_cliente.items():
    print(f"{chave}: {valor}")

tabela_veiculos = {
    "FH 540": 85600.69,
    "R450": 20900.47, 
    "Actros 2651": 800000.00
}

veiculos_disp_aluguel=[
    ("FH 540", "Volvo"), 
    ("R450", "Scania"), 
    ("Actros 2651", " Mercedes-Benz")
]

veiculos_disp_venda= [
    ("FH 540", "Volvo"), 
    ("R450", "Scania"), 
    ("Actros 2651", " Mercedes-Benz")
]

def menu():
    print("\n===MENU===")
    print("1 - Vender carro")
    print("2 - Alugar carro")
    print("3 - Comprar carro")
    print("4 - Ver saldo")
    print("0 - Sair")

def venda_veiculo():
    print("\n--- VENDA DE VEÍCULO ---")

    modelo = input("DIgite o modelo do caminhão que deseja vender: ")
    marca = input("DIgite a marca do caminhão que deseja vender: ")

    if modelo not in tabela_veiculos:
        print("Infelizmente não compramos caminhões com essa descrição...")
        return 
    
    valor_pre_definido = tabela_veiculos[modelo]
    proposta = valor_pre_definido *0.88

    print(f"\nValor de referência: R$ {valor_pre_definido:.2f}")
    print(f"\nProposta fornecida: R$ {proposta:.2f}")

    confirmacao = input("Deseja vender o veículo? (s/n): ").lower()

    if confirmacao == "s":
        cadastro_cliente["saldo_inicial"] += proposta

        veiculos_disp_venda.append((modelo,marca)) #um para adiconar outro para separar a marca e modelo
        print("Veículo vendido com sucesso!")
    
    else:
        print("Venda cancelada.")
    
def alugar_veiculo():
    print("\n--- CAMINHÕES PARA ALUGUEL ---")

    if not veiculos_disp_aluguel:
        print("Não há veículos disponíveis para aluguel.")
        return
    
    print("\nCaminhões disponíveis:")
    for i, veiculo in enumerate(veiculos_disp_aluguel):
        print(f"{i + 1} - {veiculo[0]} ({veiculo[1]})")

    escolha = int(input("Escolha o número do caminhão: ")) - 1

    if escolha < 0 or escolha >= len(veiculos_disp_aluguel):
        print("Opção inválida.")
        return
    
    dias = int(input("\nPor quantos dias deseja alugar? "))
    valor_total = dias * 285

    print(f"Valor total do aluguel: R$ {valor_total:.2f}")

    if cadastro_cliente["saldo_inicial"] < valor_total:
        print("Infelizmente você não tem saldo suficiente.")
        return
    
    confirmacao = input("\nConfirmar aluguel? (s/n): ").lower()
    if confirmacao == "s":
        # Atualiza saldo do cliente
        cadastro_cliente["saldo_inicial"] -= valor_total

        # Remove o livro da lista de aluguel
        livro = veiculos_disp_aluguel.pop(escolha)

        print(f"Parabens! Você acabou de alugar '{veiculo[0]}'.")
    else:
        print("Aluguel cancelado.")

def comprar_veiculo():
    print("\n--- COMPRA DE CAMINHÃO ---")
    if not veiculos_disp_venda:
        print("Não há caminhões disponíveis para venda.")
        return

    print("\nCaminhões à venda:")
    for i, veiculo in enumerate(veiculos_disp_venda):
        print(f"{i + 1} - {veiculo[0]} ({veiculo[1]})")

    escolha = int(input("Escolha o número do caminhão que deseja: ")) - 1

    if escolha < 0 or escolha >= len(veiculos_disp_venda):
        print("Opção inválida.")
        return
    
    marca = veiculos_disp_venda[escolha][0]

    valor_base = tabela_veiculos[marca]
    valor_final = valor_base * 1.25

    print(f"Valor do caminhão escolhido : R$ {valor_final:.2f}")

    if cadastro_cliente["saldo_inicial"] < valor_final:
        print("Saldo insuficiente.")
        return
    
    confirmacao = input("Confirmar compra? (s/n): ").lower()
    if confirmacao == "s":
        cadastro_cliente["saldo_inicial"] -= valor_final
    
        veiculo = veiculos_disp_venda.pop(escolha)

        print(f"Você comprou '{veiculo[0]}'.")
    else:
        print("Compra cancelada.")

while True:
    menu()

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            venda_veiculo()
        case "2":
            alugar_veiculo()
        case "3":
            comprar_veiculo()
        case "4":
            print(f"\nSaldo atual: R$ {cadastro_cliente['saldo_inicial']:.2f}")
        case "0":
            print("Saindo do sistema. Até logo!")
            break  
        case _:
            print("Opção inválida. Tente novamente.")
