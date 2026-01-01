import httpx

async def fetch_sector_news(sector):
    url = f"https://news.google.com/rss/search?q=india+{sector}+market&hl=en-IN&gl=IN&ceid=IN:en"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        return res.text[:3000]

