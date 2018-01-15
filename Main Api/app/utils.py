import json
import requests

from aylienapiclient import textapi

aylien_client = textapi.Client("da002498", "45ef8abb9a8248eb5cc0a238c650144e")

def get_country_information(country):
    # show the Country Profile
    searchTerm = 'https://restcountries.eu/rest/v2/name/' + country + '?fullText=true'
    response = requests.get(searchTerm)
    data = json.loads(response.text)
    return (data, response)

def get_country_reports(country):
    payload = {
                "filter":
                    {
                    "field": "country",
                    "value": country
                    }
                }
    searchTerm = 'https://api.reliefweb.int/v1/reports?appname=envapp'
    response = requests.post(searchTerm, json.dumps(payload))
    data = json.loads(response.text)
    return (data, response)

def get_summary(url, sentence_no=5):
    response = aylien_client.Summarize({'url': url, 'sentences_number': sentence_no})
    summary = response['sentences']
    data = '<br /><br />'.join(summary)
    return response

def get_report_information(report_id):
    # show the Report Profile
    searchTerm = 'https://api.reliefweb.int/v1/reports/' + str(report_id) 
    response = requests.get(searchTerm)
    data = json.loads(response.text)
    return (data, response)


