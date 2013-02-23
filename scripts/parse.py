import json
import dateutil.parser


#### Loading and cleaning data

data = json.load(open('1. Registration > 1. Pregnancy Registration.json', 'rb'))
data = data['#']
registrations = [dict(zip(data['headers'], x)) for x in data['rows']]

preg_registration_metrics = ['form|lmp', 'form|meta|timeStart', 'form|case|@case_id']

data2 = json.load(open('2. Pregnancy > 1. Pregnancy Checklist.json', 'rb'))
data2 = data2['#']
checklists = [dict(zip(data2['headers'], x)) for x in data2['rows']]

preg_checklist_metrics = ['form|case|@case_id', 'form|meta|timeStart']

preg_metric_data = {}

for registration in registrations:
    case_id = registration['form|case|@case_id']
    preg_metric_data[case_id] = {}
    preg_metric_data[case_id]['lmp'] = dateutil.parser.parse(registration['form|lmp']).date()
    preg_metric_data[case_id]['start'] = dateutil.parser.parse(registration['form|meta|timeStart']).date()
    preg_metric_data[case_id]['anc_dates'] = []
    
    for checklist in checklists:
        if checklist['form|case|@case_id'] == case_id:
            preg_metric_data[case_id]['anc_dates'].append(dateutil.parser.parse(checklist['form|meta|timeStart']).date())
    preg_metric_data[case_id]['months'] = []
    preg_metric_data[case_id]['anc_dates'] = sorted(preg_metric_data[case_id]['anc_dates'])
    for anc in preg_metric_data[case_id]['anc_dates']:
        preg_metric_data[case_id]['months'].append(int((anc - preg_metric_data[case_id]['lmp']).days / 30))

######### Prepping data for presentations

anc1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
anc2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
anc3 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
anc4 = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for entry in preg_metric_data:
    i = 0
    for month in preg_metric_data[entry]['months']:
        if month > 12:
            continue
        if i == 0:
            anc1[month] += 1
        if i == 1:
            anc2[month] += 1
        if i == 2:
            anc3[month] += 1
        if i == 3:
            anc4[month] += 1
        i += 1
        
months = range(0,13)

xy_anc1 = zip(months, anc1)
xy_anc2 = zip(months, anc2)
xy_anc3 = zip(months, anc3)
xy_anc4 = zip(months, anc4)

json.dump(xy_anc1, open('anc1testdata.json', 'w'))
json.dump(xy_anc2, open('anc2testdata.json', 'w'))
json.dump(xy_anc3, open('anc3testdata.json', 'w'))
json.dump(xy_anc4, open('anc4testdata.json', 'w'))

