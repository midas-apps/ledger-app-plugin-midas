# Technical Specification

> **Warning**
This documentation is a template and shall be updated.

## About

This documentation describes the smart contracts and functions supported by the boilerplate plugin.

## Smart Contracts

Smart contracts covered by the plugin shall be described here:

|  Network | Version | Smart Contract | Address |
|   ----   |   ---   |      ----      |   ---   |
| Mainnet   | v1  | MTbillDepositVault  | `0x99361435420711723aF805F08187c9E6bF796683` |
| Mainnet   | v1  | MTbillRedemptionVault  | `0xF6e51d24F4793Ac5e71e0502213a9BBE3A6d4517` |
| Mainnet   | v1  | MTbillRedemptionVaultBuidl  | `0x569D7dccBF6923350521ecBC28A555A500c4f0Ec` |
| Mainnet   | v1  | MBasisDepositVault  | `0xa8a5c4FF4c86a459EBbDC39c5BE77833B3A15d88` |
| Mainnet   | v1  | MBasisRedemptionVault  | `0x19AB19e61A930bc5C7B75Bf06cDd954218Ca9F0b` |
| Mainnet   | v1  | MBasisRedemptionVaultSwapper  | `0x0D89C1C4799353F3805A3E6C4e1Cbbb83217D123` |
| Mainnet   | v1  | MBtcDepositVault  | `0x10cC8dbcA90Db7606013d8CD2E77eb024dF693bD` |
| Mainnet   | v1  | MBtcRedemptionVault  | `0x30d9D1e76869516AEa980390494AaEd45C3EfC1a` |
| Base      | v1  | MTbillDepositVault  | `0x8978e327FE7C72Fa4eaF4649C23147E279ae1470` |
| Base      | v1  | MTbillRedemptionVault  | `0x2a8c22E3b10036f3AEF5875d04f8441d4188b656` |
| Base      | v1  | MBasisDepositVault  | `0x80b666D60293217661E7382737bb3E42348f7CE5` |
| Base      | v1  | MBasisRedemptionVaultSwapper  | `0xF804a646C034749b5484bF7dfE875F6A4F969840` |

## Functions

For the smart contracts implemented, the functions covered by the plugin shall be described here:

|Contract |    Function   | Selector  | Displayed Parameters |
|   ---   |    ---        | ---       | --- |
|MTbillDepositVault|depositInstant|`0xc02dd27a`| <table><tbody> <tr><td><code>address tokenIn </code></td></tr> <tr><td><code>uint256 amountToken</code></td></tr><tr><td><code>uint256 minReceiveAmount</code></td></tr> </tbody></table> |
|MTbillDepositVault|depositRequest|`0x6e26b9f8`| <table><tbody> <tr><td><code>address tokenIn </code></td></tr> <tr><td><code>uint256 amountToken</code></td></tr> </tbody></table> |
|MTbillRedemptionVault|redeemInstant|`0x8b53f75e`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr> <tr><td><code>uint256 minReceiveAmount </code></td></tr> </tbody></table> |
|MTbillRedemptionVault|redeemRequest|`0xbfc2d46a`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MTbillRedemptionVault|redeemFiatRequest|`0xd5f73f5c`| <table><tbody> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MTbillRedemptionVaultBuidl|redeemInstant|`0x8b53f75e`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr> <tr><td><code>uint256 minReceiveAmount </code></td></tr> </tbody></table> |
|MTbillRedemptionVaultBuidl|redeemRequest|`0xbfc2d46a`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MTbillRedemptionVaultBuidl|redeemFiatRequest|`0xd5f73f5c`| <table><tbody> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MBasisDepositVault|depositInstant|`0xc02dd27a`| <table><tbody> <tr><td><code>address tokenIn </code></td></tr> <tr><td><code>uint256 amountToken</code></td></tr><tr><td><code>uint256 minReceiveAmount</code></td></tr> </tbody></table> |
|MBasisDepositVault|depositRequest|`0x6e26b9f8`| <table><tbody> <tr><td><code>address tokenIn </code></td></tr> <tr><td><code>uint256 amountToken</code></td></tr> </tbody></table> |
|MBasisRedemptionVault|redeemInstant|`0x8b53f75e`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr> <tr><td><code>uint256 minReceiveAmount </code></td></tr> </tbody></table> |
|MBasisRedemptionVault|redeemRequest|`0xbfc2d46a`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MBasisRedemptionVault|redeemFiatRequest|`0xd5f73f5c`| <table><tbody> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MBasisRedemptionVaultSwapper|redeemInstant|`0x8b53f75e`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr> <tr><td><code>uint256 minReceiveAmount </code></td></tr> </tbody></table> |
|MBasisRedemptionVaultSwapper|redeemRequest|`0xbfc2d46a`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MBasisRedemptionVaultSwapper|redeemFiatRequest|`0xd5f73f5c`| <table><tbody> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MBtcDepositVault|depositInstant|`0xc02dd27a`| <table><tbody> <tr><td><code>address tokenIn </code></td></tr> <tr><td><code>uint256 amountToken</code></td></tr><tr><td><code>uint256 minReceiveAmount</code></td></tr> </tbody></table> |
|MBtcDepositVault|depositRequest|`0x6e26b9f8`| <table><tbody> <tr><td><code>address tokenIn </code></td></tr> <tr><td><code>uint256 amountToken</code></td></tr> </tbody></table> |
|MBtcRedemptionVault|redeemInstant|`0x8b53f75e`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr> <tr><td><code>uint256 minReceiveAmount </code></td></tr> </tbody></table> |
|MBtcRedemptionVault|redeemRequest|`0xbfc2d46a`| <table><tbody> <tr><td><code>address tokenOut </code></td></tr> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
|MBtcRedemptionVault|redeemFiatRequest|`0xd5f73f5c`| <table><tbody> <tr><td><code>uint256 amountMTokenIn</code></td></tr></tbody></table> |
