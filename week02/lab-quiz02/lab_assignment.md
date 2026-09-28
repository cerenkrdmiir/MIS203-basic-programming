item1_name = input("Enter first item name: ").strip()
item1_qty = int(input("Enter first item quantity: "))
item1_price = float(input("Enter first item unit price: "))

item2_name = input("Enter second item name: ").strip()
item2_qty = int(input("Enter second item quantity: "))
item2_price = float(input("Enter second item unit price: "))

delivery_fee = float(input("Enter delivery fee: "))
tax_percent = float(input("Enter tax percentage (0-100): "))

line1_total = item1_qty * item1_price
line2_total = item2_qty * item2_price
subtotal = line1_total + line2_total

tax_amount = subtotal * (tax_percent / 100)
final_total = subtotal + tax_amount + delivery_fee

print("\n" + "="*40)
print("          PURCHASE QUOTE SUMMARY          ")
print("="*40)
print(f"Item 1 ({item1_name}): {item1_qty} x {item1_price:.2f} = {line1_total:.2f} TRY")
print(f"Item 2 ({item2_name}): {item2_qty} x {item2_price:.2f} = {line2_total:.2f} TRY")
print("-" * 40)
print(f"Subtotal:      {subtotal:.2f} TRY")
print(f"Tax ({tax_percent:.1f}%):   {tax_amount:.2f} TRY")
print(f"Delivery Fee: {delivery_fee:.2f} TRY")
print("="*40)
print(f"FINAL TOTAL:   {final_total:.2f} TRY")
print("="*40)
