"""
Week 7 - Activity 4: Singeleton and Factory design pattern (due date 25 Sep 2025 )
Develop a code to show the usage of both design patterns in your coding for; 
Design a payment processing system that supports multiple payment methods 
(e.g., Creditcard, PayPal, Bank Transfer, CryptoPayment, GooglePay).
    1. Use the Factory Design Pattern to create different payment method objects dynamically.
    2. Ensure the payment gateway (the main entry point for processing payments)
       is implemented as a Singleton, so only one instance of the gateway exists in the system.
Explain your design choices and share your GitHub with code implementation.

MSE800
270765080 Kristine Gonzalvo
"""

from abc import ABC, abstractmethod
import threading

""" Payment Processing System with Factory and Singleton Patterns """

# Abstract base class for all payment methods / Abstract Product
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Different payment method classes / Concrete Products
class CreditCard(PaymentProcessor):
    def process_payment(self, amount):
        return f"Credit Card: Charged ${amount}"

class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        return f"PayPal: Transferred ${amount}"

class BankTransfer(PaymentProcessor):
    def process_payment(self, amount):
        return f"Bank Transfer: Sent ${amount}"

class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Crypto: Transferred ${amount} in Bitcoin"

class GooglePay(PaymentProcessor):
    def process_payment(self, amount):
        return f"Google Pay: Paid ${amount}"

# extend with another payment method without modifying factory code
class ApplePay(PaymentProcessor):
    def process_payment(self, amount):
        return f"Apple Pay: Paid ${amount}"

# Factory Pattern - Creates the payment method objects
""" This factory uses a registry to map payment types to their classes. This
        allows easy extension by adding new payment methods without modifying
        factory code.
    This factory creates payment method objects through the abstract base
        class PaymentProcessor.
"""
class PaymentFactory:
    _registry = {
        "credit_card": CreditCard,
        "paypal": PayPal,
        "bank_transfer": BankTransfer,
        "crypto": CryptoPayment,
        "google_pay": GooglePay,
    }

    @classmethod
    def register(cls, name: str, payment_cls: type[PaymentProcessor]) -> None:
        """Optionally register new payment methods without modifying factory code."""
        if not issubclass(payment_cls, PaymentProcessor):
            raise TypeError("Registered class must inherit from PaymentProcessor")
        cls._registry[name.lower()] = payment_cls

    @classmethod
    def create_payment(cls, payment_type) -> PaymentProcessor:
        payment_cls = cls._registry.get(payment_type.lower())
        if payment_cls is None:
            raise ValueError(f"Unknown payment type: {payment_type!r}. "
                             f"Available: {', '.join(cls._registry)}")
        return payment_cls()

# Singleton Pattern - Payment Gateway
""" PaymentGateway serves as the single entry point for processing payments and
    the one calling the factory to create payment method objects (process_payment).
    Lock threading ensures that only one instance of PaymentGateway exists."""
class PaymentGateway:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.transactions = []
                    print("Payment Gateway created!")
        return cls._instance
    
    def process_payment(self, payment_type, amount):
        # Use factory to create payment processor
        processor = PaymentFactory.create_payment(payment_type)
        
        if processor:
            result = processor.process_payment(amount)
            self.transactions.append(result)
            return result
        else:
            return "Payment method not supported"
    
    def get_transactions(self):
        return self.transactions

# Demo for testing the system
def main():
    print("\n=== Payment Processing System Demo ===\n")
    
    # Test Singleton - both variables point to same instance
    gateway1 = PaymentGateway()
    gateway2 = PaymentGateway()
    print(f"Are gateway1 and gateway2 same instances? {gateway1 is gateway2}\n") # displays True
    
    # Test different payment methods using Factory pattern
    print("Processing payments:")
    # gateway1 processes 3 various payments
    print(gateway1.process_payment("credit_card", 100))
    print(gateway1.process_payment("paypal", 50))
    print(gateway1.process_payment("bank_transfer", 200))
    # gateway2 processes 2 more payments (but still same instance as gateway1)
    print(gateway2.process_payment("crypto", 0.001))
    print(gateway2.process_payment("google_pay", 75))
    
    # This is for testing unsupported method - this statement will raise ValueError
    # because 'invalid' is of unknown payment type
    #print(gateway1.process_payment("invalid", 25))
    
    # This shows that gateway1 recognizes all transactions
    print(f"\ngateway1 transactions: {len(gateway1.get_transactions())}")
    # and this also shows that gateway2 has same transactions (because same instance)
    print(f"gateway2 transactions: {len(gateway2.get_transactions())}")

    """ Extend with new payment method without modifying factory code """
    PaymentFactory.register("apple_pay", ApplePay) # register new payment method
    print("\nProcessing payment with new method (Apple Pay):")
    print(gateway1.process_payment("apple_pay", 30)) # process payment with new method

    # gateway2 transactions has both from gateway1 and gateway2
    # because they are the same instance
    print(f"\nUpdated total gateway2 transactions: {len(gateway2.get_transactions())}")
    print(gateway2.get_transactions())

if __name__ == "__main__":
    main()
