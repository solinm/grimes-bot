import lyricsgenius
import random
import tweepy

# twitter access keys
keys = {
    'CONSUMER_API_KEY': 'wL5hPdZMrcmPOkOMuYnZPOhVk',
    'CONSUMER_API_SECRET_KEY': 'iKPaBcIhdJvB0cUdGTum2fQoDrzVyTjdRHqo0MtNzjCLo0X5B2',
    'ACCESS_TOKEN': '4654568361-821658113409515520-UsVis0fVEUqQxJZBhd5JvZwjyv1dNR5',
    'ACCESS_TOKEN_SECRET': 'uzR4tibqwCreLC6lqi56i8aZbL16PYfYQHqsB66xbHXzD'
}

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
    genius_client_access_token = "J1Gd5gO7wyI4r_qNUHtwZ-j4jMVEInNPekImNb6H0JRYWPSuz6ubYPD3j00MKXSc"
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
        keys['CONSUMER_API_KEY'],
        keys['CONSUMER_API_SECRET_KEY']
    )
    auth.set_access_token(
        keys['ACCESS_TOKEN'],
        keys['ACCESS_TOKEN_SECRET']
    )
    api = tweepy.API(auth)
    lyrics, song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics)
    status = api.update_status(tweet)
    bio = api.update_profile(description=song)

    return tweet