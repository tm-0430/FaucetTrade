import argparse
import requests

def request_tokens(network, address):
    # Example URL - replace with actual Faucet.trade API endpoint if available
    url = f"https://faucet.trade/api/request?network={network}&address={address}"
    try:
        response = requests.post(url)
        if response.status_code == 200:
            print(f"Successfully requested tokens for {address} on {network}")
        else:
            print(f"Failed to request tokens: {response.text}")
    except Exception as e:
        print(f"Error during request: {e}")

def main():
    parser = argparse.ArgumentParser(description="Faucet.trade CLI to request testnet tokens")
    parser.add_argument('network', type=str, help="Testnet network name (e.g., sepolia, polygon_amoy)")
    parser.add_argument('address', type=str, help="Your wallet address")
    args = parser.parse_args()

    request_tokens(args.network, args.address)

if __name__ == "__main__":
    main()
