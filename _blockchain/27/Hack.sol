// SPDX-License-Identifier: MIT
pragma solidity <0.7.0;

contract Hack  {
    address player = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;

    event Log(uint256);

    constructor() public{

    }


    function hack() public {
        emit Log(69);
        selfdestruct(payable(msg.sender));
    }
}