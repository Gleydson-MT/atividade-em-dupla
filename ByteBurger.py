itens  = ["X-Burguer", "X-Salada", "Fritas", "Refrigerante", "Suco", "Sorvete"]
precos = [18.50,        21.00,      9.00,     6.50,           7.00,   8.00     ]

clientes = []
faturamento_dia = 0
todos_itens_vendidos = []
# Aqui o foco é imprimir primeiro o cardápio.
print(f"    ======CARDAPIO======     ")
for i, iten in enumerate(itens):
    print (f"{i+1} - {iten} ...... R$:{precos[i]:.2f}")
print()

#Aqui a ideia é armazenar o pedido do cliente dentro dessa repetição.

while True:
    print(f"Digite (fim), para encerrar o atendimento.")
    cliente = (input("Digite o nome do cliente: "))
    
    if cliente == "fim":
        break
    else:
        print(f"Bem vindo ao ByteBurguer\n Pedido em contrução...\n: ")
        pedido_atual = []
        preco_cliente_atual = []
    while True:
        resposta = (input("Digite o numero que repreta o produto do cliente\n (DIGITE 0 PARA SAIR): "))
        if resposta == "0":
            break
        else:
            resposta = int(resposta)
            indice = resposta -1
            pedido_atual.append(itens[indice])
            preco_cliente_atual.append(precos[indice])
            todos_itens_vendidos.append(precos[indice])
            print(f"{itens[indice]} adicionado ao pedido!")
#Aqui será adicionado o primeiro bônus: Remover intem !

if len(pedido_atual) >0:
    remover = input("\nDeseja remover algum intem? (s/n): ")
    if remover.lower() == "s":
        print("\n==== ITENS DO PEDIDO ====")

        for i, iten in enumerate(pedido_atual):
            print (f"{i+1} - {iten} ...... R$:{precos[i]:.2f}")
        posicao = int(input("Digite o número do item para remover: "))
        pedido_atual.pop(posicao -1)
        preco_cliente_atual(posicao -1)

        print("Item removido com sucesso!")

# Resumo do pedido
print(f"\n===== PEDIDO DO {cliente.upper()}=====")

for i, iten in enumerate(pedido_atual):
    print (f"{i+1} - {iten} ...... R$:{preco_cliente_atual[i]:.2f}")

total_pedido = sum(preco_cliente_atual)

# Essa linha de codigo ficou para o segundo bônus: DESCONTO!

if len(preco_cliente_atual) >= 4:
    desconto = total_pedido * 0.10
    total_final = total_pedido - desconto

    print(f"\nSubtotal: R$ {total_pedido:.2f}")
    print(f"Desconto de 10%: -R$ {desconto:.2f}")
    print(f"TOTAL FINAL: R$ {total_final:.2f}")

    total_pedido = total_final
else:
    print(f"TOTAL: R$ {total_pedido:.2f}")

# FECHAMENTO
clientes.append(cliente)
faturamento_dia += total_pedido

print(f"Pedido finalizado com sucesso!")

