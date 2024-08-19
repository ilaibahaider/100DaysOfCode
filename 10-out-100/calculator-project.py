import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 /n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    should_continue = True
    n1 = float(input("Enter 1st number: "))
    while should_continue:
        operator = input("Choose an operation from below: \n '+' \n '-' \n '*' \n '/' \n")
        n2 = float(input("Enter next number: "))
        result = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        permission = input(f"Would you like to continue working with {result} results? Type 'yes' or 'no'\n")
        if permission == "yes":
            n1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()
