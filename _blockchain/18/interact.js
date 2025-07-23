const fs = require('fs');
const { ethers } = require('ethers');
const { argv } = require('node:process');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));

const contractAddress = argv[2];
const contract = new ethers.Contract(contractAddress, abi, wallet);


// contract.on("Attempt", (msg,succ) => {
//   console.log("Attempt:", msg,succ);
// });

async function main() {
  const tx = await contract.hack();
  let k = await tx.wait();
  console.log(tx)
  console.log(k)
}

main().catch(console.error);
