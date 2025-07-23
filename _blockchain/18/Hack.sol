// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ITarget {
    function setSolver(address _solver) external;
}

contract Hack {
    ITarget public target1 = ITarget1(0xe61FDeDBcb68e8966c869E51eAb9020cFAAdf066);
    constructor() {

    }

    function hack() public {

    }

}