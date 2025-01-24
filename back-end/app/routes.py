from flask import render_template
from app import app
from app.forms import CreateStrategyForm

@app.route('/')
@app.route('/index')
def index():
    current_strategy = {'name': 'testing'}

    available_strategies = [
        {
            'name': 'testing2',
            'asset_class': 'Equity'
        },
        {
            'name': 'testing3',
            'asset_class': 'Equity'
        }
    ]

    return render_template('index.html', title='Home', current_strategy=current_strategy, available_strategies=available_strategies)

@app.route('/create-strategy')
def create_strategy():
    form = CreateStrategyForm()
    return render_template('create_strategy.html', form=form)