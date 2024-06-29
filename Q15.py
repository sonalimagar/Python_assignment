input_string = "Hello, World!"
vowels = "aeiouAEIOU"
count =0
for char in input_string:
    if char in vowels:
        count += 1
print(f"number of vowels in {input_string} is =",count)
