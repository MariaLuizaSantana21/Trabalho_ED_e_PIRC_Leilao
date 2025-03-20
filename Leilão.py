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
    inorder   = 1
    
    def __init__(self):
        self.__root = None

    def estaVazia(self) ->bool:
        return self.__root == None

    def addLance(self, lance):
        if self.__root == None:
            self.__root= Node(lance)
        else:
            self.__root = self.__add(self.__root, lance)

    def __add(self, node: 'Node', lance):
        if lance >= node.lance:
           if node.dir != None:
               self.__add(node.dir, lance)
           else:
              node.dir = Node(lance)
        else:
            if node.esq != None:
                self.__add(node.esq, lance)
            else:
                node.esq = Node(lance)
        return node
    





    #Código do professor para testar a arvore e ver gráficamente se está funcionando



    def traversal(self, order:int = None):
        if order == self.__class__.inorder:
            self.__inorder(self.__root)
        else:
            raise ValueError('Invalid order value')
        print()


    def __inorder(self, node:'Node'):
        if( node != None):
            self.__inorder(node.esq)
            print(f'{node.lance} ',end='')
            self.__inorder(node.dir)



    def treeview(self):
        if self.__root is None:
            return
        lines, *_ = self.__visual(self.__root)
        for line in lines:
            print(line)

    def __visual(self, node:'Node'):
        # No child.
        if node.dir is None and node.esq is None:
            line = f'{node.lance}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.dir is None:
            lines, n, p, x = self.__visual(node.esq)
            s = f'{node.lance}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.esq is None:
            lines, n, p, x = self.__visual(node.dir)
            s = f'{node.lance}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x  = self.__visual(node.esq)
        right, m, q, y = self.__visual(node.dir)
        s = f'{node.lance}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2     
    
    






