// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


interface ITraget {
    function enter(bytes8 _gateKey) external returns (bool);
}

contract Hack {
    event Log(uint256);
    event Attempt(uint256, bool);


    ITraget public target = ITraget(0x553BED26A78b94862e53945941e4ad6E4F2497da);
    constructor() {
        bytes8 key = bytes8(uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^ type(uint64).max);
        target.enter(key);
    }

}
