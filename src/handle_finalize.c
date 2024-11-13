#include "plugin.h"

void handle_finalize(ethPluginFinalize_t *msg) {
    context_t *context = (context_t *) msg->pluginContext;

    msg->uiType = ETH_UI_TYPE_GENERIC;

    msg->numScreens = 1;

    context->is_deposit = false;
    context->is_request = false;
    context->is_fiat = false;

    switch (context->selectorIndex) {
        case DEPOSIT_INSTANT:
            context->is_deposit = true;
            __attribute__((fallthrough));
        case REDEEM_INSTANT:
            msg->numScreens += 1;
            break;
        case DEPOSIT_REQUEST:
            context->is_deposit = true;
            // dont need "You will receive" screen for deposit requests
            msg->numScreens -= 1;
            // fallthrough to REDEEM_FIAT_REQUEST case is expected
            // as it wont affect because it wont reach the screen №3
            __attribute__((fallthrough));
        case REDEEM_FIAT_REQUEST:
            context->is_fiat = true;
            __attribute__((fallthrough));
        case REDEEM_REQUEST:
            context->is_request = true;
            msg->numScreens += 2;
            break;
        default:
            PRINTF("handle_finalize: unsupported selector index");
            msg->result = ETH_PLUGIN_RESULT_ERROR;
            return;
    }

    printf_hex_array("Token lookup\n", ADDRESS_LENGTH, context->token_address);
    msg->tokenLookup1 = context->token_address;

    context->m_product = determine_product_type(msg->pluginSharedRO->txContent->destination,
                                                &msg->pluginSharedRO->txContent->chainID);

    msg->result = ETH_PLUGIN_RESULT_OK;
}
