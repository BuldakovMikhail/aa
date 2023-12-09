from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_words(resp):
    soup = BeautifulSoup(resp, "html.parser")
    text = soup.get_text().split()

    return text


def parse_text_to_file(url, fname):
    resp = urlopen(url)

    text = get_words(resp)

    with open(fname, "w") as dist:
        for w in text:
            dist.write(w + "\n")


def main():
    url = input("Url: ")
    fname = input("Fname: ")

    parse_text_to_file(url, fname)


if __name__ == "__main__":
    main()
    