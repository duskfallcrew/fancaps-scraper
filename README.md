![GitHub followers](https://img.shields.io/github/followers/duskfallcrew)  ![GitHub Sponsors](https://img.shields.io/github/sponsors/duskfallcrew)
[Discord](https://discord.gg/5t2kYxt7An)



# FanCaps-Scrapper

A Python CLI scrapper for anime screenshots & Fan Screen on https://fancaps.net.

README template from https://www.makeareadme.com/

This was forked from [Fannovel](https://github.com/Fannovel16/fancaps-scraper) , As well as the most recent fork for NodeJS: [JSarvise](https://github.com/JSarvise/fancaps-scraper)


## Note on Development and Context
This project is currently in active development as I navigate learning JavaScript, a language that differs significantly from my primary experience in Python. Please bear with me as I adapt and develop this repository.

I come from a graphic design background rather than programming, yet I find great utility in using ChatGPT to solve problems—sometimes inadvertently creating new ones in the process! While I acknowledge that NodeJS has its merits, my familiarity with Python, especially in AI training, has led me to translate this project into Python.

This repository maintains the MIT license inherited from its original creators, Fannovel and JSarvise, to whom credit is due for their initial work. My role here is to provide an alternative implementation in Python. Currently, I am also exploring the use of a Jupyter notebook, as I encountered difficulties with the existing NodeJS implementation provided by Fannovel.

The instructions in this README are initially based on the NodeJS version and are being progressively adapted for Python. Some sections retain a similar structure, and I am actively working on refining and expanding the content.

## Installation

```bash
git clone https://github.com/duskfallcrew/fancaps-scraper
cd fancaps-scraper
pip install -r requirements.txt
```

## Step-by-Step Guide
#### Ensure Python Environment:
Make sure you have Python installed on your system. You can check this by running:

```bash
python --version
```
#### Navigate to Script Directory:
Open your terminal or command prompt and navigate to the directory where your Python script (fan_caps_scraper.py) is located. You can change directories using the cd command:

```bash
cd path/to/your/script
```
#### Run the Script:
To execute your Python script with command-line arguments, use the following format:

```bash
python scraper.py --url <URL_VALUE> --saveDir <SAVEDIR_VALUE> --numOfPromises <NUMOFPROMISES_VALUE> --skipNLastPages <SKIPNLASTPAGES_VALUE>
```
Replace <URL_VALUE>, <SAVEDIR_VALUE>, <NUMOFPROMISES_VALUE>, and <SKIPNLASTPAGES_VALUE> with the actual values you want to use.

For example:
```bash
python scraper.py --url https://fancaps.net/anime/showimages.php?33224-Bocchi_the_Rock --saveDir ./fancaps-images/Bocchi_The_Rock --numOfPromises 50 --skipNLastPages 1
```


#### Executing:
After entering the command, hit Enter. Your script will start executing. Depending on the network speed, number of images, and other factors, it might take some time to complete.

Arguments:
--url: Required argument specifying the URL of the series or movie from which you want to download images.
--saveDir: Optional argument specifying the directory where images will be saved. Defaults to ./fancaps-images/<series/movie_title>.
--numOfPromises: Optional argument specifying the number of concurrent requests (promises) to use. Defaults to 75.
--skipNLastPages: Optional argument specifying how many of the last pages to skip. Defaults to 2.
### Result folder architecture

Episode
```bash
$saveDir
├── Episode 1
│   ├── intId.jpg
│   ├── anotherIntId.jpg
│   ├── ...
├── Episode 2
│   ├── intId.jpg
│   ├── anotherIntId.jpg
│   ├── ...
├── Episode ...
```
Example:

For example, running:

```bash
python fancaps_scraper.py --url="https://fancaps.net/anime/showimages.php?33224-Bocchi_the_Rock"
```
Should result in the following folder structure:

```bash
./fancaps-images/Bocchi the Rock!
├───Episode 1
│   ├── 22361835.jpg
│   ├── 22361837.jpg
│   ├── 22361838.jpg
│   ├── ...
│   ├── 22362709.jpg
├───Episode 2
│   ├──22363017.jpg
│   ├──22363020.jpg
│   ├──22363022.jpg
│   ├── ...
│   ├── ...
│   ├── 22364001.jpg
├───Episode 3
├───Episode 4
├───Episode 5
├───Episode 6
├───Episode 7
├───Episode 8
├───Episode 9
├───Episode 10
├───Episode 11
└───Episode 12
```
Movie
```bash

$saveDir
├── intId.jpg
├── anotherIntId.jpg
├── ...
```
## Contributing

I am NOT a programmer, i've been using ChatGPT to do a lot of these things, and I FULLY RESPECT Fannovel and JSarvise's original code. If you'd like to contribute to the nodeJS versions please see the linked forks in the first part of this. If you're interested in developing the python version either fork and do your own thing, or you can fork and help or however that works! 

## License

[MIT](https://choosealicense.com/licenses/mit/)
