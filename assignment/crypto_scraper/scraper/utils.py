import requests
from bs4 import BeautifulSoup

class CoinMarketCapScraper:
    BASE_URL = "https://coinmarketcap.com/currencies/"

    def __init__(self):
        pass

    def get_coin_data(self, coin_name):
        url = self.BASE_URL + coin_name + "/"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": f"Failed to retrieve data for {coin_name}"}

        soup = BeautifulSoup(response.content, 'html.parser')
        data = self.parse_coin_data(soup)
        return data

    def parse_coin_data(self, soup):
        data = {}

        # Parsing coin name
        coin_name_element = soup.find("span", class_="sc-d1ede7e3-0 JCasd base-text")
        data['coin'] = coin_name_element.text.strip() if coin_name_element else None

        # Parsing price
        price_element = soup.find("span", class_="sc-d1ede7e3-0 fsQm base-text")
        data['price'] = float(price_element.text.split('$')[1].replace(",", "")) if price_element else None

        # Parsing price change
        price_change_element = soup.find("p", {"data-change": ["up", "down"]})
        if price_change_element:
            price_change = price_change_element.text.strip().split('%')[0]
            if price_change_element['data-change'] == 'down':
                data['price_change'] = float('-' + price_change)
            else:
                data['price_change'] = float(price_change)
        else:
            data['price_change'] = None

        all_de_classes = soup.find_all("dd", class_="sc-d1ede7e3-0 hPHvUM base-text")

        # Parsing market cap
        market_cap_element = all_de_classes[0]
        if market_cap_element:
            data['market_cap'] = int(market_cap_element.text.split('$')[1].replace(",", ""))
        else:
            data['market_cap'] = None

        all_rank_classes = soup.find_all("span", class_="text slider-value rank-value")

        # Market cap rank
        market_cap_rank = all_rank_classes[0]
        data['market_cap_rank'] = int(market_cap_rank.text.split('#')[1]) if market_cap_rank else None

        # Parsing volume
        volume = all_de_classes[1]
        if volume:
            data['volume'] = int(volume.text.split('$')[1].replace(",", ""))
        else:
            data['volume'] = None

        # Volume rank
        volume_rank = all_rank_classes[1]
        data['volume_rank'] = int(volume_rank.text.split('#')[1]) if volume_rank else None

        # Volume change
        volume_change = all_de_classes[2]
        if volume_change:
            data['volume_change'] = float(volume_change.text.split('%')[0])
        else:
            data['volume_change'] = None

        # Circulating supply
        circulating_supply = all_de_classes[3]
        if circulating_supply:
            data['circulating_supply'] = int(circulating_supply.text.split()[0].replace(",", ""))
        else:
            data['circulating_supply'] = None

        # Total supply
        total_supply = all_de_classes[4]
        if total_supply:
            data['total_supply'] = int(total_supply.text.split()[0].replace(",", ""))
        else:
            data['total_supply'] = None

        # Diluted market cap
        dilute_market_cap = all_de_classes[6]
        if dilute_market_cap:
            data['dilute_market_cap'] = int(dilute_market_cap.text.split('$')[1].replace(",", ""))
        else:
            data['dilute_market_cap'] = None

        # Contracts
        contracts = soup.find('a', class_='chain-name', href=True)
        name = soup.find("span", class_="sc-71024e3e-0 dEZnuB")
        name = name.text.split(':')[0] if name else None
        address = contracts['href'].split('/')[-1] if contracts else None

        data['contracts'] = {"name": name, "address": address}

        # Official links
        blocks = soup.find_all('div', class_='sc-d1ede7e3-0 jTYLCR')
        official_links = []
        socials = []

        for block in blocks:
            title = block.find('span', {'class': 'sc-d1ede7e3-0 fTGacL base-text', 'data-role': 'title'})
            if title and title.text.lower() == 'official links':
                links = block.find_all('a', {'rel': 'nofollow noopener', 'target': '_blank'})
                for link in links:
                    name = link.contents[-1].strip().lower()
                    url = link['href']
                    official_links.append({"name": name, "link": url})
            elif title and title.text.lower() == 'socials':
                links = block.find_all('a', {'rel': 'nofollow noopener', 'target': '_blank'})
                for link in links:
                    name = link.contents[-1].strip().lower()
                    url = link['href']
                    socials.append({"name": name, "url": url})

        data['official_links'] = official_links
        data['socials'] = socials

        return data

    def get_multiple_coins_data(self, coin_names):
        result = {"job_id" : [], "tasks": []}
        for coin in coin_names:
            coin_data = self.get_coin_data(coin)
            coin = coin_data['coin']
            del coin_data['coin']
            result['tasks'].append({"coin": coin, "output": coin_data})
        return result
