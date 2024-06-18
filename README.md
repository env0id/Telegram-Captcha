# Telegram Bot with Verification Functionality

This Python script implements a Telegram bot that verifies new chat members before granting them full access to the chat. It uses the Telebot library to interact with the Telegram Bot API.

## Features

- Restricts new chat members from sending messages immediately upon joining.
- Prompts new members to verify themselves with a button click within a specified time limit.
- Automatically kicks members if verification fails (member does not click the button in time).
- Uses callback handling to manage verification status.

## Requirements

- Python 3.x
- Telebot library (`pip install pyTelegramBotAPI`)

## Setup

1. **Obtain Telegram Bot Token:**
   - Obtain a Telegram Bot token by creating a new bot through the BotFather on Telegram.
   - Replace `YOUR_BOT_TOKEN` in the script (`main.py`) with your actual bot token obtained from BotFather.

2. **Adjust Verification Time:** Modify `verification_time` in `main.py` for the duration new members have to verify themselves.

3. **Customize Messages and Button:** Edit `text` and `button_text` in `main.py` for the welcome message and button text.

4. **Bot Permissions:** Ensure your bot has admin rights in the chat for member management.

5. **Run the Script:**
   - Run the script using Python (`python main.py`).
