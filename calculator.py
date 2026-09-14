while True:

    while True:
        try:
            user_input = float(input("DO YOUR CALCULATION: "))
            break
        except ValueError:
            print("INVALID INPUT: TRY AGAIN")

    while True:
        user_operator = input("SELECT OPERATION: '+', '-', '*', '/':  ")
        if user_operator in ["+", "-", "*", "/"]:
            break
        else:
            print("INPUT A VALID OPERATION TRY AGAIN")

    while True:
        try:
            user_input2 = float(input("DO YOUR CALCULATION: "))
            break
        except ValueError:
            print("INVALID INPUT: TRY AGAIN")
            
    try:
        if user_operator == "+":
            result = user_input + user_input2
            print(result)
        elif user_operator == "-":
            result = user_input - user_input2
            print(result)
        elif user_operator == "*":
            result = user_input * user_input2
            print(result)
        elif user_operator == "/":
            result = user_input / user_input2
            print(result)
    except ZeroDivisionError:
        print("CANNOT DIVIDE BY ZERO")

    while True:
        calculate_again = input("DO YOU WANT ANOTHER CALCULATION? (yes/no): ")
        if calculate_again in ["yes", "no"]:
            break
        else:
            print("INVALID OPTION: OPTIONS ARE (yes OR no)")
    if calculate_again == "no":
        break
        
