class Bank():

    def __init__(self):
        self.c_data = [ 
            {"Pin" : 1234 , "bal" : 10000 } ,
            {"Pin" : 3456 , "bal" : 12000 } ,
            {"Pin" : 5678 , "bal" : 40000 } ,
            {"Pin" : 7890 , "bal" : 70000 } ,
            {"Pin" : 1112 , "bal" : 40000 } ,
            {"Pin" : 1314 , "bal" : 20000 } ,
            {"Pin" : 1516 , "bal" : 80000 } ,
        ]

    def Withdraw(self , c_bal):
        amount = int(input("Enter the Withdraw amount : "))
        if amount <= c_bal:
            c_bal  = c_bal - amount
            print("Transaction Successfully")
        else:
            print("Insufficient balance")


    def Check_bal(self , c_bal):
        print(f"Your current Available Balance is : {c_bal}")


    def Deposit(self , c_bal):
        D_amount = int(input("Enter your Deposit amount :"))
        c_bal = c_bal + D_amount
        print("Deposited Successfully")


    def Reset_pin(self , c_Pin):
        Current_pin = int(input("Enter Your Current Pin : "))
        new_pin = int(input("Enter New Pin Here : "))

        if Current_pin == c_Pin["Pin"]:
            c_Pin["Pin"] = new_pin
            print("Pin Reset Successfully..! ")
        else:
            print("Invalid Pin")

    def Start(self):
        print(" * * * Welcome to ATM * * * ")
        print("Please Insert Your Card Here |----|")
        Conform_pin = int(input("Enter Your ATM Pin : "))

        for User_data in self.c_data:
            if User_data ["Pin"] == Conform_pin:
                print(" ")
                print(" ---- Hii Sir/Madam Namste ----")
                print(" ")
                print("Enter W for Withdrawal amount")
                print("Enter B for Balance amount")
                print("Enter D for Deposit amount")
                print("Enter R for Reset Pin")
                print("Enter E for Exit")

                Option = input(" Choose the Option (W / B / D / R / E) : ").upper()

                if   Option == "W":
                    self.Withdraw(User_data["bal"])

                elif Option == "B":
                    self.Check_bal(User_data["bal"])

                elif Option == "D":
                    self.Deposit(User_data["bal"])

                elif Option == "R":
                    self.Reset_pin(User_data)
            
                elif Option == "E":
                    print("Thank You and Visit Again :)")

                else:
                    print("Invalid Option")
                break

        else:
            print("Invalid Pin")
            

atm = Bank()
atm.Start()            
                  
                      
            







            