from bottle import default_app
from bottle import request, redirect
from bottle import post, get
import json
import os

#f = open("docs/index.html")

@get("/")
def formularz():
    return """
<form action="http://127.0.0.1:8888/" method="post">
          <input placeholder="Imię" name="imie" type="text" />
          <input placeholder="Nazwisko" name="nazwisko" type="text" />
          <div class="dieta">
            <label for="dieta">Jaka forma jedzenia:</label><br>
            <input type="radio" name="dieta" value="zwykla"   id="zwykla"><label for="zwykla">Zwykła</label><br>
            <input type="radio" name="dieta" value="wege" id="wege"><label for="wege">Wege</label><br>
            <input type="radio" name="dieta" value="wegan"  id="wegan"><label for="wegan">Wegan</label><br>
          </div>
          <div class="uczulenia">
            <input type="checkbox" name="uczulenia"/><label for="uczulenia">Czy masz jakieś uczulenia?</label><br>
          </div>
          <div class="uwagi">
            <label for="uwagi">Uwagi/uczulenia:</label>
            <textarea name="uwagi" type="text" cols="40" rows="5"></textarea><br>
          </div>
          <input class="potwierdz" value="Potwierdź" type="submit" />
        </form>
    """


@post("/")
def create():
    username = request.forms.get("imie")
    password = request.forms.get("nazwisko")
    print(request.forms.items())
    # TODO save
    #redirect("http://127.0.0.1:5500/docs/#potwierdz")
    redirect("http://tibicen.pythonanywhere.com")


app = application = default_app()
