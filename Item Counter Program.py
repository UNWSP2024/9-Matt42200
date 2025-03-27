try:
    with open('names.txt', 'r') as file:
        names = file.readlines()
        
        num_names = len(names)
        
        print(f"The number of names in the file is: {num_names}")
except FileNotFoundError:
    print("The file 'names.txt' was not found.")