const fs = require('fs');
const { ethers } = require('ethers');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));

const contractAddress = '0xB06c856C8eaBd1d8321b687E188204C1018BC4E5';

const contract = new ethers.Contract(contractAddress, abi, wallet);


contract.on("GotMoney", (msg) => {
  console.log("Event says:", msg);
});

async function main() {
    const tx = await contract.hack(); 
    await tx.wait();
    console.log(tx)
}

main().catch(console.error);
