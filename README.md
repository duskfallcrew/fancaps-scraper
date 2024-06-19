![GitHub followers](https://img.shields.io/github/followers/duskfallcrew)  ![GitHub Sponsors](https://img.shields.io/github/sponsors/duskfallcrew)
[Discord]([https://img.shields.io/discord/1024442483750490222?style=for-the-badge](https://discord.gg/5t2kYxt7An))



# FanCaps-Scrapper

A Python CLI scrapper for anime screenshots on https://fancaps.net.

README template from https://www.makeareadme.com/

This was forked from [Fannovel](https://github.com/Fannovel16/fancaps-scraper)

As well as the most recent fork for NodeJS: [JSarvise](https://github.com/JSarvise/fancaps-scraper)

As this is in heavy developmenet because i don't understand Javascript, and i am more used to Python - please have patience.  I'm not a programmer, i'm a graphic designer by nature and I enjoy using ChatGPT to solve problems.. or in this case create them xD. 

I realize that NodeJS doesn't -SUCK- per se, but i'm so used to using python in my AI training that using Javascript at THIS STAGE confused me.  This repository retains the MIT liscence from the first two, and I do not claim to own this code. Fannovel & JSarvise are the credits to doing all of the original work, i'm just updating it to python as an alternative, and am working on a Jupyter notebook as i can't get the other one that Fannovel made to work. 

The instructions on this readme are based on the NOdeJS and i'm working on converting it to the python instructions.

## Installation

```bash
git clone https://github.com/duskfallcrew/fancaps-scraper
cd fancaps-scraper
npm install
cd ..
```

## Usage
### CLI syntax
```bash
node fancaps-scraper [-h] [-v] \ 
    --seriesUrl SERIESURL \
    [--saveDir SAVEDIR] \
    [--numOfPromises NUMOFPROMISES] \
    [--forceUnlimitedPromises] \
    [--skipNLastPages SKIPNLASTPAGES] \
    [--writeMetadata] \
    [--readMetadata] \
    [--dontDownloadImages] \
```
Arguments:
  * -h, --help:            show this help message and exit
  * -v, --version:         show program's version number and exit
  * `--url URL`: The url of the series or movie you want to download images from, not the episode url.<br>Any kind of url that starts with `https://fancaps.net/movies/MovieImages.php` or `https://fancaps.net/anime/showimages.php` will be accepted e.g.:
  ** https://fancaps.net/anime/showimages.php?33224-Bocchi_the_Rock
  ** https://fancaps.net/movies/MovieImages.php?name=Fate_Stay_Night_Heaven_s_Feel_I_Presage_Flower_2017&movieid=2666
  ** https://fancaps.net/movies/MovieImages.php?movieid=2666
  * `--saveDir SAVEDIR`:     The location to save images, the default value is ./fancaps-images/title of series<br>(e.g. ./fancaps-images/Bocchi The Rock)
  * `--numOfPromises NUMOFPROMISES`: The number of promises to use (imagine it is similar to multi-threading).<br>A error will be thrown if it > 75 due to Cloudflare CDN's hidden rate limit unless --forceUnlimitedPromises is passed
  * `--forceUnlimitedPromises`
  * `--skipNLastPages SKIPNLASTPAGES`: Skip n last pages so most of credit frames won't be downloaded
  * `--writeMetadata`:       Write episodeDataset to metadata.json
  * `--readMetadata`:        Read episodeDataset from metadata.json
  * --dontDownloadImages
  * --colab: Add line break to the progress bar if the env is Colab
  * --disableProgressBar

### Result folder architecture
#### Episode
```
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
For example: 
```bash
node fancaps-scraper --seriesUrl="https://fancaps.net/anime/showimages.php?33224-Bocchi_the_Rock"
```
Should give the following result:
```
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
#### Movie
```
$saveDir
├── intId.jpg
├── anotherIntId.jpg
├── ...
```

## Contributing

I am NOT a programmer, i've been using ChatGPT to do a lot of these things, and I FULLY RESPECT Fannovel and JSarvise's original code. If you'd like to contribute to the nodeJS versions please see the linked forks in the first part of this. If you're interested in developing the python version either fork and do your own thing, or you can fork and help or however that works! 

## License

[MIT](https://choosealicense.com/licenses/mit/)
