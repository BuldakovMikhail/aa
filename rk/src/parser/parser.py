import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize

# Загружаем русский токенизатор nltk
nltk.download("punkt")
import re


def extract_russian_words(url, output_file):
    # Получаем HTML-код страницы
    r = re.compile("[а-яА-Я]+")
    response = requests.get(url)
    html = response.text

    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, "html.parser")

    # Получаем текст из HTML-кода
    text = soup.get_text()

    # Токенизируем текст
    words = word_tokenize(text, language="russian")

    # Отбираем только русские слова
    russian_words = [word.lower() for word in words if word.isalpha()]
    russian_words = [w for w in filter(r.match, russian_words)]

    russian_words = set(russian_words)
    # Записываем русские слова в файл
    with open(output_file, "w", encoding="utf-8") as file:
        for word in russian_words:
            file.write(word + "\n")


if __name__ == "__main__":
    url = "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%BB%D0%BE%D0%B0%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D1%80%D0%B8%D1%82%D0%BE%D0%BD"  # Замените на нужный URL
    output_file = "russian_words.txt"

    extract_russian_words(url, output_file)
