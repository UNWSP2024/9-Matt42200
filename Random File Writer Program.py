import random


num_numbers = int(input("Enter how many random numbers you want in the file (up to 1000): "))


if 1 <= num_numbers <= 1000:
    with open('random_numbers.txt', 'w') as file:
        # Write the specified number of random numbers to the file
        for _ in range(num_numbers):
            random_number = random.randint(1, 500)  # Generate a random number between 1 and 500
            file.write(f"{random_number}\n")  # Write the random number to the file, followed by a newline


    print(f"Successfully written {num_numbers} random numbers to 'random_numbers.txt'.")
else:
    print("Please enter a number between 1 and 1000.")