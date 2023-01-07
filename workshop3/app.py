from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database={"admin": "password123",}
donations=[]
authorized_user=()

while True:
    show_homepage()
    if len(authorized_user) == 0:
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    option=input("Choose an option:",)
    if option == '1':
        username=input("\nEnter username:",)
        password=input("Enter password:",)
        authorized_user=login(database, username, password)
    elif option == '2':
        username=input("\nEnter username:",)
        password=input("Enter password:",)
        authorized_user= register(database, username)
        if authorized_user!='':
            database[username]=password
    elif option =='3':
        if len(authorized_user)==0:
            print("\nYou are not logged in.")
        else:
            donation_string=donate(authorized_user)
            donations.append(donation_string)
    elif option =='4':
        show_donations(donations)
    elif option == '5':
        print("Leavin DonateMe...")
        break
    else:
        print("Invalid Command.")