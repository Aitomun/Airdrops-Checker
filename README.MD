# 🛡️ Airtdrops-Checker

![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**A professional-grade, multi-chain wallet scanner built for speed and simplicity.**

This tool automatically detects **EVM (Ethereum, Base, Arb)** and **Solana** addresses, scans them for native balances and **Memecoins**, and generates a detailed CSV report with Net Worth calculations. Powered by the [Moralis API](https://moralis.io).

---

## ⚡ Features

* **🔍 Auto-Detection:** Smartly identifies if an address is ETH/EVM or Solana.
* **💰 Memecoin Scanner:** Detects top token holdings (not just ETH/SOL).
* **📊 Excel Export:** Automatically saves all data to `premium_report.csv` for easy viewing.
* **🎨 Pro UI:** Color-coded terminal output (Green = Money found, Red = Error).
* **🔒 Secure:** API Keys are stored locally on your machine.
* **🚀 Executable Ready:** Can be bundled into a `.exe` for one-click use.

---

## 🛠️ Installation & Setup

### Prerequisites
1.  **Python 3.8+** installed ([Download Here](https://www.python.org/downloads/)).
2.  A free **Moralis API Key** (See "Configuration" below).

### Step 1: Clone or Download
Download this project to a folder on your computer (e.g., `Documents/Airdrops-Checker`).

### Step 2: Install Dependencies
Open your terminal (Command Prompt or VS Code) in the project folder and run:

```bash
pip install -r requirements.txt

If you do not have a requirements.txt file yet, run this command instead:

Bash

pip install moralis pandas colorama auto-py-to-exe
⚙️ Configuration
1. Get your API Key
Go to Moralis.io and sign up (It's free).

Go to the Dashboard -> Settings -> API Keys.

Copy your Web3 API Key.

2. Prepare your Wallets
Create a file named wallets.txt in the project folder.

Paste your wallet addresses (one per line). You can mix ETH and SOL addresses.

Example wallets.txt:

Plaintext

0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA
0x57760A81D3E08170868351F9F8d380e5571216d6
🚀 Usage
Option A: Run via Python (For Developers)
Run the script directly in your terminal:

Bash

python checker.py
On the first run, it will ask for your Moralis API Key. Paste it and press Enter.

Option B: Build a One-Click App (For Customers/Non-Tech)
You can turn this script into a CryptoScanner.exe file that works without installing Python.

In your terminal, run:

Bash

auto-py-to-exe
Script Location: Browse and select checker.py.

Onefile: Select "One File" (Important!).

Console Window: Select "Console Based".

Icon: (Optional) Add an .ico file to make it look professional.

Click Convert .py to .exe.

The output file will be in the output folder. You can now send this .exe and the wallets.txt file to anyone!

📂 Project Structure
Your folder should look like this:


Airdrops-Checker/
│
├── checker.py             # The main script
├── wallets.txt            # Your list of addresses
├── api_key.secret         # Generated automatically (Stores your key)
├── premium_report.csv     # Generated automatically (The results)
└── README.md              # This file
⚠️ Disclaimer
EDUCATIONAL PURPOSES ONLY.

This software is provided "as is", without warranty of any kind. The authors are not responsible for any financial losses, API rate limits, or bans resulting from the use of this tool.

Always verify the code before running it.

Never share your api_key.secret file with others.

This tool reads public blockchain data only; it cannot access private keys or funds.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Built by [Your Name]

Appendix: Requirements.txt
If you need to create the requirements.txt file, copy the content below:

Plaintext

moralis==0.1.31
pandas==2.1.4
colorama==0.4.6
web3==6.11.1
solana==0.30.2
solders==0.18.0

auto-py-to-exe==2.41.0
