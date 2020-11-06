
class PrimeGenerator:
    def __init__(self, stop=None):
        self.stop = stop
    def Prime_generator(self,bound):
      for n in range(2,bound):
        for x in range(2,n):
          if n % x==0:
              print(f"is  not a prime number")
          
          else:
            yield (f"{n} is a prime number")
            
          if n>=bound:
            self.stop = StopIteration()
            raise self.stop

l = PrimeGenerator()
pr = l.Prime_generator(12)
