filename = input("Enter file name: ")
try:
    with open(filename, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")