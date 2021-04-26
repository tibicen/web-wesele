#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import DEBUG, default_app
from bottle import request, redirect
from bottle import post, get
from bottle import auth_basic
import json
import os

# URL = "http://127.0.0.1:5500/docs/"
URL = "https://wesele.huczynski.pl/"


def isfolder():
    if not os.path.exists("ludzie"):
        os.mkdir("ludzie")


def user_auth(user, password):
    if user == "tibicen" and password == "sparta11":
        return True
    else:
        return False


def check_update():
    if os.path.exists("ilosc.txt"):
        return int(open("ilosc.txt", "r").read())
    else:
        return 0


@get("/")
@auth_basic(user_auth)
def formularz():
    isfolder()
    ppl = os.listdir("ludzie")
    html = """
	<h1>Lista uczestników:</h1>
    <p>{}</p>
	 <table style="width:100%; border:1px solid; border-collapse: collapse; text-align:center;">
        <tr>
            <th style="border:1px solid">Imię</th>
            <th style="border:1px solid">Nazwisko</th>
            <th style="border:1px solid">Dieta</th>
            <th style="border:1px solid">Uczulenia</th>
            <th style="border:1px solid">Uwagi</th>
        </tr>{}
     </table> 
	"""
    if check_update() == len(ppl):
        with open("ludzie.json", "r") as f:
            dieta, ludzie = json.load(f)
    else:
        ludzie = []
        dieta = {
            "zwykla": 0,
            "wege": 0,
            "wegan": 0,
        }
        for x in ppl:
            with open(os.path.join("ludzie", x)) as f:
                osoba = json.load(f)
            ludzie.append(osoba)
            dieta[osoba["dieta"]] += 1

        f = open("ilosc.txt", "w")
        f.write(str(len(ppl)))
        f.close()
        with open("ludzie.json", "w") as f:
            json.dump([dieta, ludzie], f)

    text_dieta = ""
    for k, v in dieta.items():
        text_dieta += f"{k}:{v}<br>"
    text_dieta += f"Potwierdziły {len(ludzie)} osoby"

    dane = ""
    for o in sorted(ludzie, key=lambda x: x["nazwisko"].lower()):
        osoba = "<tr>"
        for k, v in o.items():
            osoba += f'<td style="border:1px solid gray">{v}</td>'
        osoba += "</tr>"
        dane += osoba

    return html.format(text_dieta, dane)


@post("/")
def create():
    p = {
        "imie": request.forms.imie,
        "nazwisko": request.forms.nazwisko,
        "dieta": request.forms.dieta,
        "uczulenia": request.forms.uczulenia,
        "uwagi": request.forms.uwagi,
    }

    if p["imie"] == "" or p["nazwisko"] == "" or p["dieta"] == "":
        redirect(f"{URL}#error")
    else:
        isfolder()
        naz = p["nazwisko"]
        imie = p["imie"]
        name = f"{naz} {imie}.json"
        with open(os.path.join("ludzie", name), "w") as f:
            json.dump(p, f)
        redirect(f"{URL}#sukces")


app = application = default_app()
