print("1.If you pick an apple a banana.\n""2.If you pick oranges you an pick grapes.\n""3.If you pick grapes you can pick bananas.")
choice = print(input("\nEnter the fruit you want and you will get another fruit: "))
if choice == 'apple':
    print("Banana")
elif choice == 'oranges':
    print("grapes")
else:
    print("Banana")