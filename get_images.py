import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import json
import argparse

url_a = 'https://www.google.com/search?ei=1m7NWePfFYaGmQG51q7IBg&hl=en&q={}'
url_b = '\&tbm=isch&ved=0ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ&start={}'
url_c = '\&yv=2&vet=10ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ.1m7NWePfFYaGmQG51q7IBg'
url_d = '\.i&ijn=1&asearch=ichunk&async=_id:rg_s,_pms:s'
url_base = ''.join((url_a, url_b, url_c, url_d))

headers = {'User-Agent': 'Chrome/41.0.2228.0 Safari/537.36'}


def get_links(search_name):
    search_name = search_name.replace(' ', '+')
    url = url_base.format(search_name, 0)
    request = ulib.Request(url, None, headers)
    json_string = ulib.urlopen(request).read()
    json_string = json_string.decode('utf-8')
    page = json.loads(json_string)
    new_soup = Soup(page[1][1], 'lxml')
    images = new_soup.find_all('img')
    links = [image['src'] for image in images]
    return links


def save_images(links, search_name):
    directory = search_name.replace(' ', '_')
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, link in enumerate(links):
        savepath = os.path.join(directory, '{:06}.jpg'.format(i))
        ulib.urlretrieve(link, savepath)


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Downloads images from the internet')
    parser.add_argument('name', metavar='N', help='the name of the images to be searched and downloaded')

    args = parser.parse_args()

    search_name = args.name
    links = get_links(search_name)

    for l in links:
        print(l)

save_images(links, search_name)