import requests
from bs4 import BeautifulSoup
import csv
import time
import random

def scrape_webdev_articles():
    sources = [
    "https://www.smashingmagazine.com/category/web-development/",
    "https://css-tricks.com/",
    "https://dev.to/t/webdev",
    "https://medium.com/tag/web-development",
    "https://web.dev/",
    "https://www.freecodecamp.org/news/tag/web-development/",
    "https://hackernoon.com/tagged/web-development",
    "https://www.sitepoint.com/web-development/",
    "https://scotch.io/",
    "https://www.taniarascia.com/",
    "https://davidwalsh.name/",
    "https://www.codementor.io/community/topic/web-development",
    "https://www.webdesignerdepot.com/category/development/",
    "https://www.frontendmag.com/",
    "https://benediktas.dev/",
    "https://www.codeinwp.com/blog/category/web-development/",
    "https://www.moz.com/blog/category/web-development",
    "https://www.semrush.com/blog/category/web-development/",
    "https://www.logrocket.com/blog/",
    "https://www.aleksandrhovhannisyan.com/blog/",
    "https://typeofnan.dev/",
    "https://flaviocopes.com/",
    "https://overreacted.io/",
    "https://webdesign.tutsplus.com/categories/web-development",
    "https://www.joshwcomeau.com/",
    "https://www.kevinpowell.co/blog/",
    "https://www.digitalocean.com/community/tutorials",
    "https://betterprogramming.pub/tagged/web-development",
    "https://www.webfx.com/blog/web-design/",
    "https://devdojo.com/",
    "https://javascript.plainenglish.io/",
    "https://www.reddit.com/r/webdev/",
    "https://blog.bitsrc.io/",
    "https://moderncss.dev/",
    "https://learn.shayhowe.com/",
    "https://snipcart.com/blog/",
    "https://www.w3.org/blog/",
    "https://www.uxdesign.cc/",
    "https://css-irl.info/",
    "https://www.frontendjournal.com/",
    "https://www.webdesignledger.com/category/development/",
    "https://codepen.io/",
    "https://medium.com/tag/javascript",
    "https://frontendfoc.us/",
    "https://www.fullstackacademy.com/blog",
    "https://webplatform.news/",
    "https://www.w3schools.com/",
    "https://www.html5rocks.com/",
    "https://cssauthor.com/category/web-development/",
    "https://frontendmasters.com/blog/",
    "https://addyosmani.com/",
    "https://alistapart.com/",
    "https://www.sitesaga.com/blog/",
    "https://dennisdel.com/",
    "https://gomakethings.com/",
    "https://codeburst.io/",
    "https://stackabuse.com/",
    "https://matthewstrom.com/blog/",
    "https://una.im/",
    "https://blog.logrocket.com/",
    "https://engineering.linkedin.com/blog",
    "https://frontendhorse.com/",
    "https://www.webdesignerdepot.com/",
    "https://frontendweekly.co/",
    "https://jakearchibald.com/",
    "https://www.smashingmagazine.com/",
    "https://frontendresources.io/",
    "https://scotch.io/tutorials",
    "https://frontendfocus.co/",
    "https://www.telerik.com/blogs",
    "https://www.zachleat.com/web/",
    "https://codefrontend.com/",
    "https://www.toptal.com/developers/blog",
    "https://blog.logrocket.com/category/javascript/",
    "https://dailydevlinks.com/",
    "https://frontendweekly.dev/",
    "https://davidwalsh.name/javascript",
    "https://webtips.dev/",
    "https://getflywheel.com/layout/category/development/",
    "https://thekitze.com/",
    "https://css-tricks.com/archives/",
    "https://peterthaleikis.com/",
    "https://bignerdranch.com/blog/",
    "https://uxdesign.cc/",
    "https://usehooks.com/",
    "https://techblog.constantcontact.com/",
    "https://blog.risingstack.com/",
    "https://leerob.io/blog/",
    "https://webflow.com/blog/",
    "https://michaelnthiessen.com/",
    "https://frontendchecklist.io/blog/",
    "https://mediatemple.net/blog/",
    "https://joshtronic.com/",
    "https://www.keycdn.com/blog",
    "https://chrisnoring.medium.com/",
    "https://itnext.io/",
    "https://catalins.tech/",
    "https://javascriptweekly.com/",
    "https://devblog.media/",
    "https://thenewstack.io/category/development/",
    "https://sebastienlorber.com/"

    #...100 MORE SITES (TOTAL 200 SITES) 
]


    headers = {"User-Agent": "Mozilla/5.0"}
    text_samples = []
    max_samples = 6000  # Target jumlah teks

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
    with open("datasets/webdev_text_samples.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Text Sample"])
        writer.writerows(text_samples)
    
    print("Data saved to webdev_text_samples.csv")

if __name__ == "__main__":
    scrape_webdev_articles()
