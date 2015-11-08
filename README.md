# FHIR AMP Tutorial

This is a guide for creating a simple application that can let you extract and display Allergies, Medications and Problems (Conditions) from a FHIR server.

We are going to be using the following stack for demonstration purposes
    * [Epic FHIR Resources](https://open.epic.com/Interface/FHIR) 
    * [Python Flask](http://flask.pocoo.org/) - a very decent micro-framework

# Setup
 
Fork this, and run on heroku.

If you are going to run this locally, then you should install the pip requirements.

    pip install -r requirements.txt
    
If you are going to do local development, I much prefer using [LiveReload](https://github.com/lepture/python-livereload) so that tests are re-run on change, and the server is restarted when updated. If you want to use reload you should install the dev requirements.

    pip install -r requirements_dev.txt
    
Then to use LiveReload during development, use

    python live.py

# What the app does

It connects to the demo epic instance, and for a prespecified list of patients, lets you see their 

* allergies
* medications
* conditions (aka problems or diagnoses)

The scope of this project is just to show you how you might show a read-only view of this data.

# Lessons learned

The patient search interface is not designed to allow you to search for all patients in the system. It is designed to only allow you to search for patients by some strong criteria (generally has to include a family and a given name).

You can see a list of all the available patients in the [Epic Patient Resource API page](https://open.epic.com/Clinical/Patient).

The FHIR id is hard coded in this application. When you do a search, the ID returned is actually the internal id. You cannot use this as your patient id. See this [example](https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient?family=Argonaut&given=Jessica) 

You will see the following returned:

```json
 "entry": [
    {
      "fullUrl": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/TUKRxL29bxE9lyAcdTIyrWC6Ln5gZ-z7CLr2r-2SY964B",
    }]
```

In theory, you could use the full url as the ID (according to Janet from Epic), or you could just parse the ID from the url above. In this application, Flask routing does not like the full URL as a parameter, just the ID. 
