import asyncio
import aiohttp
from bs4 import BeautifulSoup

class ScriptGenerator:
    def __init__(self, url):
        self.url = url

    async def scrape_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                content = await response.text()

            async def process_article(x):
                year = f"Today in {x.find('h3', class_='gb-headline gb-headline-c9c17c19 gb-headline-text gb-headline-4d358535').text.strip()}"
                titl = x.find('h3', class_='gb-headline gb-headline-9b8b6052 gb-headline-text gb-headline-db047b70').text.strip()
                return year+" "+titl
            
            soup = BeautifulSoup(content, 'html.parser')
            test = soup.find_all('div', class_='gb-container gb-container-0e5155aa gb-container-529120bd')
            tasks = [process_article(x) for x in test]
            results = await asyncio.gather(*tasks)
            full_text = f"Create a youtube short about: {results[-1]} Settings: Use a male old husky British voice. Show subtitles in the video. Video length from 21 to 24 seconds. Clear end. Engaging video."
            print(full_text)
            return full_text

        

