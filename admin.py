from config import dp, bot, admin

import data


@dp.message_handler(commands='admin')
async def NewLang(message):
    if message.chat.id == admin:
        await bot.send_message(message.chat.id, 'NewLang')
        if message.text == 'NewLang':
            await bot.send_message(message.chat.id, 'Code')
            Code = message.text
            await bot.send_message(message.chat.id, 'Name')
            Name = message.text
            await bot.send_message('Greetings')
            Greetings = message.text
            await bot.send_message('SeLan')
            SeLan = message.text
            await bot.send_message('SeReg')
            SeReg = message.text
            await bot.send_message('SeDev')
            SeDev = message.text
            await bot.send_message('NewTempButton')
            NewTempButton = message.text
            await bot.send_message('AboutButton')
            AboutButton = message.text
            await bot.send_message('HelpButton')
            HelpButton = message.text

            await bot.send_message(
                f'All right\n{Code}\n{Name}\n{Greetings}\n{SeLan}\n{SeReg}\n{SeDev}\n{NewTempButton}\n{AboutButton}\n{HelpButton}')
            await bot.send_message(message.chat.id, "Commit?\nY - Yes else - canceled ")
            if message.text == 'Y':
                await bot.send_message(message.chat.id, 'Success')
                data.NewLang(Code, Name, Greetings, SeLan, SeReg, SeDev, NewTempButton, AboutButton, HelpButton)

        else:
            await bot.send_message(message.chat.id, 'OK operation is canceled')

    else:
        await bot.send_message(message.chat.id, "Sorry, You don't admin")
