import os
# Function to clear the output.txt file
def clear_output_file():
    if os.path.exists("output.txt"):
        os.remove("output.txt")
        print("Previous messages cleared from output.txt.")