import requests


def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    url = "http://quotes.stormconsultancy.co.uk/random.json".format()

    response = requests.get(url).json()

    return response