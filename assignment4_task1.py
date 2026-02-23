try:
    # Opening the file in read mode
    with open("sample.txt", "r") as file:
        # Reading and printing line by line
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

except Exception as e:
    print("An unexpected error occurred:", e)