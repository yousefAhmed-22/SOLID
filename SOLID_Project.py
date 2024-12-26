from abc import ABC, abstractmethod

# 1. Single Responsibility Principle (SRP)
class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class PaymentLogger:
    def log(self, message):
        print(f"Log: {message}")

# 2. Open/Closed Principle (OCP)
class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass

class NoDiscount(Discount):
    def apply(self, amount):
        return amount

class PercentageDiscount(Discount):
    def apply(self, amount):
        return amount * 0.9

# 3. Liskov Substitution Principle (LSP)
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

# 4. Interface Segregation Principle (ISP)
class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class OnlinePayable(ABC):
    @abstractmethod
    def validate_card(self, card_number):
        pass

class CreditCardPayment(Payable, OnlinePayable):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

    def validate_card(self, card_number):
        print(f"Validating card {card_number}")

class CashPayment(Payable):
    def pay(self, amount):
        print(f"Paid ${amount} in Cash")

# 5. Dependency Inversion Principle (DIP)
class PaymentService:
    def __init__(self, payment_method: Payable, notification: Notification, logger: PaymentLogger):
        self.payment_method = payment_method
        self.notification = notification
        self.logger = logger

    def execute_payment(self, amount, discount: Discount):
        final_amount = discount.apply(amount)
        self.payment_method.pay(final_amount)
        self.notification.send(f"Payment of ${final_amount} successful")
        self.logger.log(f"Payment executed: ${final_amount}")
