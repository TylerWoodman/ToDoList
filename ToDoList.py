import json

username = input("What is your username?")

option = 0

def calculate_total_spend(subscriptions):
    total = int(0)
    amount = int(0)
    for items in subscriptions.values():
        cost = items["cost"]
        total = total + cost 
        amount = amount + 1
    print(f"Subscription Amount: {amount}")
    print(f"Total Monthly: £{total}/month")
    print(f"Total Yearly: £{total * 12}/year")

def load_subscriptions():
    try:
        with open("subscriptions.json","r") as file:
            subscriptions = json.load(file)
            return subscriptions
    except FileNotFoundError:
        subscriptions = {}
        return subscriptions

def save_subscriptions(subscriptions):
    try:
        with open("subscriptions.json", "w") as file:
            json.dump(subscriptions, file)
    except Exception as e:
        print(e)   

def view_subscriptions(subscriptions):
    try:
        if not subscriptions:
            print("You have no active subscriptions.")
        else:
            for service, details in subscriptions.items():
                print(f"\n--- {service} ---")
                print(f"Cost: £{details["cost"]}")
                print("Ending Date:", details["end_date"])
    except Exception as e:
        print(e)

def add_subscriptions(subscriptions):
    try: 
        service = input("What is the service name?")
        while True:
            try:
                cost = float(input("What is the cost per month?"))
                break
            except ValueError:
                print("Invalid entry. Please enter a number (e.g. 5.99)")

        end_date = input("When is the next service payment due?")
        dictionary = {
            "cost": cost,
            "end_date": end_date
        }
        subscriptions[service] = dictionary
        print(f"The following has been added ~ {service}: £{cost}/month")
        save_subscriptions(subscriptions)
    except Exception as e:
        print(e)

def delete_subscriptions(subscriptions):
    try:
        service = input("What subscription would you like to remove?")
        if service in subscriptions:
            removed_subscription = subscriptions.pop(service)
            print (f"The service to {service} has been removed.")
            save_subscriptions(subscriptions)
        else:
            print("Sorry that service is not in your subscriptions, maybe your spelling is incorrect?")
    except Exception as e:
        print(e)

def edit_subscriptions(subscriptions):
    try:
        service = input("What subscription would you like to edit?")
        if service in subscriptions:
            option = int(input("Enter the corresponding number for your option: 1 = Update Cost, 2 = Update Due Date"))
            if option == 1:
                edit_cost = float(input("Update the cost"))
                subscriptions[service]["cost"] = edit_cost
                save_subscriptions(subscriptions)
            if option == 2:
                edit_end_date = input("Update the due date")
                subscriptions[service]["end_date"] = edit_end_date
                save_subscriptions(subscriptions)
    except Exception as e:
        print(e)

subscriptions = load_subscriptions()

while option != 3:
    print("\n--- MENU ---")
    while True:
        try:
            option = int(input("Enter the corresponding number for your option: 1 = View Subscription, 2 = Add Subscription, " \
            "3 = Quit, 4 = View Total Spend, 5 = Delete Subscription, 6 = Edit Subscription\nEnter option: "))
            break
        except ValueError:
            print("Invalid entry. Please enter a valid number from 1-5.\n")

    if option == 1:
        view_subscriptions(subscriptions)

    if option == 2:
        add_subscriptions(subscriptions)

    if option == 3:
        print("System shutting down....")
        break

    if option == 4:
        calculate_total_spend(subscriptions)

    if option == 5:
        delete_subscriptions(subscriptions)

    if option == 6:
        edit_subscriptions(subscriptions)

    




