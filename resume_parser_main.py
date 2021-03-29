from pdfminer.high_level import extract_text
import docx2txt
import nltk
from nltk.corpus import stopwords
import re

#nltk.download('stopwords') #dont need to use everytime

#no need to download everytime
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

#using extract_text from pdfminer to convert to txt
def pdf_to_txt(pdf_path):
    return extract_text(pdf_path)

#to convert resume file into text, using docx2txt in case of word files
def word_to_txt(word_path):
    text = docx2txt.process(word_path)
    if text:
        return text
        #.replace('\t',' ')
    return None


#TO EXTRACT EMAIL
#define a regex, first letter should be small in email
#EMAIL_REGEX = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
#use regex in function
def extract_email(resume):
    return re.findall(EMAIL_REGEX, resume)





if __name__ == '__main__':
    #print(pdf_to_txt('test_resume.pdf'))
    #taking input and converting to text
    raw_text = word_to_txt('test_resume.docx')

    text_output=' '.join(raw_text.split())
    print(text_output)


    #calling func to get email
    emails_extracted = extract_email(text_output)
    if emails_extracted:
        print("Email: ", emails_extracted)



#note: in case of doc use catdoc
#now we should have output in txt


#what __name__ means, top level code
#https://www.freecodecamp.org/news/if-name-main-python-example/ 

