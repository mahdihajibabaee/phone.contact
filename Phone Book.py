X = True
Contact ={}

while X:
    F = True
    userorder = input("Please enter your order number 1.Add contact 2.Search contact 3.Delete contact 4.Show contacts 5.Exit :")
    if userorder == "1":
        while F:
            print("************************************")
            Username = input("enter your contact name (Q to quit):").upper()
            if Username == "Q":
                F = False
            else:
                Usernumber = input("enter your contact number :").upper()
                Contact.update({Username:Usernumber})
                print(f"{Username} add to contact / number={Usernumber}")
    elif userorder == "2":
        while F:
              Userordersesrch = input("enter your contact name (Q to quit):").upper()
              if Userordersesrch == "Q":
                  F = False
              else:
                  if Userordersesrch in Contact:
                    print(f"phone number :{Contact.get(Userordersesrch)}")
                    print("************************************")
                  else:
                    print("contact not found")
    elif userorder == "3":
        while F:
            UserorderDelete = input("enter your contact name to deleate (Q to quit):").upper()
            if UserorderDelete == "Q":
                F = False
            else:
                if UserorderDelete in Contact:
                    Contact.pop(UserorderDelete)
                    print(f"{UserorderDelete} deleted")
                else:
                    print("contact not found")
    elif userorder == "4":
        while F:
            print(Contact)
            quit = input("for quit press Q :").upper()
            if quit == "Q":
                F = False
    elif userorder == "5":
        X = False

