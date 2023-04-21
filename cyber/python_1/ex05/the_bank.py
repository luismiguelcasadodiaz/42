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
        if not hasattr(self, 'value'):
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
        if new_account is None:
            # i got bank.add() wiht nothing to add
            msg = f"ADD:Account '{new_account}' ==> invalid class"
            raise ValueError(msg)
        else:
            # check for the right objec  
            if isinstance(new_account, Account):
                # check for an exixting account
                if account_to_add_ok(new_account):
                    self.accounts.append(new_account)
                else:
                    msg = f"Bank already has An account for '{new_account.name}'"
                    raise ValueError(msg)
            else:
                msg = f"ADD: {new_account} is an {type(new_account)} \
                        instead of an account"
                raise ValueError(msg)

    def transfer(self, orig, dest, amount):
        """" Perform the fund transfer
        @origin:  str(name) of the first account
        @dest:    str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return   True if success, False if an error occured
        """

        # accounts validity
        if not_corrupted_account(orig) and not_corrupted_account(dest):

            # positive amount verification

            if amount < 0:
                msg = f"TRANSFER: incorrect amount '{amount}' for a transfer"
                raise ValueError(msg)

            # verification for Enough funds at origin

            if amount > origin.value:
                msg = f"TRANSFER: '{orig.name} has less than '{amount}'"
                raise ValueError(msg)

            if orig.name == dest.name:
                print(f"Transfert between same accout {dest.name}")
        else:
            # this is the case of a regular transfer.
            orig.transfer(- amount)
            dest.transfer(+ amount)

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name:   str(name) of the account
        @return  True if success, False if an error occured
        """
        # ... Your code ...

    def account_to_add_ok(acc):
        """
        checking if account's name already exist in the bank
        """
        return __account_exists(acc)

    def not_corrupted_account(acc):
        """
        Check if any of corrpted account condition exist
        RETURN
            True if the account is not corrupted
            False Otherwise
        """
        if event_num_atrributes(acc) or \
                an_attri_start_w_b(acc) or \
                no_attri_start_w_z_or_a(acc) or \
                no_attr_n_i_v(acc) or \
                name_no_str(acc) or \
                id_not_int(acc) or \
                __value_not_int_or_float(acc):
            return False
        else: # As the account is corrupted ....
            # if the account exist in the bank
            if __account_exists(acc):
                # I try to fix it
                if fix_me(acc):
                    # with sucess at fix_me ...
                    # the account is not corrupted any more
                    return False
                else:
                    # with fail at fix_me...
                    # The account is still corrupted
                    return True

    def event_num_atrributes(acc):
        """ """
        # TODO: watch inside a dictionary's class
        return (len(acc.__dict__) % 2 == 0)

    def an_attri_start_w_b(acc):
        """ check first letter of each attibute"""
        for k in acc.__dict__Keys():
            if k[0].lower == "b":
                return True

    def no_attri_start_w_z_or_a(acc):
        """ verifies attributes startin with zip or addr
            no_zip   or no_addr     Corrupted
            ======      =======     =========
            True        True        True
            True        False       True
            False       True        True
            False       False       False
        """
        no_zip = True
        no_addr = True

        for k in acc.__dict__keys():
            if k.lower().startswidth("zip"):
                no_zip = False
                break
        for k in acc.__dict__keys():
            if k.lower().startswidth("addr"):
                no_addr = False
                break
        return (no_zip or no_addr)

    def no_attr_n_i_v(acc):
        """ Verifies existence of name, id and value
            no_name  or no_id  or no_value   Corrupted
            =======     =====     ========   =========
            True        True        True      True
            True        True        False     True
            True        False       True      True
            True        False       False     True
            False       True        True      True
            False       True        False     True
            False       False       True      True
            False       False       False     False
        """
        no_name = True
        no_id = True
        no_value = True

        for k in acc.__dict__keys():
            if k.lower() == "name":
                no_name = False
                break
        for k in acc.__dict__keys():
            if k.lower() == "id":
                no_id = False
                break
        for k in acc.__dict__keys():
            if k.lower() == "value":
                no_value = False
                break
        return (no_name or no_id or no_value)

    def no_attr_n_i_v(acc):
        """ Verifies existence of name, id and value
            no_name  or no_id  or no_value   Corrupted
            =======     =====     ========   =========
            True        True        True      True
            True        True        False     True
            True        False       True      True
            True        False       False     True
            False       True        True      True
            False       True        False     True
            False       False       True      True
            False       False       False     False
        """
        checks = {"no_name": True, "no_id": True, "no_value": True}

        for k in acc.__dict__keys():
            if k.lower() == "name":
                checks["no_name"] = False
            if k.lower() == "id":
                checks["no_id"] = False
            if k.lower() == "addr":
                checks["no_value"] = False
        # when no value is true, means all are false, so corrupted is false
        return any(checks.values())

    def name_no_str(acc):
        if hasattr(acc, "name"):
            # isinstance is false when name is not STR.So Corruptes is true
            return not isinstance(acc.name, str)
        else:
            # Has not name, so name_no_str is true
            return True

    def id_not_int(acc):
        if hasattr(acc, "id"):
            # isinstance is false when id  is not INT.So Corruptes is true
            return not isinstance(acc.id, int)
        else:
            # Has not id, so id_not_int is true
            return True

    def __value_not_int_or_float(acc):
        if hasattr(acc, "value"):
            # isinstance is false when id  is not INT.So Corruptes is true
            return not isinstance(acc.id, (int | float))
        else:
            # Has not value, so value_not_int_or_float is true
            return True

    def __account_exist(acc):
        """ Looks for acc.name inside the Bank's list of accounts
        """
        acc_exist = False
        for a in self.accounts:
            if acc.name == a.name:
                acc_exist = True
                break
        return acc_exist


if __name__ == "__main__":
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation'
    ))

    if bank.transfer('William John', 'Smith Jane', 545.0) is False:
        print('Failed')
    else:
        print('Success')


