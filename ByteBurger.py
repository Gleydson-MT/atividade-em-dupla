itens  = ["X-Burguer", "X-Salada", "Fritas", "Refrigerante", "Suco", "Sorvete"]
precos = [18.50,        21.00,      9.00,     6.50,           7.00,   8.00     ]

cliente_do_dia = []
faturamento_dia = 0
# Aqui o foco é imprimir primeiro o cardápio.
print(f"    ======CARDAPIO======     ")
for i, iten in enumerate(itens):
    print (f"{i+1} - {iten} ...... R$:{precos[i]:.2f}")
print()

#Aqui a ideia é armazenar o pedido do cliente dentro dessa repetição.
pedido_atual = []
preco_cliente = []
while True:
    print(f"Digite (fim), para encerrar o atendimento.")
    cliente = (input("Digite o nome do cliente: "))
    cliente_do_dia.append
    if cliente == "fim":
        break
    else:
       print(f"Bem vindo ao ByteBurguer\n Pedido em contrução...\n: ")
    while True:
#Aqui eu fiquei em duvida, se ele digitar "0" sai do programa, mas ao mesmo tempo no enumerate o primeiro indíce repreta o número "0".
        resposta = (input("Digite o numero que repreta o produto do cliente\n (DIGITE 0 PARA SAIR): "))
        if resposta == "0":
            break
        else:
            resposta = preco_cliente
            print(preco_cliente)