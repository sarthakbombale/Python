def my_function():
    print("Hello My_Function")
my_function()

def greet_by_name(name):
    print(f'Hellow {name} Bhai whats up!! ')
greet_by_name("Harry")

def calculate_tax(bill_amount):
    tax = bill_amount * 0.18
    return tax
    
final_tax = calculate_tax(500)
print(f'Your tax amount is {final_tax}')

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32) * 5 / 7
    
print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(64))

def get_greeting():
    return "WE GET GRETINGS"
greeting = get_greeting()
print(greeting)

print(get_greeting())

def is_password_safe(password):
    if len(password) >= 8:
      return True
    else:
      return False

user_input = "pass123"
if is_password_safe(user_input) == True:
    print("password accepted")
else:
    print("Registration failed: Password is too short.")

def format_currency(amount):
    return f"${amount:,.2f}"

def calculate_discount(price, discount_percentage):
    return price * (discount_percentage / 100)

total_price = 1000
discount_amount = calculate_discount(total_price, 15)
print(format_currency(discount_amount))

def create_user_session(username,role="guest"):
    return f'User login with {username} role is {role}'
print(create_user_session("Sarthak", "admin"))
print(create_user_session("Harry")) 

def send_notification(message, channel="email"):
    return f"Sending alert via {channel}: {message}"

print(send_notification("Your order shipped", "sms"))
print(send_notification("Welcome to our app"))

def format_percentage(value):
    return f"{value}%"

def calculate_tax(subtotal, tax_rate):
    return subtotal * (tax_rate / 100)

order_subtotal = 500
tax_paid = calculate_tax(order_subtotal, 18)
print(format_percentage(18))

def send_notification(message, channel="email"):
    return f"Sending alert via {channel}: {message}"

print(send_notification("Your order shipped", "sms"))
print(send_notification("Welcome to our app"))

def format_currency(amount):
    return f"${amount:,.2f}"

def calculate_discount(price, discount_percentage):
    return price * (discount_percentage / 100)

total_price = 1000
discount_amount = calculate_discount(total_price, 15)
print(format_currency(discount_amount))

def check_email_domain(email):
    if email.endswith("@gmail.com"):
        return True
    else:
        return False

user_email = "test@gmail.com"
if check_email_domain(user_email) == True:
    print("Email approved")
else:
    print("Registration failed: Only Gmail addresses allowed.")
