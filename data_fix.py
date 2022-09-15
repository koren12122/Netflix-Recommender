from torch_geometric.data import download_url, extract_zip

def download_MovieLens():
    url = 'https://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
    extract_zip(download_url(url, '.'), '.')

def fix_rating_template():
    # After download netflix dataset (partial)
    # https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data?select=combined_data_1.txt
    extract_zip("combined_data_1.txt.zip", '.')
    file = open("combined_data_1.txt", 'r')
    read = file.readlines()
    new_file = open("new_file.txt", "w")
    curr_number = 0
    new_file.write("userId,movieId,rating,data" + '\n')
    for line in read:
        if len(line[:-2]) < 7:   # if a number
            print(line[:-2])
            curr_number = int(line[:-2])
            continue
        new_file.write(str(curr_number) + ',' + line)

# need to download https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data?select=movie_titles.csv
# movie list and delete all line expect first 4500

def fix_movies_validation():
    file = open("movie_titles.csv", 'r')
    read = file.readlines()
    new_file = open("new_movie_file.txt", "w")
    psik_counter = 0
    new_word = ''
    new_file.write("movieId,year,title" + '\n')
    for line in read:
        stripped_line = line.strip()
        psik_counter = 0
        for letter in str(stripped_line):
            if letter == ",":
                psik_counter += 1
            if psik_counter == 3:
                break
            new_word += letter
        print(new_word)
        new_file.write(new_word + '\n')
        new_word = ''

def fix_rating_file():
    file = open("new_file.txt", 'r')
    read = file.readlines()
    new_file = open("new_rating_file.txt", "w")
    counter = 0
    new_file.write("movieId,userId,rating,data" + '\n')
    for line in read:
        counter += 1
        if counter == 1:
            continue
        new_file.write(line)

def sample_mini_dataset():
    """"
    create file with much less user-item connections
    """
    file = open("new_rating_file.txt", 'r')
    read = file.readlines()
    new_file = open("new_mini_rating_file.txt", "w")
    counter = 0
    new_file.write("movieId,userId,rating,data" + '\n')
    for line in read:
        counter += 1
        if counter % 220 == 0:
            new_file.write(line)

download_MovieLens()
fix_rating_template() # only after download https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data?select=combined_data_1.txt
fix_movies_validation()
fix_rating_file()
sample_mini_dataset()