#my module, a calculator

def Calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operationo ==  'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a/b
        if b != 0:
            return a/b
        else:
            return "Error, invalid operation "
    else: 
        return "Error: invalid input"