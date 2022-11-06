# Be sure you've done pip install z3-solver
from telnetlib import X3PAD
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
def hw2():
    
    
    # Create z3 variable(s) representing the unknown
    # Here, the unknown, x, is the square root of n.
    X, Y, Z = Bools('X Y Z')
    
    s = Solver()
    
    # 1. X ∨ Y, X ⊢ ¬Y 
    # As proposition in PL: ((X \/ Y) /\ X) -> ~Y
    C1 = Implies(And(Or(X,Y),X),Not(Y))
    
    s.add(Not(C1))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C1",s)
    # otherwise return inconsistent value for error
    
        
    #2. X, Y ⊢ X ∧ Y
    s.reset()
    C2 = Implies(And(X,Y),And(X,Y))
    
    s.add(Not(C2))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C2",s)
    #3. X ∧ Y ⊢ X
    s.reset()
    C3 = Implies(And(X,Y),X)
    
    s.add(Not(C3))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C3",s)
    
    #4. X ∧ Y ⊢ Y
    s.reset()
    C4 = Implies(And(X,Y),Y)
    
    s.add(Not(C4))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C4",s)
    
    #5. ¬¬X ⊢ X
    s.reset()
    C5 = Implies(Not(Not(X)),X)
    
    s.add(Not(C5))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C5",s)
        
    #6. ¬(X ∧ ¬X)
    s.reset()
    C6 = Not(And(X,Not(X)))
    
    s.add(Not(C6))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C6",s)

    #7. X ⊢ X ∨ Y
    s.reset()
    C7 = Implies(X,Or(X,Y))
    
    s.add(Not(C7))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C7",s)
        
    #8. Y ⊢ X ∨ Y
    s.reset()
    C8 = Implies(Y,Or(X,Y))
    
    s.add(Not(C8))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C8",s)
    
    #9. X → Y, ¬X ⊢ ¬ Y 
    s.reset()
    C9 = Implies(X,Y)
    
    s.add(Not(C9))
    # I believe it's not valid
  
    r = s.check()
    
    # If there's a model/solution return it 
    valid(r,"C9",s)
    
def valid(r,st,s):
    if r == unsat:
        print("Is Valid:" ,st) 
    else:
        print ("Is not Valid,", st, "Counter example", s.model())
    
        
    
hw2()