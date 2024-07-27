import discord
import youtube_dl
from spotify_integration import SpotifyIntegration

class Music:
    def __init__(self, client, spotify_client_id, spotify_client_secret):
        self.client = client
        self.spotify = SpotifyIntegration(spotify_client_id, spotify_client_secret)

    async def join(self, message):
        """Joins a voice channel"""
        if message.author.voice:
            channel = message.author.voice.channel
            await channel.connect()
        else:
            await message.channel.send("You are not connected to a voice channel")

    async def leave(self, message):
        """Leaves a voice channel"""
        if message.guild.voice_client:
            await message.guild.voice_client.disconnect()
        else:
            await message.channel.send("I am not connected to a voice channel")

    async def play(self, message, query):
        """Plays a song from YouTube or Spotify based on a search query"""
        if not message.guild.voice_client:
            if message.author.voice:
                channel = message.author.voice.channel
                await channel.connect()
            else:
                await message.channel.send("You are not connected to a voice channel")
                return

        if "spotify.com" in query:
            track_info = self.spotify.get_track_info(query)
            search_query = track_info
        else:
            search_query = query

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{search_query}", download=False)
            if info and 'entries' in info and len(info['entries']) > 0:
                url2 = info['entries'][0]['url']
                title = info['entries'][0]['title']
            else:
                await message.channel.send("No results found on YouTube")
                return

        source = await discord.FFmpegOpusAudio.from_probe(url2)
        message.guild.voice_client.play(source)
        await message.channel.send(f"Now playing: {title}")

    async def stop(self, message):
        """Stops the currently playing song"""
        if message.guild.voice_client and message.guild.voice_client.is_playing():
            message.guild.voice_client.stop()
        else:
            await message.channel.send("I am not playing any song")
