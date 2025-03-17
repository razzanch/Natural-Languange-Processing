import requests
from bs4 import BeautifulSoup
import csv
import time
import random

def scrape_webdev_articles():
    sources = [
    "https://www.geeksforgeeks.org/",
    "https://stackoverflow.com/questions/tagged/web-scraping",
    "https://towardsdatascience.com/tagged/web-scraping",
    "https://realpython.com/",
    "https://www.datacamp.com/community/tutorials/web-scraping-python",
    "https://www.scrapehero.com/",
    "https://www.promptcloud.com/blog/",
    "https://www.webharvy.com/articles/",
    "https://www.octoparse.com/blog",
    "https://www.parsehub.com/blog/",
    "https://www.apify.com/blog",
    "https://www.brightdata.com/blog",
    "https://www.proxycrawl.com/blog/",
    "https://www.scraperapi.com/blog/",
    "https://www.zyte.com/blog/",
    "https://www.diffbot.com/blog/",
    "https://www.import.io/blog/",
    "https://www.webhose.io/blog/",
    "https://www.crawlingbee.com/blog/",
    "https://www.smartproxy.com/blog/",
    "https://www.limeproxies.com/blog/",
    "https://www.microleaves.com/blog/",
    "https://www.scrapingdog.com/blog/",
    "https://www.scrapingbee.com/blog/",
    "https://www.webscrapingapi.com/blog/",
    "https://www.scraping-bot.io/blog/",
    "https://www.scrapy.org/",
    "https://www.beautifulsoup.dev/",
    "https://www.selenium.dev/documentation/",
    "https://www.puppeteer.dev/",
    "https://www.playwright.dev/",
    "https://www.cheerio.js.org/",
    "https://www.colab.research.google.com/",
    "https://www.kaggle.com/learn",
    "https://www.analyticsvidhya.com/",
    "https://www.dataquest.io/blog/",
    "https://www.freecodecamp.org/news/tag/python/",
    "https://www.python.org/doc/",
    "https://www.w3schools.com/python/",
    "https://www.programiz.com/python-programming/",
    "https://www.geeksforgeeks.org/python-programming-language/",
    "https://www.tutorialspoint.com/python/",
    "https://www.codecademy.com/learn/learn-python-3",
    "https://www.edureka.co/blog/web-scraping-with-python/",
    "https://www.upwork.com/resources/web-scraping-guide",
    "https://www.fiverr.com/gigs/web-scraping",
    "https://www.reddit.com/r/webscraping/",
    "https://www.quora.com/topic/Web-Scraping",
    "https://www.linkedin.com/feed/",
    "https://www.github.com/topics/web-scraping",
    "https://www.gitlab.com/explore/projects/topics/web-scraping",
    "https://www.hackernoon.com/tagged/web-scraping",
    "https://www.dev.to/t/web-scraping",
    "https://www.medium.com/tag/web-scraping",
    "https://www.substack.com/explore/category/technology",
    "https://www.producthunt.com/topics/web-scraping",
    "https://www.indiehackers.com/tag/web-scraping",
    "https://www.hashnode.com/tag/web-scraping",
    "https://www.sitepoint.com/premium/books/web-scraping-with-python",
    "https://www.packtpub.com/product/web-scraping-with-python/9781789539640",
    "https://www.oreilly.com/library/view/web-scraping-with/9781491985564/",
    "https://www.manning.com/books/web-scraping-with-python",
    "https://www.springer.com/gp/book/9781484239124",
    "https://www.academia.edu/topics/web_scraping",
    "https://www.researchgate.net/topic/Web-Scraping",
    "https://www.slideshare.net/search/slideshow?searchfrom=header&q=web+scraping",
    "https://www.youtube.com/results?search_query=web+scraping",
    "https://www.udemy.com/topic/web-scraping/",
    "https://www.edx.org/learn/web-development",
    "https://www.pluralsight.com/browse/software-development/web-scraping",
    "https://www.skillshare.com/browse/web-scraping",
    "https://www.futurelearn.com/courses/web-scraping",
    "https://www.linkedin.com/learning/topics/web-scraping",
    "https://www.codeproject.com/Articles/Topic/Web-Scraping",
    "https://www.dzone.com/refcardz/web-scraping",
    "https://www.techrepublic.com/article/web-scraping-tools/",
    "https://www.makeuseof.com/tag/web-scraping-tools/",
    "https://www.digitaltrends.com/computing/best-web-scraping-tools/",
    "https://www.pcworld.com/article/352056/web-scraping-tools.html",
    "https://www.tomshardware.com/reviews/web-scraping-tools",
    "https://www.forbes.com/sites/forbestechcouncil/?sh=4f3b3d5e4f3b",
    "https://www.inc.com/guides/web-scraping",
    "https://www.businessinsider.com/web-scraping-tools",
    "https://www.cnbc.com/select/web-scraping-tools/",
    "https://www.wsj.com/articles/web-scraping-tools",
    "https://www.bloomberg.com/news/articles/web-scraping-tools",
    "https://www.nytimes.com/guides/technology/web-scraping",
    "https://www.theguardian.com/technology/web-scraping",
    "https://www.wired.com/tag/web-scraping/",
    "https://www.theverge.com/tag/web-scraping/",
    "https://www.engadget.com/tag/web-scraping/",
    "https://www.techradar.com/news/web-scraping-tools",
    "https://www.zdnet.com/article/web-scraping-tools/",
    "https://www.cnet.com/how-to/web-scraping-tools/",
    "https://www.pcmag.com/picks/the-best-web-scraping-tools",
    "https://www.tomsguide.com/us/web-scraping-tools,review-5224.html",
    "https://www.trustpilot.com/review/web-scraping-tools",
    "https://www.g2.com/categories/web-scraping",
    "https://www.capterra.com/web-scraping-software/",
    "https://www.softwareadvice.com/web-scraping/",
    "https://www.getapp.com/web-scraping-software/"
]


    headers = {"User-Agent": "Mozilla/5.0"}
    text_samples = []
    max_samples = 4000  # Target jumlah teks

    print("Scraping Web Development Articles...")
    
    for source in sources:
        try:
            print(f"Scraping from {source}...")
            response = requests.get(source, headers=headers, timeout=10)
            
            if response.status_code != 200:
                print(f"Failed to retrieve {source}, skipping...")
                continue
            
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("a", href=True)  # Mencari semua link artikel
            
            for article in articles:
                if len(text_samples) >= max_samples:
                    break
                
                link = article.get("href")
                if not link.startswith("http"):
                    continue
                
                try:
                    article_response = requests.get(link, headers=headers, timeout=10)
                    if article_response.status_code != 200:
                        continue
                    
                    article_soup = BeautifulSoup(article_response.text, "html.parser")
                    paragraphs = article_soup.find_all("p")
                    article_text = " ".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
                    
                    if article_text:
                        text_samples.append([link, article_text])
                        print(f"Collected: {len(text_samples)}/{max_samples}")
                
                except requests.RequestException as e:
                    print(f"Error fetching article {link}: {e}, skipping...")
                    continue
                
                # Delay random untuk menghindari pemblokiran
                time.sleep(random.uniform(1, 0.5))
        
        except requests.RequestException as e:
            print(f"Error accessing {source}: {e}, skipping...")
            continue
    
    print(f"Total text samples collected: {len(text_samples)}")
    
    # Simpan ke CSV
    with open("datasets/webdev_text_samples2.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Text Sample"])
        writer.writerows(text_samples)
    
    print("Data saved to webdev_text_samples2.csv")

if __name__ == "__main__":
    scrape_webdev_articles()
