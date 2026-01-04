from quotes_scraper_project.config.settings import minio_config
#from quotes_scraper_project.etl.extract.scraper import QuotesScraper
from quotes_scraper_project.utils.util_logs import write_log

def main():
    print("-> in main")




if __name__ == "__main__":
    main()
    # === call settings:
    # print(minio_config.endpoint)

    # === call QuotesScraper:
    #quotes_scraper_obj = QuotesScraper()
    # -- Attribute
    # print(quotes_scraper_obj.base_url)
    # -- scrape_quotes_page()
    # print(quotes_scraper_obj.scrape_quotes_page(quotes_scraper_obj.base_url))
    # -- scrape_all_quotes()
    # quotes = quotes_scraper_obj.scrape_all_quotes()
    # cpt = 1
    # for quote in quotes:
    #     print(f"======= Quote {cpt} =======")
    #     print(quote)
    #     cpt += 1
    # -- scrape_author()
    # url_page_author = "https://quotes.toscrape.com/author/Mark-Twain/"
    # print(quotes_scraper_obj.scrape_author(url_page_author))
    # -- scrape_by_tag()
    # quotes = quotes_scraper_obj.scrape_by_tag("truth")
    # cpt = 1
    # for quote in quotes:
    #     print(f"======= Quote {cpt} =======")
    #     print(quote)
    #     cpt += 1
    # -- get_available_tags()
    # print(quotes_scraper_obj.get_available_tags())# *****must be more than 10. (misattributed-mark-twain)
    # -- scrape_complete()
    # complete_scrape = quotes_scraper_obj.scrape_complete()
    # quotes = complete_scrape['quotes']
    # authors = complete_scrape['authors']
    # cpt = 1
    # for quote in quotes:
    #     print(f"======= Quote {cpt} =======")
    #     print(quote)
    #     cpt += 1
    # for author in authors:
    #     print(f"======= author {cpt} =======")
    #     print(author)
    #     cpt += 1
    # # -- close():
    # quotes_scraper_obj.close()

    #-----
    write_log("infoo", "log msg")





