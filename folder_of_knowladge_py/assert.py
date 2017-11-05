def new_funct(state):
    assert state,"U tink so?1"
 
def inputy(n):
    assert n>0, "Must be positive num"

n = input("Is 2 + 2 = 4? ")
state = 2+2==4
if n.lower() != "yes":
    state = False
   
new_funct(state)
print("Last output")
