class Stack():
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        '''返回栈顶元素'''
        return self.items[len(self.items)-1]

    def size(self):
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