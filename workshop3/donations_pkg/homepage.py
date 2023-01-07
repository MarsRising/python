def show_homepage():
    print("      === DonateMe Homepage ===     ")
    print("------------------------------------")
    print("| 1. Login       | 2. Register      |")
    print("------------------------------------")
    print("| 3. Donate      | 4. Show Donations|")
    print("------------------------------------")
    print("|             5. Exit               |")
    print("------------------------------------")

def donate(username):
    donation_amount=input("\nEnter amount to donate:",)
    donation_string=username+ " donated $"+ str(donation_amount)
    print("Thank you for donating!\n")
    return donation_string

def show_donations(donations):
    print("\n---All Donations---")
    if len(donations)<=0:
        print("Currently, there are no donations.")
    else:
        for i in donations:
            print(i)