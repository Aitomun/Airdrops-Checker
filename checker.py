import time
import pandas as pd
from moralis import evm_api, sol_api
from colorama import Fore, Style, init

# Initialize Colorama for colored text
init(autoreset=True)

def get_api_key():
    """
    Asks the user for their API Key on startup.
    """
    print(Fore.YELLOW + "--- Crypto Universal Checker v3 ---")
    print(Fore.CYAN + "To use this tool, you need a free Moralis API Key.")
    print(Fore.CYAN + "Get it here: https://admin.moralis.io/web3apis")
    print("-" * 40)
    
    # Try to load from a hidden file first (convenience for you)
    try:
        with open("api_key.secret", "r") as f:
            key = f.read().strip()
            if len(key) > 10:
                print(Fore.GREEN + "✅ Found saved API Key!")
                return key
    except FileNotFoundError:
        pass

    # If not found, ask user
    key = input(Fore.WHITE + "👉 Paste your API Key here: ").strip()
    
    # Save it for next time
    with open("api_key.secret", "w") as f:
        f.write(key)
    print(Fore.GREEN + "✅ Key saved for future use.")
    return key

def get_wallet_type(address):
    address = address.strip()
    if address.startswith("0x") and len(address) == 42:
        return "evm"
    elif 30 < len(address) < 45 and "0x" not in address:
        return "solana"
    else:
        return "unknown"

def check_evm_wallet(api_key, address):
    try:
        # 1. Get Native Balance (ETH)
        native = evm_api.balance.get_native_balance(
            api_key=api_key,
            params={"address": address, "chain": "eth"}
        )
        # FIX: Ensure we convert string to float immediately
        raw_balance = float(native["balance"]) 
        balance = raw_balance / 10**18
        
        # 2. Get Token Balances
        tokens = evm_api.token.get_wallet_token_balances(
            api_key=api_key,
            params={"address": address, "chain": "eth"}
        )
        
        token_list = []
        for token in tokens:
            if token.get('symbol') and float(token.get('balance', 0)) > 0:
                token_list.append(token['symbol'])
                
        return {
            "Type": "ETH",
            "Balance": balance,  # Return number, not formatted string yet
            "Tokens": ", ".join(token_list[:3]),
            "Token_Count": len(token_list),
            "Status": "Active"
        }
    except Exception as e:
        return {"Type": "ETH", "Status": "Error", "Tokens": str(e), "Balance": 0.0}

def check_solana_wallet(api_key, address):
    try:
        # 1. Get Portfolio
        portfolio = sol_api.account.get_portfolio(
            api_key=api_key,
            params={"network": "mainnet", "address": address}
        )
        
        # FIX: Handle the 'nativeBalance' being inside nested dicts and convert to float
        native_bal_data = portfolio.get('nativeBalance', {})
        sol_bal_str = native_bal_data.get('solana', '0')
        balance = float(sol_bal_str) # Convert string "1.5" to float 1.5
        
        tokens = portfolio.get('tokens', [])
        token_list = []
        for t in tokens:
             if t.get('symbol'):
                 token_list.append(t['symbol'])
             
        return {
            "Type": "SOL",
            "Balance": balance, # Return number
            "Tokens": ", ".join(token_list[:3]),
            "Token_Count": len(token_list),
            "Status": "Active"
        }
    except Exception as e:
         return {"Type": "SOL", "Status": "Error", "Tokens": str(e), "Balance": 0.0}

def main():
    api_key = get_api_key()
    
    try:
        with open("wallets.txt", "r") as f:
            wallets = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "❌ 'wallets.txt' not found! Please create it.")
        input("Press Enter to exit...")
        return

    print(Fore.CYAN + f"\n🚀 Scanning {len(wallets)} wallets...\n")
    results = []

    for wallet in wallets:
        chain = get_wallet_type(wallet)
        data = {}
        
        # Small delay to prevent connection errors
        time.sleep(0.2)

        if chain == "evm":
            data = check_evm_wallet(api_key, wallet)
            color = Fore.BLUE
        elif chain == "solana":
            data = check_solana_wallet(api_key, wallet)
            color = Fore.MAGENTA
        else:
            color = Fore.RED
            data = {"Type": "???", "Status": "Invalid Key", "Balance": 0.0, "Tokens": "-"}

        # Print to Terminal with safe formatting
        # We use :.4f safely because we ensured 'Balance' is a float above
        try:
            bal_display = f"{data['Balance']:.4f}"
        except:
            bal_display = "0.0000"

        print(f"{color}[{data.get('Type')}] {wallet[:6]}... | Bal: {bal_display} | Memes: {data.get('Token_Count', 0)} ({data.get('Tokens', '-')})")
        
        results.append({**{"Address": wallet}, **data})

    # Save Report
    try:
        df = pd.DataFrame(results)
        df.to_csv("premium_report.csv", index=False)
        print(Fore.GREEN + "\n✅ Scan Complete! Saved to 'premium_report.csv'")
    except Exception as e:
        print(Fore.RED + f"❌ Could not save CSV: {e}")

    input(Fore.WHITE + "\nPress Enter to close...")

if __name__ == "__main__":
    main()