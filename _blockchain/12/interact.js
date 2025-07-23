const fs = require('fs');
const { ethers } = require('ethers');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));

const contractAddress = '0xe70f935c32dA4dB13e7876795f1e175465e6458e';

const contract = new ethers.Contract(contractAddress, abi, wallet);


contract.on("Log", (msg) => {
  console.log("Event says:", msg);
});

async function main() {
    const tx = await contract.hack(); 
    await tx.wait();
    console.log(tx)
}

main().catch(console.error);
