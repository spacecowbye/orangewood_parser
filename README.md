# Resume Parser Application

## Description
This Streamlit-based application processes multiple resumes from a zip file, extracts key information, and uploads the data to Airtable. It uses various libraries for resume parsing, natural language processing, and cloud storage integration.

## Features
- Upload multiple resumes in a zip file
- Parse resumes to extract key information
- Utilize AI (Gemini) for enhanced data extraction when needed
- Upload parsed data to Airtable
- User-friendly interface built with Streamlit

## Prerequisites
- Python 3.x
- Streamlit
- parcv
- pyairtable
- openai
- zipfile
- tempfile

## Installation
1. Clone the repository:

```
git clone https://github.com/spacecowbye/orangewood_parser.git
cd orangewood_parser
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Set up your environment variables:
- `AUTH_TOKEN`: Your Airtable API key
- `BASE_ID`: Your Airtable base ID
- `TABLE_ID`: Your Airtable table ID
- `Api key` : Gemini api key in src/gemini_query.py

To get the airtable api keys
https://airtable.com/
https://support.airtable.com/docs/finding-airtable-ids

4. Run the Streamlit app

```
streamlit run main.py
```