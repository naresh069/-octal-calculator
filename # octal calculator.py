# octal calculator
def add_in_octal(num1, num2):
    # Convert the integers to octal
    num1 = abs(num1)
    num2 = abs(num2)
    octal_num1 = oct(num1)[2:]  # Slice to remove the '0o' prefix
    octal_num2 = oct(num2)[2:]
    
    # Convert octal back to decimal for addition
    sum_decimal = int(octal_num1, 8) + int(octal_num2, 8)
    
    # Convert the sum back to octal
    octal_sum = oct(sum_decimal)[2:]
    
    return octal_sum

# Example usage
print("Enter two integers:")
do:
    try:
        in1, in2 = input().split()
    except EOFError:
        pass
    num1 = int(in1)
    num2 = int(in2)
    result = add_in_octal(num1, num2)
    print(result)
while True