from celery import shared_task
from .utils import CoinMarketCapScraper

@shared_task
def scrape_coins(coin_names):
    scraper = CoinMarketCapScraper()
    return scraper.get_multiple_coins_data(coin_names)
