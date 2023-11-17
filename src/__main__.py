# Import necessary libraries/modules
#general libs
import os
import time

#computing libs
import numpy as np
import pandas as pd

#ml model libs
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import SimpleImputer


# plotting libs
import matplotlib.pyplot as plt
import seaborn as sns



file_path = "data/internal/data.csv"
data = pd.read_csv(file_path,
                  sep=",")

#movies
movies = data['Movie'].unique()

#average ratings
average_ratings = data.groupby('Movie')['Rating'].mean().reset_index()

# Collaborative Filtering Algorithm
user_movie_matrix = data.pivot_table(index='User', columns='Movie', values='Rating', fill_value=0)

cosine_sim = cosine_similarity(user_movie_matrix.T)
data_cos = pd.DataFrame(cosine_sim, columns=movies, index=movies)


def get_top_indices(df, n):
    # Flatten the DataFrame and sort the values
    flatten_values = df.values.flatten() 
    sorted_values = sorted(flatten_values, reverse=True)
    
    # Get the unique indices of the n largest values
    unique_indices = df[df.isin(sorted_values[:n] ).values].dropna().index.unique()
    return unique_indices

def recommend_movies(user):
    movie_ratings = user_movie_matrix.loc[user]
    watched_list = movie_ratings[movie_ratings > 0]
    
    mod_data_cos = data_cos.drop(watched_list.index, axis = 1)
    
    recc_list = []
    for index, value in watched_list.items():
        weight = value/watched_list.sum()
        recc_list.append(mod_data_cos.loc[index]*(1+weight))
        
        final_df = pd.concat(recc_list, axis=1)
    return get_top_indices(final_df, 3)

def main():
    user_name = input("Please enter your name: ").upper()

    # Check if the user exists in the data
    if user_name not in user_movie_matrix.index:
        print(f"User {user_name} not found !!!")
        time.sleep(0.1)
        print("Recommending popular movies.")
        time.sleep(1)
        popular_movies = average_ratings.sort_values(by='Rating', ascending=False)['Movie']
        recommendations = list(popular_movies.head(3))

    else :
        recommendations = list(recommend_movies(user_name))
        print(f"Recommended movies for {user_name}")

    time.sleep(1)
    for mv in recommendations :
            print(mv)

    print("\n")



# Check if the script is run as the main program
if __name__ == "__main__":
    try:
        # load data
        #file_path = "../data/internal/data.csv"
        
        while True:
            # Call the main function
            main()

    except KeyboardInterrupt:
        print('Exiting ...')


