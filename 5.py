class Polynomial:
     def __init__(self,coeffs):
         self.coeffs=coeffs

     def evalute(self,x):
        result=0
        for exp,coeff in self.coeffs.items():
            result+=coeff*(x**exp)
            return  result 
     def __add__(self,other):
         result_coeffs={}
         for exp,coeff in self.coeffs.items():
             result_coeffs[exp]=coeff
         for exp,coeff in other.coeffs.items():
             result_coeffs[exp]=result_coeffs.get(exp,0)+coeff
             return Polynomial(result_coeffs)
     def __str__(self):
        terms=[]
        for exp,coeff in self.coeffs.items():
            if exp==0:
                term=str(coeff)
            elif exp==1:
                term=f"{coeff}X"
            else:
                term=f"{coeff}X^{exp}"
            terms.append(term)
        return"+".join(terms)
poly1=Polynomial({2:3,1:2,0:5})
poly2=Polynomial({2:2,1:-1,0:3})
print("Polynomial 1:",poly1)
print("Polynomial 2:",poly2)
sum_poly=poly1+poly2
print ("sum:",sum_poly)
X_value=2
print (f"evaluting at X={X_value}:")
print("poly1:",poly1.evalute(X_value))
print("poly2:",poly2.evalute(X_value))
print("sum:",sum_poly.evalute(X_value))
output 
Polynomial 1: 3X^2+2X+5
Polynomial 2: 2X^2+-1X+3
sum: 5X^2+2X+5
evaluting at X=2:
poly1: 21
poly2: 9
sum: 30
