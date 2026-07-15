# Enter your code here. Read input from STDIN. Print output to STDOUT# Read the number of test cases
t = int(input().strip())

# Loop through each test case
for _ in range(t):
    s = input().strip()
    
    # Python Slicing magic:
    # s[::2] reads from start to end, skipping by 2 (even indices: 0, 2, 4...)
    # s[1::2] reads starting from index 1, skipping by 2 (odd indices: 1, 3, 5...)
    even_chars = s[::2]
    odd_chars = s[1::2]
    
    print(f"{even_chars} {odd_chars}")
