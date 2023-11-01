# Program that opens this file, reads it, and prints the contents of the file
# to the screen
from pathlib import Path

# Accessing file in same directory
path = Path("pi_digits.txt")
contents = path.read_text().rstrip()
print(contents)
print(f"\nPath to file is: {path}")

# Accessing file in a sub-directory of current directory
# Relative path
path = Path("text_files/more_text.txt")
contents = path.read_text().rstrip()
print(contents)
print(f"\nPath to file is: {path}")

# Accessing file in a completely separate directory of current directory
# Absolute Path
path = Path("C:/Users/17732/Desktop/python_work/example_text_doc.txt")
contents = path.read_text().rstrip()
print(contents)
print(f"\nPath to file is: {path}")