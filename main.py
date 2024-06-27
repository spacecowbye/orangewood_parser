import os
import json
import streamlit as st
from parcv import parcv
from pyairtable import Api
from openai import AzureOpenAI
import zipfile
import tempfile
from src.gemini_query import get_answer_gemini
from src.resume_prompts import get_work_experience_resume
from utils import get_skills


AUTH_TOKEN = ''
BASE_ID = ''
TABLE_ID = ''

def upload_to_airtable(data):
    try:
        # Initialize the Airtable API
        api = Api(AUTH_TOKEN)
        table = api.table(BASE_ID, TABLE_ID)
        table.create(data)
    except Exception as e:
        st.error(f"Error uploading data to Airtable: {e}")

# Function to process a single resume
def process_resume(resume_path, drive_location):
    try:
        # Parse the resume
        parser = parcv.Parser(pickle=True, load_pickled=True)
        json_output = parser.parse(resume_path)

        # Get resume lines and segments
        lines = parser.get_resume_lines()
        resume_text = '\n'.join(lines)
        segments = parser.get_resume_segments()

        file_name = "output.json"
        parser.save_as_json(file_name)

        # Load and modify the output JSON for better efficiency
        with open("output.json", "r") as json_file:
            resume_data = json.load(json_file)
            work_exp_string = ""
            if "Job History" in resume_data:
                companies_worked = [entry["Company"] for entry in resume_data["Job History"]]
                companies_worked = list(set(companies_worked))  # Remove duplicates if needed

                if len(companies_worked) == 0:
                    # Use gemini to get work experience if not found
                    work_exp_prompt = get_work_experience_resume(resume_text)
                    work_exp_string = get_answer_gemini(work_exp_prompt)
                    if not work_exp_string or work_exp_string.strip().lower() == 'n/a':
                        work_exp_string = "No Work Experience Found"

                else:
                    companies_string = ", ".join(companies_worked)
                    work_exp_string = f"Worked at: {companies_string}"

            first_education_entry = resume_data["Education"][0]
            education_string = f"Studied at {first_education_entry['School Name']}"
            skills_resume = resume_data["Skills"]
            skills_string = ''
            if not skills_resume:
                skills_resume = ",".join(get_skills(resume_text))
                skills_string = skills_resume
            else:
                skills_string = ",".join(resume_data["Skills"])

            name_string = resume_data["Name"]
            email_string = resume_data["Contact Info"]["Email"]
            phone_number_string = resume_data["Contact Info"]["phone1"]

        # Prepare data for Airtable
        data = {
            'Name': name_string,
            'Email': email_string,
            'Phone Number': phone_number_string,
            'Work Experience': work_exp_string,
            'Education': education_string,
            'Skills': skills_string,
            'Resume Path': drive_location  # Use the drive location provided by the user
        }

        # Upload data to Airtable
        upload_to_airtable(data)

    except Exception as e:
        st.error(f"Error in processing resume: {e}")

    finally:
        # Delete the temporary PDF file
        if os.path.exists(resume_path):
            os.remove(resume_path)

# Function to process multiple resumes from a zip file
def process_resumes_from_zip(zip_path, drive_location):
    try:
        # Create a temporary directory for extracting the zip file
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            for root, _, files in os.walk(temp_dir):
                for filename in files:
                    if filename.endswith(".pdf"):
                        resume_path = os.path.join(root, filename)
                        process_resume(resume_path, drive_location)

    except Exception as e:
        st.error(f"Error processing resumes from zip file: {e}")

# Main Streamlit app code
def main():
    st.title('Resume Processing App')

    # Get zip file from user input
    uploaded_file = st.file_uploader("Upload a zip file containing resumes (PDF format)", type="zip")

    # Get drive location from user input
    drive_location = st.text_input("Enter the drive folder of the resumes")

    # Process the uploaded zip file
    if uploaded_file is not None and drive_location:
        try:
            with open("uploaded_resumes.zip", "wb") as f:
                f.write(uploaded_file.getvalue())
            process_resumes_from_zip("uploaded_resumes.zip", drive_location)
            st.success("Resume processing complete.")
            os.remove("uploaded_resumes.zip")
        except Exception as e:
            st.error(f"Error during file upload or processing: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    main()

