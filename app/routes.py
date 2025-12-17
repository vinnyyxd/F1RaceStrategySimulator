from flask import Blueprint, render_template, request
from .strategy import simulate_strategy

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/simulate', methods=['POST'])
def simulate():
    circuit = request.form['circuit']
    tyre = request.form['tyre']
    pit_stops = int(request.form['pit_stops'])

    result = simulate_strategy(circuit, tyre, pit_stops)

    return render_template('result.html', result=result)


@main.route('/about')
def about():
    return "F1 Race Strategy Simulator using Flask"
