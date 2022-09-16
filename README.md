# Netflix-Recommender

## About the project
In 2006 Netflix Lunch a competition with a prize of 1,000,000$ .
The mission was to improve Netflix's Recommender system.

## My Approach
In this project, I'll leverage deep learning for building a recommender system with 
the dataset of the competition.
Graph Neural Networks are shown to perform very well on missions like recommendation systems.
I will use the [LightGCN](https://arxiv.org/abs/2002.02126) model (2020) for this mission.


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
5) PyG

Several things that we learned in this project are:
1) PyTorch Geometric - library for graph neural networks (PyG).
2) Create a model that learn also with negative Samples.
3) Graph Neural Nets and Graph machine learning.
4) Stuff about recommendation systems like collaborative filtering and so on.
