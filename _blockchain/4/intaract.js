const fs = require('fs');
const { ethers } = require('ethers');

// RPC provider (Anvil or other)
const provider = new ethers.JsonRpcProvider('http://localhost:8545');

// Wallet (must match the one you used to deploy)
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

// Load ABI
const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));

// Address of deployed contract
const contractAddress = '0x4b6aB5F819A515382B0dEB6935D793817bB4af28';

// Create contract instance
const contract = new ethers.Contract(contractAddress, abi, wallet);


// contract.on("LogAddress", (msg) => {
//   console.log("Event says:", msg);
// });

// Example interaction
async function main() {
    const value = await contract.hack(); // replace with real function
    await value.wait();
}

main().catch(console.error);
