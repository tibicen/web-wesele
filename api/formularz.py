#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import default_app
from bottle import request, redirect
from bottle import post, get
import json
import os


def isfolder():
    if not os.path.exists("ludzie"):
        os.mkdir("ludzie")


@get("/")
def formularz():
	isfolder()
	ppl = os.listdir("ludzie")
	ludzie = '''
	<h1>Lista uczestników:</h1>
	<ul>\n
	'''
	for x in ppl:
		osoba = os.path.splitext(x)[0]
		naz, im = osoba.split()
		naz = naz[:3]
		im = im[:3]
		ludzie += f"<li>{naz} {im}</li>\n"
    
	ludzie += "</ul>\n"
	return ludzie


@post("/")
def create():
    imie = request.forms.imie
    nazwisko = request.forms.nazwisko
    dieta = request.forms.dieta
    uczulenia = request.forms.uczulenia
    uwagi = request.forms.uwagi

    if imie == "" or nazwisko == "" or dieta == "":
        # redirect("http://127.0.0.1:5500/docs/#error")
        redirect("https://wesele.huczynski.pl/#error")
    else:
        isfolder()
        name = f"{nazwisko} {imie}.txt"
        f = open(os.path.join("ludzie", name), "w")
        for x in (imie, nazwisko, dieta, uczulenia, uwagi):
            print(x)
            f.write(x + "\n")
        f.close()
        # redirect("http://127.0.0.1:5500/docs/#sukces")
        redirect("https://wesele.huczynski.pl/#sukces")


app = application = default_app()
