import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    args = message.content.replace('py!', '').split(' ')
    command = args[0].lower()

    if command == "ping":
        await message.channel.send("pong!")

    elif command == "join":
        channel = message.author.voice.channel
        if channel:
          voice = await channel.connect()
          voice.play(discord.FFmpegPCMAudio(source="https://n-6-12.dcs.redcdn.pl/sc/o2/Eurozet/live/audio.livx"))
          await message.channel.send(f"Joined {channel}")
        else:
          await message.channel.send("No channel!")
    
    elif command == "leave":
        channel = message.guild.voice_client
        if channel:
            await channel.disconnect()
            await message.channel.send("Ok!")
        else:
            await message.channel.send("No channel!")

client.run("TOKEN")
