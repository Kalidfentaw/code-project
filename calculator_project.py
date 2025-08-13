def calculator ():
    print("standard calculator")
    try:
        while True:
            op = input("enter the operators [/,*,-,+,** and exit] = ")
            if op.lower().strip()=="exit":
                break
            list_op = ['+','-','*','/','**']
            if op not in list_op:
                print("please enter the correct oprator = ")
                continue

            numbers = []
            while True:
                number = input("please enter the number or = sign to calculate thr number = ").strip()
                if number =="=":
                    if len(numbers)<2:
                        print("please enter atleast 2 number = ")
                        continue
                    break
                try:
                    num = float(number)
                    numbers.append(num)
                except ValueError:
                    print("please enter only number = ")
                    continue

            """performing different arthimetic operations
            after performing arthimetic
            operations we have to store the result on some variable"""
            
            if op =="+":
                result = numbers[0]
                for item in numbers[1:]:
                    result =result + item 
                print(" + ".join(map(str, numbers)) + f" = {result}")
            elif op == "*":
                result = numbers[0]
                for item in numbers[1:]:
                    result = result * item
                print(" * ".join(map(str,numbers)) + f"  = {result}")
            elif op == "/":
                result = numbers[0]
                for item in numbers[1:]:
                    try:
                        if item ==0:
                            raise ZeroDivisionError()                      
                        result = result / item
                    except ZeroDivisionError:
                        print("denominator can not be zero = ")
                        continue
                print(" / ".join(map(str,numbers)) + f" = {result}") 
            if op =="-":
                result = numbers[0]
                for item in numbers[1:]:
                    result =result - item 
                print(" - ".join(map(str, numbers)) + f" = {result}")
            elif op == "**":
                result = numbers[0]
                for item in numbers[1:]:
                    result = result ** item
                print(" ** ".join(map(str,numbers)) + f" = {result}")



    except Exception as e:
        print(f"operation failed! {e}")
    print("Developed by: kalid F")


calculator()