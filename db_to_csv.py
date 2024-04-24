# This program reads the problems.db file and writes the contents to a csv file
# in order to process the data further

import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('problems.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM problems")
    problems = c.fetchall()
    with open ('final.csv', 'w') as f:
        for problem in problems:
            name = problem[1]
            link = problem[2]
            link = link.replace('\r', '').replace('\n', '').replace(' ', '')   
            difficulty = problem[3]
            # remove /n and /r from the difficulty
            difficulty = difficulty.replace('\r', '').replace('\n', '').replace(' ', '')            
            tags = problem[4]
            dp = 'no'
            greedy = 'no'
            binary_search = 'no'
            if 'dp' in tags:
                dp = 'yes'
            if 'greedy' in tags:
                greedy = 'yes'
            if 'binary search' in tags:
                binary_search = 'yes'
            f.write(name + ',' + link + ',' + str(difficulty) + ',' + dp + ',' + greedy + ',' + binary_search + '\n')
        
        conn.commit()
        
    conn.close()
    
    conn = sqlite3.connect('problems.db')
    c = conn.cursor()
    
    