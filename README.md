# Resume Processing App

A Streamlit application that processes resumes from a zip file and uploads the extracted data to Airtable. The application parses the resumes, extracts relevant information such as name, email, phone number, work experience, education, and skills, and stores this information in Airtable.

## Features

- Upload a zip file containing resumes in PDF format.
- Extracts and parses resume information.
- Extracted information includes:
  - Name
  - Email
  - Phone number
  - Work experience
  - Education
  - Skills
- Uploads the extracted information to Airtable.

## Requirements

- Python 3.6 or later
- Streamlit
- parcv
- pyairtable
- openai
- zipfile
- tempfile
- dotenv (for environment variable management)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/resume-processing-app.git
   cd resume-processing-app
   ```
2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
# orangewood_parser
