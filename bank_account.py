class BankAccount:
    total_accounts = 0  
    
    def __init__(self, name, account_type, balance=0):
        if not name:
            raise ValueError("Account holder's name cannot be empty.")
        
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.transactions = []  
        
        BankAccount.total_accounts += 1  
        print(f"New {account_type} account created for {self.name}. Total accounts: {BankAccount.total_accounts}")
    
    def deposit(self, amount):
        if amount > 50000:
            print("Deposit amount exceeds ₹50,000 limit.")
            return
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited. New balance: ₹{self.balance}")
    
    def withdraw(self, amount):
        if amount > 50000:
            print("Withdrawal amount exceeds ₹50,000 limit.")
            return
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return
        if self.balance - amount < 0:
            print("Insufficient balance.")
            return
        
        self.balance -= (amount + 10)  
        self.transactions.append(f"Withdrew ₹{amount}, Fee: ₹10")
        print(f"₹{amount} withdrawn (₹10 fee applied). New balance: ₹{self.balance}")
    
    def transfer(self, recipient, amount):
        if not isinstance(recipient, BankAccount):
            print("Invalid recipient.")
            return
        if amount <= 0:
            print("Invalid transfer amount.")
            return
        if self.balance - amount < 0:
            print("Insufficient balance for transfer.")
            return
        
        self.balance -= amount
        recipient.balance += amount
        self.transactions.append(f"Transferred ₹{amount} to {recipient.name}")
        recipient.transactions.append(f"Received ₹{amount} from {self.name}")
        print(f"₹{amount} transferred to {recipient.name}. New balance: ₹{self.balance}")
    
    def check_balance(self):
        print(f"Account balance: ₹{self.balance}")
    
    def get_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
    
    @classmethod
    def get_total_accounts(cls):
        print(f"Total accounts in the bank: {cls.total_accounts}")
    
    @staticmethod
    def validate_amount(amount):
        return amount > 0


acc1 = BankAccount("Harsh","Savings",10000)
acc2 = BankAccount("Ram","Current",11000)
acc3 = BankAccount("Shiv","Savings",18900)
acc4 = BankAccount("Savings",18900)

acc1.deposit(102)
acc2.withdraw(10000)
acc1.transfer(acc2,3000)
acc1.check_balance()
acc2.check_balance()
acc1.get_transaction_history()
BankAccount.get_total_accounts()
acc3.check_balance()
acc1.deposit(50000)
