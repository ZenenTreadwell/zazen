#!/bin/python

from flask import Flask, render_template, url_for
import requests
import json
app = Flask(__name__)

@app.route('/')
def main():
    req = requests.get("https://js.adapools.org/pools/4f5e469a40547208cf9876b36ae9b23874c302ab8ab263a952bbae6a/summary.json")
    pooldata = json.loads(req.content)
    live_stake = round(int(pooldata['data']['total_stake']) / 1000000000, 2)
    return render_template('main.html', data=pooldata, live_stake=live_stake)
