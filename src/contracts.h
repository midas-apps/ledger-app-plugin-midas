#include "eth_plugin_interface.h"

#define ETH_CHAIN_ID_LENGTH 1

#define M_TBILL_DEPOSIT_VAULT_ADDRESS_ETH                                                         \
    {                                                                                             \
        0x99, 0x36, 0x14, 0x35, 0x42, 0x07, 0x11, 0x72, 0x3a, 0xF8, 0x05, 0xF0, 0x81, 0x87, 0xc9, \
            0xE6, 0xbF, 0x79, 0x66, 0x83                                                          \
    }

#define M_TBILL_REDEMPTION_VAULT_ADDRESS_ETH                                                      \
    {                                                                                             \
        0xf6, 0xe5, 0x1d, 0x24, 0xf4, 0x79, 0x3a, 0xc5, 0xe7, 0x1e, 0x05, 0x02, 0x21, 0x3a, 0x9b, \
            0xbe, 0x3a, 0x6d, 0x45, 0x17                                                          \
    }

#define M_TBILL_REDEMPTION_BUIDL_VAULT_ADDRESS_ETH                                                \
    {                                                                                             \
        0x56, 0x9D, 0x7d, 0xcc, 0xBF, 0x69, 0x23, 0x35, 0x05, 0x21, 0xec, 0xBC, 0x28, 0xA5, 0x55, \
            0xA5, 0x00, 0xc4, 0xf0, 0xEc                                                          \
    }

#define M_BTC_DEPOSIT_VAULT_ADDRESS_ETH                                                           \
    {                                                                                             \
        0x10, 0xcc, 0x8d, 0xbc, 0xa9, 0x0d, 0xb7, 0x60, 0x60, 0x13, 0xd8, 0xcd, 0x2e, 0x77, 0xeb, \
            0x02, 0x4d, 0xf6, 0x93, 0xbd                                                          \
    }

#define M_BTC_REDEMPTION_VAULT_ADDRESS_ETH                                                        \
    {                                                                                             \
        0x30, 0xd9, 0xd1, 0xe7, 0x68, 0x69, 0x51, 0x6a, 0xea, 0x98, 0x03, 0x90, 0x49, 0x4a, 0xae, \
            0xd4, 0x5c, 0x3e, 0xfc, 0x1a                                                          \
    }

#define M_TBILL_DEPOSIT_VAULT_ADDRESS_BASE                                                        \
    {                                                                                             \
        0x89, 0x78, 0xe3, 0x27, 0xfe, 0x7c, 0x72, 0xfa, 0x4e, 0xaf, 0x46, 0x49, 0xc2, 0x31, 0x47, \
            0xe2, 0x79, 0xae, 0x14, 0x70                                                          \
    }

#define M_TBILL_REDEMPTION_VAULT_ADDRESS_BASE                                                     \
    {                                                                                             \
        0x2a, 0x8c, 0x22, 0xE3, 0xb1, 0x00, 0x36, 0xf3, 0xAE, 0xF5, 0x87, 0x5d, 0x04, 0xf8, 0x44, \
            0x1d, 0x41, 0x88, 0xb6, 0x56                                                          \
    }

typedef enum m_product_e { M_TBILL, M_BASIS, M_BTC } m_product_t;

static const uint8_t m_tbill_deposit_vault_address_eth[ADDRESS_LENGTH] =
    M_TBILL_DEPOSIT_VAULT_ADDRESS_ETH;
static const uint8_t m_tbill_redemption_vault_address_eth[ADDRESS_LENGTH] =
    M_TBILL_REDEMPTION_VAULT_ADDRESS_ETH;
static const uint8_t m_tbill_redemption_buidl_vault_address_eth[ADDRESS_LENGTH] =
    M_TBILL_REDEMPTION_BUIDL_VAULT_ADDRESS_ETH;

static const uint8_t m_btc_deposit_vault_address_eth[ADDRESS_LENGTH] =
    M_BTC_DEPOSIT_VAULT_ADDRESS_ETH;
static const uint8_t m_btc_redemption_vault_address_eth[ADDRESS_LENGTH] =
    M_BTC_REDEMPTION_VAULT_ADDRESS_ETH;

static const uint8_t m_tbill_deposit_vault_address_base[ADDRESS_LENGTH] =
    M_TBILL_DEPOSIT_VAULT_ADDRESS_BASE;
static const uint8_t m_tbill_redemption_vault_address_base[ADDRESS_LENGTH] =
    M_TBILL_REDEMPTION_VAULT_ADDRESS_BASE;

static const uint8_t ETH_CHAIN_ID[ETH_CHAIN_ID_LENGTH] = {0x01};