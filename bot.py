import discord, subprocess, os

client = discord.Client() #declare discord client

@client.event
async def on_message(message): #on new message
        if message.content.find("!exec")!=-1: #and message.author.id == 1234
                output = subprocess.getoutput(message.content.split("!exec ")[1])
                if output=="":
                        await message.channel.send("[]") #cannot send an empty message
                elif len(output) > 1999: #2000 is max characters count on discord
                        await message.channel.send("[Response is too long]")
                else:
                        await message.channel.send("[" + output + "]")
                print(message.content.split("!exec ")[1] + " | Executed by " + message.author.name) #at least log the commands since I haven't implemented any password protection
try:
        client.run(os.getenv("TOKEN")) #don't forget to configure token env variable in heroku project settings, it is unsecure to have it in plaintext
except Exception as e:
        print(e)
