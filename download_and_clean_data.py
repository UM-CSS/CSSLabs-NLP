# Thi code is identical to the data munging notebook. Reference that for explanation.
# Run this script to fetch and prepare the data for other labs.
#     
# @Author: [Jeff Lockhart](http://www-personal.umich.edu/~jwlock/)

#imports
import pandas as pd
import numpy as np
import urllib.request
import os.path

#data dictionary
essay_cols = ['essay0', 'essay1', 'essay2', 'essay3', 'essay4', 'essay5', 'essay6', 
              'essay7', 'essay8', 'essay9']
ed_levels = {'<HS': ['dropped out of high school', 'working on high school'],
             'HS': ['graduated from high school', 'working on college/university', 
                    'two-year college', 'dropped out of college/university', 
                    'high school'], 
             'BA': ['graduated from college/university', 
                    'working on masters program', 'working on ph.d program', 
                    'college/university', 'working on law school', 
                    'dropped out of masters program', 
                    'dropped out of ph.d program', 'dropped out of law school', 
                    'dropped out of med school'],
             'Grad_Pro': ['graduated from masters program',
                          'graduated from ph.d program',                           
                          'graduated from law school', 
                          'graduated from med school', 'masters program', 
                          'ph.d program', 'law school', 'med school']
            }
bodies = {'average': ['average'], 'fit': ['fit', 'athletic', 'jacked'], 'thin': ['thin', 'skinny'], 'overweight': ['curvey', 'a little extra', 'full figured', 'overweight']}
smoke = {'no': ['no'], np.nan: ['nan']}
kids = {'yes': ['has a kid', 'has kids']}
has_pets = {'yes': ['has']}
drinks = {'no': ['rarely', 'not at all']}
drugs = {'no': ['never']}
jobs = {'education': ['student', 'education'], 'STEM': ['science', 'computer'], 'business': ['sales', 'executive', 'banking'], 'creative': ['artistic', 'entertainment'], 'med_law': ['medicine', 'law'], np.nan: ['nan']}
religion = {'none': ['agnosticism', 'atheism'], 'catholicism': ['catholicism'], 'christianity': ['christianity'], 'judaism': ['judaism'], 'buddhism': ['buddhism'], np.nan: ['nan']}
languages = {'multiple': [',']}
ethn = {'White': ['white', 'middle eastern', 'middle eastern, white'], 'Asian': ['asian', 'indian', 'asian, pacific islander'], 'Black': ['black']}   
ethn2 = {'Latinx': ['latin'], 'multiple': [','], np.nan: ['nan']}   

#functions
def group_age(a):
    return str(int(a/10)*10)

def height(inches):
    h = 'under_6'
    if inches >= 72:
        h = 'over_6'
    return h

def concat(row, cols):
    tmp = []
    for c in cols:
        tmp.append(str(row[c]))
    new = '\n'.join(tmp)
    return new

def recode(text, dictionary, default=np.nan):
    '''Function for recoding categories in a column based on exact matches'''
    out = default
    text = str(text)

    for x in dictionary.keys():
        for y in dictionary[x]:
            if y == text: #exact match
                out = x
                return out
    return out

def recode_fuzzy(text, dictionary, default=np.nan):
    '''Function for recoding categories in a column based on partial matches'''
    out = default
    text = str(text)

    for x in dictionary.keys():
        for y in dictionary[x]:
            if y in text: #partial match
                out = x
                return out
    return out

def census_2010_ethnicity(t):
    text = str(t)
    e = recode(text, ethn, default='other')
    if 'other' == e:
        e = recode_fuzzy(text, ethn2, default='other')
    return e

def which_pets(t, criterion='has'):
    '''Function for determining which pets someone has or likes'''
    d = False
    c = False
    t = str(t)
    p = 'neither'
    if t == 'nan':
        p = np.nan

    if 'has dogs' in t:
        d = True
    if 'has cats' in t:
        c = True

    if criterion == 'likes':
        if 'likes dogs' in t:
            if 'dislikes dogs' not in t:
                d = True
        if 'likes cats' in t:
            if 'dislikes cats' not in t:
                c = True

    if c and d:
        p = 'both'
    elif c:
        p = 'cats'
    elif d:
        p = 'dogs'

    return p

def clean():    
    profiles = pd.read_csv('data/profiles.csv.zip')
    
    # clean up profiles
    profiles = profiles[(profiles.age < 60) & (profiles.age > 17)]
    profiles['text'] = profiles.apply(concat, axis=1, cols=essay_cols)
    profiles['age_group'] = profiles.age.apply(group_age)
    profiles['height_group'] = profiles.height.apply(height)
    profiles['edu'] = profiles.education.apply(recode, dictionary=ed_levels, default='unknown')
    profiles['kids'] = profiles.offspring.apply(recode_fuzzy, dictionary=kids,  default='no')
    profiles['smoker'] = profiles.smokes.apply(recode, dictionary=smoke, default='yes')
    profiles['body'] = profiles.body_type.apply(recode, dictionary=bodies, default='unknown')
    profiles['alcohol_use'] = profiles.drinks.apply(recode, dictionary=drinks, default='yes')
    profiles['drug_use'] = profiles.drugs.apply(recode, dictionary=drugs, default='yes')
    profiles['industry'] = profiles.job.apply(recode_fuzzy, dictionary=jobs, default='other')
    profiles['religion'] = profiles.religion.apply(recode_fuzzy, dictionary=religion, default='other')
    profiles['languages'] = profiles.speaks.apply(recode_fuzzy, dictionary=languages, default='English_only')
    profiles['race_ethnicity'] = profiles.ethnicity.apply(census_2010_ethnicity)
    profiles['pets_likes'] = profiles.pets.apply(which_pets, criterion='likes')
    profiles['pets_has'] = profiles.pets.apply(which_pets, criterion='has')
    profiles['pets_any'] = profiles.pets.apply(recode_fuzzy, dictionary=has_pets, default='no')
    profiles = profiles[['age_group', 'age', 'body', 'alcohol_use', 'drug_use', 'edu', 
                         'race_ethnicity', 'height_group', 'industry', 'kids', 
                         'orientation', 'pets_likes', 'pets_has', 'pets_any', 
                         'religion', 'sex', 'smoker', 'languages', 'text', 'essay0', 
                         'essay1', 'essay2', 'essay3', 'essay4', 'essay5', 'essay6', 
                         'essay7', 'essay8', 'essay9']]

    #save
    profiles.to_csv('data/clean_profiles.tsv', sep='\t', index=False)
    return

#run logic
if os.path.isfile("data/clean_profiles.tsv"):
    # if we have the final output, do nothing
    pass
elif os.path.isfile("data/profiles.csv.zip"):
    # if we don't have the output but we do have the data, clean it
    clean()
else:
    # if we have either data nor output, fetch data and clean it
    URL = "https://www.dropbox.com/s/gpjwfq1c652kyyg/profiles.csv.zip?dl=1"
    urllib.request.urlretrieve(url=URL, filename="data/profiles.csv.zip")
    clean()
