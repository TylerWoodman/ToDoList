import json

username = input("What is your username?")

try:
    with open("subscriptions.json","rb") as file:
        subscriptions = json.load(file)
except FileNotFoundError:
    subscriptions = {}

option = 0

def calculate_total_spend(subscriptions):
    total = 0
    amount = 0
    for cost in subscriptions.values():
        total = total + cost
        amount = amount + 1
    print(f"Subscription Amount: {amount}")
    print(f"Total Monthly: £{total}/month")
    print(f"Total Yearly: £{total * 12}/year")

while option != 3:
    print("\n--- MENU ---")
    option = int(input("Enter the corresponding number for your option: 1 = View Subscription, 2 = Add Subscription, 3 = Quit, 4 = View Total Spend\nEnter option: "))

    if option == 1:
        if not subscriptions:
            print("You have no active subscriptions.")
        else:
            for service, cost in subscriptions.items():
                print(f"{service}: £{cost:.2f}/month")

    if option == 2:
        service = input("What is the service name?")
        cost = float(input("What is the cost per month?"))
        end_date = input("When is the next service payment due?")
        dictionary = {
            "cost": cost,
            "end_date": end_date
        }
        subscriptions[service] = dictionary
        print(f"The following has been added ~ {service}: £{cost}/month")
        with open("subscriptions.json", "w") as file:
            json.dump(subscriptions, file)

    if option == 3:
        print("System shutting down....")
        break

    if option == 4:
        calculate_total_spend(subscriptions)
    




