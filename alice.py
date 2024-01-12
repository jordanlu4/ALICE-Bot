import requests
import json
import time
import random


TOKEN = "PRIVATE TOKEN" 
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
BIBLE_API_URL = "https://bible-api.com/john 3:16"

BIBLE_VERSES = [
    "John 3:16", "Genesis 1:1", "Psalm 23:1",
    "Proverbs 3:5", "Matthew 5:9", "1 Corinthians 13:4",
    "John 13:7", "Psalm 51:1", "Exodus 14:14"
    "Jeremiah 29:11", "Romans 8:28", "Psalm 23:4",
    "Psalm 23:6", "Psalm 23:5", "Matthew 6:33",
    "Psalm 23:3", "Psalm 23:1", "Philippians 4:6",
    "Romans 12:2", "Psalm 23:2", "Philippians 4:7",
    "Ephesians 6:12", "Isaiah 41:10", "Philippians 4:8",
    "Philippians 4:13", "Joshua 1:9", "John 16:33",
    "John 14:6", "Isaiah 40:31", "2 Corinthians 5:17",
    "Proverbs 3:5", "Proverbs 3:6", "1 Peter 5:7",
    "John 10:10", "Galatians 5:22", "Psalm 91:11",
    "Matthew 28:20", "Matthew 28:19", "Matthew 11:28",
    "2 Timothy 1:7", "Psalm 91:1", "Ephesians 2:10",
    "Psalm 91:4", "Galatians 5:23", "Psalm 91:2",
    "Ephesians 3:20", "Psalm 139:14", "Proverbs 18:10",
    "Matthew 11:29", "Isaiah 41:13", "Matthew 6:34",
    "Psalm 46:1", "Philippians 1:6", "Isaiah 40:29",
    "2 Timothy 1:7", "1 Corinthians 16:14", "2 Corinthians 12:9",
    "Proverbs 17:22", "Hebrews 11:1", "James 1:3",
    "Philippians 2:3", "Proverbs 16:3", "Philippians 4:19",
    "Matthew 6:24", "Isaiah 26:3", "Psalm 37:4",
    "1 Corinthians 10:13", "1 John 4:19", "Psalm 27:1",
    "2 Corinthians 5:7", "Galatians 2:20", "John 14:27",
    "Psalm 46:5", "Romans 15:13", "Psalm 20:4",
    "Colossians 3:23", "1 Peter 5:6", "Isaiah 54:17",
    "Romans 8:31", "Jeremiah 17:7", "Psalm 121:2",
]


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def get_bible_verse():
    random_verse = random.choice(BIBLE_VERSES)
    response = requests.get(f"https://bible-api.com/{random_verse}")
    data = response.json()
    verse_text = data.get("text") 
    verse_reference = data.get("reference") 
    full_message = f'{verse_text} - {verse_reference}'
    return full_message

def get_motivation():
    quote = requests.get("https://zenquotes.io/api/random")
    data = quote.json()
    quote_text = data[0].get("q")  
    quote_author = data[0].get("a")  
    full_quote = f'"{quote_text}" - {quote_author}'
    return full_quote

def send_prayer_options(chat_id):
    keyboard = json.dumps({
        "inline_keyboard": [
            [{"text": "Health", "callback_data": "prayer_health"}],
            [{"text": "Strength", "callback_data": "prayer_strength"}],
            [{"text": "Peace", "callback_data": "prayer_peace"}],
            [{"text": "Guidance", "callback_data": "prayer_guidance"}],
            [{"text": "Foregiveness", "callback_data": "prayer_forgive"}],
            [{"text": "Lust", "callback_data": "prayer_lust"}],
            [{"text": "Nightly Prayer", "callback_data": "prayer_nightly"}],
        ]
    })
    text = "Please choose what you would like to pray for:"
    url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format(text, chat_id, keyboard)
    get_url(url)
    

def handle_callback_query(callback_query):
    message = callback_query["message"]
    chat_id = message["chat"]["id"]
    data = callback_query["data"]

    if data == "prayer_health":
        prayer = "Dear Heavenly Father,\nI humbly come to you asking for your blessings and guidance in matters of health. You are the ultimate healer, and I trust in your infinite power to protect and strengthen our physical, emotional, and mental well-being. I pray for your divine protection against illnesses and diseases that threaten our health. I also ask for your mercy and comfort for those who are experiencing pain and suffering. May your love and grace be a source of comfort for them and their loved ones.\nAmen."
    elif data == "prayer_strength":
        prayer = "Dear Heavenly Father,\nI humbly ask for your strength to sustain me in all aspects of my life. Grant me the inner strength to face any challenges or obstacles that come my way. Help me to remain steadfast in my faith and trust in your guiding hand. Give me strength to stay true to myself and my beliefs, even when others may try to influence me otherwise. Show me the path to overcoming my weaknesses and growing into a better version of myself, through Jesus Christ.\nAmen."
    elif data == "prayer_peace":
        prayer = "Dear Heavenly Father,\nIn a world full of chaos and unrest, we come to you with heavy hearts, seeking your divine intervention and peace. We pray for your mercy and love to rain down upon us and fill our hearts with compassion, understanding, and forgiveness.We thank you for your promise of peace, and we trust in your unfailing love. May your peace reign in our homes, communities, and the whole world.\nAmen."
    elif data == "prayer_guidance":
        prayer = "Dear Heavenly Father,\nI pray that you will come guide me alongside your path. I pray that you will shelter and protect me from sin and evil. Be my light and guidance on the path of a Christ-Like life through the salvation of Jesus.\nAmen."
    elif data == "prayer_forgive":
        prayer = "Dear Heavenly Father,\nCome into my life, change me, rearrange me, forgive me of anything that I've said or done that was not like you. Cleanse me God, I want to be made new. Come into my life and make me one of yours in Jesus's name.\nAmen."
    elif data == "prayer_lust":
        prayer = "Dear Heavenly Father,\nPlease remove any impure thoughts and desires from my mind and replace them with thoughts of love, purity, and righteousness. Help me to seek your will and follow your commandments in all aspects of my life, including my relationships. Fill me with your love and grace, so that I may be a reflection of your goodness in this world.\nAmen."
    elif data == "prayer_nightly":
        prayer = "Dear Heavenly Father,\nI pray that you would forgive me of the sins I have commited today as I forigve the people who have wronged me today as well as protection throughout the night. I commit my whole self, mind, body, and soul to you. Watch over me as I sleep, protect me from evil, and supply me with the energy I need for tomorrow, through Jesus Christ, our eternal lord.\nAmen."
    send_message(prayer, chat_id)


def handle_updates(updates):
    for update in updates["result"]:
        try:
            if "message" in update:
                text = update["message"]["text"]
                chat = update["message"]["chat"]["id"]
                if text.startswith("/"):
                    if text == "/verse":
                        verse = get_bible_verse()
                        send_message(verse, chat)
                    elif text == "/motivate":
                        quote = get_motivation()
                        send_message(quote, chat)
                    elif text == "/prayer":
                        send_prayer_options(chat)
                else:
                    send_message("Hey! What would you like to do?\n/verse: Bible Verse\n/motivate: Motivational Quote\n/prayer: Request A Prayer", chat)
            elif "callback_query" in update:
                callback_query = update["callback_query"]
                handle_callback_query(callback_query)
        except Exception as e:
            print(f"Error: {e}")

def get_updates(last_update_id):
    url = URL + "getUpdates?timeout=100"
    if last_update_id:
        url += "&offset={}".format(last_update_id)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    return max(int(update["update_id"]) for update in updates["result"])

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()