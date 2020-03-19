'''
通过两个栈来实现队列
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.b) == 0:
            while self.a:
                self.b.append(self.a.pop())
        return self.b.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.b) == 0:
            while self.a:
                self.b.append(self.a.pop())
        return self.b[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if (len(self.a) == 0) and (len(self.b) == 0):
            return True
        else:
            return False