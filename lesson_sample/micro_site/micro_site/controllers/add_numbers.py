from utils import parse_post, render_template
from app_logic import set_first_value, set_second_value, get_addition


def add_numbers(environ):
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = parse_post(environ)
        first_value = data.get("first_value", [0])[0]
        second_value = data.get("second_value", [0])[0]
        set_first_value(first_value)
        set_second_value(second_value)

        #ここに処理を書く


    addition = get_addition()

    # additionの結果を渡す
    return render_template("boundaries/add_numbers_data.html", addition=addition)