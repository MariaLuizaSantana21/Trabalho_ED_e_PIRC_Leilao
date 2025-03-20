from Leilão import Node, ArvoreBinaria

arvore = ArvoreBinaria()
arvore.addLance(30)
arvore.addLance(40)
arvore.addLance(20)
arvore.addLance(35)
arvore.addLance(-60)
arvore.addLance(25)
arvore.addLance(80)
   

arvore.traversal(ArvoreBinaria.inorder)


arvore.treeview()
