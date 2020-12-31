import discord, subprocess, os

client = discord.Client()

@client.event
async def on_message(message):
        if message.content.find("!exec")!=-1:
                output = subprocess.getoutput(message.content.split("!exec ")[1])
                if output=="":
                        await message.channel.send("No output")
                else:
                        await message.channel.send(output)
                print(message.content.split("!exec ")[1] + " | Executed by " + message.author.name)

client.run(os.getenv("TOKEN")) #don't forget to configure token env variable in heroku project settings, it is unsecure to have it in plaintext
