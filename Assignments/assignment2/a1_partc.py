# Copy over your a1_partc.py file here
class Stack:

    def __init__(self, cap=10):
        self.data = [None] * cap
        self.top = 0
        self.cap = cap
        self.used = 0

    def capacity(self):
        return self.cap

    def push(self, data):
        if self.used == self.cap:
            self.grow()
        self.data[self.top] = data
        self.top += 1
        self.used += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        self.top -= 1
        value = self.data[self.top]
        self.data[self.top] = None
        return value

    def get_top(self):
        return self.data[self.top - 1]

    def is_empty(self):
        return self.top == 0

    def __len__(self):
        return self.top

    def grow(self):
        new_cap = self.cap * 2
        new_data = [None] * new_cap
        for i in range(self.used):
            new_data[i] = self.data[i]
        self.data = new_data
        self.cap = new_cap


class Queue:
    def __init__(self, cap=10):
        self.data = [None] * cap
        self.front = 0
        self.back = 0
        self.cap = cap
        self.use = 0

    def capacity(self):
        return self.cap

    def enqueue(self, data):
        if self.use == self.cap:
            self.grow()
        self.data[self.back] = data
        self.back = (self.back + 1) % self.cap
        self.use += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        value = self.data[self.front]
        self.front = (self.front + 1) % self.cap
        self.use -= 1
        return value

    def get_front(self):
        if self.is_empty():
            return None
        return self.data[self.front]

    def is_empty(self):
        return self.use == 0

    def __len__(self):
        return self.use

    def grow(self):
        new_cap = self.cap * 2
        new_data = [None] * new_cap
        for i in range(self.use):
            new_data[i] = self.data[(self.front + i) % self.cap]
        self.data = new_data
        self.front = 0
        self.back = self.use
        self.cap = new_cap

class Deque:

    def __init__(self, cap=10):
        self.data=[None] *cap
        self.front=0
        self.back=0
        self.cap=cap
        self.used=0

    def capacity(self):
        return self.cap

    # resize cap grow double
    def grow(self):
        new_cap = self.cap*2
        new_data=[None] * new_cap
        for i in range(self.used):
            new_data[i] = self.data[(self.front + i) % self.cap]

        #update all member
        self.data=new_data
        self.front=0
        self.back=self.used
        self.cap=new_cap

    def push_front(self, data):
        if self.used==self.cap: # when it is full
            self.grow()

        # apply modulo x%y = x-y * floor(x/y)
        self.front=(self.front-1)% self.cap
        self.data[self.front]=data
        self.used +=1

    # same logic with push_front
    def push_back(self, data):
        if self.used==self.cap: # if full
            self.grow()

        self.data[self.back]= data
        self.back=(self.back+1) % self.cap # apply modulo
        self.used+=1

    def pop_front(self):
        if self.is_empty(): # empty list
            raise IndexError('pop_front() used on empty deque')

        remove = self.front
        value = self.data[remove] # get value
        self.front=(self.front+1)%self.cap # update self.front
        self.used-=1
        return value

    # same logic with pop_front()
    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')

        self.back = (self.back-1) % self.cap

        remove = self.back
        value = self.data[remove]

        self.used -= 1
        return value

    def get_front(self):
        if self.is_empty():
            return None
        return self.data[self.front]

    def get_back(self):
        if self.is_empty():
            return None
        return self.data[(self.back-1) % self.cap]

    def is_empty(self):
        return self.used==0

    def __len__(self):
        return self.used

    def __getitem__(self, k):
        if k<0 or k >= self.used:
            raise IndexError('Index out of range')
        idx = (self.front+k) % self.cap
        return self.data[idx]
