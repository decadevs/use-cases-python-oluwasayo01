# Document at least 3 use cases of iterators

class MyIterator: 

    def __init__(self, limit): 
        self.limit = limit 
  
    def __iter__(self): 
        self.x = 1
        return self
  
    def __next__(self): 
   
        x = self.x 
  
        if x > self.limit: 
            raise StopIteration 
  
        self.x = x + 1
        return x

class MyIteratorTwo: 

    def __init__(self, limit): 
        self.limit = limit 
  
    def __iter__(self): 
        self.x = 1
        return self
  
    def __next__(self): 
   
        x = self.x 
  
        if x > self.limit: 
            raise StopIteration 
  
        self.x = x + 1

class MyIteratorThree:

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
