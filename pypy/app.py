weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    convert = weight / 0.45
    print("Weight in Lbs " + str(convert))
else:
    convert = weight * 0.45
    print("Weight in Kg " + str(convert))
exit()