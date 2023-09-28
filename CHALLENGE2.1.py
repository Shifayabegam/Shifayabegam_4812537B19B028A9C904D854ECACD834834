 class BankAccount:
def init(self,account number, acco unt holder_name, initial balance-0.0) 

  self.__account number=account_number

   self.__account holder_name=account_holder_name

   self.__account-balance=initial_balance

def deposit(self, amount) 
if amount>8:

self.__account_balance + amount

print("Deposited ₹{}, New balance:₹{}", format(amount,self.__account_balance)) 
 else:
  print("Invalid deposit amount.please deposit a positive amount,") 
   def withdraw(self,amount)
   if amount>0 and amount<=
self.__account_balance:
    self.__account_balance-=amount
  print(" withdrew ₹{}. New balance:₹{}",format(amount, self.__account_balance))
  else:

  print("Invalid withdrawal amount or insufficient balance.")
  def display balance(self):
  print("Account balance for{}(Account #{}) :₹{}",format(self.__account_name, self.__account_number, self.account balance)) 

#create # Instance of the BankAccount class


account=BankAccount (account number="123456789",account holder_name="Hari prabu", initial_balance 5000.0)

#Test deposit and withdrawl functiomality 
account. display_balance() 
account. deposit(500.0) 
account. withdraw(200.0)
account. display_balance()