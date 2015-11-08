import json
import sys
import unittest

data = """
{
  "resourceType": "Bundle",
  "link": [
    {
      "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder?_app=FHIR&_ver=DSTU2&patient=Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB&status=active",
      "relation": "self"
    }
  ],
  "total": 4,
  "type": "searchset",
  "entry": [
    {
      "resource": {
        "status": "active",
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "resourceType": "MedicationOrder",
        "dateWritten": "2015-11-07T00:00:00Z",
        "substitution": {
          "type": {
            "coding": [
              {
                "code": "N",
                "system": "urn:oid:2.16.840.1.113883.1.11.16621"
              }
            ]
          }
        },
        "dosageInstruction": [
          {
            "text": "Take 1 tablet (100 mg total) by mouth 3 (three) times a day before meals.",
            "route": {
              "text": "Oral",
              "coding": [
                {
                  "code": "15",
                  "system": "urn:oid:1.2.840.114350.1.13.327.1.7.4.698288.330",
                  "display": "Oral"
                }
              ]
            },
            "doseQuantity": {
              "code": "mg",
              "system": "urn:oid:2.16.840.1.113883.6.8",
              "value": 100.0
            },
            "timing": {
              "repeat": {
                "periodUnits": "h",
                "frequency": 1,
                "period": 8.0,
                "bounds": {
                  "start": "2015-11-07T00:00:00Z",
                  "end": "2016-11-06T00:00:00Z"
                }
              }
            },
            "asNeededBoolean": false,
            "method": {
              "text": "Take",
              "coding": [
                {
                  "code": "11",
                  "system": "urn:oid:1.2.840.114350.1.13.327.1.7.4.798268.8600",
                  "display": "Take"
                }
              ]
            }
          }
        ],
        "medicationReference": {
          "display": "allopurinol (ZYLOPRIM) 100 MG tablet",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Medication/T7pCFfhRFJYHch5D3Tt4XaQB"
        },
        "prescriber": {
          "display": "Physician Cdr Inpatient, MD",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Practitioner/TJIwbotDwiZ6wgU-.V1OgUAB"
        },
        "identifier": [
          {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.327.1.7.2.798268",
            "value": "971105"
          },
          {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.327.1.7.3.798268.801",
            "value": "971105:2902914733"
          }
        ]
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder/T85bAGuKFO3l.38SFGT3bKgB",
          "relation": "self"
        }
      ]
    },
    {
      "resource": {
        "status": "active",
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "resourceType": "MedicationOrder",
        "dateWritten": "2015-11-07T00:00:00Z",
        "substitution": {
          "type": {
            "coding": [
              {
                "code": "N",
                "system": "urn:oid:2.16.840.1.113883.1.11.16621"
              }
            ]
          }
        },
        "dosageInstruction": [
          {
            "text": "Take 1 capsule (15 mg total) by mouth every morning. Max Daily Amount: 15 mg",
            "route": {
              "text": "Oral",
              "coding": [
                {
                  "code": "15",
                  "system": "urn:oid:1.2.840.114350.1.13.327.1.7.4.698288.330",
                  "display": "Oral"
                }
              ]
            },
            "doseQuantity": {
              "code": "mg",
              "system": "urn:oid:2.16.840.1.113883.6.8",
              "value": 15.0
            },
            "timing": {
              "repeat": {
                "periodUnits": "d",
                "frequency": 1,
                "period": 1.0,
                "bounds": {
                  "start": "2015-11-07T00:00:00Z",
                  "end": "2015-12-07T00:00:00Z"
                }
              }
            },
            "asNeededBoolean": false,
            "method": {
              "text": "Take",
              "coding": [
                {
                  "code": "11",
                  "system": "urn:oid:1.2.840.114350.1.13.327.1.7.4.798268.8600",
                  "display": "Take"
                }
              ]
            }
          }
        ],
        "medicationReference": {
          "display": "amphetamine-dextroamphetamine XR (ADDERALL XR) 15 MG 24 hr capsule",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Medication/TDJEToqCVh79KnGH7H7PdSwB"
        },
        "prescriber": {
          "display": "Physician Cdr Inpatient, MD",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Practitioner/TJIwbotDwiZ6wgU-.V1OgUAB"
        },
        "identifier": [
          {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.327.1.7.2.798268",
            "value": "971103"
          },
          {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.327.1.7.3.798268.801",
            "value": "971103:2802249019"
          }
        ]
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder/TsmsDHh.ouMCg8QqhDaAMSAB",
          "relation": "self"
        }
      ]
    },
    {
      "resource": {
        "status": "active",
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "resourceType": "MedicationOrder",
        "dateWritten": "2015-09-18T00:00:00Z",
        "substitution": {
          "type": {
            "coding": [
              {
                "code": "N",
                "system": "urn:oid:2.16.840.1.113883.1.11.16621"
              }
            ]
          }
        },
        "dosageInstruction": [
          {
            "text": "Take 1 tablet (80 mg total) by mouth daily.",
            "route": {
              "text": "Oral",
              "coding": [
                {
                  "code": "15",
                  "system": "urn:oid:1.2.840.114350.1.13.327.1.7.4.698288.330",
                  "display": "Oral"
                }
              ]
            },
            "doseQuantity": {
              "code": "mg",
              "system": "urn:oid:2.16.840.1.113883.6.8",
              "value": 80.0
            },
            "timing": {
              "repeat": {
                "periodUnits": "d",
                "frequency": 1,
                "period": 1.0,
                "bounds": {
                  "start": "2015-09-18T00:00:00Z",
                  "end": "2016-09-17T00:00:00Z"
                }
              }
            },
            "asNeededBoolean": false,
            "method": {
              "text": "Take",
              "coding": [
                {
                  "code": "11",
                  "system": "urn:oid:1.2.840.114350.1.13.327.1.7.4.798268.8600",
                  "display": "Take"
                }
              ]
            }
          }
        ],
        "medicationReference": {
          "display": "atorvastatin (LIPITOR) 80 MG tablet",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Medication/TkhAZad-0I-LgUa6HbXU3gwB"
        },
        "prescriber": {
          "display": "Physician Allergy, MD",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Practitioner/TIY9FQ1OkFbokwyIOagncLAB"
        },
        "identifier": [
          {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.327.1.7.2.798268",
            "value": "971101"
          },
          {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.327.1.7.3.798268.801",
            "value": "971101:2835804257"
          }
        ]
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder/Tw.v50ASgwkc..KACD2lswgB",
          "relation": "self"
        }
      ]
    },
    {
      "resource": {
        "status": "active",
        "patient": {
          "display": "Jason Argonaut",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Patient/Tbt3KuCY0B5PSrJvCu2j-PlK.aiHsu2xUjUM8bWpetXoB"
        },
        "resourceType": "MedicationOrder",
        "dateWritten": "2015-11-07T00:00:00Z",
        "substitution": {
          "type": {
            "coding": [
              {
                "code": "N",
                "system": "urn:oid:2.16.840.1.113883.1.11.16621"
              }
            ]
          }
        },
        "dosageInstruction": [
          {
            "text": "Take 1 tablet (2 mg total) by mouth 2 (two) times a day before meals.",
            "route": {
              "text": "Oral",
              "coding": [
                {
                  "code": "15",
                  "system": "urn:oid:1.2.840.114350.1.13.327.1.7.4.698288.330",
                  "display": "Oral"
                }
              ]
            },
            "doseQuantity": {
              "code": "mg",
              "system": "urn:oid:2.16.840.1.113883.6.8",
              "value": 2.0
            },
            "timing": {
              "repeat": {
                "periodUnits": "h",
                "frequency": 1,
                "period": 12.0,
                "bounds": {
                  "start": "2015-11-07T00:00:00Z",
                  "end": "2016-11-06T00:00:00Z"
                }
              }
            },
            "asNeededBoolean": false,
            "method": {
              "text": "Take",
              "coding": [
                {
                  "code": "11",
                  "system": "urn:oid:1.2.840.114350.1.13.327.1.7.4.798268.8600",
                  "display": "Take"
                }
              ]
            }
          }
        ],
        "medicationReference": {
          "display": "rosiglitazone (AVANDIA) 2 MG tablet",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Medication/TbowHkSVWnx7IORtUe8fiaQB"
        },
        "prescriber": {
          "display": "Physician Cdr Inpatient, MD",
          "reference": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/Practitioner/TJIwbotDwiZ6wgU-.V1OgUAB"
        },
        "identifier": [
          {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.327.1.7.2.798268",
            "value": "971104"
          },
          {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.327.1.7.3.798268.801",
            "value": "971104:2886137114"
          }
        ]
      },
      "search": {
        "mode": "match"
      },
      "link": [
        {
          "url": "https://open-ic.epic.com/FHIR/api/FHIR/DSTU2/MedicationOrder/Tw263wu6vdgnipYaCIKrh8wB",
          "relation": "self"
        }
      ]
    }
  ]
}
"""


class TestMedicationParsing(unittest.TestCase):
    def setUp(self):
        self.medications = json.loads(data)

    def test_can_parse_medication_total(self):
        self.assertEqual(self.medications['total'], 4)

    def test_can_parse_entry(self):
        entry = self.medications['entry'][0]
        resource = entry['resource']
        self.assertEqual(resource['resourceType'],'MedicationOrder')

        substitution = resource['substitution']['type']['coding'][0]['code']
        self.assertEqual(substitution,'N')

        dosageInstruction = resource['dosageInstruction'][0]
        self.assertEqual(dosageInstruction['text'],'Take 1 tablet (100 mg total) by mouth 3 (three) times a day before meals.')

        medicationReference = resource['medicationReference']
        self.assertEqual(medicationReference['display'],'allopurinol (ZYLOPRIM) 100 MG tablet')

        prescriber = resource['prescriber']
        self.assertEqual(prescriber['display'],'Physician Cdr Inpatient, MD')


if __name__ == '__main__':
    unittest.main()
