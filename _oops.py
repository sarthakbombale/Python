class User:
    def __init__(self, username, email, role="guest"):
        self.username = username
        self.email = email
        self.role = role

    def upgrade_membership(self, new_role):
        self.role = new_role
        return f"{self.username} upgraded to {self.role}"

user1 = User("sarthak_dev", "sarthak@email.com")
user2 = User("harry_coder", "harry@email.com", "admin")
print(user1.upgrade_membership("premium"))


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount:,.2f}. Balance: ${self.balance:,.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount:,.2f}. Balance: ${self.balance:,.2f}"

account = BankAccount("Sarthak", 500)
print(account.deposit(200))
print(account.withdraw(100))


class Car:
    def __init__(self, brand, model, battery_level=100):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def drive(self, distance):
        charge_lost = distance * 0.5
        if charge_lost > self.battery_level:
            return "Not enough battery charge for this trip"
        self.battery_level -= charge_lost
        return f"Drove {distance}km. Battery left: {self.battery_level}%"

ev = Car("Tesla", "Model 3", 80)
print(ev.drive(100))


class Order:
    def __init__(self, order_id, items, status="Pending"):
        self.order_id = order_id
        self.items = items
        self.status = status

    def ship_order(self):
        self.status = "Shipped"
        return f"Order #{self.order_id} has been dispatched"

cart = Order(1024, ["laptop", "mouse"])
print(cart.ship_order())


class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.enrolled_students = []

    def enroll(self, student_name):
        self.enrolled_students.append(student_name)
        return f"{student_name} enrolled in {self.title}"

python_class = Course("Python Basics", "Alex")
print(python_class.enroll("Harry"))
