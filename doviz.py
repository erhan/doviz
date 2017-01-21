import click
import requests
from bs4 import BeautifulSoup

FG = "white"  # foreground color
pdov_arrow = {"esit": "blue", "yukseldi": "green", "dustu": "red"}
dov_arrow = {"arrow-line": "blue", "arrow-up": "green", "arrow-down": "red"}


def get_rate_from_dov():
    res = requests.get("http://www.doviz.com")
    soup = BeautifulSoup(res.text.replace(",", "."), "lxml")
    rates = soup.findAll("div", {"class": "column2-row2"})
    arrow = soup.findAll("div", {"class": "arrow-row"})
    return {
        "USD": (rates[2].text, rates[3].text, dov_arrow[arrow[2].find('span')["class"][0]]),
        "EUR": (rates[4].text, rates[5].text, dov_arrow[arrow[3].find('span')["class"][0]]),
        "GBP": (rates[6].text, rates[7].text, dov_arrow[arrow[4].find('span')["class"][0]])
    }


def get_rate_from_pdov():
    res = requests.get("http://www.piyasadoviz.com")
    soup = BeautifulSoup(res.text.replace(",", "."), "lxml")
    rates = soup.findAll("li", {"class": "midrow"})
    arrow = soup.findAll("li", {"class": "rrow"})
    return {
        "USD": (rates[3].text, rates[4].text, pdov_arrow[arrow[1].find('span')["class"][0]]),
        "EUR": (rates[9].text, rates[10].text, pdov_arrow[arrow[3].find('span')["class"][0]]),
        "GBP": (rates[15].text, rates[16].text, pdov_arrow[arrow[5].find('span')["class"][0]])
    }


def print_rate(kur, rate):
    click.secho('-' * 30, bg=rate[2], fg=FG, bold=True)
    click.secho('|            %s             |' % kur, bg=rate[2], fg=FG, bold=True)
    click.secho('|       %s - %s      |' % rate[:2], bg=rate[2], fg=FG, bold=True)
    click.secho('-' * 30, bg=rate[2], fg=FG, bold=True)
    pass


@click.command()
@click.option('--site', default="DOV", help='Kuru çekmek istediğiniz siteniz kısa kodunu giriniz.DOV (doviz.com) - PDOV (piyasadoviz.com)', type=click.Choice(['DOV', 'PDOV']))
@click.option('--kur', default="ALL", help='Görmek istediğiniz kurun kısa kodunu giriniz.Tüm kurlar için ALL girebilirsiniz.', type=click.Choice(['ALL', 'USD', 'EUR', 'GBP']))
def get_exchange_rate(kur, site):
    """Kur alış/satış değerlerini istediğiniz siteden çekip komut satırında kurun artış azalışına göre renkli olarak görebileceğiniz program.
    Desteklenen kurlar USD - EUR - GBP """
    func_name = get_rate_from_dov() if site == "DOV" else get_rate_from_pdov()
    for key, value in func_name.items():
        if kur == "ALL" or kur == key:
            print_rate(key, value)


if __name__ == '__main__':
    get_exchange_rate()
