nomes = []
def adicionar_nome():
    nome = input("digite um nome: ")
    nomes.append(nome)
def listar_nomes():
    for nome in nomes:
        print(nomes)
adicionar_nome()
listar_nomes()