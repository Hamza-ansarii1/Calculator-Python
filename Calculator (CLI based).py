while True:
 print("Simple CLI Calculator")
 print("1. Addition (+)")
 print("2. Substraction (-)")
 print("3. Multiplication (x)")
 print("4. Division (/)")
 print("5. Exit")

 choice = input("choice operation (1-5) : ")

 if choice=="5":
    print("Calculator closed.")
    break
 
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))

 
 if choice =="1":
   print("Result:",num1 + num2)

 elif choice=="2":
   print("Result:",num1 - num2)  

 elif choice=="3":
   print("Result:",num1 * num2)

 elif choice=="4":
   if num2 !=0:
    print("Result:",num1 / num2)
   else:
     print("Error: Division by zero")

 else:
   print("Invalid choice. Try again.")        
