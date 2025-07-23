const fs = require('fs');
const { ethers } = require('ethers');

// RPC provider (Anvil or other)
const provider = new ethers.JsonRpcProvider('http://localhost:8545');

// Wallet (must match the one you used to deploy)
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

// Load ABI
const abi = JSON.parse(fs.readFileSync('build/Token.abi', 'utf8'));

// Address of deployed contract
const contractAddress = '0x32467b43BFa67273FC7dDda0999Ee9A12F2AaA08';

// Create contract instance
const contract = new ethers.Contract(contractAddress, abi, wallet);


// contract.on("LogAddress", (msg) => {
//   console.log("Event says:", msg);
// });


let other_addr = "0x071f6047dD4715008fA1bF0f1Bd6d75e8486f15e"
// Example interaction
async function main() {
    const value = await contract.balanceOf(wallet.address); 
    console.log(value)
    return;

    // const tx = await contract.transfer(other_addr,20); 
    // await tx.wait();
    // console.log(tx)
}

main().catch(console.error);
