import discord

TOKEN = ""   # put ur token here

SKIP_BOTS=FALSE

cliet =discord.Client()

@client.event
async def on_ready():
print('logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
print('council0002')
print('join discord.gg/listing')

for member in client.get_all_members():
        if member.bot and SKIP_BOTS:
            continue
        await member.ban(reason="ur reason here", delete_message_days=7)
        print(f"banned {member.display_name}!")
    print("banall succesful")

client.run(TOKEN)
