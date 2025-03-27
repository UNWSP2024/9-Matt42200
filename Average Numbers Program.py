def calculate_total(filename):
    try:
        with open(filename, 'r') as file:
            total = 0
            for line in file
                try:
                    number = int(line.strip())  # Remove any extra spaces or newlines
                    total += number  # Add the number to the total
                except ValueError:
                    print(f"Warning: Skipping invalid data '{line.strip()}' that is not a valid integer.")
            return total
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError:
        print(f"Error: An unexpected I/O error occurred while accessing the file '{filename}'.")
        return None


filename = 'numbers.txt'  # The file containing the integers
total = calculate_total(filename)


if total is not None:
    print(f"The total of the numbers in '{filename}' is: {total}")