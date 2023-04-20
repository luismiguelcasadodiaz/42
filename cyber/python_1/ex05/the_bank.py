#!/usr/bin/python3
class Account(object):
    ID_COUNT = 1  # Class Atribut: counts number of accounts

    def __init__(self, name, **kwargs):
        # Update the instance internal dictionary
        # with dictionary got in argument
        self.__dict__.update(kwargs)

        # set the account number
        self.id = self.ID_COUNT
        # prepare the class for next accout creation
        Account.ID_COUNT += 1

        # set the account holder
        self.name = name

        # in case i was instantiated without value attribute
        # i self create such atribute and set it to zero
        if not hasattr(self, ’value’):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


# in the_bank.py

class Bank(object):
    """The bank"""
    def __init__(self): 
        self.accounts = []

    def add(self, new_account=None):
        """ 
        Add new_account in the Bank verification has to be performed when
        account objects are added to to Bank instance

        @new_account: Account() new account to append
        @return   True if success, False if an error occured


        """
        # test if new_account is an Account() instance and if 
        # it can be appended to the attribute accounts
        if new_account not is none:
            if isinstance(new_account, Account) and \
                self.account_to_add_ok(Account):
                    self.accounts.append(new_account)
                    return True
            else:
                return False
        else:
            raise ValueError(f"ADD:Account '{new_account}' is not a valid account")

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin:  str(name) of the first account
        @dest:    str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return   True if success, False if an error occured
        """
        # positive amount verification

        if amount < 0:
            msg = f"TRANSFER: incorrect amount '{amount}' for a transfer"
            raise ValueError(msg)

        # verification for Enough funds at origin

        if amount > origin.value:
            msg = f"TRANSFER: '{origin.name} has less than '{amount}'"
            raise ValueError(msg)

        if
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name:   str(name) of the account
        @return  True if success, False if an error occured
        """
        # ... Your code ...
    def account_to_add_ok(account):
        """
        checking if account's name already exist in the bank
        TODO: Verify Account type
        """
        
        accoun_exist = False
        for a in self.accounts:
            if account.name == a.name:
                account_exist = True
                break
        if account_exist: return False

    def not_corrupted_account(account):
        if event_num_atrributes(account) or
            an_attribute_start_with_b(a)
        
        
        
        
        
        event_num_atrributes = len(account.__dict__) % 2 == 0
        an_attribute_start 
                

