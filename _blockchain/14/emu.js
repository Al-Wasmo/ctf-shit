const fs = require('fs');
const { ethers } = require('ethers');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/GatekeeperOne.abi', 'utf8'));

const contractAddress = '0x4631BCAbD6dF18D94796344963cB60d44a4136b6';

const contract = new ethers.Contract(contractAddress, abi, wallet);


contract.on("printInt", (msg) => {
  console.log("Event says:", msg);
});

async function main() {

}

main().catch(console.error);
