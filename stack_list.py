class Stack:
    def __init__(self, limit=1000):
        self.__stack = []
        self.limit = limit

    def push(self, value):
        if len(self.__stack) < self.limit:
            self.__stack.append(value)
            return f"{value} added to stack. Stack length: {len(self.__stack)}"
        else:
            return "Stack is full"

    def pop(self):
        if len(self.__stack) > 0:
            return self.__stack.pop()
        else:
            return "Stack is empty"

    def clear(self):
        if len(self.__stack) > 0:
            cleared_items = []

            for item in reversed(self.__stack):
                cleared_items.append(self.__stack.pop())
            return cleared_items
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.__stack) == 0


stack = Stack(10)

print(stack.is_empty())

for i in range(11):
    print(stack.push(i))

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.push(200))
print(stack.clear())
print(stack.is_empty())
