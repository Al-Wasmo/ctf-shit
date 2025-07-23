// quickstart.js
const { ethers } = require("ethers");
const fs = require("fs");


// Connect to local Anvil node
const provider = new ethers.JsonRpcProvider("http://localhost:8545");

// Use private key from Anvil output
const privateKey = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";  // ← copy from Anvil
const wallet = new ethers.Wallet(privateKey, provider);

// Deployed contract address
const contractAddress = "0x5b87990083eb4231D662e3f2EF6e602BE2a59Be0";


const json = JSON.parse(fs.readFileSync("./CoinFlip.json", "utf8"));
const abi = json.abi

const contract = new ethers.Contract(contractAddress, abi, wallet);

async function main() {
    console.log("Connected as:", await wallet.getAddress());
    for (let index = 0; index < 1; index++) {
        let a = await (async () => {
            const latestBlockNum = await provider.getBlockNumber();
            const prevBlock = await provider.getBlock(latestBlockNum - 1);
            return prevBlock;
        })();
        a = (a / 57896044618658097711785492504343953926634992332820282019728792003956564819968) > 0;
        console.log(a);

        // const tx = await contract.flip(false);
        // console.log((await contract.consecutiveWins()).toString())

const wins = await contract.consecutiveWins();  // this returns a BigNumber
console.log("Consecutive Wins:", wins.toString());        

        // const receipt = await tx.wait();
        // console.log("TX status:", receipt.status); // must be 1
    }

}

main().catch(console.error);

