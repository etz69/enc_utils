from st2actions.runners.pythonrunner import Action
from lxml import html
import requests
import random


class RandomDilbert(Action):
    def __init__(self, config=None):
        super(RandomDilbert, self).__init__(config=config)

    def run(self):
        random_terms_year = str(int(random.uniform(1989, 2017)))
        random_terms_month = str(int(random.uniform(1, 12)))
        random_terms_day = str(int(random.uniform(1, 30)))

        page = requests.get('http://dilbert.com/strip/'+random_terms_year+"-"+random_terms_month+"-"+random_terms_day)
        tree = html.fromstring(page.content)

        div = tree.xpath('//img[@class="img-responsive img-comic"]')
        dilbert_image = div[0].attrib['src']

        return True, dilbert_image
