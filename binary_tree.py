class BinaryTree:
    def em_ordem(self, arvore):
        if arvore != None:
            self.em_ordem(arvore.esq)
            print(arvore.lance, end='')
            self.em_ordem(arvore.dir)


