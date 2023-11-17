class Metro:
    def __init__(self,new_balance):
        self.old_balance=100
        self.new_balance=new_balance
    def menu(self):
        user_input = input("""Please select from the following options:
        1. Enter the amount to deposit
        2. Check balance
        3. Select source station
        4. Select destination station
        """)
        if user_input == "1":
            self.deposit = int(input("Please enter the amount you want to deposit: "))
            new_balance=int(self.old_balance+self.deposit)
        elif user_input == "2":
          print("Your balance is:",new_balance)
        elif user_input == "3":
            print("""Please select a station from where you want to travel:
            1. Kirti Nagar
            2. Moti Nagar
            3. Ramesh Nagar
            4. Nawada
            5. Uttam Nagar
            6. Janakpuri
            7. Rajeev Chowk
            8. Mandi House
            9. Akshardham
            10. Noida
            11. Dwarka Mor
            12. Tilak Nagar""")
        elif user_input == "4":
            print("""Please select a station where you want to reach:
            1. Kirti Nagar
            2. Moti Nagar
            3. Ramesh Nagar
            4. Nawada
            5. Uttam Nagar
            6. Janakpuri
            7. Rajeev Chowk
            8. Mandi House
            9. Akshardham
            10. Noida
            11. Dwarka Mor
            12. Tilak Nagar""")
        else:
            print("Exit")

blueline = Metro()
blueline.menu()
