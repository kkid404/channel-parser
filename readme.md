<h1>Telegram channel parser</h1>
<p>
    This project is designed to collect information and pass it to the bot. The author's original intent is to track crypto projects from various sources, but it can also be used for any other purpose.
</p>
<h2>Settings bot</h2>

<p>
    The .env.example should be renamed to .env. In this file you should save bot's token from <a target="_blank" href="https://t.me/BotFather">@BotFather</a>. You also need to specify the data to connect to the database.
</p>

<h3>
Install all dependencies from the requirements.txt file with the command:
</h3>

```bash
pip install -r requirements.txt
```

<h3>
Run the bot with the command:
</h3>

```bash
python main.py
```
<h2>Settings client</h2>
<p>
The .env.example should be renamed to .env. In this file you should save api_id, api_hash, phone from telegram account. <a target="_blank" href="https://my.telegram.org/apps">api_id, api_hash here</a>. You also need to specify the data to connect to the database.
</p>
<h3>
Run the client with the command
</h3>

```bash
python main.py
```

<h2>Links to framework documentation</h2>
<h3><a href="https://docs.aiogram.dev/en/latest/" target="_blank">Aiogram</a></h3>
<h3><a href="https://docs.telethon.dev/en/stable/" target="_blank">Telethon</a></h3>
<h3><a href="https://www.sqlalchemy.org/" target="_blank">SQLAlchemy</a></h3>
