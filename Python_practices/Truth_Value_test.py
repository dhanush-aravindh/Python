# False/0 and True/1
# Truth Value Testing:
# Constants defined to be false: None and False
# zero of any numeric type: 0,0.0,0j,Decimal(0),Fraction(0,1)
# Empty sequences and collections: '',{},[],(),set(),range(0)
# all the above mentioned elements takes the truth value as false as given in the documentation

python = 1

if python:
    print("Congrats you know python")

else:
    print("Go and Learn Python")

name = ""

if name:
    print(f"Hey {name}, cool name")

else:
    print("You don't have any name?")