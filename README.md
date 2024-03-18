Scanner Bot
This is an OCR (Optical Character Recognition) scanner bot built using Python and the Pyrogram library. It allows users to send images of bills, extract data from them using OCR, and store the information in an Excel sheet.

Features
Extracts shop name, date, and amount from bill images.
Creates an Excel sheet with the extracted data.
Supports multiple bills scanning in a single session.
Dependencies
Python 3.x
Pyrogram
EasyOCR
XlsxWriter
Installation
Clone this repository to your local machine.
Install the dependencies by running:
Obtain API credentials from Telegram.
Replace 'api_id', 'api_hash', 'bot_token', and 'bot_username' in the script with your actual credentials.
Usage
Run the script using:
Start the bot by sending /start command in the chat.
Use /help command to get information about how to use the bot.
Send the number of bills you want to scan using the /scan command.
Send images of bills one by one when prompted.
Once all bills are scanned, the bot will generate an Excel sheet with the extracted data and send it to you.
