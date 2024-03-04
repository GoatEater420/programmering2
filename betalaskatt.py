pengar = float (input("dinna pengar = "))

if pengar < 85528:
    pengar = pengar * 0.32 + 14839.02
    
else: pengar = pengar * 0.18 + 556.02


print("skatt att betala", pengar, "Thalers")
