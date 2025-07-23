const fs = require('fs');
const { ethers } = require('ethers');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const contractAddress = '0xe70f935c32dA4dB13e7876795f1e175465e6458e';

async function main() {
    // let data = await provider.getStorage("0x32467b43BFa67273FC7dDda0999Ee9A12F2AaA08",5);
    let _1 = 0x7c4132911140941f6873d6de6aaf4933;
    let _2 = 0x8f9d8e96290e457f8e061096f66518fe;
    

}

main().catch(console.error);
