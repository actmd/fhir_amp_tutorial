import json
import requests
from urllib import quote_plus
from flask import Flask, render_template

app = Flask(__name__)

BASE_URL = 'https://open-ic.epic.com/FHIR/api/FHIR/DSTU2'

DB_PATIENTS = [
    {'firstname': 'Jason', 'lastname': 'Argonaut', 'fhir_id': 'Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB'},
    {'firstname': 'Jessica', 'lastname': 'Argonaut', 'fhir_id': "TUKRxL29bxE9lyAcdTIyrWC6Ln5gZ-z7CLr2r-2SY964B"},
    {'firstname': 'James', 'lastname': 'Kirk', 'fhir_id': 'ToHDIzZiIn5MNomO309q0f7TCmnOq6fbqOAWQHA1FRjkB'}
]


@app.route('/')
def patients():
    return render_template('patients.html', db=DB_PATIENTS)


@app.route('/patient/<id>/allergies')
def allergies(id):
    url = url_patient_allergies(id)
    allergies = get_json(url)
    return render_template('allergies.html', allergies=allergies)


@app.route('/patient/<id>/medications')
def medications(id):
    url = url_patient_medications(id)
    medications = get_json(url)
    return render_template('medications.html', medications=medications)


@app.route('/patient/<id>/conditions')
def conditions(id):
    url = url_patient_conditions(id)
    conditions = get_json(url)
    return render_template('conditions.html', conditions=conditions)


# URL wrangling #
#################
def url_patient_allergies(id):
    return ('%s/AllergyIntolerance?patient=%s' % (BASE_URL, quote_plus(id)))


def url_patient_medications(id):
    return ('%s/MedicationOrder?patient=%s&status=active' % (BASE_URL, quote_plus(id)))


def url_patient_conditions(id):
    return ('%s/Condition?patient=%s&category=diagnosis' % (BASE_URL, quote_plus(id)))


# Request
def get_json(url):
    request = requests.get(url, headers={'Accept': 'application/json'})
    if request.status_code == requests.codes.ok:
        return json.loads(request.text)
    else:
        request.raise_for_status()


if __name__ == '__main__':
    app.run()
