import sys

WEEKDAYS = {
    "воскресенье": "Sunday",
    "понедельник": "Monday",
    "вторник": "Tuesday",
    "среда": "Wednesday",
    "четверг": "Thursday",
    "пятница": "Friday",
    "суббота": "Saturday",
}

MONTHS = {
    "января": "January",
    "февраля": "February",
    "марта": "March",
    "апреля": "April",
    "мая": "May",
    "июня": "June",
    "июля": "July",
    "августа": "August",
    "сентября": "September",
    "октября": "October",
    "ноября": "November",
    "декабря": "December"
}

NOTE_TYPES = {
    "Ваш выделенный отрывок на странице": "Your Highlight on page",
    "Ваш выделенный отрывок в месте": "Your Highlight in location",
    "Ваша закладка на странице": "Your Bookmark on page",
    "Ваша закладка в месте": "Your Bookmark in location",
    "Ваша заметка на странице": "Your Note on page",
    "Ваша заметка в месте": "Your Note in location",
}


def translate_with_dictionary(to_translate, ru_en_dictionary):
    no_match = True

    for ru, en in ru_en_dictionary.items():
        if ru in to_translate:
            translated = to_translate.replace(ru, en)
            no_match = False
            break

    if no_match:
        translated = to_translate
        print(f"No match found for '{to_translate}' with dictionary: {ru_en_dictionary}")
    return translated


def translate_highlight(highlight):
    translated = translate_with_dictionary(highlight, NOTE_TYPES)
    translated = translated.replace("Добавлено:", "Added on")
    translated = translate_with_dictionary(translated, WEEKDAYS)
    translated = translate_with_dictionary(translated, MONTHS)
    translated = translated.replace("Место", "location")
    # Russian version uses en-dashes!!
    # En dash to regular dash
    translated = translated.replace("–", "-")
    translated = translated.replace("г. в ", "")
    return translated


def test_translate_highlight():
    highlight = "Ваш выделенный отрывок на странице 110 | Место 2128–2132 | " \
                "Добавлено: понедельник, 23 декабря 2019 г. в 8:59:02"
    translated = translate_highlight(highlight)
    assert translated == "Your Highlight on page 110 | Location 2128–2132 | Added on Monday, 23 December 2019 8:59:02"


def translate_my_clippings(filename, output_filename):
    with open(output_filename, "w") as f_out:
        with open(filename) as f_in:
            for line in f_in.readlines():
                if "Добавлено:" in line:
                    # if line.startswith("- ") or line.startswith("— "):
                    translated = translate_highlight(line)
                    f_out.write(translated)
                else:
                    f_out.write(line)


if __name__ == "__main__":
    input_clippings = sys.argv[1]
    output_clippings = sys.argv[2]
    translate_my_clippings(input_clippings, output_clippings)

