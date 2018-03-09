from data_cleaning_and_preparation.clean import remove_unwanted_rows, remove_unwanted_columns

remove_unwanted_rows("movie_metadata.csv")
remove_unwanted_columns("clean_movie_data.csv")
