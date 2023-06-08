######### bank_transactions.py

import re
import random
import string
import datetime

# datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S.%f")

# print(''.join(random.choice(string.digits) for _ in range(8)))
customer_account=set()
cust_list={}
bank_history={}
class customer():
    balance=0
    def __init__(self,first_name,last_name,phone_num,address,passw,conf_passw):
        self.first_name=first_name
        self.last_name=last_name
        self.phone_num=phone_num
        self.address=address
        if(self.validate_passw(passw,conf_passw)):
            self.passw=passw
            account_num=''.join(random.choice(string.digits) for _ in range(8))
            # print('account_num',account_num)
            while (account_num  in customer_account):
                account_num=''.join(random.choice(string.digits) for _ in range(8))
                # print('account_num in while',account_num)
            self.account_num=account_num
            customer_account.add(account_num)
            temp_dict={account_num:{'timestap':datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S.%f"),'balance':self.balance,'description':'First time'}}
            print('temp_dict : ',temp_dict)
            global bank_history
            bank_history={**bank_history,**temp_dict}
            # print('account_num : ',account_num)
        # return account_num
    def get_account_num(self):
        return self.account_num
    def withdraw(self,ammount,type='withdraw',from_account_num='',to_account_num=''):
        if(self.balance>ammount):
            self.balance=self.balance-ammount
            global bank_history
            # d.strftime("%d/%m/%y %H:%M:%S.%f")
            temp_dict={self.account_num:{'timestap':datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S.%f"),'balance':self.balance,'description':'withdraw','type':type,'from_account_num':from_account_num,'to_account_num':to_account_num}}
            bank_history={**bank_history,**temp_dict}
            return 
        else:
            return 
    def deposite(self,ammount,type='deposite',from_account_num='',to_account_num=''):
        self.balance=self.balance+ammount
        global bank_history
        temp_dict={self.account_num:{'timestap':datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S.%f"),'balance':self.balance,'type':type,'from_account_num':from_account_num,'to_account_num':to_account_num}}
        bank_history={**bank_history,**temp_dict}
        return
    def transfer(self, ammount,dest_account_numb):
        print('inside transfer',dest_account_numb)
        if (dest_account_numb  in customer_account):
            print('inside transfer',dest_account_numb)
            for i in cust_list:
                # print('inside transfer',i)
                if(cust_list[i].account_num==dest_account_numb):
                    self.withdraw(ammount,'transfer',to_account_num=cust_list[i].account_num,from_account_num=self.account_num)
                    print('inside transfer',i)
                    cust_list[i].deposite(ammount,'transfer',self.account_num)
        return
    def validate_passw(self,passw,conf_passw):
            if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', passw):
                # print('Very nice password. Much secure')
                if(passw==conf_passw):
                    # print('Confirm password pass')
                    return True
                else:
                    # print('Confirm password failed')
                    return False
            else:
                print('Not a valid password')
# first_name,last_name,phone_num,address,passw,conf_passw
# cust1 =customer('Aksha','Mok','909090','Nagpur','Pass@1234','Pass@1234')
# cust2 =customer('Aksha','Mok','909090','Nagpur','Pass@1234','Pass@1234')

# for i in range(3):
#     temp =f"cust{i}"
#     cust_list[temp] =customer(f'Akshay{i}',f'{i}',f'909090909{i}','Nagpur','Pass@1234','Pass@1234')
#     # cust_list[temp]=cust_list[temp].get_account_num()
# # print('cust_list : ',cust_list)
# # print('customer_account',customer_account)
# cust_list['cust0'].deposite(5000)
# cust_list['cust0'].deposite(580)
# print('cust0 :',cust_list['cust0'].balance)

# cust_list['cust0'].withdraw(540)
# print('cust0 :',cust_list['cust0'].balance)
# print('cust1 :' ,cust_list['cust1'].balance)

# cust_list['cust0'].transfer(2300,cust_list['cust1'].account_num)

# print('cust1 :' ,cust_list['cust1'].balance)

# print('cust0 :' ,cust_list['cust0'].balance)
# # for i in cust_list:
# #     print(cust_list[i].balance)

# print(bank_history)




