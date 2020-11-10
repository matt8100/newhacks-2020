from flask import render_template, flash, redirect, request, session
from app import app
from app.forms import TokenForm, SearchForm
import canvas
import sys

pageUrls = []
bodies = []
token = ""

@app.route("/access", methods=["GET", "POST"])
def tokenSubmit():
    form = TokenForm()
    if form.validate_on_submit():
        flash("Token {} submitted, rememberMe={}".format(form.token.data, form.rememberMe.data))
        session["token"] = form.token.data
        return redirect("/search"+"?token="+form.token.data)
    return render_template("token.html", title="Access Token", form=form)

@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash("Searching for {}".format(form.query.data))
        session["query"] = form.query.data
        return redirect("/results"+"?query="+form.query.data)
    return render_template("search.html", title="Search", form=form)

@app.route("/results", methods=["GET", "POST"])
def results():
    query = session.get("query")
    print(query, file=sys.stderr)
    token = session.get("token")
    print(token, file=sys.stderr)
    pageUrls = canvas.retrieveUrls(token)
    bodies = canvas.retrieveText(token)
    searchResults = canvas.search(query, bodies)
    print(searchResults, file=sys.stderr)
    results = []
    print(len(searchResults), file=sys.stderr)
    print(len(pageUrls), file=sys.stderr)
    for i in searchResults:
        results.append(pageUrls[i])
    print(results, file=sys.stderr)
    return render_template("results.html", results=results, query=query)
    
