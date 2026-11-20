"""
Supermercado, pedidos através de um menu e deixar o cliente escolher e somar os valores no fim.

"""

with open("Supermercado_menu.txt", "r", encoding="utf-8") as ficheiro:
    leitor = ficheiro.read()

    print("#"*10, "Menu Supermercado", "#"*10)
    print(leitor,"\n")
    linhas = leitor.splitlines()

    menu ={}
        
    for linha in linhas:
        if linha.strip():
        #   print(linha)
            partes_linha = linha.split(":")
            produtos = partes_linha[0].strip().lower()
            valor_texto = partes_linha[1].strip().lower().replace("€", "").replace(",", ".")
            preco_limpo = float(valor_texto)
            menu[produtos]= preco_limpo
            #print (menu)

    carrinho=[]
    total = 0.0

    while True:
        compra = input("Qual o item da lista acima que deseja adicionar ao seu carrinho (ou digite fim para acabar as suas compras): ")

        if compra.strip().lower() == "fim":
            break

        if compra.strip().lower() in menu:
            preco_produto = menu[compra.strip().lower()]
            total += preco_produto
            encontrado = False

            for produto in carrinho:
                if produto["nome"] == compra.strip().lower():
                    produto["quantidade"] += 1
                    encontrado = True
                    break
            
            if not encontrado:
                produto = {
                    "nome": compra.strip().lower(),
                    "preço": preco_produto,
                    "quantidade": 1
                }
                carrinho.append(produto)
            print(f"{compra.title()} foi adicionado ao carrinho, com o valor {preco_produto:.2f}€")
        else:
                    print(f"{compra} não existe no nosso menu")

    
    print(f"="*10,"Carrinho final", "="*10)
    print(f"Produto - Quantidades - Preço")

    for produto in carrinho:
        print(f"{produto['nome']} => {produto['quantidade']} => {produto['preço']:.2f} €")

    print("="*30)

    print(f"O seu total é: {total:.2f} €")

