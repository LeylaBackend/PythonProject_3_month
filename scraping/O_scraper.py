# from parsel import Selector
# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-GB,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate, br',
# }
# class ServiceOScrapper:
#     URL = 'https://www.o.kg/ru/chastnym-klientam/uslugi/uslugi/'
#     LINK_XPATH = '//div[@class="col-lg-9 col-xs-12"]/div/a/@href'
#     PLUS_URL = 'https://www.o.kg'
#
#     def parse_data(self):
#         html = requests.get(self.URL).text
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         for link in links:
#             pass
#         return links[:5]
#
#
# if __name__ == "__main__":
#     scraper = ServiceOScrapper()
#     scraper.parse_data()