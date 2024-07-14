import aiohttp
import asyncio

async def file_get_contents(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def is_instagram_username_not_available(username):
    url = f'https://www.instagram.com/{username}/'
    insta_content = await file_get_contents(url)
    if insta_content.lower().find('<title>instagram</title>') == -1:
        return True
    else:
        return False

async def main():
    name = input("Username: ")

    while True:
        username = name
        is_not_available = await is_instagram_username_not_available(username)

        if not is_not_available:
            print(f'The username `{username}` is not registered on Instagram.')
            break  # Exit the loop if an unregistered username is found
        else:
            print(f'The username `{username}` is already registered on Instagram. Try another one.')
            break

if __name__ == "__main__":
    asyncio.run(main())
