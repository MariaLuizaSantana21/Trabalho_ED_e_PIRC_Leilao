from Leilão import ArvoreBinaria
from arvorebinaria_exception import BinaryTreeException

print("--------Bem Vindo ao Leilão!!!----------\n Estamos leiloando um Notebook!!!\n Prepare seus melhores lances e vamos lá!")
print("O lance inicial é R$30,00")
print()

arvore = ArvoreBinaria()
arvore.addLance(30)

for i in range(0,5):
   try:
      arvore.addLance(int(input("R$" )))
   
   except BinaryTreeException:
        print("Não é permitido valores negativos ou nulos. Faça um lance.")
   except ValueError:
       print("Por favor digite um valor válido. Letras e simbolos não são permitidos.")

print()
print("Valores em Ordem:")
arvore.traversal(ArvoreBinaria.inorder)
print()
print("A arvore fica assim:")
arvore.treeview()
print()

   
maiorlance = arvore.buscarmaior()
print("O ganhador do Leilão é: \nUsuário Fulado com maior lance de: R$",maiorlance.lance)
   


