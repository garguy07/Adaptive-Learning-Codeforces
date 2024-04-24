# This program scrapes problem names, links, difficulties, and tags from the Codeforces website
# for problems with ratings up to 1200, stores them in a SQLite database, 
# and filters out problems not tagged with 'greedy', 'binary search', or 'dp'.

import requests
from bs4 import BeautifulSoup
import sqlite3
import os

# create a database
def create_database():
    conn = sqlite3.connect('problems.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE problems
                 (id integer primary key, name text, link text, difficulty text, tags text)''')
    conn.commit()
    conn.close()
    
# insert problems into the database
def insert_problem(name, link, difficulty, tags):
    conn = sqlite3.connect('problems.db')
    c = conn.cursor()
    c.execute("INSERT INTO problems (name, link, difficulty, tags) VALUES (?, ?, ?, ?)", (name, link, difficulty, tags))
    conn.commit()
    conn.close()

# scrape the 100 problems on that page that are to be inserted
def get_problems(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    problems = soup.find_all('tr')
    difficulties = []
    for problem in problems[1:100]:
        difficulty = problem.find_all('td')[3].text
        difficulties.append(difficulty)
    
    ind = 0
    problems = soup.find_all('div', style="float: left;")
    for problem in problems[1:100]:
        link = problem.find('a')['href']
        link = 'https://codeforces.com' + link
        name = problem.find('a').text.strip()
        difficulty = difficulties[ind]
        ind += 1
        tags = problem.find_next_sibling('div').text.strip()
        insert_problem(name, link, difficulty, tags)
    

# scrape problems from codeforces
def scrape_problems():
    
    create_database()
    
    url = 'https://codeforces.com/problemset?tags=0-1200'
    get_problems(url)
    url = 'https://codeforces.com/problemset/page/2?tags=0-1200'
    get_problems(url)
    url = 'https://codeforces.com/problemset/page/3?tags=0-1200'
    get_problems(url)
    url = 'https://codeforces.com/problemset/page/4?tags=0-1200'
    get_problems(url)
    url = 'https://codeforces.com/problemset/page/5?tags=0-1200'
    get_problems(url)



if __name__ == '__main__':
        
    # check if the database already exists
    if not os.path.exists('problems.db'):
        scrape_problems()

    # print the problems in the database
    conn = sqlite3.connect('problems.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM problems")
    
    # in case, there is no rating available for a problem, discard it.    
    problems = c.fetchall()
    for problem in problems:
        tags = problem[4]
        if 'greedy' not in tags and 'binary search' not in tags and 'dp' not in tags:
            c.execute("DELETE FROM problems WHERE id = ?", (problem[0],))
            conn.commit()
                
        # conn.close()

    conn.close()
