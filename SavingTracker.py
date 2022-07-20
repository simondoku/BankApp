#Libraries:
import random

#Global variable
Checking = None
Saving = None
businessAccount = None
routingNum = 234543345
lists = []


#Classes:


class Bank:
    typeofaccunt = None
    def __init__ (self, first, last,money,Types):
        self.first = first
        self.last = last
        self.money = money
        self.routingNum = routingNum
        self.number = int(random.random()*1000000000000)
        self.Types = Types
        self.lists = lists

    def set_amount(self, a):
        self.money = a

    def get_balance(self):
        return self.money

    def get_number(self):
        return self.number

    def get_customer(self):
        return self.first, self.last

    def getType(self):
        return self.Types

    def getList(self):
        return self.lists



def main():
    '''
    Greet customer
    ask if they want to open an account
    if yes, ask the name, the type (3choices), and $$$
    ask if they want to open another account, view balalnce...
    #...deposit $$$, withdraw $$$, transfer $$$ from one account to another
    or quit
    '''
    Fname = input("Welcome to Hatter Bank! \nWhat is your first name")
    Sname = input("What is your last name")
    x = float(input("How much money would you like to Deposit"))
    typess = int(input("Enter the type of account would you be creating (1.Checking, 2.Savings, or 3. Business)"))
    switch = {1: "Checking", 2: "Savings", 3: "Business"}
    z = switch.get(typess)


    create_account(Fname, Sname, x, z)

    bools = True
    while bools == True:
        x = int(input("Do you want to 1. create another account 2. View Balance 3. Withdraw 4. Transfer to another account 5. Quit"))
        if x == 1:
            accounttyper = int(input("What type 1. Checking 2.Saving 3. Business"))
            switcher = {1: "Checking", 2: "Savings", 3: "Business"}
            y = switcher[accounttyper]
            monetary = float(input("Please deposit an amount of money"))
            create_account(Fname, Sname, monetary, y)

        elif x == 2:
            viewbalance()

        elif x == 3:
            x = float(input("How much do you want to withdraw"))
            withdraw(x)

        elif x == 4:
            transfer()

        elif x == 5:
            bools = False
            print('Thank you for banking with us!')


def create_account(first, last, money, Types):
    new_account = Bank(first, last, money, Types)
    lists.append(new_account)
    print(f'Your {Types} account has been created successfully with name: {new_account.first} {new_account.last}, account number {new_account.number} with routing number {new_account.routingNum}')
    return new_account


def accountType(account):
    y = account.getType()
    return y

def withdraw(amount):
    x = int(input("Which account do you want to withdraw from 1. Checking 2. Saving 3. Business"))
    switcher = {1: "Checking", 2: "Savings", 3: "Business"}
    y = switcher.get(x)
    for i in range(len(lists)):
        if accountType(lists[i]) == y:
            if lists[i].get_balance() >= amount:
                x = lists[i].get_balance() - amount
                z = x
                lists[i].set_amount(z)
                print("You withdrew", amount, "from your", y, "account")
                print(f'Your balance is $ {z} ')
            else:
                x = lists[i].get_balance() - amount
                z = x
                lists[i].set_amount(z)

                print(f'Your balance is $ {z} ')
                print('Your account has entered a red zone')

    return amount



def viewbalance():
    if len(lists) > 1:
        x = int(input("What account balance do you want to view? 1:Checking 2: Saving 3: Business"))
        switcher = {1:"Checking", 2:"Savings", 3:"Business"}
        y= switcher.get(x)
        for i in lists:
            if y == accountType(i):
                print(f"Your {accountType(i)} balance is $ {i.get_balance()}")
    else:
        for i in lists:
            print(f"Your {accountType(i)} balance is $ {i.get_balance()}")
def transfer():
    To = int(input("Which account do you want to transfer from 1:Checking 2: Saving 3: Business"))
    switcher1 = {1: "Checking", 2: "Savings", 3: "Business"}
    From = int(input("Which account do you want to transfer to 1:Checking 2: Saving 3: Business"))
    switcher2 = {1: "Checking", 2: "Savings", 3: "Business"}
    count =0
    accunt= None
    for i in lists:

        if switcher1.get(To) == accountType(i):
            count+=1

            accountTo = i.get_balance()
            how_much = int(input("How much do you want to transfer?"))
            accunt=how_much
            if how_much > accountTo:
                print("Insufficient Balance")
                break
            else:
                x = i.get_balance() - how_much
                amountTo = x
                i.set_amount(amountTo)

    for i in lists:
        if count==1:
            if switcher2.get(From) == accountType(i):
                count += 1
                balance = i.get_balance() + accunt
                i.set_amount(balance)

    if count ==2:
        print(f"You have deposited an amount of ${accunt} from your  {switcher1.get(To)} account")
        print(f"Your {switcher2.get(From)} account has been deposited with {accunt} from your {switcher1.get(To)} account")
    else:
        print("I am sorry you do not have one or both of the accounts asked. Thank you")


#Running Code
main()
