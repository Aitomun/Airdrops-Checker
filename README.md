A program to help crypto farmers check their coins and airdrops easily all locally
# 🛡️ Crypto Universal Checker (V3)

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
Download this project to a folder on your computer (e.g., `Documents/Crypto_Scripts`).

### Step 2: Install Dependencies
Open your terminal (Command Prompt or VS Code) in the project folder and run:

```bash
pip install -r requirements.txt
