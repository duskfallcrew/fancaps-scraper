const { JSDOM } = require("jsdom");
const axios = require("./createAxios")();

async function getTVShowData(tvShowUrl) {
    tvShowUrl = new URL(tvShowUrl);
    let episodes = [];
    let pageI = 0;
    let seriesTitle;

    while (true) {
        tvShowUrl.searchParams.set('page', ++pageI);
        const { data: subPageHtml } = await axios(tvShowUrl.toString());
        const { document } = (new JSDOM(subPageHtml)).window;
        console.log("Processing page:", pageI, "of series URL:", tvShowUrl.toString());

        // Adjusted the selector for TV shows
        const currEpisodes = [...document.querySelectorAll("h3 > a[href*='/tv/episodeimages.php?']")].map(el => ({
            episodeTitle: el.textContent.trim(),
            episodeUrl: new URL(el.href, "https://fancaps.net").toString()
        }));
        console.log("Current Episodes:", currEpisodes);

        if (currEpisodes.length === 0) break;
        episodes.push(...currEpisodes);

        if (!seriesTitle) {
            seriesTitle = document.querySelector("h1.post_title").textContent
                .trim()
                .replace(': ', ' - '); // Adjusting title extraction
        }
    }

    tvShowUrl.searchParams.delete("page");
    console.log("Finished processing series:", seriesTitle);
    return { seriesTitle, episodes };
}

module.exports = { getTVShowData };
