# 1️⃣ Creating a dictionary
students = {
    "Ayush": 85,
    "Rahul": 78,
    "Priya": 92,
    "Neha": 88
}

# 2️⃣ Taking user input
name = input("Enter the student's name: ")

# 3️⃣ Retrieving and displaying marks
if name in students:
    print(f"{name}'s marks are:", students[name])
else:
    # 4️⃣ If name not found
    print("Student not found in the record.")