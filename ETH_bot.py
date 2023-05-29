import time

from web3 import Account, Web3
from bridge.eth_bridge import swap_eth_arbitrum_optimism, swap_eth_optimism_arbitrum, get_balance_eth_arbitrum, balance_eth_arbitrum, balance_eth_optimism, get_balance_eth_optimism


def main(tr):
    with open('keys.txt', 'r') as keys_file:
        accounts = [Account.from_key(line.replace("\n", "")) for line in keys_file.readlines()]
        for _ in range(0, tr):
            for account in accounts:
                arbitrum_balance = get_balance_eth_arbitrum(account.address)
                optimism_balance = get_balance_eth_optimism(account.address)

                if arbitrum_balance + optimism_balance < Web3.to_wei(0.02, 'ether'):
                    continue

                if arbitrum_balance > optimism_balance:
                    print("Swapping ETH from Arbitrum to Optimism...")
                    arbitrum_to_optimism_txs_hash = swap_eth_arbitrum_optimism(account=account, amount=arbitrum_balance - Web3.to_wei(0.01, 'ether'))
                    print("Waiting for the swap to complete...")
                    time.sleep(20)
                    print(f"Transaction: https://arbiscan.io/tx/{arbitrum_to_optimism_txs_hash.hex()}")
                else: 
                    print("Swapping ETH from Optimism to Arbitrum...")
                    optimism_to_arbitrum_txs_hash = swap_eth_optimism_arbitrum(account=account, amount=optimism_balance - Web3.to_wei(0.01, 'ether'))
                    print("Waiting for the swap to complete...")
                    time.sleep(20)
                    print(f"Transaction: https://optimistic.etherscan.io/tx{optimism_to_arbitrum_txs_hash.hex()}")

                print("Sleeping 60 seconds for the next account")
                time.sleep(60)

            print("Sleeping 1200 seconds for the next cycle")
            print("Balance Arbitrum in eth: ")
            arbitrum_balance_txn = balance_eth_arbitrum(account=account)
            print(arbitrum_balance)
            print("Balance Optimism in eth: ")
            optimism_balance_txn = balance_eth_optimism(account=account)
            print(optimism_balance)
            time.sleep(1200)


if __name__ == '__main__':
    total_rounds = 10
    main(total_rounds)
    
