import os

import requests
from flask import Flask,  render_template_string
from bs4 import BeautifulSoup

app = Flask(__name__)
pig_latinizer = "https://hidden-journey-62459.herokuapp.com"


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def pig_latinize(phrase):
    """Takes a phrase, submits it to the piglatinizer, and returns a link"""
    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    # phrase = "what is this"
    input = {"input_text": phrase}
    resp = requests.post(url, data=input, allow_redirects=False)
    return resp.headers.get('Location')


@app.route('/')
def home():
    fact = get_fact().strip()
    pl_link = pig_latinize(fact)
    template = "<a href={{ link }}>{{ link }}</a>"
    return render_template_string(template, link=pl_link)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
