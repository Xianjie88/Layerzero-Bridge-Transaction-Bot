# Layerzero-Bridge-Transaction-Bot

This bot is for the upcoming LayerZero airdrop, Automatically record Stargate Finance Bridge transactions.

## ✨Summary

Automatically transfer **$STG** or **$USDC** held in your wallet from the **Polygon network** to the **Fantom network**, or vice versa. (via **Stargate Finance Bridge**).

  > Why polygon, fhantom networks?
  > The reason is simple. It's because gas fees are the cheapest.

## 💨 Features

- Automation

- Repeat

- Supports $STG, $USDC (more tokens coming soon)

  > $USDC is a stablecoin and you don't have to worry about price fluctuations. However, slippage occurs and the balance decreases ever so slightly.
  >
  > $STG never slippage and always has the same balance. However, prices change frequently.

## 🚧 Prerequisites

- **Python 3.10.6** (3.10.x versions are also possible)
- **$STG** or **$USDC** (Bridge)
- **$MATIC** and **$FTM** (Gas fee)

## 📝 Setup

1. Install python 3.10.6
2. Clone repository
3. Install required packages

```python
pip install -r requirements.txt
```

4. Paste your metamask private keys in **keys.txt**

   > **No, mnemonic seed phrase**
   >
   > How to export an accounts private key​ https://support.metamask.io/hc/en-us/articles/360015289632-How-to-export-an-account-s-private-key 

   

---

## 📝 Usage

If you want to bridge $USDC, run 'USDC_bot.py'

  ```python
python USDC_bot.py
  ```

If you want to bridge $STG, run 'STG_bot.py'.

  ```python
python STG_bot.py
  ```

The bot automatically detects the wallet balance and starts the bridge operation. It takes about two to three minutes per time and repeats until the user interrupts the action.
