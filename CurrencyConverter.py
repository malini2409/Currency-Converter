# CURRENCY CONVERTER
def convert_currency(amount, from_currency, to_currency):
    rates = {
        'USD': 1.0,
        'INR': 83.0,
        'EUR': 0.91
    }

    if from_currency not in rates or to_currency not in rates:
        return "Currency not supported."

    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    return converted

# Example usage
amount = float(input("Enter amount: "))
from_curr = input("From currency (USD/INR/EUR): ")
to_curr = input("To currency (USD/INR/EUR): ")

result = convert_currency(amount, from_curr.upper(), to_curr.upper())
print(f"Converted Amount: {result:.2f}")
