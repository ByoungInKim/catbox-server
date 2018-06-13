import bitcoin
from bitcoin.wallet import CBitcoinAddress
from bitcoin.core.script import CScript
from bitcoin.rpc import Proxy

bitcoin.SelectParams('testnet')

class BitcoinRpc():
    def get_new_address(self):
        bitcoin_proxy = Proxy()
        return bitcoin_proxy.getnewaddress()
