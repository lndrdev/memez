import requests
import discord

def getMeme(subreddit: str = None, json: bool = False):
    if json == True:
        request = requests.get(f"https://meme-api.com/gimme/{subreddit}" if subreddit else f"https://meme-api.com/gimme/")
        request_json = request.json()
        return request_json
    else:
        request = requests.get(f"https://meme-api.com/gimme/{subreddit}" if subreddit else f"https://meme-api.com/gimme/")
        request_json = request.json()
        return request_json["url"]




def get_embed(subreddit: str) -> discord.Embed:
    url = f"https://meme-api.com/gimme/{subreddit}" if subreddit else "https://meme-api.com/gimme/"
    request = requests.get(url)
    data = request.json()
    
        
    embed = discord.Embed(
            title=data["title"] if data["title"] else None,
            url=data["postLink"] if data["postLink"] else None,
            color=discord.Color.random()
    )
    embed.set_image(url=data["url"],spoiler=True if data["nsfw"] else False)
    embed.set_footer(text=f"r/{data['subreddit']}| 👍 {data['ups']} Upvotes ")
        
    return embed
