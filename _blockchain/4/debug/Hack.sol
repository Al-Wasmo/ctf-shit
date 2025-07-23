// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Telephone.sol";



contract Hack {
    event LogAddress(address addr);

    address public owner;

    Telephone telephone = Telephone(0x1F708C24a0D3A740cD47cC0444E9480899f3dA7D);

    function log_tx_msg() public {
        emit LogAddress(msg.sender);
        emit LogAddress(tx.origin);
    }
}
