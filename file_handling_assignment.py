
# Python script to create a file, read, append, and handle errors.

try:
    # Step 1: Writing to the file
    with open('my_file.txt', 'w') as f:
        f.write("Hello, this is the first line.")
        f.write("Here is a number: 42")
        f.write("Goodbye, end of initial content.")
    print("Initial content written to 'my_file.txt'.")
    
    # Step 2: Reading and displaying the file content
    with open('my_file.txt', 'r') as f:
        content = f.read()
        print("File content after writing:", content)

    
    # Step 3: Appending additional lines
    with open('my_file.txt', 'a') as f:
        f.write("Now we are adding more content.")
        f.write("The number 100 is here.")
        f.write("Appending is complete.")
    print("Additional content appended to 'my_file.txt'.")
    
    # Step 4: Reading and displaying the appended content
    with open('my_file.txt', 'r') as f:
        updated_content = f.read()
        print("File content after appending:", updated_content)


except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to write to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operation completed.")
