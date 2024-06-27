
import google.generativeai as genai
import os
def get_answer_gemini(prompt):
    
    ''' method to get the answer from the gemini '''

    API_KEY1 = ""
    genai.configure(api_key=API_KEY1)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)    

    return response.text



