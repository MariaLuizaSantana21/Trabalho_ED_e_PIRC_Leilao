from Leilão import Node, ArvoreBinaria
from arvorebinaria_exception import BinaryTreeException

print("leilão    Bem vindo!\n Estamos leiloando um Notebook!!!\n Prepare seus melhores lances e vamos lá!")
print("O lance inicial é R$30,00")
print()

arvore = ArvoreBinaria()
arvore.addLance(30)

for i in range(0,5):
   try:
      arvore.addLance(int(input()))
   
   except BinaryTreeException:
        print("Não é permitido valores negativos ou nulos. Faça um lance.")
   except ValueError:
       print("Por favor digite um valor válido. Letras e simbolos não são permitidos.")

arvore.traversal(ArvoreBinaria.inorder)
arvore.treeview()

   
   


