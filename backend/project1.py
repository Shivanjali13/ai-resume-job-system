import numpy as np
import pandas as pd
jobs = pd.read_csv('naukri_data_science_jobs_india.csv')
jobs.head()
jobs.shape
# since here all columns have importance hence none removed
jobs["Job_Role"].value_counts()
jobs["Company"].value_counts()
jobs["Location"].value_counts()
jobs["Job Experience"].value_counts()
jobs["Skills/Description"].value_counts()

## all are balanced

jobs = jobs[["Job_Role",'Skills/Description','Company','Location','Job Experience']]
jobs.head()
jobs.isnull().sum()

## no missing values
jobs.duplicated().sum()
## no repeatition
jobs.rename(columns={
    'Job_Role': 'job_title',
    'Skills/Description': 'required_skills',
    'Company': 'company',
    'Location': 'location',
    'Job Experience': 'exp_lvl'
}, inplace=True)

jobs.head()

jobs.iloc[1].required_skills
jobs['required_skills'] = jobs['required_skills'].str.lower().str.split(', ')
## list conversion needed because we are usine cosine sil=milarity and TF-IDF CountVectorizer Word embeddings
jobs['required_skills']
jobs.info()


jobs['company'] = jobs['company'].str.lower()
jobs['location'] = jobs['location'].str.lower()


jobs['job_title'] = jobs['job_title'].str.lower()

# remove words like opening, urgent, etc.
remove_words = ['urgent','opening','role','with','for']

for w in remove_words:
    jobs['job_title'] = jobs['job_title'].str.replace(w, '')

# remove punctuation
jobs['job_title'] = jobs['job_title'].str.replace('[^a-zA-Z ]','',regex=True)

# normalize spaces
jobs['job_title'] = jobs['job_title'].str.strip()
jobs.head()
jobs['required_skills'].apply(type).value_counts()
## space removal because space separated entities will be treated differnetly as separate individuals
jobs['location']=jobs['location'].str.replace(" ","_")
jobs['exp_lvl']=jobs['exp_lvl'].str.replace(" ","_")
jobs['company']=jobs['company'].str.replace(" ","_")
jobs['job_title']=jobs['job_title'].str.replace(" ","_")

jobs['required_skills']=jobs['required_skills'].apply(lambda x:[i.replace(" ","_") for i in x])
jobs.head()
jobs['exp_lvl'] = jobs['exp_lvl'].apply(lambda x: [x])
jobs['location'] = jobs['location'].apply(lambda x: [x])
jobs['tags']=jobs['required_skills']+(jobs['exp_lvl'])
jobs.head()
jobs_new = jobs[['company','job_title','tags','location','required_skills']].copy()
jobs_new['tags']=jobs_new['tags'].apply(lambda x:" ".join(x))
jobs_new.head()
# -company ,job title, company, location create vectors of job title and we'll go for closest vectors                    
# -used bag of words for text vectorization but switched to tfidf because in BoW frequency directly proportional to importance .                            
#  #### Example : python repeated a number of times hence python is important but its not               
 #### tfidf : uniqueness based                   
# -combine the words of a tag = large text                      
# -find most common words and extract them                   
# -now take the tag and find the frequency of previously extracted words in each vector of tags               
# -now find the closeness of input to vectors                 
# -this is the answer                        
# -stop words : words used for sentence formation though not present here but will be ignored in case job description provided as paragraphs
from sklearn.feature_extraction.text import TfidfVectorizer#CountVectorizer
cv = TfidfVectorizer(stop_words='english') 
vectors=cv.fit_transform(jobs_new['tags']).toarray()
vectors
cv.get_feature_names_out()
# cosine similarity : we will calculate angle instead of eucleadian distance (preffered for high dimensional data)  
                                             
# refer curse of dimensionality topic                                             
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectors)
def recommend_from_skills(data):
    
    # extract skills from JSON
    skills_list = data.get("skills", [])
    
    # convert list → string (same format as before)
    skills = " ".join(skills_list).lower()
    
    resume_vector = cv.transform([skills]).toarray()
    
    similarity_scores = cosine_similarity(resume_vector, vectors)
    
    scores = list(enumerate(similarity_scores[0]))
    
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
    
    # store results instead of printing
    results = []
    
    for i in sorted_scores:
        row = jobs_new.iloc[i[0]]
        results.append({
            "job_title": row.job_title,
            "company": row.company,
            "location": row.location,
             "description": " ".join(row.required_skills),
            "score": float(i[1])   # convert numpy float → normal float
        })
    
    return results
jobs_new[jobs_new['tags'].str.contains("python sql machine_learning")].head()