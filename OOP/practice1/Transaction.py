import uuid


class Transaction:
    def __init__(self, amount):
        self.transaction_id = None
        self.amount = amount
        self.status = "pending"

    def get_details(self):
        print(
            f"Transaction ID : {self.transaction_id} \nAmount : {self.amount} \nStatus : {self.status}"
        )

    def execute(self):
        self.transaction_id = str(uuid.uuid4())
        if self._process():
            self.status = "Successful"
        else:
            self.status = "Failed"
        self.get_details()

    def _process(self, *args) -> bool:
        return False


class Deposit(Transaction):
    def __init__(self, amount, destination_account):
        super().__init__(amount)
        self.destination_account = destination_account

    def get_details(self):
        super().get_details()
        print(f"Deposit to Account : {self.destination_account}")

    def _process(self, *args):
        print(f"Depositing Money to {self.destination_account}")
        return True


class Withdraw(Transaction):
    def __init__(self, amount, source_account):
        super().__init__(amount)
        self.source_account = source_account

    def get_details(self):
        super().get_details()
        print(f"Withdraw from Account : {self.source_account}")

    def _process(self, *args):
        print(f"Withdrawing Money from {self.source_account}")
        return True


class Transfer(Transaction):
    def __init__(self, amount, source_account, destination_account):
        super().__init__(amount)
        self.source_account = source_account
        self.destination_account = destination_account

    def get_details(self):
        super().get_details()
        print(f"Transfer from {self.source_account} to {self.destination_account}")

    def _process(self, *args):
        print(
            f"Transfering Amount from account {self.source_account} to account {self.destination_account}"
        )
        return True



def main(): 
  while True:
   print(""" 
      *********** Welcome to ABSA banking system***********
      Select your option:
      1. Make deposit
      2. Make withdraw
      3. Make transfer
      4. Quit
      *****************************************************
      """)    
   choice = input()
   if not choice.isdigit() or  int(choice) not in [x for x in range(1,5)]:
       print("Invalid selection, try again")
       continue
   else:
       match choice:
           case "1":
               amount = input("Enter the amount : ")
               if amount.isdigit() and int(amount) > 0:
                    account_no = input("Enter your bank account: ")
                    deposit = Deposit(int(amount), account_no)
                    deposit.execute()
                    break
               else:
                    print("Please enter a valid amount!")
                    continue
           case "2":
               amount = input("Enter the amount to wthdraw: ")
               if amount.isdigit() and int(amount) > 0:
                    account_no = input("Enter your bank account: ")
                    withdraw = Withdraw(amount=int(amount), source_account=account_no)
                    withdraw.execute()
                    break
               else:
                    print("Please enter a valid amount!")
                    continue
           case "3":
               amount = input("Enter the amount to transfer: ")
               if amount.isdigit() and int(amount) > 0:
                    account_no1 = input("Enter the source account: ")
                    account_no2 = input("Enter the destination account: ")
                    transfer = Transfer(amount= amount, source_account= account_no1, destination_account= account_no2)
                    transfer.execute()
                    break
               else:
                    print("Please enter a valid amount!")
                    continue
           case "4":
               print("*****Thank you for visting ABSA banking system******")
               break
            
if __name__ == "__main__":
    main()              
               
               
