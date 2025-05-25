import os
import fitz
import spacy
import pandas as pd

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_keywords(resume_text, nlp):
    doc = nlp(resume_text)
    keywords = [ent.text for ent in doc.ents]
    return keywords

def main(resume_dir, output_excel):
    nlp = spacy.load('en_core_web_sm')
    all_resume_data = []
    for filename in os.listdir(resume_dir):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(resume_dir, filename)
            text = extract_text_from_pdf(file_path)
            keywords = extract_keywords(text, nlp)
            all_resume_data.append({
                'Filename': filename,
                'Keywords': ', '.join(keywords)
            })
    df = pd.DataFrame(all_resume_data)
    df.to_excel(output_excel, index=False)
    print(f"Data saved to: {output_excel}")

if __name__ == '__main__':
    resume_directory =  '/home/tushar/resumes'
    output_file = 'extracted_keywords.xlsx'
    main(resume_directory, output_file)
