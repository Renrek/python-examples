FILE_PATH = "library/"

def main():
    userName = input("Enter person's name: ")
    print("D = Deposit, W = Withdrawl, Q = Quit")
    transactionControl(SavingsAccount(userName))

def transactionControl(account):
    action = str(input("Enter D, W, or Q: ")).strip().upper()
    if action == "D": # Deposit
        account.makeDeposit(float(input("Enter amount to deposit: ")))
        print("Balance: ${:,.2f}".format(account._accountBalance))
        transactionControl(account)
    elif action == "W": #Withdrawl
        account.makeWithdrawal(float(input("Enter amount to withdrawl: ")))
        print("Balance: ${:,.2f}".format(account._accountBalance))
        transactionControl(account)
    elif action == "Q": # poor account only lives as long as object lol
        print("End of transactions. Have a good day "+account._name+".")

class SavingsAccount:
    def __init__(self, name:str):
        self._name = name
        self._accountBalance = float(0)

    def makeDeposit(self, amount):
        self._accountBalance += amount

    def makeWithdrawal(self, amount):
        if self._accountBalance < amount:
            print("Insufficient funds, transaction denied.")
        else:
            self._accountBalance -= amount

main()