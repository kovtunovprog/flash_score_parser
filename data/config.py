import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

# Если понадобится добавить еще одного администратора,
# добавьте в .env ADMIN_ID2=12345, и os.getenv("ADMIN_ID2")
admins = [
    os.getenv('ADMIN_ID'),
]

parsing_url = 'https://www.flashscore.ru/hockey/'
