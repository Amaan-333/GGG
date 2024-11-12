// SPDX-License-Identifier:  License
pragma solidity ^0.8.0;

contract Bank {
    // mapping(type => type) 
    mapping(address => uint256) private balances;

    function createAccount() public {
        balances[msg.sender] = 0;
    }

    // payable is necessary because the function accepts a value (amount) as a parameter (EXTERNAL SOURCE AHE MHANUN)
    function deposit(uint256 amount) public payable {
        balances[msg.sender] += amount;
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
    }

    // view does not modify values within the contract (return kartana lihaycha)
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}

//install metamask
//change to testnet sepolia
//open 2 accounts
//open sepolia faucet and paste wallet address
//in remix deploy tab open environment and select connected wallets
//then deploy

ha bagh nit chalto
