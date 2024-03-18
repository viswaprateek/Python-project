import os
import time
import easyocr
import xlsxwriter
from pyrogram import Client, filters
from pyromod import listen

api_id = "api_id"
api_hash = "api_hash"
TOKEN='bot_token'
BOT_USERNAME = 'bot_username'

bot = Client("ocrbot", api_id=api_id, api_hash=api_hash, bot_token=TOKEN)

@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(f'Hello {message.from_user.first_name}...! I am a Scanner bot')

@bot.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text(f'I am a Scanner bot! Send me the number of bills and images of bills. Data gets entered into excel sheet and you can download it...!')

@bot.on_message(filters.command("custom"))
async def custom_command(client, message):
    await message.reply_text(f'Are you Ready ...?')

@bot.on_message(filters.command("scan"))
async def scan(client, message):
    bills_count_msg = await message.chat.ask("Send the number of bills.")
    xlcx_file = f'Balance Sheet {time.time()}.xlsx'
    workbook = xlsxwriter.Workbook(xlcx_file)
    worksheet = workbook.add_worksheet("2023")
    worksheet.write(0, 0, "#")
    worksheet.write(0, 1, "Shop")
    worksheet.write(0, 2, "DATE")
    worksheet.write(0, 3, "Amount")

    for index in range(int(bills_count_msg.text)):
        photo = await message.chat.ask("Send me the bill photo.")
        msg = await photo.reply("Processing your request....")
        photo_location = await photo.download()
        reader = easyocr.Reader(['en','Te'])
        r = reader.readtext(photo_location)

        result=[]
        date="  -  "
        amount=0
        for i in r:
            result.append(i[1])
        ans=" ".join(result)
        l=list(ans.split())
        store=r[0][1]

        for i in range(len(l)):
            if l[i].lower()=="amount" or l[i].lower()=="total" or l[i].lower()=="amount:" or l[i].lower()=="total:" or l[i].lower()=="fare:" l[i].lower()=="fare":
                amount=l[i+1]

        for i in range(len(l)):
            if l[i].upper() == "DATE" or l[i].upper() =="DATE:":
                date=l[i+1]
                break

        os.remove(photo_location)
        await msg.delete()
        
        #Saving data into excel
        worksheet.write(index+1,0,index+1)
        worksheet.write(index+1,1,store)
        worksheet.write(index+1,2,date)
        worksheet.write(index+1,3,amount)
    workbook.close()
    msg = await message.reply("Excel file created sucessfully.\n\nUploading to telegram.")
    await message.reply_document(document=xlcx_file)
    await msg.delete()
    os.remove(xlcx_file)


if __name__ == '__main__':
    bot.run()