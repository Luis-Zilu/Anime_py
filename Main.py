import os
Animes = ["Animes em estoque\n","Yosuga no Sora\n", "Over flow\n", "Shoujo Ramune\n", "Harem Meikyuu\n"]
xxs = ["Acchi|\n", "Hentai\n", "Hentai\n", "Acchi\n", "Acchi\n"]
y = len(Animes)
while True:
    os.system("cls")
    print('''             
█▀█ █ █▀▀ ▄▀█ █▀█ █▀▄ █▀█   ▄▀█ █▄░█ █ █▀▄▀█ █▀▀ █▀
█▀▄ █ █▄█ █▀█ █▀▄ █▄▀ █▄█   █▀█ █░▀█ █ █░▀░█ ██▄ ▄█''')
    print('''Para acessar as opções escreva seu respectivo número:
        Ver animes em estoque [1]
        Venda seu mangá [2]
        Realize alterações nos Animes [3]
        Adicione um anime ao catálago [4]''')


    def Estoque():
        os.system("cls")
        for x in range(y):
            print(f"{x+1} {Animes[x]} {xxs[x]}")


    def Vandas(VerVendas):

        pass


    def AlterarEstoques(FazerAlteracoes):
        pass


    def CadastrarProduto(Cadastrar):
        pass

    while True:
        Comando = input("Selecione a opção desejada: ").lower()
        if Comando == "1" or "ver animes em estoque":
            Estoque()
            print('Para Voltar para o menu aperte \"Enter\"')
        DefComando = input("")
        if DefComando == "":
            break