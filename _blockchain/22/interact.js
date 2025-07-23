const fs = require('fs');
const { ethers, keccak256, toBeHex, zeroPad, BigNumber, zeroPadValue, getBytes } = require('ethers');
const { argv } = require('node:process');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));

const contractAddress = argv[2];
const contract = new ethers.Contract(contractAddress, abi, wallet);


contract.on("Log", (msg,succ) => {
  console.log("Log:", msg);
});




async function main() {
  let tx = await contract.hack()
  await tx.wait()
}

main();
