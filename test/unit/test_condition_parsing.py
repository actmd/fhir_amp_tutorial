import json
import sys
import unittest

data = """
{
  "resourceType": "Bundle",
  "link": [
    {
      "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Condition?_app=FHIR&_ver=DSTU2&patient=Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB&category=diagnosis",
      "relation": "self"
    }
  ],
  "total": 3,
  "type": "searchset",
  "entry": [
    {
      "resource": {
        "category": {
          "text": "Diagnosis",
          "coding": [
            {
              "code": "diagnosis",
              "system": "http://hl7.org/fhir/condition-category",
              "display": "Diagnosis"
            },
            {
              "code": "439401001",
              "system": "http://snomed.info/sct",
              "display": "Diagnosis"
            }
          ]
        },
        "code": {
          "text": "Agoraphobia",
          "coding": [
            {
              "code": "F40.00",
              "system": "2.16.840.1.113883.6.90",
              "display": "Agoraphobia"
            },
            {
              "code": "70691001",
              "system": "http://snomed.info/sct",
              "display": "Agoraphobia"
            }
          ]
        },
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "severity": {
          "text": "Medium"
        },
        "resourceType": "Condition",
        "onsetDateTime": "2015-08-24T00:00:00Z",
        "clinicalStatus": "active",
        "dateRecorded": "2015-08-24T00:00:00Z",
        "verificationStatus": "confirmed"
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Condition/T1kK.xqvU20cEJe860G4aKgB",
          "relation": "self"
        }
      ],
      "fullUrl": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Condition/T1kK.xqvU20cEJe860G4aKgB"
    },
    {
      "resource": {
        "category": {
          "text": "Diagnosis",
          "coding": [
            {
              "code": "diagnosis",
              "system": "http://hl7.org/fhir/condition-category",
              "display": "Diagnosis"
            },
            {
              "code": "439401001",
              "system": "http://snomed.info/sct",
              "display": "Diagnosis"
            }
          ]
        },
        "code": {
          "text": "Chronic cough",
          "coding": [
            {
              "code": "R05",
              "system": "2.16.840.1.113883.6.90",
              "display": "Chronic cough"
            },
            {
              "code": "68154008",
              "system": "http://snomed.info/sct",
              "display": "Chronic cough"
            }
          ]
        },
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "severity": {
          "text": "Medium"
        },
        "resourceType": "Condition",
        "onsetDateTime": "2015-08-24T00:00:00Z",
        "clinicalStatus": "active",
        "dateRecorded": "2015-08-24T00:00:00Z",
        "verificationStatus": "confirmed"
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Condition/ToXGIl7BNrvoF6BVybVSoawB",
          "relation": "self"
        }
      ],
      "fullUrl": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Condition/ToXGIl7BNrvoF6BVybVSoawB"
    },
    {
      "resource": {
        "category": {
          "text": "Diagnosis",
          "coding": [
            {
              "code": "diagnosis",
              "system": "http://hl7.org/fhir/condition-category",
              "display": "Diagnosis"
            },
            {
              "code": "439401001",
              "system": "http://snomed.info/sct",
              "display": "Diagnosis"
            }
          ]
        },
        "code": {
          "text": "Asthma",
          "coding": [
            {
              "code": "J45.909",
              "system": "2.16.840.1.113883.6.90",
              "display": "Asthma"
            },
            {
              "code": "195967001",
              "system": "http://snomed.info/sct",
              "display": "Asthma"
            }
          ]
        },
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "severity": {
          "text": "Low"
        },
        "resourceType": "Condition",
        "onsetDateTime": "2015-08-24T00:00:00Z",
        "clinicalStatus": "active",
        "dateRecorded": "2015-08-24T00:00:00Z",
        "verificationStatus": "confirmed"
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Condition/T14QqO8NyASby4jGtzuSA6gB",
          "relation": "self"
        }
      ],
      "fullUrl": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Condition/T14QqO8NyASby4jGtzuSA6gB"
    }
  ]
}
"""


class TestConditionParsing(unittest.TestCase):
    def setUp(self):
        self.conditions = json.loads(data)

    def test_can_parse_conditions_total(self):
        self.assertEqual(self.conditions['total'], 3)

    def test_can_parse_entry(self):
        entry = self.conditions['entry'][0]

        resource = entry['resource']

        category = resource['category']
        self.assertEqual(category['text'],'Diagnosis')

        code = resource['code']
        self.assertEqual(code['text'],'Agoraphobia')

        severity = resource['severity']
        self.assertEqual(severity['text'],'Medium')

        self.assertEqual(resource['resourceType'], 'Condition')
        self.assertEqual(resource['clinicalStatus'], 'active')


if __name__ == '__main__':
    unittest.main()
