from .utils import MToken,  prepare_tx_params_deposit_instant
from .token_metadata_database import UNKN
from types import SimpleNamespace
from eth_typing import ChainId

class TestDepositInstant:
    def __deposit_instant(self, request, sign_helper, eth_client, m_token, params = None):
        tx_params = prepare_tx_params_deposit_instant(eth_client, m_token, params)
        sign_helper.sign_and_ui_validate(tx_params)

    def test_deposit_instant_m_tbill(self, request, sign_helper, eth_client):
        self.__deposit_instant(request, sign_helper, eth_client, MToken.mTBILL)

    def test_deposit_instant_m_basis(self, request, sign_helper, eth_client):
        self.__deposit_instant(request, sign_helper, eth_client, MToken.mBASIS)

    def test_deposit_instant_m_btc(self, request, sign_helper, eth_client):
        self.__deposit_instant(request, sign_helper, eth_client, MToken.mBTC)

    def test_deposit_instant_m_tbill_unknown_payment_token(self, request, sign_helper, eth_client):
        self.__deposit_instant(request, sign_helper, eth_client, MToken.mBASIS, SimpleNamespace(token=UNKN))

    def test_deposit_instant_m_tbill_base(self, request, sign_helper, eth_client):
        self.__deposit_instant(request, sign_helper, eth_client, MToken.mTBILL_BASE, SimpleNamespace(chainId=ChainId.BASE))

    def test_deposit_instant_m_basis_base(self, request, sign_helper, eth_client):
        self.__deposit_instant(request, sign_helper, eth_client, MToken.mBASIS_BASE, SimpleNamespace(chainId=ChainId.BASE))
