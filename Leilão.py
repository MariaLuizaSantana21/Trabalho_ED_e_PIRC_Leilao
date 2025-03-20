from arvorebinaria_exception import BinaryTreeException

class Node:
    def __init__(self, lance = None):
        self.__lance = lance
        self.__esq = None
        self.__dir = None

    @property
    def lance(self):
        return self.__lance
    
    @lance.setter
    def lance(self, novo):
        self.__lance = novo
    
    @property
    def esq(self):
        return self.__esq
    
    @esq.setter
    def esq(self, novo):
        self.__esq = novo
    
    @property
    def dir(self):
        return self.__dir
    
    @dir.setter
    def dir(self, novo):
        self.__dir = novo
    

class ArvoreBinaria:
    def __init__(self):
        self.__root = None

    def addLance(self, lance):
        if self.__root == None:
            self.__root= Node(lance)
        else:
            self.__root = self.__add(self.__root, lance)

    def __add(self, node, lance):
        if lance <= node.lance:
           if node.esq != None:
               node.esq = self.__add(node.esq, lance)
           else:
              node.esq = Node(lance)
        else:
            if node.dir != None:
                node.dir = self.__add(node.dir, lance)
            else:
                node.dir = Node(lance)
        return node
    



