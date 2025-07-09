
---

## 📁 2. Currency Converter — `README.md`

```markdown
# 💱 Currency Converter (Static Rates)

A simple Python CLI tool to convert an amount from one currency to another using fixed (mock) exchange rates.

---

## ✨ Features
- Converts between USD, INR, and EUR
- Demonstrates basic math operations and function usage
- Easy to understand and modify

---

## ✅ Prerequisites
- Python 3.x

---

## ▶️ How to Run
1. Save the file as `currency_converter.py`
2. Run it:
```bash
python currency_converter.py

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
