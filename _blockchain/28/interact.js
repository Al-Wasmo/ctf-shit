const fs = require('fs');
const { ethers, keccak256, toBeHex, zeroPad, BigNumber, zeroPadValue, getBytes, Interface } = require('ethers');
const { argv } = require('node:process');
const { Contract } = require('ethers');
const { ChainstackProvider } = require('ethers');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');

async function main() {
console.log(await provider.getStorage('0xBF908677c54510FE1b47FD0C212355A36417A8c7',0));
console.log(await provider.getStorage('0xBF908677c54510FE1b47FD0C212355A36417A8c7',1));
}

main();




