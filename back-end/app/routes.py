from flask import render_template, flash, redirect
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

@app.route('/create-strategy', methods = ['GET', 'POST'])
def create_strategy():
    form = CreateStrategyForm()
    if form.validate_on_submit():
        flash("Strategy with name {} created, HFT enabled: {}".format(form.name.data, form.high_frequency.data))
        return redirect('/index')
    return render_template('create_strategy.html', form=form)