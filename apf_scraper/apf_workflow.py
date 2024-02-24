import subprocess
import sys
import time
import logging


def run_spiders(city, state):
    start = time.time()
    # Run apartment link retrieval
    # subprocess.run(['scrapy', 'crawl', 'apf_crawler', '-a', f'city={city}', '-a', f'state={state}'])
    # logging.info('Crawler Finished')

    # Run parser on apartment
    # subprocess.run(['scrapy', 'crawl', 'apf_parser', '-a', f'city={city}', '-a', f'state={state}'])
    # logging.info('Parser Finished')

    # run zillow unit search 
    subprocess.run(['scrapy', 'crawl', 'zillow_crawler', '-a', f'city={city}', '-a', f'state={state}'])
    subprocess.run(['scrapy', 'crawl', 'zillow_parser', '-a', f'city={city}', '-a', f'state={state}'])

    end = time.time()
    print(f"runtime: {end-start}")
    
if __name__ == "__main__":
    # city = sys.argv[1]
    # state = sys.argv[2]
    # run_spiders(city, state)

    city_list = [('san-diego','ca'),('san-francisco','ca'),('seattle','wa')]
    for city,state in city_list:
        run_spiders(city,state)