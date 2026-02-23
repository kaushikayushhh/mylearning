data = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data written successfully.")

# 2️⃣ Append additional data
more_data = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(more_data + "\n")

print("Data appended successfully.")

# 3️⃣ Read and display final content
print("\nFinal content of the file:")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)