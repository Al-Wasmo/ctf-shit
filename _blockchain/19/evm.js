const { ethers } = require("ethers");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://localhost:8545");
    const signer = provider.getSigner();

    const bytecode = "0x69602a60005260206000f3600052600a6016f3";

    const tx = await (await signer).sendTransaction({
        data: bytecode,
    });

    const receipt = await tx.wait();
    console.log("Contract deployed at:", receipt.contractAddress);
}

main();
