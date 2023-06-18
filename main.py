import lyricsgenius
import random
import tweepy
import config

# twitter access keys
bearer_token = config.BEARER_TOKEN
consumer_key = config.CONSUMER_API_KEY
consumer_secret = config.CONSUMER_API_SECRET_KEY
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET

# array of songs
songs = ["Kill V. Maim", "Oblivion", "Genesis", "Flesh Without Blood", "REALiTi", "Butterfly", "Delete Forever", "Venus Fly", "We Appreciate Power", "California",
"SCREAM", "My Name is Dark (Art Mix)", "World Princess, Pt. II", "4ÆM", "Pin", "Artangels", "Shinigami Eyes", "IDORU", "You’ll miss me when I’m not around", "Skin",
"Be a Body (侘寂)", "So Heavy I Fell Through the Earth (Art Mix)", "Belly of the Beat", "Life in the Vivid Dream", "Entropy", "Go", "Player of Games", "Circumambient",
"​laughing and not being normal", "Easily", "New Gods", "Nightmusic", "Before the fever", "Vanessa", "Symphonia IX (my wait is u)", "World ♡ Princess", "Dream Fortress",
"Rosa", "Vowels = space and time", "Pretty Dark (Demo)", "Eight", "Infinite ♡ Without Fulfillment", "Colour of Moonlight (Antiochus)", "Sagrad Прекрасный", "Visiting Statue",
"My Sister Says the Saddest Things", "Weregild", "Devon", "Delicate Weapon", "Zoal, Face Dancer", "Crystal Ball","100% Tragedy", "‌know the way", "Caladan", "Avi", "Darq Souls", 
"David", "Beast Infection", "Venus in Fleurs", "Sardaukar Levenbrech", "Grisgris", "Feyd Rautha Dark Heart", "Heartbeats", "Gambang", "Swan Song", "LOVE", "≈Ω≈Ω≈Ω≈Ω≈Ω≈Ω≈Ω≈Ω≈",
"Shadout Mapes", "∆∆∆∆Rasik∆∆∆∆", "Intro / Flowers", "Life After Death", "Ambrosia", "Favriel", "† River †", "Christmas Song", "Urban Twilight", "Angel", "Utopia", "Hallways",
"Dragvandil", "Enjoy the angels on earth", "Outer", "Song for Ric", "Black Swan Blues", "Welcome to the Opera", "Last Call", "Orphia", "Hedra", "Digital Calypso", "Cryptid", 
"Anhedonia (Death of the Old)", "Deth Angels", "Saturn Princess", "Stoned Henge (whoknoidontno)", "​gloam", "Swan Lake", "Samana", "Voignamir", "Black Hair"]

def get_raw_lyrics():
    genius_client_access_token = config.genius_client_access_token
    genius = lyricsgenius.Genius(genius_client_access_token)
    random_song_title = random.choice(songs)
    lyrics = genius.search_song(random_song_title, "Grimes").lyrics
    song = random_song_title.upper()
    return lyrics, song

def get_tweet_from(lyrics):
    lines = lyrics.split('\n')
    for index in range(len(lines)):
        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i != "XXX"]

    random_num = random.randrange(0, len(lines)-1)
    tweet = lines[random_num] + "\n" + lines[random_num+1]
    tweet = tweet.replace("\\", "")
    return tweet

def handler(event, context):
    auth = tweepy.OAuthHandler(
        consumer_key,
        consumer_secret
    )
    auth.set_access_token(
        access_token,
        access_token_secret
    )
    client = tweepy.Client(
        bearer_token=bearer_token,
        client=auth,
    )
    lyrics, song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics)
    create_tweet = client.create_tweet(text=tweet)

    return tweet