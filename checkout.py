def get_discount_rate(customer_type):
    """Return the discount rate for a given customer type."""
    rates = {"regular": 0.0, "silver": 0.05, "gold": 0.10}
    return rates.get(customer_type)


def calculate_total(price, quantity, discount):
    """Calculate the discounted subtotal."""
    subtotal = price * quantity
    total = subtotal - (subtotal * discount)
    return total


def get_customer_tier(total_spent):
    """Classify a customer based on lifetime spend."""
    if total_spent >= 1000:
        return "gold"
    elif total_spent >= 500:
        return "silver"
    elif total_spent >= 100:
        return "regular"


def format_receipt(customer_name, items, total):
    """Build a printable receipt string."""
    lines = [f"Receipt for {customer_name}"]
    for item in items:
        lines.append(f"- {item}")
    lines.append(f"Total: ${total:.2f}")
    return "\n".join(lines)


# --- main flow ---
customer_name = "Amina Uwase"
items = ["Laptop", "Mouse", "Keyboard"]
price = 850.00
quantity = 1
customer_type = "platinum"        # not one of the known tiers
customer_lifetime_spend = 45      # a new customer

discount = get_discount_rate(customer_type)
total = calculate_total(price, quantity, discount)
tier = get_customer_tier(customer_lifetime_spend)
receipt = format_receipt(customer_name, items, total)

print(receipt)
print(f"Customer tier: {tier}")
