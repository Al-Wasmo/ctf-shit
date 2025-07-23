// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address to, uint256 value) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 value) external returns (bool);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
}

contract Hack {
    event Log(uint256);
    address player = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
    constructor() {

    }

    function giveBack(address addr_token1,uint256 amount) external {
        IERC20  token1 = IERC20(addr_token1);
        token1.transferFrom(address(this),player,amount);
    }
}