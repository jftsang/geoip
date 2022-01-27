import json
from datetime import datetime

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/leaflet')
def leaflet_view():
    return render_template('leaflet.html')


@app.route('/reportPosition', methods=['POST'])
def report_position_view():
    location = json.loads(request.data)
    resp = location.copy()
    resp['timestamp'] = datetime.fromtimestamp(location['timestamp'] / 1000) \
                                    .strftime('%Y-%m-%d %H:%M:%S')
    resp['ip'] = request.remote_addr
    print(resp)
    return jsonify(resp)
