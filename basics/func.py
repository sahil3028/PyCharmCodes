# -------- 1. Simple Function --------
def welcome():
    print("Welcome to the Utility App")

# -------- 2. Function with Parameters & Return --------
def add(a, b):
    return a + b

# -------- 3. Function with Default Argument --------
def power(num, exp=2):
    return num ** exp

# -------- 4. Function without Return --------
def show_message(msg):
    print("Message:", msg)

# -------- 5. *args (Variable Length Arguments) --------
def total_sum(*numbers):
    return sum(numbers)

# -------- 6. **kwargs (Keyword Arguments) --------
def show_profile(**details):
    print("User Profile:")
    for key, value in details.items():
        print(key, ":", value)

# -------- Program Execution --------
welcome()   # function call

result = add(10, 5)
print("Addition:", result)

print("Power (default exp):", power(4))
print("Power (custom exp):", power(4, exp=3))  # keyword argument

show_message("Learning Python for real projects")

print("Total Sum:", total_sum(1, 2, 3, 4, 5))

show_profile(name="Sahil", role="Developer", language="Python")

# -------- Built-in Function Example --------
print("Length of name:", len("Python"))