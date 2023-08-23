import tkinter as tk
from forex_python.converter import CurrencyRates

# Create a tkinter window
window = tk.Tk()
window.title("Currency Converter")

#Set the size of the window
window.geometry("400x450")  


# Function to perform the conversion
def convert_currency():
    amount = float(entry_amount.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    
    result_text = f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
    label_result.config(text=result_text)

# List of available currencies
currencies = [
    "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK",
    "NZD", "KRW", "SGD", "NOK", "MXN", "INR", "RUB", "BRL", "ZAR",
    "TRY", "HKD", "ILS", "IDR", "PLN", "PHP", "THB", "MYR", "HUF",
    "CZK", "DKK", "RON", "COP", "ARS", "AED", "SAR", "CLP", "EGP",
    "KWD", "QAR", "VND", "BDT", "NGN", "PKR", "LKR", "TWD", "TND",
    "UAH", "PEN", "XAF", "NGN", "UGX", "RWF", "GHS", "ZWD", "TZS"
]

# Currency choices
from_currency_var = tk.StringVar(value=currencies[0])
to_currency_var = tk.StringVar(value=currencies[1])

# Widgets with styling
label_title = tk.Label(window, text="Currency Converter", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
label_amount = tk.Label(window, text="Enter amount:", font=("Arial", 14), bg="#f0f0f0", fg="#555")
entry_amount = tk.Entry(window, font=("Arial", 14), width=10, bg="white", fg="#222", relief="flat")

label_from_currency = tk.Label(window, text="From currency:", font=("Arial", 14), bg="#f0f0f0", fg="#555")
dropdown_from_currency = tk.OptionMenu(window, from_currency_var, *currencies)
dropdown_from_currency.configure(bg="white", fg="#222", relief="flat")

label_to_currency = tk.Label(window, text="To currency:", font=("Arial", 14), bg="#f0f0f0", fg="#555")
dropdown_to_currency = tk.OptionMenu(window, to_currency_var, *currencies)
dropdown_to_currency.configure(bg="white", fg="#222", relief="flat")

btn_convert = tk.Button(window, text="Convert", command=convert_currency, font=("Arial", 16, "bold"), bg="#007f5f", fg="white", padx=20, pady=10, borderwidth=0)
label_result = tk.Label(window, text="", font=("Arial", 18, "bold"), padx=20, pady=10, bg="#f0f0f0", fg="#333")

# Layout
label_title.pack(pady=10)
label_amount.pack()
entry_amount.pack()
label_from_currency.pack()
dropdown_from_currency.pack()
label_to_currency.pack()
dropdown_to_currency.pack()
btn_convert.pack(pady=15)
label_result.pack()

# Start the GUI event loop
window.mainloop()