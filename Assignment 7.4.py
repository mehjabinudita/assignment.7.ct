numbers = []  
while True:
    user_input = input("PLease enter an integer: ")

    if user_input == 'done':
        break 

    try:
        number = int(user_input)
        numbers.append(number)  
        if len(numbers) > 0:
            average = sum(numbers) / len(numbers)
            print(f"Average so far: {average:.2f}")
        else:
            print("Average so far: 0.00")
    except ValueError:
        print("Invalid input. Please enter an integer or 'done'.")

print("---------- Bye !! --------------")
