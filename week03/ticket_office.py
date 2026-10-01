total_tickets = 0
total_revenue = 0.0
free_tickets = 0

while True:
    name = input("Customer name (or q to quit): ").strip()
    if name.lower() == 'q':
        break
    
    
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        continue

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    
    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue

    
    student = input("Student (yes/no): ").strip().lower()
    if student not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    
    base_price = 200.0 if day == "weekday" else 250.0
    discount = 0.0
    category = "Standard"

    if age < 6:
        discount = 1.00
        category = "Free"
    elif age >= 65:
        discount = 0.50
        category = "Senior"
    elif 6 <= age <= 12:
        discount = 0.40
        category = "Child"
    elif student == "yes" and age <= 25:
        discount = 0.30
        category = "Student"
    else:
        discount = 0.00
        category = "Standard"

    final_price = base_price * (1 - discount)

    print(f"{name}: {final_price:.2f} TRY ({category})")

    total_tickets += 1
    total_revenue += final_price
    if category == "Free":
        free_tickets += 1

if total_tickets == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / total_tickets
    print(f"Tickets sold: {total_tickets} Total revenue: {total_revenue:.2f} TRY Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
