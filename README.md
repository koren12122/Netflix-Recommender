# Netflix-Recommender

## About the project
Back in 2006, Netflix organized a competition with a grand prize of $1,000,000. The aim of the competition was to enhance the effectiveness of Netflix's Recommender system.

## My Approach
In this project, I will be leveraging deep learning to build a recommender system using the dataset from the competition. Graph Neural Networks have been shown to perform very well on tasks such as recommendation systems.
I will use the [LightGCN](https://arxiv.org/abs/2002.02126) model (2020) for this mission.


### Instructions:
1) download the file [movie_titles.csv](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data?select=movie_titles.csv).
2) download the file "combined_data_1.txt" from https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data?select=combined_data_1.txt.
3) run the script "data_fix.py".
4) delete all lines except the first 4500 in the file "movie_titles.csv". 

### Requirement:
1) python 3.9
2) torch 1.11.0
3) pandas 1.4.3
4) numpy 1.21.5
5) PyG

### Several things that we learned in this project are:
1) PyTorch Geometric - library for graph neural networks (PyG).
2) Create a model that learn also with negative Samples.
3) Graph Neural Nets and Graph machine learning.
4) Stuff about recommendation systems like collaborative filtering and so on.
