import random

# Get input range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Generate a random number within the range
random_number = random.randint(start, end)

# Print the random number
print(f"The random number is : {random_number}")

# Check if the random number is Positive or Negative
if random_number >= 0:
    print(f"{random_number} is Positive.")
else:
    print(f"{random_number} is Negative.")
