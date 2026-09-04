import exception_handling

print("--- Start of import_demo.py ---")
print("Module 'exception_handling' imported successfully.")
print("Notice that the menu from 'exception_handling.py' did not appear.")
print("This confirms that the 'if __name__ == \"__main__\":' block protected the code.")

print("\nNow calling a function from the imported module:")
print("Calling exception_handling.addition()...")

# This will ask for user input, just like in the original file
# exception_handling.addition()
# exception_handling.substraction()

print("\n--- End of import_demo.py ---")
