class Stack():
    def __init__(self):
        self.items = []

    def is_Empty(self):
		'''判空'''
        return self.items == []

    def push(self,item):
		'''入栈'''
        self.items.append(item)

    def pop(self):
		'''出栈'''
        return self.items.pop()

    def peek(self):
        '''返回栈顶元素'''
        return self.items[len(self.items)-1]

    def size(self):
		'''返回大小'''
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    s.push('hello')
    s.push('world')
    s.push('python')
    print(s.size())
    print(s.peek())
    s.pop()
    s.pop()
    s.pop()
