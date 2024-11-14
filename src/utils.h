#include "eth_plugin_interface.h"
#include "contracts.h"

static inline void printf_hex_array(const char *title __attribute__((unused)),
                                    size_t len __attribute__((unused)),
                                    const uint8_t *data __attribute__((unused))) {
    PRINTF(title);
    for (size_t i = 0; i < len; ++i) {
        PRINTF("%02x", data[i]);
    };
    PRINTF("\n");
}
static inline m_product_t determine_product_type_eth(uint8_t *contract_address) {
    bool isMtbill =
        memcmp(m_tbill_deposit_vault_address_eth, contract_address, ADDRESS_LENGTH) == 0 ||
        memcmp(m_tbill_redemption_vault_address_eth, contract_address, ADDRESS_LENGTH) == 0 ||
        memcmp(m_tbill_redemption_buidl_vault_address_eth, contract_address, ADDRESS_LENGTH) == 0;

    if (isMtbill) {
        return M_TBILL;
    }

    bool isMbtc = memcmp(m_btc_deposit_vault_address_eth, contract_address, ADDRESS_LENGTH) == 0 ||
                  memcmp(m_btc_redemption_vault_address_eth, contract_address, ADDRESS_LENGTH) == 0;

    if (isMbtc) {
        return M_BTC;
    }

    return M_BASIS;
}

static inline m_product_t determine_product_type_base(uint8_t *contract_address) {
    bool isMtbill =
        memcmp(m_tbill_deposit_vault_address_base, contract_address, ADDRESS_LENGTH) == 0 ||
        memcmp(m_tbill_redemption_vault_address_base, contract_address, ADDRESS_LENGTH) == 0;

    if (isMtbill) {
        return M_TBILL;
    }

    return M_BASIS;
}

static inline bool is_eth_network(const txInt256_t *chain_id) {
    if (memcmp(chain_id->value, ETH_CHAIN_ID, ETH_CHAIN_ID_LENGTH) == 0) {
        return true;
    }

    return false;
}

static inline m_product_t determine_product_type(uint8_t *contract_address,
                                                 const txInt256_t *chain_id) {
    if (is_eth_network(chain_id)) {
        return determine_product_type_eth(contract_address);
    } else {
        return determine_product_type_base(contract_address);
    }
}
