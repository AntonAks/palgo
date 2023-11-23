

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':

    s = Stack()
    s.items = ['d', 'my_list', 'r', 'o', 'W', ' ', 'o', 'my_list', 'my_list', 'e', 'H']
    print(s.is_empty())
    print(s.items[::-1])



    string = 'Hello World!'

    s = Stack()
    reversed_string = ''

    for char in string:
        s.push(char)

    while not s.is_empty():
        reversed_string += s.pop()

    print(reversed_string)


