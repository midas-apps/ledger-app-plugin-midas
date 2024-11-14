from .utils import MToken, RedemptionVaultType, prepare_tx_params_redeem_instant
from types import SimpleNamespace
from .token_metadata_database import UNKN
from eth_typing import ChainId


class TestRedeemInstant:
    def __redeem_instant(self, request, sign_helper, eth_client, m_token, vault_type = RedemptionVaultType.REGULAR, params = None):
        tx_params = prepare_tx_params_redeem_instant(eth_client, m_token, vault_type, params)
        sign_helper.sign_and_ui_validate(tx_params)

    def test_redeem_instant_m_tbill(self, request, sign_helper, eth_client):
        self.__redeem_instant(request, sign_helper, eth_client, MToken.mTBILL)

    def test_redeem_instant_m_basis(self, request, sign_helper, eth_client):
        self.__redeem_instant(request, sign_helper, eth_client, MToken.mBASIS)

    def test_redeem_instant_m_btc(self, request, sign_helper, eth_client):
        self.__redeem_instant(request, sign_helper, eth_client, MToken.mBTC)

    def test_redeem_instant_buidl_m_tbill(self, request, sign_helper, eth_client):
        self.__redeem_instant(request, sign_helper, eth_client, MToken.mTBILL, RedemptionVaultType.BUIDL)

    def test_redeem_instant_swapper_m_basis(self, request, sign_helper, eth_client):
        self.__redeem_instant(request, sign_helper, eth_client, MToken.mBASIS, RedemptionVaultType.SWAPPER)

    def test_redeem_instant_m_tbill_unknown_payment_token(self, request, sign_helper, eth_client):
        self.__redeem_instant(request, sign_helper, eth_client, MToken.mBASIS, RedemptionVaultType.REGULAR, SimpleNamespace(token=UNKN))

    def test_redeem_instant_m_tbill_base(self, request, sign_helper, eth_client):
        self.__redeem_instant(request, sign_helper, eth_client, MToken.mTBILL_BASE, RedemptionVaultType.REGULAR, SimpleNamespace(chainId=ChainId.BASE))

    def test_redeem_instant_m_basis_base(self, request, sign_helper, eth_client):
        self.__redeem_instant(request, sign_helper, eth_client, MToken.mBASIS_BASE, RedemptionVaultType.REGULAR, SimpleNamespace(chainId=ChainId.BASE))