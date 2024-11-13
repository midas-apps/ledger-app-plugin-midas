import os
import re
from pathlib import Path
from typing import Optional
import json
from enum import Enum

from web3 import Web3

from eth_typing import ChainId
from .token_metadata_database import USDT
from ledger_app_clients.ethereum.client import EthAppClient
import ledger_app_clients.ethereum.response_parser as ResponseParser
from ledger_app_clients.ethereum.utils import get_selector_from_data, recover_transaction
from ragger.navigator import NavInsID
import ledger_app_clients.ethereum.response_parser as ResponseParser

DERIVATION_PATH = "m/44'/60'/0'/0/0"
makefile_relative_path = "../Makefile"

makefile_path = (Path(os.path.dirname(os.path.realpath(__file__))) / Path(makefile_relative_path)).resolve()

pattern = r'.*APPNAME.*=.*'

default_strip_parameter = " \t\n\r\x0b\x0c"

ABIS_FOLDER = "%s/abis" % (os.path.dirname(__file__))



def get_appname_from_makefile() -> str:
    '''
    Parse the app Makefile to automatically get the APPNAME value
    '''
    APPNAME: Optional[str] = None
    with open(makefile_path) as file:
        for line in file:
            if re.search(pattern, line):
                _, var = line.partition("=")[::2]
                APPNAME = var.strip(default_strip_parameter + '"')

    if APPNAME is None:
        raise AssertionError("Unable to find APPNAME in the Makefile")

    return APPNAME


class WalletAddr:
    client: EthAppClient

    def __init__(self, backend):
        self.client = EthAppClient(backend)

    def get(self, path=DERIVATION_PATH) -> bytes:
        with self.client.get_public_addr(display=False, bip32_path=path):
            pass
        return ResponseParser.pk_addr(self.client.response().data)[1]

class Object(object):
    pass

class MToken(Enum):
    mBASIS = "mBASIS"
    mTBILL = "mTBILL"
    mBASIS_BASE = "mBASIS_BASE"
    mTBILL_BASE = "mTBILL_BASE"
    mBTC = "mBTC"

class RedemptionVaultType(Enum):
    REGULAR = 0
    BUIDL = 0
    SWAPPER = 0
    

def load_contract(m_product_name, addr):
    with open(f"{ABIS_FOLDER}/{m_product_name}/{addr}.abi.json") as file:
        contract = Web3().eth.contract(
            abi=json.load(file),
            # Get address from filename
            address=bytes.fromhex(os.path.basename(file.name).split(".")[0].split("x")[-1])
        )
    return contract

def load_contracts():
    obj = Object()
    
    obj.mTBillDepositVaultContract = load_contract("mTBILL","0x99361435420711723aF805F08187c9E6bF796683")
    obj.mTBillRedemptionVaultContract = load_contract("mTBILL","0xF6e51d24F4793Ac5e71e0502213a9BBE3A6d4517")
    obj.mTBillRedemptionVaultBuidlContract = load_contract("mTBILL","0x569D7dccBF6923350521ecBC28A555A500c4f0Ec")
    
    obj.mBasisDepositVaultContract = load_contract("mBASIS","0xa8a5c4FF4c86a459EBbDC39c5BE77833B3A15d88")
    obj.mBasisRedemptionVaultContract = load_contract("mBASIS","0x19AB19e61A930bc5C7B75Bf06cDd954218Ca9F0b")
    obj.mBasisRedemptionVaultSwapperContract = load_contract("mBASIS","0x0D89C1C4799353F3805A3E6C4e1Cbbb83217D123")
    
    obj.mBtcDepositVaultContract = load_contract("mBTC","0x10cC8dbcA90Db7606013d8CD2E77eb024dF693bD")
    obj.mBtcRedemptionVaultContract = load_contract("mBTC","0x30d9D1e76869516AEa980390494AaEd45C3EfC1a")

    obj.mTBillBaseDepositVaultContract = load_contract("mTBILL_BASE","0x8978e327FE7C72Fa4eaF4649C23147E279ae1470")
    obj.mTBillBaseRedemptionVaultContract = load_contract("mTBILL_BASE","0x2a8c22E3b10036f3AEF5875d04f8441d4188b656")
    
    obj.mBasisBaseDepositVaultContract = load_contract("mBASIS_BASE","0x80b666D60293217661E7382737bb3E42348f7CE5")
    obj.mBasisBaseRedemptionVaultContract = load_contract("mBASIS_BASE","0xF804a646C034749b5484bF7dfE875F6A4F969840")

    return obj

contracts = load_contracts()
PLUGIN_NAME = get_appname_from_makefile()

def provide_token_metadata(client, token_metadata):
    client.provide_token_metadata(token_metadata.ticker,
                                    bytes.fromhex(token_metadata.address),
                                    token_metadata.decimals,
                                    token_metadata.chain_id)

def prepare_tx_params_deposit_instant(client, m_token = MToken.mTBILL, params = None):
    depositVault = None
    
    if m_token == MToken.mTBILL:
        depositVault = contracts.mTBillDepositVaultContract  
    elif m_token == MToken.mTBILL_BASE:
        depositVault = contracts.mTBillBaseDepositVaultContract  
    elif m_token == MToken.mBASIS: 
        depositVault = contracts.mBasisDepositVaultContract
    elif m_token == MToken.mBASIS_BASE: 
        depositVault = contracts.mBasisBaseDepositVaultContract
    else:
        depositVault = contracts.mBtcDepositVaultContract
    
    token = getattr(params, 'token', USDT)
    if token.supported:
        provide_token_metadata(client, token)

    data = depositVault.encode_abi("depositInstant", args=[
        Web3.to_checksum_address(token.address),
        Web3.to_wei(getattr(params, 'tokenAmount', 100), "ether"),
        Web3.to_wei(getattr(params, 'minToReceive', 0), "ether"),
        bytes.fromhex(getattr(params, 'referrerId', "00" * 32)),
    ])

    # first setup the external plugin
    client.set_external_plugin(PLUGIN_NAME,
                               depositVault.address,
                               # Extract function selector from the encoded data
                               get_selector_from_data(data))

    tx_params = {
        "nonce": 20,
        "maxFeePerGas": Web3.to_wei(145, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(1.5, "gwei"),
        "gas": 173290,
        "to": depositVault.address,
        "value": Web3.to_wei(0, "ether"),
        "chainId": getattr(params, 'chainId', ChainId.ETH),
        "data": data
    }

    return tx_params

def prepare_tx_params_deposit_request(client, m_token = MToken.mTBILL, params = None):
    depositVault = None

    if m_token == MToken.mTBILL:
        depositVault = contracts.mTBillDepositVaultContract  
    elif m_token == MToken.mTBILL_BASE:
        depositVault = contracts.mTBillBaseDepositVaultContract  
    elif m_token == MToken.mBASIS: 
        depositVault = contracts.mBasisDepositVaultContract
    elif m_token == MToken.mBASIS_BASE: 
        depositVault = contracts.mBasisBaseDepositVaultContract
    else:
        depositVault = contracts.mBtcDepositVaultContract
    
    token = getattr(params, 'token', USDT)
    if token.supported:
        provide_token_metadata(client, token)

    data = depositVault.encode_abi("depositRequest", args=[
        Web3.to_checksum_address(token.address),
        Web3.to_wei(getattr(params, 'tokenAmount', 100), "ether"),
        bytes.fromhex(getattr(params, 'referrerId', "00" * 32)),
    ])

    # first setup the external plugin
    client.set_external_plugin(PLUGIN_NAME,
                               depositVault.address,
                               # Extract function selector from the encoded data
                               get_selector_from_data(data))

    tx_params = {
        "nonce": 20,
        "maxFeePerGas": Web3.to_wei(145, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(1.5, "gwei"),
        "gas": 173290,
        "to": depositVault.address,
        "value": Web3.to_wei(0, "ether"),
        "chainId": getattr(params, 'chainId', ChainId.ETH),
        "data": data
    }

    return tx_params


def prepare_tx_params_redeem_instant(client, m_token = MToken.mTBILL, vault_type = RedemptionVaultType.REGULAR, params = None):
    redeemVault = None

    if vault_type == RedemptionVaultType.REGULAR:
        if m_token == MToken.mTBILL:
            redeemVault = contracts.mTBillRedemptionVaultContract  
        elif m_token == MToken.mTBILL_BASE:
            redeemVault = contracts.mTBillBaseRedemptionVaultContract  
        elif m_token == MToken.mBASIS: 
            redeemVault = contracts.mBasisRedemptionVaultContract
        elif m_token == MToken.mBASIS_BASE: 
            redeemVault = contracts.mBasisBaseRedemptionVaultContract
        else:
            redeemVault = contracts.mBtcRedemptionVaultContract
    elif vault_type == RedemptionVaultType.BUIDL:
        assert(m_token == MToken.mTBILL)
        redeemVault = contracts.mTBillRedemptionVaultBuidlContract
    elif vault_type == RedemptionVaultType.SWAPPER:
        assert(m_token == MToken.mBASIS)
        redeemVault = contracts.mBasisRedemptionVaultSwapperContract

    token = getattr(params, 'token', USDT)
    if token.supported:
        provide_token_metadata(client, token)

    data = redeemVault.encode_abi("redeemInstant", args=[
        Web3.to_checksum_address(token.address),
        Web3.to_wei(getattr(params, 'mTokenAmount', 10), "ether"),
        Web3.to_wei(getattr(params, 'minToReceive', 0), "ether")
    ])

    # first setup the external plugin
    client.set_external_plugin(PLUGIN_NAME,
                               redeemVault.address,
                               # Extract function selector from the encoded data
                               get_selector_from_data(data))

    tx_params = {
        "nonce": 20,
        "maxFeePerGas": Web3.to_wei(145, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(1.5, "gwei"),
        "gas": 173290,
        "to": redeemVault.address,
        "value": Web3.to_wei(0, "ether"),
        "chainId": getattr(params, 'chainId', ChainId.ETH),
        "data": data
    }

    return tx_params

def prepare_tx_params_redeem_request(client, m_token = MToken.mTBILL, vault_type = RedemptionVaultType.REGULAR, params = None):
    redeemVault = None

    if vault_type == RedemptionVaultType.REGULAR:
        if m_token == MToken.mTBILL:
            redeemVault = contracts.mTBillRedemptionVaultContract  
        elif m_token == MToken.mTBILL_BASE:
            redeemVault = contracts.mTBillBaseRedemptionVaultContract  
        elif m_token == MToken.mBASIS: 
            redeemVault = contracts.mBasisRedemptionVaultContract
        elif m_token == MToken.mBASIS_BASE: 
            redeemVault = contracts.mBasisBaseRedemptionVaultContract
    elif vault_type == RedemptionVaultType.BUIDL:
        assert(m_token == MToken.mTBILL)
        redeemVault = contracts.mTBillRedemptionVaultBuidlContract
    elif vault_type == RedemptionVaultType.SWAPPER:
        assert(m_token == MToken.mBASIS)
        redeemVault = contracts.mBasisRedemptionVaultSwapperContract

    data = None

    if getattr(params, 'requestFn', "redeemRequest") == 'redeemRequest':
        token = getattr(params, 'token', USDT)
        if token.supported:
            provide_token_metadata(client, token)

        data = redeemVault.encode_abi('redeemRequest', args=[
            Web3.to_checksum_address(token.address),
            Web3.to_wei(getattr(params, 'mTokenAmount', 100), "ether"),
        ])
    else:
        data = redeemVault.encode_abi('redeemFiatRequest', args=[
            Web3.to_wei(getattr(params, 'mTokenAmount', 100), "ether"),
        ])

    # first setup the external plugin
    client.set_external_plugin(PLUGIN_NAME,
                               redeemVault.address,
                               # Extract function selector from the encoded data
                               get_selector_from_data(data))

    tx_params = {
        "nonce": 20,
        "maxFeePerGas": Web3.to_wei(145, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(1.5, "gwei"),
        "gas": 173290,
        "to": redeemVault.address,
        "value": Web3.to_wei(0, "ether"),
        "chainId": getattr(params, 'chainId', ChainId.ETH),
        "data": data
    }

    return tx_params
