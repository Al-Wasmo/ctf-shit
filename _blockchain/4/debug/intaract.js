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
const contractAddress = '0xA4899D35897033b927acFCf422bc745916139776';

// Create contract instance
const contract = new ethers.Contract(contractAddress, abi, wallet);


contract.on("LogAddress", (msg) => {
  console.log("Event says:", msg);
});

// Example interaction
async function main() {
    const value = await contract.log_tx_msg(); // replace with real function
    await value.wait();
}

main().catch(console.error);
