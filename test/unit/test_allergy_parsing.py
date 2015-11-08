import json
import sys
import unittest

data = """
{
  "resourceType": "Bundle",
  "link": [
    {
      "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/AllergyIntolerance?_app=FHIR&_ver=DSTU2&patient=Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB",
      "relation": "self"
    }
  ],
  "total": 3,
  "type": "searchset",
  "entry": [
    {
      "resource": {
        "status": "confirmed",
        "reaction": [
          {
            "onset": "2012-11-07T00:00:00Z",
            "note": {
              "text": "Severity low enough to be prescribed if needed."
            },
            "certainty": "confirmed",
            "manifestation": [
              {
                "text": "Hives"
              }
            ]
          }
        ],
        "substance": {
          "text": "PENICILLIN G",
          "coding": [
            {
              "code": "Q42T66VG0C",
              "system": "http://fdasis.nlm.nih.gov",
              "display": "PENICILLIN G"
            }
          ]
        },
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "criticality": "CRITL",
        "resourceType": "AllergyIntolerance",
        "recordedDate": "2015-08-24T18:11:36Z"
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/AllergyIntolerance/TBwnNbrAqC0Qw5Ha7AFT-2AB",
          "relation": "self"
        }
      ],
      "fullUrl": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/AllergyIntolerance/TBwnNbrAqC0Qw5Ha7AFT-2AB"
    },
    {
      "resource": {
        "status": "confirmed",
        "reaction": [
          {
            "onset": "2010-05-02T00:00:00Z",
            "certainty": "confirmed",
            "manifestation": [
              {
                "text": "Itching"
              }
            ]
          }
        ],
        "substance": {
          "text": "SHELLFISH-DERIVED PRODUCTS",
          "coding": [
            {
              "code": "N0000007624",
              "system": "http://hl7.org/fhir/ndfrt",
              "display": "SHELLFISH-DERIVED PRODUCTS"
            }
          ]
        },
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "criticality": "CRITL",
        "resourceType": "AllergyIntolerance",
        "recordedDate": "2015-11-07T14:55:10Z"
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/AllergyIntolerance/TPcWiBG2h2E114Vh0sRT8fQB",
          "relation": "self"
        }
      ],
      "fullUrl": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/AllergyIntolerance/TPcWiBG2h2E114Vh0sRT8fQB"
    },
    {
      "resource": {
        "status": "confirmed",
        "reaction": [
          {
            "onset": "2014-03-07T00:00:00Z",
            "certainty": "confirmed",
            "manifestation": [
              {
                "text": "Anaphylaxis"
              }
            ]
          }
        ],
        "substance": {
          "text": "STRAWBERRY",
          "coding": [
            {
              "code": "4J2TY8Y81V",
              "system": "http://fdasis.nlm.nih.gov",
              "display": "STRAWBERRY"
            }
          ]
        },
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "criticality": "CRITH",
        "resourceType": "AllergyIntolerance",
        "recordedDate": "2015-11-07T14:56:34Z"
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/AllergyIntolerance/TKebKfLXzu6Sp.LY-IpvpmQB",
          "relation": "self"
        }
      ],
      "fullUrl": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/AllergyIntolerance/TKebKfLXzu6Sp.LY-IpvpmQB"
    }
  ]
}
"""


class TestAllergyParsing(unittest.TestCase):
    def setUp(self):
        self.allergies = json.loads(data)

    def test_can_parse_allergy_totals(self):
        self.assertEqual(self.allergies['total'], 3)

    def test_can_parse_allergy_reactions(self):
        entry = self.allergies['entry'][0]
        resource = entry['resource']
        self.assertEqual(resource['status'], 'confirmed')

        substance = resource['substance']
        self.assertEqual(substance['text'], 'PENICILLIN G')

        reaction = resource['reaction'][0]
        self.assertEqual(reaction['onset'], '2012-11-07T00:00:00Z')
        self.assertEqual(reaction['certainty'], 'confirmed')
        self.assertEqual(reaction['manifestation'][0]['text'], 'Hives')


if __name__ == '__main__':
    unittest.main()
