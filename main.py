from bs4 import BeautifulSoup
import lxml
import requests



base_url = 'https://www.coingecko.com/'
output_file = 'output.txt'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

max_pages = 111

with open(output_file, 'w', encoding='utf-8') as file:
    for page_number in range(1, max_pages + 1):
        url = f'{base_url}?page={page_number}'
        page_all = requests.get(url, headers=headers)

        if page_all.status_code == 200:
            soup = BeautifulSoup(page_all.text, 'lxml')
            z = soup.find_all('div', class_='tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5')

            for item in z:
                file.write(item.text.strip() + '\n')
