# encapsulation - hiding data
class Bank:
    def __init__(self, name: str, balance: int, bank_name: str) -> None:
        self.name = name  # public
        self._bank_name = bank_name  # protected
        self.__balance = balance  # private

    def deposit(self, amount: int):
        if amount < 0:
            print("Invalid amount")
        else:
            self.__balance += amount
            print(f"Balance is: {self.__balance}")


c1 = Bank("anirudh", 1000, "abc bank")
c1.deposit(200)
# c1.balance = 200 // not possible
c1.deposit(-2)
# in python it is not real security because we can still access the private members like-
print(c1._Bank__balance)
# even we have made the balance private but still we can access this ;
