import os
Animes = [
    "One piece",
    "Dragon Ball (Super)"
]
Generos = [
    "Aventura e comédia",
    "Ação e aventura"
]
Mangas = [
    "20th Century Boys",
    "Fullmetal Alchemist",
    "Attack on Titan"
]
Quantidade = [
    2,
    3,
    4
]
def Estoque():
    os.system("cls")
    print("Animes em estoque:")
    for x in range(len(Animes)):
        print(f"[{x+1 }]{Animes[x]}: {Generos[x]}")
    print("\nEstoque de mangás:")
    for x in range(len(Mangas)):
        print(f"[{x+1}] {Mangas[x]}")


def Vendas():
    os.system("cls")
    print("Mangás disponíveis para venda:")
    for x in range(len(Mangas)):
        print(f"[{x+1}] {Mangas[x]}| Quantidade: {Quantidade[x]}")
    try:
        comprar = int(input("Compra: ")) -1
    except ValueError:
        print("Digite o número do mangá: ")
    if 0=< comprar < len(Quantidade):
        input

def AlterarEstoques(FazerAlteracoes):
    os.system("cls")
    if FazerAlteracoes == 1:
        escolha = int(input("Escolha qual mangá deseja alterar: ")) -1
        Mangas[escolha] = input("Faça as alterações: ").capitalize()
                

    elif FazerAlteracoes == 2:
        escolha = int(input("Digite o número do Anime que deseja alterar: ")) - 1
        Animes[escolha] = input("Digite a alteração: ")
        for x in range(len(Animes)):
            print(Animes[x])


def CadastrarProduto(Cadastrar):
    Anime_Modificado = []
    Mangas_Modificado = []
    if Cadastrar == "1":
            A_dd = input("Digite o anime: ")
            Anime_Modificado.append(A_dd)
            Animes.extend(Anime_Modificado)
            for x in range(len(Anime_Modificado)):
                print(f"[{x+1}] {Anime_Modificado[x]}")
                
    elif Cadastrar == "2":
            A_ddM = input("Adicione seu mangá: ")
            Mangas.append(A_ddM)
            Mangas_Modificado.extend(Mangas)
            for x in range(len(Mangas_Modificado)):
                print(f"[{x+1}] {Mangas_Modificado[x]}")
                
while True:
    os.system("cls")
    print('''             
█▀█ █ █▀▀ ▄▀█ █▀█ █▀▄ █▀█   ▄▀█ █▄░█ █ █▀▄▀█ █▀▀ █▀
█▀▄ █ █▄█ █▀█ █▀▄ █▄▀ █▄█   █▀█ █░▀█ █ █░▀░█ ██▄ ▄█''')
    print('''Para acessar as opções escreva seu respectivo número:
        Ver animes em estoque [1]
        Compre seu mangá [2]
        Cadastre seu mangá [3]
        Sair [0]''')
    PSair = input("Caso deseja sair, se não aperte \"enter\": ")
    if  PSair == "0":
        os.system("cls")
        break
    while True:
        Comando = input("Selecione a opção desejada: ").lower()
        if Comando == "1" or Comando == "ver animes em estoque":
            Estoque()
            print('Para Voltar para o menu aperte \"Enter\"')
            input()
            break

        elif Comando == "desenvolvedor":
            mode = int(input("Escolha sua alteração: Mangá [1], Animes[2]: "))
            AlterarEstoques(mode)
            print("Para voltar ao menu aperte \"Enter\"")
            input()
            break
 
 
 
        elif Comando == "2":
            Vendas()
            input()
            break


        elif Comando == "":
            break
        
        elif Comando == "3":
            Cadastro = input("Escolha entre anime [1] ou mangá [2]: ")
            CadastrarProduto(Cadastro)
            break