def detail(roll):
 x = [23,43,22,56]
 if roll in x:
    print(f"Roll number {roll} is present")
 else:
    print(f"Roll number {roll} is absent")
roll = int(input("Enter roll no. "))
detail(roll)