from Leilão import Node, ArvoreBinaria

arvore = ArvoreBinaria()
arvore.addLance(50)
arvore.addLance(30)
arvore.addLance(70)
arvore.addLance(40)
arvore.addLance(60)
   

arvore.traversal(ArvoreBinaria.inorder)


arvore.treeview()
