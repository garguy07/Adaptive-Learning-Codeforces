# Adaptive Learning For Codeforces - Google Girl Hackathon

### The directory structure is as follows:

```
.
├── app.ipynb
├── db_to_csv.py
├── final.csv
├── problem_scraper.py
├── problems.db
├── README.md
└── user.csv

0 directories, 7 files
```

### Following are the commands that are to be used.

1. First execute the following command to remove the existing databases. They are provided if you directly want to jump to step 4 instead of running the scraper all over again. The files `final.csv`, `problems.db` and `user.csv` are created using the first 3 commands. 

```
rm final.csv problems.db user.csv
```

2. Then execute the following command:

```
python3 problem_scraper.py
```

3. Then, run the following command to obtain the final database:

```
python3 db_to_csv.py
```

The files `final.csv`, `problems.db` and `user.csv` will be generated after executing the above commands. 


4. Finally, click `Run all` on the Jupyter notebook `app.ipynb` to run the code. You will be prompted enter the Codeforces handle of the user. Enter the handle, then press enter. At the end of the Jupyter notebook, the recommended problems will be displayed.

Additionally, I have also displayed a plot that shows the problems from the expert database. A list of problems solved by the user is also displayed.

### Theory

- `final.csv` is the expert dataset of the model. It contains everything that a person could learn using this system.
- `user.csv` is the learner dataset of the model. It contains the history of the problems solved by the user.
- Tutor model here is the one that recommends problems to the user based on the problems solved by the user and the expert dataset. This is contained in the `recommend_problems` list in the Jupyter notebook.
- The interface here is the terminal, on which the recommended problems are displayed.

The algorithm used is K-Nearest Neighbours. Currently, the value of k is set to 10. The distance metric used is the Euclidean distance. 

### Remarks

Since, the dataset of training and testing is not available on the internet, math is used to calculate the distance between the user and the expert dataset. The problems are recommended based on the distance between the user and the expert dataset. The problems that are closest to the user are recommended to the user. As mentioned in the 'Solution Summary' document, the AI model can be trained using a larger dataset and increased parameter, in order to obtain accurate results. 
