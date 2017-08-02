class add :    
   def sum(self,a,b):        
       self.a=a        
       self.b=b
   def printsum(self) :        
       print('sum' ,(self.a + self.b))
       
c=int( input("enter no 1: "))
d=int( input("enter no 2: "))
addi = add()
addi.sum(c,d)
addi.printsum()
