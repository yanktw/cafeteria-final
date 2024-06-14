import json

# Funções da cafeteria
def retornarLinha(indice):
    with open("cardapio.txt", "r", encoding="utf8") as arquivo:
        linha = arquivo.read().splitlines()
    cardapio = json.loads(linha[indice])
    return cardapio

def escrever_linhas(numero, conteudo):
    with open("cardapio.txt", "r", encoding="utf8") as arquivo:
        todas_linhas = arquivo.read().splitlines()
    todas_linhas[numero] = json.dumps(conteudo)
    with open("cardapio.txt", "w", encoding="utf8") as arquivo:
        for linha in todas_linhas:
            arquivo.write(f"{linha}\n")
            
def remover_linhas(numero, item):
    menu = retornarLinha(numero)
    if item in menu:
        del menu[item]
        escrever_linhas(numero, menu)
        print("Item removido com sucesso!")
    else:
        print("Item não encontrado no cardápio.")



# adicionar itens ao cardápio
def adicionar():
    print("(1)Bebidas")
    print("(2)Entradas")
    print("(3)Pratos Principais")
    print("(4)Sobremesas")
    print("(5)Sair")
    categoria = int(input("Digite a categoria do item que deseja adicionar: "))
    if categoria == 1:
        itemadd = input("Digite o item que deseja adicionar: ").lower() 
        valoradd = input("Digite o valor do item que deseja adicionar: ")
        menu = retornarLinha(0)
        menu[itemadd] = valoradd
        escrever_linhas(0, menu)
    elif categoria == 2:
        itemadd= input("Digite o item que deseja adicionar: ").lower() 
        valoradd= input("Digite o valor do item que deseja adicionar: ")
        menu = retornarLinha(1)
        menu[itemadd] = valoradd
        escrever_linhas(1, menu)
    elif categoria == 3: 
        itemadd= input("Digite o item que deseja adicionar: ").lower() 
        valoradd= input("Digite o valor do item que deseja adicionar: ")
        menu = retornarLinha(2)
        menu[itemadd] = valoradd
        escrever_linhas(2, menu)
    elif categoria == 4:
        itemadd= input("Digite o item que deseja adicionar: ").lower() 
        valoradd= input("Digite o valor do item que deseja adicionar: ") 
        menu = retornarLinha(3)
        menu[itemadd] = valoradd
        escrever_linhas(3, menu)
    elif categoria == 5:
        return True


# remover itens do cardápio

def remover():
    print("(1)Bebidas")
    print("(2)Entradas")
    print("(3)Pratos Principais")
    print("(4)Sobremesas")
    print("(5)Sair")
    categoria = int(input("Digite a categoria do item que deseja remover: "))
    if categoria in range(1, 5):
        print(retornarLinha(categoria - 1))
        itemrem = input("Digite o item que deseja remover: ").lower()
        remover_linhas(categoria - 1, itemrem)
    elif categoria == 5:
        return True



# alterar itens do cardapio

def alterar():
    print("(1)Bebidas")
    print("(2)Entradas")
    print("(3)Pratos Principais")
    print("(4)Sobremesas")
    print("(5)Sair")
    categoria = int(input("Digite a categoria do item que deseja alterar: "))
    if categoria == 1:
      itemalt = input("Digite o item que deseja alterar: ").lower()
      menu = retornarLinha(0)
      if itemalt in menu.keys():
        nomealt = input("Digite o novo nome do item: ").lower()
        valoralt = input("Digite o novo valor do item: ").lower()
        menu[nomealt] = valoralt
        del menu[itemalt]  
        escrever_linhas(0, menu)
      else:
        print("O item não existe, portanto não pode ser alterado.")

    elif categoria == 2:
        itemalt = input("Digite o item que deseja alterar: ").lower()
        menu = retornarLinha(1)
        if itemalt in retornarLinha(1).keys():
            nomealt = input("Digite o novo nome do item: ").lower()
            valoralt = input("Digite o novo valor do item: ").lower()
            menu[nomealt] = valoralt
            del menu[itemalt]
            escrever_linhas(1, menu)
        else:
            print("O item não existe, portanto não pode ser alterado.")

    elif categoria == 3:
        itemalt = input("Digite o item que deseja alterar: ").lower()
        menu = retornarLinha(3)
        if itemalt in retornarLinha(2).keys():
            nomealt = input("Digite o novo nome do item: ").lower()
            valoralt = input("Digite o novo valor do item: ").lower()
            menu[nomealt] = valoralt
            del menu[itemalt]
            escrever_linhas(2, menu)
        else:
            print("O item não existe, portanto não pode ser alterado.")

    elif categoria == 4:
        itemalt = input("Digite o item que deseja alterar: ").lower()
        menu = retornarLinha(3)
        if itemalt in retornarLinha(3).keys():
            nomealt = input("Digite o novo nome do item: ").lower()
            valoralt = input("Digite o novo valor do item: ").lower()
            menu[nomealt] = valoralt
            del menu[itemalt]
            escrever_linhas(3, menu)
        else:
            print("O item não existe, portanto não pode ser alterado.")

    elif categoria ==5:
       return True     



# buscar itens do cardapio

def buscar():
    procurar = (input("Digite o item que deseja verificar: ")).lower()
    if procurar in retornarLinha(0).keys():
        print("O item está no cardápio e na categoria bebidas")
        nomes = retornarLinha(0)
        print(nomes)
    elif procurar in retornarLinha(1).keys():
        print("O item está no cardápio e na categoria entradas")
        nomes = retornarLinha(1)
        print(nomes)
    elif procurar in retornarLinha(2).keys():
        print("O item está no cardápio e na categoria pratos principais")
        nomes = retornarLinha(2)
        print(nomes)
    elif procurar in retornarLinha(3).keys():
        print("O item está no cardápio e na categoria entradas")
        nomes = retornarLinha(3)
        print(nomes)
    else:
        print(f"O item {procurar} não está no cardápio")



# listar todos os itens do cardapio

def listar():
    print("==BEBIDAS==")
    print(retornarLinha(0))
    print("==ENTRADAS==")
    print(retornarLinha(1))
    print("==PRATOS PRINCIPAIS==")
    print(retornarLinha(2))
    print("==SOBREMESAS==")
    print(retornarLinha(3))



while True:
    print("(1) Adicionar itens ao cardápio")
    print("(2) Excluir itens do cardápio")
    print("(3) Alterar itens do cardápio")
    print("(4) Buscar itens no cardápio")
    print("(5) Listar todos os itens do cardápio")
    print("(6) Sair")
    escolha = int(input("Selecione o que deseja fazer agora: "))
    if escolha ==1:
        funcao1 = adicionar()
    if escolha == 2:
        funcao2 = remover()
    if escolha == 3:
        funcao3 = alterar()
    if escolha == 4:
        funcao4 = buscar()
    if escolha == 5:
        funcao5 = listar()
    elif escolha == 6:
        print("Saindo...")
        break
