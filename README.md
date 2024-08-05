# resume_to_json_parser.github.io

# Resume to JSON Parser

This Streamlit app uses OpenAI's GPT-3.5 to parse resume text and output it in JSON format.

## Requirements

- Python 3.6+
- OpenAI API key

## Setup



1. Install the required packages:

    ```sh
    pip install streamlit openai
    ```

2. Set your OpenAI API key as an environment variable:

    ```sh
    export OPENAI_API_KEY='your-openai-api-key'
    ```

    Alternatively, you can set the API key directly in the script:

    ```python
    openai.api_key = 'your-openai-api-key'
    ```

## Usage

1. Navigate to the directory containing `app.py`.

2. Run the Streamlit app:

    ```sh
    streamlit run cv.py
    ```

3. Upload your CV in text format using the file uploader.

4. Click the "Parse Resume" button to generate the JSON output of your resume.

The parsed resume will be displayed in JSON format in the app.

## Example

The following is an example structure of the JSON output:

```json
{
  "name": "Your Name",
  "contact": {
    "email": "Your Email",
    "phone": "Your Phone Number",
    "address": "Your Address"
  },
  "summary": "Brief summary about yourself",
  "education": [
    {
      "degree": "Your Degree",
      "institution": "Institution Name",
      "year": "Year of Graduation"
    }
  ],
  "experience": [
    {
      "position": "Job Title",
      "company": "Company Name",
      "duration": "Start Date - End Date",
      "responsibilities": [
        "Responsibility 1",
        "Responsibility 2"
      ]
    }
  ],
  "skills": [
    "Skill 1",
    "Skill 2"
  ],
  "certifications": [
    {
      "name": "Certification Name",
      "institution": "Issuing Organization",
      "year": "Year of Certification"
    }
  ],
  "projects": [
    {
      "title": "Project Title",
      "description": "Project Description",
      "technologies": [
        "Technology 1",
        "Technology 2"
      ]
    }
  ]
}


## Contributing
Feel free to open issues or submit pull requests if you have any improvements or suggestions for the project.

## License
This project is licensed under the MIT License.

This `README.md` file is now properly formatted for GitHub, with clear sections and code blocks for setup, usage, and examples.
