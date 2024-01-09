import os
import requests
import json
import time
import random

TOKEN = "YOUR TOKEN" 
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
    full_message = f'"{verse_text}" - {verse_reference}'
    return full_message

def get_motivation():
    quote = requests.get("https://zenquotes.io/api/random")
    data = quote.json()
    quote_text = data[0].get("q")  
    quote_author = data[0].get("a")  
    full_quote = f'"{quote_text}" - {quote_author}'
    return full_quote

def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            if text.startswith("/"):
                if text == "/verse":
                    verse = get_bible_verse()
                    send_message(verse, chat)
                elif text == "/motivate":
                    quote = get_motivation()
                    send_message(quote, chat)
            else:
                send_message("Hey! What would you like to do?\n/verse: Bible Verse\n/motivate: Motivational Quote\n/count", chat)
        except Exception as e:
            print("Error:", e)

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