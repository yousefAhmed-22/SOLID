# Examples of SOLID Principles

# 1. Single Responsibility Principle (SRP)
# A class should have only one reason to change.

# Wrong way:
class Invoice:
    def calculate_total(self, items):
        return sum(item['price'] for item in items)

    def print_invoice(self, items):
        print("Invoice Details:")
        for item in items:
            print(f"{item['name']}: ${item['price']}")

items = [{'name': 'Apple', 'price': 1}, {'name': 'Banana', 'price': 2}]
invoice = Invoice()
invoice.calculate_total(items)
invoice.print_invoice(items)

# Correct way:
class InvoiceCalculator:
    def calculate_total(self, items):
        return sum(item['price'] for item in items)

class InvoicePrinter:
    def print_invoice(self, items):
        print("Invoice Details:")
        for item in items:
            print(f"{item['name']}: ${item['price']}")

calculator = InvoiceCalculator()
printer = InvoicePrinter()
items = [{'name': 'Apple', 'price': 1}, {'name': 'Banana', 'price': 2}]
calculator.calculate_total(items)
printer.print_invoice(items)

# 2. Open/Closed Principle (OCP)
# Classes should be open for extension but closed for modification.

# Wrong way:
class Discount:
    def apply_discount(self, price, discount_type):
        if discount_type == "percentage":
            return price * 0.9
        elif discount_type == "fixed":
            return price - 10

# Correct way:
class Discount:
    def apply_discount(self, price):
        raise NotImplementedError("This method should be overridden")

class PercentageDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.9

class FixedDiscount(Discount):
    def apply_discount(self, price):
        return price - 10

# 3. Liskov Substitution Principle (LSP)
# Subtypes must be substitutable for their base types.

# Wrong way:
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly!")

# Correct way:
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("Flying")

class NonFlyingBird(Bird):
    def move(self):
        print("Walking")

# 4. Interface Segregation Principle (ISP)
# No client should be forced to implement methods it does not use.

# Wrong way:
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("Working")

    def eat(self):
        raise NotImplementedError("Robots don't eat")

# Correct way:
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating")

class Robot(Workable):
    def work(self):
        print("Working")

# 5. Dependency Inversion Principle (DIP)
# High-level modules should not depend on low-level modules. Both should depend on abstractions.

# Wrong way:
class LightBulb:
    def turn_on(self):
        print("LightBulb is ON")

    def turn_off(self):
        print("LightBulb is OFF")

class Switch:
    def __init__(self):
        self.lightbulb = LightBulb()

    def press(self):
        self.lightbulb.turn_on()

# Correct way:
class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb is ON")

    def turn_off(self):
        print("LightBulb is OFF")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def press(self):
        self.device.turn_on()
