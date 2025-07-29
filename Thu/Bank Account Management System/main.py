class Account:
    bank_name = "Default Bank"
    minimum_balance = 0
    total_accounts = 0

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

        Account.total_accounts += 1

    def get_balance(self):
        return self.balance

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @classmethod
    def set_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    def set_minimum_balance(cls, amount):
        cls.minimum_balance = amount




class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)

        if interest_rate < 0:
            raise ValueError("Interest rate must be non-negative")

        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance - amount < Account.minimum_balance:
            return "Insufficient balance"
        self.balance -= amount
        return "Withdrawal successful"

    def calculate_monthly_interest(self):
        return self.balance * (self.interest_rate / 100) / 12



s = SavingsAccount("SA001", "Alice", 1000, 2.5)
s.deposit(500)
print(s.get_balance())  # 1500
print(s.withdraw(200))  # "Withdrawal successful"
print(s.calculate_monthly_interest())  # ≈ 2.7083
