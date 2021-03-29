# resume-parser
Parse a resume to extract common fields like name, college, contact, skills.

The first step is to convert resume to text, typically resumes are PDFs or WORD files. I'm using word file here.
Python doc2txt library helps convert word to text.
word_to_txt(word_path) 

To extract email we can use a Regular Expression to find matching patterns. Emails are usually places at the top of the resume, so the first matching pattern can be assumed to be the email id.
