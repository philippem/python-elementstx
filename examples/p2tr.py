import os
import elementstx
from bitcointx import ChainParams, get_current_chain_params
from bitcointx.wallet import CCoinKey, CCoinExtKey, CCoinAddress, P2PKHCoinAddress, P2TRCoinAddress

## requires pip install wallycore
import wallycore as wally

k = CCoinExtKey.from_seed(os.urandom(32))
first_key_path="m/0'/0'/1"
first_key = k.derive_path(first_key_path)
first_key_pub = first_key.pub
mainnet_wif = first_key_priv = first_key.priv

print(f"pub={first_key_pub} priv={first_key_priv}")

key = wally.wif_to_bytes(str(mainnet_wif), wally.WALLY_ADDRESS_VERSION_WIF_MAINNET, wally.WALLY_WIF_FLAG_COMPRESSED)
testnet_wif = wally.wif_from_bytes(key, wally.WALLY_ADDRESS_VERSION_WIF_TESTNET, wally.WALLY_WIF_FLAG_COMPRESSED)
converted_mainnet_wif = wally.wif_from_bytes(key, wally.WALLY_ADDRESS_VERSION_WIF_MAINNET,
                                             wally.WALLY_WIF_FLAG_COMPRESSED)

assert converted_mainnet_wif == str(mainnet_wif)

print(f"elementsregtest privkey={testnet_wif} mainnet privkey={converted_mainnet_wif}")
with ChainParams('elements/elementsregtest'):


    a = P2PKHCoinAddress.from_pubkey(first_key_pub)
    print('example P2PKH {} address: {}'.format(get_current_chain_params().name, a))
    assert CCoinAddress(str(a)) == a

    b = P2TRCoinAddress.from_pubkey(first_key_pub)
    print('example P2TR {} address: {}'.format(get_current_chain_params().name, b))
    assert CCoinAddress(str(b)) == b

    print("\n")
    print("on receiver run:")
    print("\n")
    print("on receiver run:")
    print(f"elements-cli importprivkey {testnet_wif}")
    print(f"elements-cli importaddress {a}")
    print(f"elements-cli importaddress {b}")
    print(f"elements-cli getaddressinfo {b}")
    print(f"elements-cli getaddressinfo {a}")
    print("\n")
    print("on sender (must be e-21) run:")
    print(f"elements-cli sendtoaddress {b} <amount>")
    print("\n")
    print("\n")


with ChainParams('elements/liquidv1'):
    a = P2PKHCoinAddress.from_pubkey(first_key_pub)
    print('example {} address: {}'.format(get_current_chain_params().name, a))
    assert CCoinAddress(str(a)) == a

    b = P2TRCoinAddress.from_pubkey(first_key_pub)
    print('example {} address: {}'.format(get_current_chain_params().name, b))
    assert CCoinAddress(str(b)) == b

