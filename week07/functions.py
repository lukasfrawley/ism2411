#exercise 1
def calculate_tax(price, rate):
    return price * rate
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(200, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $200 at 8%: ${tax2:.2f}")
print(f"Another tax : ${calculate_tax(150, 0.05):.2f}")

#exercise2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
price = 200
tier = ["gold", "silver", "bronze", "none"]
for t in tier:
    discounted_price = apply_discount(price, t)
    print(f"Price after {tier} discount: ${discounted_price:.2f}")

#exercise 3
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"after gold discount: ${discounted:.2f}")
print(f"after tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

#Exercise 4
orders = [(200,"gold"), (150,"silver"), (80,"bronze"), (50,"none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Final price for ${price} with {tier} tier: ${total:.2f}")

#exercise 6
x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)
