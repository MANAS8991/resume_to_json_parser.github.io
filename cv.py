import openai
import os
import streamlit as st

# Set your OpenAI API key here or ensure it's set as an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_parsed_resume(resume_text):
    prompt = f"""
    You are a tool that processes resumes. I will provide you with the text of my resume, and I need you to parse the content and output it in JSON format. Here's the structure to follow:

    ```json
    {{
      "name": "Your Name",
      "contact": {{
        "email": "Your Email",
        "phone": "Your Phone Number",
        "address": "Your Address"
      }},
      "summary": "Brief summary about yourself",
      "education": [
        {{
          "degree": "Your Degree",
          "institution": "Institution Name",
          "year": "Year of Graduation"
        }}
      ],
      "experience": [
        {{
          "position": "Job Title",
          "company": "Company Name",
          "duration": "Start Date - End Date",
          "responsibilities": [
            "Responsibility 1",
            "Responsibility 2"
          ]
        }}
      ],
      "skills": [
        "Skill 1",
        "Skill 2"
      ],
      "certifications": [
        {{
          "name": "Certification Name",
          "institution": "Issuing Organization",
          "year": "Year of Certification"
        }}
      ],
      "projects": [
        {{
          "title": "Project Title",
          "description": "Project Description",
          "technologies": [
            "Technology 1",
            "Technology 2"
          ]
        }}
      ]
    }}
    ```

    Please parse the following resume text into the JSON structure above:

    ```
    {resume_text}
    ```
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0
    )

    parsed_resume = response.choices[0].text.strip()
    return parsed_resume

def main():
    st.title("Resume to JSON Parser")

    uploaded_file = st.file_uploader("Upload your CV", type=["txt"])

    if uploaded_file is not None:
        resume_text = uploaded_file.read().decode("utf-8")
        st.text_area("Resume Text", resume_text, height=300)

        if st.button("Parse Resume"):
            with st.spinner("Parsing resume..."):
                parsed_resume = get_parsed_resume(resume_text)
                st.json(parsed_resume)

if __name__ == "__main__":
    main()
