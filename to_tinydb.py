from tinydb import TinyDB, Query

# Key-value pairs
data = {
    'Company Name': 'BRAINBOOST LTD.',
    'First name': 'Pablo Tomas',
    'Last name': 'Borda',
    'Preferred Name': 'Pablo',
    'Email to apply for jobs': 'bordapablotomas@gmail.com',
    'Password': '$yqbG1qnCt!Y8G^wcsdT',
    'VAT Number': 'IE3435462UH',
    'Company number': '589489',
    'CRO': '589489',
    'Address': 'PALMERSTON HALL, DOMINICK STREET UPPER',
    'Postal code': 'D07 YW50',
    'City': 'Dublin',
    'District': 'Dublin',
    'Linkedin Profile': 'https://www.linkedin.com/in/pabloborda/',
    'Github': 'https://github.com/PabloBorda',
    'Portfolio website': 'https://goldenthinker.com',
    'email for job search': 'bordapablotomas@gmail.com',
    'Cover letter for financial job USA': 'Dear Recruiter, Hello, I am a Software Engineer, Architect, Business Analyst. I have 18+ years of work experience...',
    'Cover letter for normal job USA': 'Dear Recruiter, Hello, I am a Software Engineer, Architect, Business Analyst. I have 18+ years of work experience...',
    'My Curriculum in Text mode in a single line': 'Pablo Tomas BordaDublin, Ireland D07YW50+16503186295...',
    'Company website': 'https://goldenthinker.com',
    'Phone': '+16503186295',
    'Mobile': '+16503186295',
    'site': 'https://goldenthinker.com',
    'skype': 'brainboost@brainboost.ie'
}

# Initialize TinyDB and the 'form_values' table
db = TinyDB('db.json')
table = db.table('form_values')

# Insert key-value pairs with initialized non-negative number field
for key, value in data.items():
    table.insert({key: value, 'frequency': 0})

# Close the database connection
db.close()
