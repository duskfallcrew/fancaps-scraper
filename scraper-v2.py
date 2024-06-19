import asyncio
import os
import argparse
import logging
from urllib.parse import urlparse, urljoin
import aiohttp
from bs4 import BeautifulSoup
import aiofiles

# This version is a testing version I have because neither are tested yet but this handles memory leaks

# Function to fetch HTML content using aiohttp
async def fetch_html(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except aiohttp.ClientError as e:
        logging.error(f"Error fetching HTML from {url}: {str(e)}")
        return None

# Function to download an image asynchronously
async def download_image(session, image_url, save_dir):
    try:
        async with session.get(image_url) as response:
            if response.status == 200:
                image_data = await response.read()
                filename = os.path.basename(urlparse(image_url).path)
                save_path = os.path.join(save_dir, filename)
                async with aiofiles.open(save_path, 'wb') as f:
                    await f.write(image_data)
                logging.info(f"Downloaded: {image_url}")
            else:
                logging.error(f"Failed to download {image_url}. Status: {response.status}")
    except aiohttp.ClientError as e:
        logging.error(f"Error downloading {image_url}: {str(e)}")

# Function to download images asynchronously using aria2c
async def download_images_async(image_urls, save_dir):
    tasks = []
    for image_url in image_urls:
        tasks.append(download_image_async(image_url, save_dir))
    await asyncio.gather(*tasks)

async def download_image_async(image_url, save_dir):
    try:
        aria2c_command = f"aria2c -x 16 -s 16 -d {save_dir} {image_url}"
        process = await asyncio.create_subprocess_shell(aria2c_command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            logging.info(f"Downloaded: {image_url}")
        else:
            logging.error(f"Failed to download {image_url}. Error: {stderr.decode().strip()}")
    except asyncio.subprocess.SubprocessError as e:
        logging.error(f"Error running aria2c for {image_url}: {str(e)}")

# Function to get series data from the provided URL
async def get_series_data(series_url):
    try:
        series_url = urlparse(series_url)
        episodes = []
        page_i = 0
        series_title = None
        async with aiohttp.ClientSession() as session:
            while True:
                page_i += 1
                series_url = series_url._replace(query=f'page={page_i}')
                html_content = await fetch_html(session, series_url.geturl())
                if not html_content:
                    break
                soup = BeautifulSoup(html_content, 'html.parser')

                curr_episodes = soup.select("a[style='color:black;']")
                if not curr_episodes:
                    break

                for episode in curr_episodes:
                    episode_title = episode.text.strip().replace("Images From ", '')
                    episode_url = urljoin(series_url.geturl(), episode['href'])
                    episodes.append({'episodeTitle': episode_title, 'episodeUrl': episode_url})

                if not series_title:
                    series_title = soup.select_one("h1.post_title").text.replace("Viewing Popular Images From", '').strip().replace(': ', ' - ')

        return {'seriesTitle': series_title, 'episodes': episodes}
    except Exception as e:
        logging.error(f"Error fetching series data from {series_url}: {str(e)}")
        return None

# Function to get TV show data from the provided URL
async def get_tv_show_data(tv_show_url):
    try:
        tv_show_url = urlparse(tv_show_url)
        episodes = []
        page_i = 0
        series_title = None
        async with aiohttp.ClientSession() as session:
            while True:
                page_i += 1
                tv_show_url = tv_show_url._replace(query=f'page={page_i}')
                html_content = await fetch_html(session, tv_show_url.geturl())
                if not html_content:
                    break
                soup = BeautifulSoup(html_content, 'html.parser')

                curr_episodes = soup.select("h3 > a[href*='/tv/episodeimages.php?']")
                if not curr_episodes:
                    break

                for episode in curr_episodes:
                    episode_title = episode.text.strip()
                    episode_url = urljoin(tv_show_url.geturl(), episode['href'])
                    episodes.append({'episodeTitle': episode_title, 'episodeUrl': episode_url})

                if not series_title:
                    series_title = soup.select_one("h1.post_title").text.replace(': ', ' - ')

        return {'seriesTitle': series_title, 'episodes': episodes}
    except Exception as e:
        logging.error(f"Error fetching TV show data from {tv_show_url}: {str(e)}")
        return None

# Main function to handle argument parsing and invoke appropriate functions
async def main(args):
    url = args.url
    save_dir = args.saveDir
    num_of_promises = args.numOfPromises
    skip_n_last_pages = args.skipNLastPages
    disable_progress_bar = args.disableProgressBar

    if 'anime' in url or 'series' in url:
        data = await get_series_data(url)
    elif 'tv' in url:
        data = await get_tv_show_data(url)
    # Add other data retrieval functions (e.g., get_movie_data, get_episode_data)

    if data:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Downloading images
        if 'imageUrls' in data:
            await download_images_async(data['imageUrls'], save_dir)
    else:
        logging.error(f"Failed to retrieve data from {url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FanCaps-Scraper - An async scraper for anime screenshots on fancaps.net")
    parser.add_argument("--url", required=True, type=str, help="The URL of the series or movie you want to download images from, not the episode URL (e.g. https://fancaps.net/anime/showimages.php?33224-Bocchi_the_Rock)")
    parser.add_argument("--saveDir", required=False, type=str, help="The location to save images, the default value is ./fancaps-images/title of series (e.g. ./fancaps-images/Bocchi The Rock)")
    parser.add_argument("--numOfPromises", required=False, type=int, default=75, help="The number of promises to use (imagine it is similar to multi-threading). An error will be thrown if it > 75 due to Cloudflare CDN's hidden rate limit unless --forceUnlimitedPromises is passed")
    parser.add_argument("--skipNLastPages", required=False, type=int, default=2, help="Skip n last pages so most of credit frames won't be downloaded")
    parser.add_argument("--disableProgressBar", required=False, action='store_true', help="Disable progress bar output")

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Run the main function asynchronously
    asyncio.run(main(args))
