from flask import Flask, render_template, request, send_file
from scrapper import job_scrapper
from make_csv import save_to_csv


app = Flask("home")

# make_url(urls)

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    key = request.args.get("key")
    key_lowered = key.lower().strip()
    if key_lowered in db:
        data = db.get(key_lowered)
        return render_template("search.html", jobs=data, leng=len(data), keyword=key, csv_key=key_lowered)
    else:
        data = job_scrapper(key_lowered)
        if data:
            db[key_lowered] = data
            return render_template("search.html", jobs=data, leng=len(data), keyword=key, csv_key=key_lowered)
        else:
            return render_template("search.html", jobs=data, leng=len(data), keyword=key, csv_key=0)


@app.route("/csv")
def csv():
    key = request.args.get("key")
    save_to_csv(key, db[key])
    return send_file(f"{key}.csv")


app.run(host="0.0.0.0")
