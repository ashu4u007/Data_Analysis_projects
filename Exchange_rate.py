import requests

def get_exchange_rate(base_currency, target_currency):
    """
    Fetches the live exchange rate between two currencies using ExchangeRate-API.
    """
    # Using the free, no-auth pair conversion endpoint from ExchangeRate-API
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an error for bad status codes
        data = response.json()
        
        if data.get("result") == "success":
            rates = data.get("rates", {})
            target_rate = rates.get(target_currency.upper())
            
            if target_rate:
                return target_rate
            else:
                print(f"❌ Error: Currency '{target_currency}' not found.")
                return None
        else:
            print("❌ Error: Unable to fetch data from the API.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: Could not connect to the exchange rate service. ({e})")
        return None

def convert_currency():
    print("🌍 --- Global Jetsetter Currency Converter --- 🌍")
    
    # 1. Get User Input
    base = input("Enter base currency (e.g., USD, EUR, GBP): ").strip().upper()
    target = input("Enter target currency (e.g., INR, JPY, CAD): ").strip().upper()
    
    try:
        amount = float(input(f"Enter amount in {base}: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")
        return

    # 2. Fetch live rate and calculate
    rate = get_exchange_rate(base, target)
    
    if rate:
        converted_amount = amount * rate
        print("\n--- Live Conversion Result ---")
        print(f"💰 {amount:,.2f} {base} = {converted_amount:,.2f} {target}")
        print(f"📈 Current Rate: 1 {base} = {rate:.4f} {target}")
        
        # 3. Handle Reverse Conversion
        reverse = input(f"\n🔄 Do you want to see the reverse conversion ({target} to {base})? (y/n): ").strip().lower()
        if reverse == 'y':
            reverse_rate = 1 / rate
            reverse_amount = amount * reverse_rate
            print(f"\n🔄 {amount:,.2f} {target} = {reverse_amount:,.2f} {base}")
            print(f"📈 Reverse Rate: 1 {target} = {reverse_rate:.4f} {base}")
            
    print("\nSafe travels! 🛫")

# Run the tool
if __name__ == "__main__":
    convert_currency()
