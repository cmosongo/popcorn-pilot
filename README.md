# popcorn-pilot
popcorn-pilot is a simple movie recommendation system based of a challenge.

The purpose of the challenge is to develop a system providing more accurate and personalized movie recommendations. The solution will not only increase user engagement but also improve subscription renewals, making a significant impact in the world of entertainment.

## Challenge Breakdown
The challenge involves the use of pre-existing user data and a current movie catalog to deliver personalized movie recommendations and can be chategorized in the following steps

*[Data Analysis]()*
- Data Cleaning
- Value extraction

*[Algorithm Development]()*
- Development of  a movie recommendation algorithm.
- Handle irregular or incomplete data.
- Fallback system.

*[User Interface]()*
- CLI for interaction.
- User-friendly output.


### Data Analysis
- Data Cleaning

The data cleaning process revealed some flaw in the raw data.

 - The list of unique movies included  'Matrix' and 'The Matrix' which were combined as the was only one entry of the movie 'Matrix'
 
 - Users were converted to uppercase to limit any erronoes outcomes, and the strings treated as unique entries or IDs
 
 - The ratings had several different values but were required to be intergers  but were in several different formats. All none integer values were converted to `NaNs` and later filled using the median values of all ratings. The median values of all ratings seemed to mimic the true representation  of the sample as compared to the median of indiviual moveie ratings 

- Value extraction



From the data we can extract some valuable insights

Users

The distribution of movies by users is as seen below:

![Distribution of Movies by User](images/dist_movies.png).


### Algorithm Development

The algorithm used relies on cosine similarity. 

Cosine similarity is a metric that measures the cosine of the angle between two vectors. i.e it compares the similarity between the preferences of users. 

Each user and movie are represented as vectors in a high-dimensional space based on their ratings. The cosine similarity between these user and movie vectors is calculated, and movies with the highest cosine similarity to a user's preferences are recommended. 

*Slight Modification*

Given that cosine simiarity generates a matrix of siliraities based of historical ratings for all movies and ratings, I had to adjust for individual preferences of the user. I adjustd by weights depending on the ratings assigned to a paticular mvies and consequently, to the cosine similarity of its recommendations 

Essentially, the algorithm suggests movies that align closely with a user's historical preferences, making it a useful method for personalized movie recommendations

- Fallback system.

The fallback system relies on the movies with the highest avarage ratings and simply recoomends three of the best, by rating. An alternative might be the movies with the highest similarity value in the csine similarity matrix.

### User Interface
- CLI for interaction.

When running the interface displays 

```python 
Please enter your name: <user name>

```
Example
```python 
Please enter your name: dave
```
And the output is as follows if the user exists 

```python 
Recommended movies for DAVE
Star Wars
The Godfather
Pulp Fiction
```

ora s follows if the user does not exists 

```python 
User CHARLIE not found !!!
Recommending popular movies.
The Godfather
Titanic
Star Wars
```


