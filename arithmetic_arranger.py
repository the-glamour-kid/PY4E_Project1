def arranger(lst, control):
    result = []
    num1_lst = []
    num2_lst = []
    op_lst = []
    num = 0
    if len(lst) > 5:
        print("Error: More number of problems")
    else:
        for i, l in enumerate(lst):
            num3, op, num4 = l.split(" ")
            num1 = int(num3)
            num2 = int(num4)
            num1_lst.append(num1)
            num2_lst.append(num2)
            op_lst.append(op)
            if op == "-":
                num = num1 - num2
                result.append(num)
            elif op == "+":
                num = num1 + num2
                result.append(num)
            else:
                return "Error: Unsupported operand type"
        # printing first list items
        for i in range(len(lst)):
            if num1_lst[i] > 9999 or num2_lst[i] > 9999:
                print("Error: stack overflow")
            else:
                if num1_lst[i] > 0 and num1_lst[i] < 10:
                    print("  ", num1_lst[i], end="\t\t")
                elif num1_lst[i] > 10 and num1_lst[i] < 1000:
                    print("   ", num1_lst[i], end="\t\t")
                else:
                    print(" ", num1_lst[i], end="\t\t")
        print("\n")
        # printing second list items 
        for i in range(len(lst)):
                if num2_lst[i] > 0 and num2_lst[i] < 10:
                    print(op_lst[i], "  ", num2_lst[i], end="\t\t")
                elif num2_lst[i] > 10 and num2_lst[i] < 1000:
                    print(op_lst[i], " ", num2_lst[i], end="\t\t")
                else:
                    print(op_lst[i], "", num2_lst[i], end="\t\t")
        # printing result list
        print("\n")
        if control:
            for i in range(len(result)):
                print("  ", result[i], end="\t\t")
    print("\n")
