def lin():
    print("-" *40)


def calcular_desconto(preco):
  porcentagem = preco * 0.10
  return porcentagem
desconto = calcular_desconto(200)
preco_final = 200 - desconto
print("Desconto aplicado:" , desconto)
print("preco final:" , preco_final)

lin()

def dobro(a):
   dobro = a * 2
   print(f"O dobro do número é: {dobro}")
   return dobro
dobro(5)
#bnnnn