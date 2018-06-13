import bitcoin
from bitcoin.wallet import CBitcoinAddress
from bitcoin.core.script import CScript
from bitcoin.rpc import Proxy

bitcoin.SelectParams('testnet')

class BitcoinRpc():
    bitcoin_proxy = None
    
    def __init__(self):
        self.bitcoin_proxy = Proxy()

    def get_new_address(self):
        return self.bitcoin_proxy.getnewaddress()

    def get_balance(self):
        return self.bitcoin_proxy.getbalance()