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
const contractAddress = '0x5302E909d1e93e30F05B5D6Eea766363D14F9892';

// Create contract instance
const contract = new ethers.Contract(contractAddress, abi, wallet);


// contract.on("LogAddress", (msg) => {
//   console.log("Event says:", msg);
// });

async function main() {

    // let tx = await wallet.sendTransaction({
    // to: contractAddress,
    // value: ethers.parseEther("0.5")
    // });
    // await tx.wait();
    // console.log("DONE");


    const tx = await contract.hack("0x524F04724632eED237cbA3c37272e018b3A7967e"); 
    await tx.wait();
    console.log(tx)
}

main().catch(console.error);
