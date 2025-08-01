const fs = require('fs');
const { ethers } = require('ethers');

// Connect to local Anvil/Hardhat node
const provider = new ethers.JsonRpcProvider("http://localhost:8545");

// Use a pre-funded account (from Anvil)
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'; // Anvil prints private keys
const wallet = new ethers.Wallet(privateKey, provider);

// Load ABI and bytecode
const abi = JSON.parse(fs.readFileSync('build/AnotherHack.abi', 'utf8'));
const bytecode = '0x' + fs.readFileSync('build/AnotherHack.bin', 'utf8');

// Deploy
async function main() {
    const factory = new ethers.ContractFactory(abi, bytecode, wallet);
    const contract = await factory.deploy(/* constructor args if any */);

    console.log("Deploying...");
    await contract.waitForDeployment();
    console.log("Contract deployed at:", await contract.getAddress());
}

main().catch(console.error);
