# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 00:41:52 2024

@author: Marco
"""
"Class implenmentation of a bank account with subclasses for types of accounts"

#class Penalty(): "If there is a penalty, what is it?"
"""
Accounts -> Various accounts will be used containing, at minimum, a deposit
amount, an owner.


What types of accounts?
-Checking accounts
-Savings accounts
-Money Market Accounts

Business Rules:

-Savings accounts have a 6 limit withdrawal per month until a penalty applies. Let's say the penalty is $15
-Checking accounts have no withdrawal limits
-Money market accounts have no withdrawal limits
-CD accounts have a penalty. Let's say, for now, it is 5% of the withdrawal amount.

Questions to explore:

How do we model withdrawal limits. This may have to be logged on the database
side. Here, I think we can perform a query to withdraw.


More classes we need:

Penalty class that has 2 methods:
   1. getPenaltyAmount(Account account) - Determines the penalty amount for the account passed in
   2. penaltyApplies(Account account) - Determines if a penalty needs to be applied for the account.


Transaction class that stores information about a transaction made.

Part 1: Account Modeling

Accounts -> Various accounts will be used containing, at minimum, a deposit
amount, an owner.


What types of accounts?
-Checking accounts
-Savings accounts
-Money Market Accounts

Business Rules:

-Savings accounts have a 6 limit withdrawal per month until a penalty applies. Let's say the penalty is $15
-Checking accounts have no withdrawal limits
-Money market accounts have no withdrawal limits
-CD accounts have a penalty. Let's say, for now, it is 5% of the withdrawal amount.

Questions to explore:

How do we model withdrawal limits. This may have to be logged on the database
side. Here, I think we can perform a query to withdraw (This may be something I will have to take a look into when it comes to modeling it).

Possible classes we may need to model:
1. Accounts
2. Penalties
3. Transactions (deposits and withdrawals)

"""
"I will create account classes, determine if penalties apply,and keep track of transactions"
    

import random
"I will randomly generate account numbers of a certain size"
"methods I will pass down to all subclasses"
class Account():
    def __init__(self, owner_name, date_opened, initial_deposit, account_number = None, account_type = None):
        self.owner_name = owner_name
        self.date_opened = date_opened
        self.account_number = random.randint(00000,99999)
        self.initial_deposit = initial_deposit
        self.history = [initial_deposit]
        
"I need to consider the methods that will be specific to the account types"

"Money market, no withdrawal limits, no penalties"
class MoneyMarket(Account):
    def __init__(self, owner_name,date_opened,initial_deposit,account_number = None, account_type = None):
        Account.__init__(self,owner_name,date_opened,initial_deposit, account_number = None, account_type = None)
        self.account_type = "checking"

"withdrawal limits of 6 times per month, penalty of $15 per every extra withdrawal"
class Savings(Account):
    def __init__(self, owner_name,date_opened,initial_deposit,withdraw_count, account_number = None, account_type = None):
        Account.__init__(self,owner_name,date_opened,initial_deposit, account_number = None, account_type = None)
        self.account_type = "savings"

"if withdrawing before the expiration date, penalty of withdrawal is 5%"
class CD(Account):
    pass

"no withdrawal, no penalties"
class Checking(Account):
    pass

"Call this object to make deposits or withdrawals to an object"
"store deposit dates and withdrawal dates as datetime objects"
class Transactions():
    def __init__(self, account):
        "account is an account object"
        self.__account = account
        
    "make a deposit into an account"
    def MakeDeposit(self,account,deposit_amount):
        account.initial_deposit += deposit_amount
        account.history.append(deposit_amount)
        
    def GetDeposits(self,account):
        deposits = []
        for entry in account.history:
            if entry>0:
                deposits.append(entry)
        return deposits
    
    def MakeWithdrawal(self,account,withdraw_amount):
        "eventually include the penalty in here"
        "I will include the penalty amount as a unique entry"
        account.history.append(withdraw_amount)
        account.initial_deposit -= withdraw_amount
        
        
    def GetWithdrawals(self,account):
        withdraws = []
        for entry in account.history:
            if entry < 0:
                withdraws.append(entry)
        return withdraws
    
    def GetAccountBalance(self,account):
        return account.initial_deposit
        
class Penalties():
    def __init__(self, account):
        self.account = account
    
    def PenaltyApplies(self,account):
        if account.account_type == "checking" or account.account_type == "money market":
            return False
        if account.account_type == "savings":
            return True
        if account.account_type == "CD":
            return True
    def getPenaltyAmount(self,account, withdrawal):
        penalty = 0
        if account.account_type == "CD":
            penalty = withdrawal * .05
        return penalty
    
        



           