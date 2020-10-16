import pandas as pd
import numpy as np

listings = pd.read_csv('listings.csv')

# filter only necessary columns
listings = listings[
                    ['id',
                    'neighbourhood_cleansed',
                    'latitude',
                    'longitude',
                    'room_type',
                    'accommodates',
                    'beds',
                    'price',
                    'review_scores_rating',
                    'review_scores_accuracy',
                    'review_scores_cleanliness',
                    'review_scores_checkin',
                    'review_scores_communication',
                    'review_scores_location',
                    'review_scores_value']
            ]

# converting price column to float
listings['price'] = listings['price'].str.replace('$','').str.replace(',','').astype(float)

# removing any rows with na
listings = listings.dropna()