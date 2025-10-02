class A:
    def action(self):
        print("A")

class B(A):
    def action(self):
        print("B")
        super().action() # Викликає наступний метод у MRO (Якщо закоментувати цей рядюк, то викличеться тільки D і B)

class C(A):
    def action(self):
        print("C")
        #super().action() # Викликає наступний метод у MRO

class D(B, C):
    def action(self):
        print("D")
        super().action()
        
d = D()
d.action()