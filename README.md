# ERC20 Smart Contract.
#### Deploy your own ERC20 Token easily!

Created using [OpenZeppelin](https://openzeppelin.com/)'s [ERC20](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol) and its extensions Smart Contracts.

### Features:

1. Mint
1. Pause/Unpause transfers
1. Burn


### Prerequisites:

##### Rinkeby deployment
- [Python](https://www.python.org/downloads/)
- Brownie
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart terminal
pipx install eth-brownie
```
- A free [Infura](https://infura.io/) Project Id key for Rinkeby Network

### Instalation 

Clone this repo:

```
git clone https://github.com/andreitoma8/ERC20-Token
cd ERC20-Token
```

### Deploy to Rinkeby

- Add a `.env` file with the same contents of `.env.example`, but replaced with your variables.

- In `scripts/deploy.py` change `"Ethereum", "ETH"` with your wanted Token Name or Symbol.

- Run the command:
```
brownie run scripts/deploy.py --network rinkeby
```
The script will deploy your Smart Contract and mint 1.000.000 tokens for yourself.

To deploy to any other network change rinkeby in the command with the name of the network:

```
brownie run scripts/deploy.py --network [network name]
```
and your `WEB3_INFURA_PROJECT_ID` in the `.env` file with a Project Id for that network.

##### Any feedback is much apreciated! 
##### If this was helpful please consider donating: 
`0xA4Ad17ef801Fa4bD44b758E5Ae8B2169f59B666F`

# Happy hacking!
