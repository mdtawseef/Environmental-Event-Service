import json
import requests



from app import app
from flask import render_template, flash, request, redirect, url_for, abort
from flask.ext.responses import json_response
from flask import jsonify
from .forms import SearchForm
from .utils import *




# -------------------------------------------------------------------------------
# Custom error page

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# -------------------------------------------------------------------------------
# API Views

# Get Facts about Country
@app.route('/api/v1/country/<country>')
def show_country_info(country):
    data, response = get_country_information(country)
    if response.status_code == 200:
        return json_response(data[0], status_code=200)
    else:
        return jsonify(
            status=404,
            message="Not Found"
        )

# Get Reports based on country
@app.route('/api/v1/reports/<country>')
def show_country_reports(country):
    # List the country reports
    data, response = get_country_reports(country)
    if response.status_code == 200:
        return json_response(data, status_code=200)
    else:
        return jsonify(
            status=404,
            message="Not Found"
        )

#Summarize report based on id
@app.route('/api/v1/reports/summary/<int:report_id>')
def show_report_summary(report_id):
    # List the country reports
    url = 'http://reliefweb.int/node/' + str(report_id)
    summary = get_summary(url)
    if summary:
        return jsonify(summary)
    else:
        return jsonify(
            status=404,
            message="Not Found"
        )

# Get Report Details and Content
@app.route('/api/v1/report/<int:report_id>')
def show_report_details(report_id):
    data, response = get_report_information(report_id)
    if response.status_code == 200:
         return json_response(data, status_code=200)
    else:
        return jsonify(
            status=404,
            message="Not Found"
        )


# -------------------------------------------------------------------------------
# Main Views
@app.route('/')
@app.route('/index')
def index():
    form = SearchForm()
    return render_template('index.html', title='Home', form=form)


@app.route('/results/', methods=['POST'])
def results():

    form = SearchForm()
    if not form.validate():
        flash('No keyword supplied to search.')
        return redirect(url_for('index'))
    
    data, response = get_country_information(request.form['search_term'])
    if response.status_code == 200:
        country = data[0]
    else:
        abort(404)


    data, response = get_country_reports(request.form['search_term'])
    if response.status_code == 200:
        reports = data["data"]
    else:
        abort(404)

    return render_template('results.html', theKey=request.form['search_term'], countryData=country, reportsData=reports)

@app.route('/details/<int:report_id>')
def details(report_id):
    data, response = get_report_information(report_id)
    if response.status_code == 200:
         report = data["data"][0]
    else:
        abort(404)

    url = report["fields"]["url"]
    summary = get_summary(url)

    return render_template('details.html',  reportData=report, reportSummary=summary)
    