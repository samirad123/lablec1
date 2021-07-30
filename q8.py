A = int(input("Enter number A: "))
B = int(input("Enter number B: "))
C = int(input("Enter number C: "))
if A > B and A > C:
    print(f"{A} is the largest number")
elif B > A and B > C:
    print(f"{B} is the largest number")
else:
    print(f"{C} is the largest number")