class BankAccount:
    def __init__(self, name: str, balance: int):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.name = name
        self.__balance = balance
        self.__history = []

    def deposit(self, amount: int):
        if amount <= 0 or amount % 100 != 0:
            raise ValueError("Amount must be positive and multiple of 100")

        self.__balance += amount
        self.__history.append(f"Deposited {amount}")
        print("New balance:", self.__balance)

    def withdraw(self, amount: int):
        if amount <= 0 or amount % 50 != 0:
            raise ValueError("Withdraw amount must be multiple of 50")

        if amount > self.__balance:
            raise ValueError(f"Insufficient funds. Balance: {self.__balance}")

        self.__balance -= amount
        self.__history.append(f"Withdrew {amount}")
        print("New balance:", self.__balance)

    def query_balance(self):
        print("Current balance:", self.__balance)

    def transfer_to(self, other: "BankAccount", amount: int):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds for transfer")

        self.__balance -= amount
        other.__balance += amount

        self.__history.append(f"Transferred {amount} to {other.name}")
        other.__history.append(f"Received {amount} from {self.name}")

    def show_history(self):
        print(f"Transaction history for {self.name}:")
        for h in self.__history:
            print("-", h)


# if __name__ == "__main__":
