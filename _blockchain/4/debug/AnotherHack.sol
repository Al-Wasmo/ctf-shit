// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Telephone.sol";
import "./Hack.sol";



contract AnotherHack {
    event LogAddress(address addr);

    address public owner;

    Hack hack = Hack(0xA4899D35897033b927acFCf422bc745916139776);

    function log_tx_msg() public {
        hack.log_tx_msg();
    }
}
