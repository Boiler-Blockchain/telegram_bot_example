# Telegram Bot with Ethereum Integration Tutorial

## Overview
This tutorial guides you through creating a simple Telegram bot that interacts with the Ethereum blockchain. The bot allows users to send transactions of specfic amounts using a specified Ethereum account.

## Prerequisites
1. Python installed on your machine.
2. Telegram Bot Token.
3. Ethereum Account with a private key.

## Steps

### Step 1: Set Up Environment
1. Clone this repository to your local machine.
2. Create a `.env` file in the project directory.

### Step 2: Obtain Telegram Bot Token
1. Create a Telegram bot on Telegram by talking to the BotFather.
2. Copy the bot token provided by BotFather.
3. Open the `.env` file and add the following line:
BOT_TOKEN=<your_telegram_bot_token>

### Step 3: Configure Ethereum Account
1. Obtain an Ethereum account with a private key.
2. Open the `.env` file and add the following line:
SECRET_KEY=<your_ethereum_private_key>

### Step 4: Install Dependencies
1. Open a terminal in the project directory and run: `pip install -r requirements.txt`

### Step 5: Run the Bot
1. Execute the following command in the terminal: `python your_bot_script.py`

### Step 6: Interact with the Bot
1. Open your Telegram app and find your bot.
2. Send the `/hello` command to receive a greeting.
3. Send the `/transact` command to initiate a transaction.