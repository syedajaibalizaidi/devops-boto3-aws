### CODE FROM DEVSECOPS NANA COURSE, DEFECTDOJO MODULE VID 3 
import requests 

### Authorization Header
headers = {
    'Authorization': 'Token gdg643hdegt737433g45e5qf' ### we pasted here api token from defectdojo in order to connect through.
}

###endpoint 
url = 'https://demo.defectdojo.org/api/v2/import-scan/'

### data configuration for import scan.
data = {
    'active': True,
    'verified': True,
    'scan_type': 'Gitleaks_Scan',
    'minimum_severity': 'Low',
    'engagement': 29
}

### sending the files.
files = {
    'file': open('gitleaks.json', 'rb')
}

response = requests.post(url, headers=headers, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')