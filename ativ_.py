nomes = []
def adicionar_nome(): 
    input("Digite um nome: ") 
    nomes.append(nomes) 
    def listar_nomes(): 
        for nome in nomes: 
            print(nome) 
            adicionar_nome() 
            listar_nomes()