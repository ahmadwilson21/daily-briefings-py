# Georgetown Food Ordering Service Web App

A Web App that allows students to preorder food from one of our four on-campus restaurants. Then, it sends an email to user after completing the ordering process.

## Setup

Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/final-project-py
```

Create and activate a new Anaconda virtual environment, perhaps named "final-env":

```sh
conda create -n final-env python=3.7
conda activate final-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

### Google Sheets API Installation

#### Downloading API Credentials

Visit the Google Developer Console (https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the API Credentials page (https://console.developers.google.com/apis/credentials), follow the process to create and download credentials to use the APIs. Fill in the form to find out what kind of credentials:

    API: "Google Sheets API"
    Calling From: "Web Server"
    Accessing: "Application Data"
    Using Engines: "No"

The suggested credentials will be for a service account. Follow the prompt to create a new service account with a role of: "Project" > "Editor", and create credentials for that service account. Download the resulting .json file. Place it into a CREDENTIALS_JSON env variable. 

```sh
CREDENTIALS_JSON='{
 "type": "service_account",
  "project_id": "abc`12",
  "private_key_id": "122345",
  "private_key": "-----BEGIN PRIVATE KEY-----",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "urltoken",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/fsaifjsaofjsaofj"
}'
```

Another way you could do this would be to download the resulting .json file. Rename it google_api_credentials.json and place it into the following directory.

```sh
cd final-project-py/app/auth/google_api_credentials.json
```

You would alter the final-project-py/app/spreadsheet.py file and uncomment the designated code to run the API credentials from there instead.

```sh
cd final-project-py/app/spreadsheet.py
```

#### Google Sheets ENV installation
Use this example google sheet https://docs.google.com/spreadsheets/d/1pNcQBXxmKpusOGHKbYZ_IOn5Bew3v4466xeMfk95Oa4/edit#gid=0 or create your own. Note the document's unique identifier (e.g. 1pNcQBXxmKpusOGHKbYZ_IOn5Bew3v4466xeMfk95Oa4) from its URL, and store the identifier in an environment variable called GOOGLE_SHEET_ID.

If you create your own, make sure it contains four sheets called "Starbucks", "Wisey's", "Chick Fil A", "Epi" with column headers Item ID, Name, Category, Price, and Image Link. And modify the document's sharing settings to grant "edit" privileges to the "client email" address located in the credentials file.

Additionally, you need four Google Sheets for outputting the location of the data as well. We provide one Google Sheets worksheet for each restaurant: 

"Starbucks" - https://docs.google.com/spreadsheets/d/15QlB-cxEhAanuWyiypuL0Ckq4ibYO0CF1b0aplg-MGY/edit?ts=5eb18c5d#gid=0 - 
```sh
STARBUCKS_SHEET_ID="15QlB-cxEhAanuWyiypuL0Ckq4ibYO0CF1b0aplg-MGY"
```
"Chick Fil A" - https://docs.google.com/spreadsheets/d/1I9-2Mi3jfeqUb-4fG7O6YbyQ1Avlbpp9SVqaFuhtRBI/edit#gid=1689009743
```sh
CFA_SHEET_ID="1I9-2Mi3jfeqUb-4fG7O6YbyQ1Avlbpp9SVqaFuhtRBI"
```
"Wisey's"-https://docs.google.com/spreadsheets/d/16IYUNq5mOwNcTPI0RqZHXHR6x3LAo45lmXbR01pCUnc/edit#gid=1904370108
```sh
WISEYS_SHEET_ID = "16IYUNq5mOwNcTPI0RqZHXHR6x3LAo45lmXbR01pCUnc"
```
"Epi" - https://docs.google.com/spreadsheets/d/1tHleFMMoucS7IkeUsjrJpDUWMp3oxXnGrC_dzsQw1DE/edit#gid=0
```sh
EPI_SHEET_ID = "1tHleFMMoucS7IkeUsjrJpDUWMp3oxXnGrC_dzsQw1DE"
```
If you do not use these, create four sheets and add their IDs to the respective
sheet. If you replace the restaurant, then you need to replace the ENV ID
and replace the call in the app/spreadsheet.py file

### Sendgrid API Installation
First, sign up for a free account here (https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then create an API Key here (https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

To setup the usage examples below, store the API Key value in an environment variable called SENDGRID_API_KEY. Also set an environment variable called MY_EMAIL_ADDRESS to be the email address you just associated with your SendGrid account (e.g. "abc123@gmail.com"). You will send emails from this account

You should have the following variables in your .env file
```sh
# .env example

APP_ENV="development" # or set to "production" on Heroku server

GOOGLE_SHEET_ID = "abcd123"
WISEYS_SHEET_ID = "12345abc"
CFA_SHEET_ID = "12345abc"
EPI_SHEET_ID = "12345abc"
STARBUCKS_SHEET_ID = "12345abc"
SENDGRID_API_KEY="exampleid12345"
MY_EMAIL_ADDRESS="me@example.com"

#Depending on which route you choose to implement your JSON file
CREDENTIALS_JSON='{
 "type": "service_account",
  "project_id": "abc`12",
  "private_key_id": "122345",
  "private_key": "-----BEGIN PRIVATE KEY-----",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "urltoken",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/fsaifjsaofjsaofj"
}'

```

> IMPORTANT: remember to save the ".env" file :-D



## Web App Usage
Run the app:

On Mac:
```py
FLASK_APP=web_app flask run
```

On Windows:
```py
export FLASK_APP=web_app 
flask run
```


## Testing
Install pytest package using the following command:

```py
pip install pytest
```

To run test, use the following python script:

```py
pytest
```


