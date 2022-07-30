class pay_gate_app:
    def __init__(self):

        self.store_database={ "siva":"654321",
                              "sathiya":"123456",
                              "raghul":"654322"
                            }
        self.contacts_data={ "sanjai":"9443664576",
                             "rakesh":'9791307977',
                             "vijay":'9952389956'
                            }
        self.cash_amount={ "siva":500,
                           "sathiya":500,
                           "raghul":200
                          }
    def welcome(self):
        print("Welcome to pay_gate_app")
        self.pay_1=input("If you already signup in pay_gate_app type yes or no: ")
        if  self.pay_1.lower()=="no":
            self.singup()
        else:
            self.singin()
    
    def singup(self):
        self.s1=str(input("Enter the name: "))
        self.s2=str(input("Enter tha passward: "))
        self.s3=int(input("Enter you current saving amount: "))
        if len(self.s2)==6:
            self.store_database.update({self.s1:self.s2})
            self.cash_amount.update({self.s1:self.s3})
            print("Thankyou for singup pay_gate_app")
            self.f3=input("Do you want to signin pay_gate_app type yes or no: ")
            if  self.f3.lower()=="yes":
                self.singin()
            else:
                print("Thankyou visit again")
        else:
            print("Password should be must in 6 numbers")

    def data_time(self):
        import datetime as dt
        self.current_date=dt.datetime.now()
        self.current_time=dt.datetime.now()
        self.date=self.current_date.strftime("%d-%b-%Y")
        self.time=self.current_time.strftime("%I:%M:%S")
    
    def singin(self):
        self.s1=input("Enter the user_name: ")
        if self.s1 in self.store_database:
            self.s2=str(input("Enter the password: "))
            if len(self.s2)==6:
                if self.store_database[self.s1]==self.s2:
                        self.deposit()
                else:
                    self.chance=3
                    while self.chance !=0:
                        self.s3=input("Enter the  re enter your passward: ")
                        if len(self.s3)==6:
                            if self.store_database[self.s1]==self.s3:
                                self.deposit()
                                quit()
                            else:
                                self.chance-=1
                        else:
                            print("Password should be must in 6 numbers")
                    if self.chance==0:
                        print("your chance is over please exit this app")
            else:
                print("please type 6 number passward")
        else:
            print("invalid user name")
        
    def deposit(self):
        self.z1=input("if you want to deposit type yes or no: ")
        if self.z1.lower()=="yes":
            self.a1=int(input("Enter The Deposit Amount: "))
            self.a2=self.cash_amount[self.s1] 
            self.a3=self.a1+self.a2
            self.cash_amount.update({self.s1:self.a3})
            self.data_time()
            print(self.a1,"amount is Debited on Time :",self.time,",Date:",self.date,"and your total balance is",self.a3)
            self.contacts()
        else:
            self.contacts()
            quit()

    def contacts(self):
       self.c1=input("if you want to send money for your friends type yes or no: ")
       if  self.c1.lower()=="yes":
           for self.i in self.contacts_data.keys():
               print(self.i)
           self.c2=input("Enter the name: ")
           self.c3=self.contacts_data[self.c2]
           print(self.c3)
           self.c3=input("Are you sure to send amount in this number type yes or no: ")
           if self.c3.lower()=="yes":
                self.c4=int(input("How many amount you want to send: "))
                self.c7=self.cash_amount[self.s1]
                self.c8=self.c7-self.c4
                if self.c7>=self.c4:
                    self.data_time()
                    print(self.c4,"is Debited  on Time:",self.time,",Date:",self.date,"in your account")
                    self.c9=self.c7-self.c4
                    print(self.s1,"in your Total balace is",self.c9,"on Time:",self.time,",Date:",self.date)
                else:
                    print("not avaliable that much of amount in",self.s1,"account")
           else:
                print("okay please check the number once again")
       else:
           print("Thank_you")

p1=pay_gate_app()
p1.welcome()