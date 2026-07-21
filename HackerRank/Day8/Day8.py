# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Read all input at once from STDIN
input_data = sys.stdin.read().split()

if input_data:
    # 1. Number of entries in the phone book
    n = int(input_data[0])
    
    # 2. Build the phone book dictionary
    phone_book = {}
    index = 1
    for _ in range(n):
        name = input_data[index]
        phone = input_data[index + 1]
        phone_book[name] = phone
        index += 2
        
    # 3. Process the remaining queries
    queries = input_data[index:]
    for name in queries:
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
