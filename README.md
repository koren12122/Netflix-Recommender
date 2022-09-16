# Netflix-Recommender

## About the project
In 2006 Netflix Lunch a competition with a prize of 1,000,000$ .
The mission was to improve Netflix's Recommender system.

## My Approach
In this project i'll levarage deep learning for building a recommender system with 
the dataset of the competition.
Graph Neural Netwoks are showen to perform very well on missions like recomendation systems.
I will use the LightGCN model (2020) for this mission


Instructions:
1) download the file "movie_titles.csv" from https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data?select=movie_titles.csv.
2) download the file "combined_data_1.txt" from https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data?select=combined_data_1.txt.
3) run the script "data_fix.py".
4) delete all lines expect first 4500 in the file "movie_titles.csv". 

Requinment:
1) python 3.9
2) torch 1.11.0
3) pandas 1.4.3
4) numpy 1.21.5
