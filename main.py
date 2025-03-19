from Leilão import Node
from binary_tree import BinaryTree

if __name__ == "__main__":
    raiz = Node(1)
    raiz.esq = Node(2)
    raiz.dir = Node(4)

    p = raiz.esq
    q = raiz.dir

    p.esq = Node(5)
    p = p.esq

    p.dir = Node(6)

    q.esq = Node(7)
    q.dir = Node(11)

    q = q.esq

    q.esq = Node(3)
    q.dir = Node(8)

    arvore = BinaryTree()
    arvore.em_ordem(raiz)



