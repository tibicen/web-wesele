from bottle import default_app
from bottle import request
from bottle import post, get
import json


@get("/")
def login():
    return """
        <form action="/names" method="post">
            Imię: <input name="imie" type="text" /> <br>
            Nazwisko: <input name="nazwisko" type="text" /> <br>
            Jaka forma jedzenia:<br>
            <input type="radio" id="male" name="gender" value="male">
            <label for="male">dieta 1</label><br>
            <input type="radio" id="female" name="gender" value="female">
            <label for="female">dieta 2</label><br>
            <input type="radio" id="other" name="gender" value="other">
            <label for="other">dieta 3</label><br>
            <input type="checkbox" /> Czy masz jakieś uczulenia? <br>
            Opis uczulenia: <input type="text" /> <br>
            <input value="Wyślij" type="submit" />
        </form>
    """


@post("/")
def create():
    username = request.forms.get("username")
    password = request.forms.get("password")
    print(username)
    print(password)
    return f"<p>{username}</p><br><p>{password}</p>"


app = application = default_app()
