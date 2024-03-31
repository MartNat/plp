# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with a mix of text and numbers: 7, 8, 9\n")
except IOError as e:
    print("Error:", e)
finally:
    file.close()

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError as e:
    print("Error:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
except PermissionError as e:
    print("Error:", e)
finally:
    file.close()
