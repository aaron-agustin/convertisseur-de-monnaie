from forex_python.converter import CurrencyRates
import json

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    
    try:
        rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        return converted_amount
    except:
        print("Conversion impossible. Vérifiez les devises fournies.")
        return None

def save_conversion_history(history, filename='conversion_history.json'):
    with open(filename, 'w') as file:
        json.dump(history, file)

def main():
    amount = float(input("Entrez le montant à convertir : "))
    from_currency = input("Entrez la devise de départ (par exemple, USD) : ").upper()
    to_currency = input("Entrez la devise cible (par exemple, EUR) : ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")

        # Enregistrement de l'historique
        history_entry = {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "converted_amount": converted_amount
        }

        try:
            with open('conversion_history.json', 'r') as file:
                history = json.load(file)
        except FileNotFoundError:
            history = []

        history.append(history_entry)
        save_conversion_history(history)

if __name__ == "__main__":
    main()
