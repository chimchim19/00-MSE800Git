"""
Week 3 - Activity 3: using parquet  format for big data
MSE800
270765080 Kristine Gonzalvo 
Develop a Python project using an object-oriented (OO) approach to convert large datasets 
into Parquet format. Then, compute the maximum, minimum, average, and absolute values 
for each column in the dataset. (see link to download a big numerical data in csv format 
from link: https://archive.ics.uci.edu/datasets)
Sample: https://archive.ics.uci.edu/dataset/332/online+news+popularity
"""

import pandas as pd

class FileProcessing:

    def __init__(self, import_file):
        # initialize with the path to the file to be loaded
        self.import_file = import_file
        self.dataframe = None

    def load_csv_file(self):
        # read the input CSV file into a Pandas dataframe
        self.dataframe = pd.read_csv(self.import_file)
        print("\nLoading file...")

    def convert_to_parquet(self, destination_file):
        # convert/write the dataframe to a parquet file
        self.dataframe.to_parquet(destination_file)
        print(f"\nSuccessfully converted '{self.import_file}' to '{destination_file}' .")

    def process_parquet(self, parquet_file):
        # load the Parquet file into a Pandas dataframe
        df_file = pd.read_parquet(parquet_file)

        if df_file.empty:
            print("\nParquet file is empty.")
            return None
        
        print(f"\nSuccessfully loaded {parquet_file} with {df_file.shape[0]} rows and {df_file.shape[1]} columns.")

        # subset of dataframe with the numeric columns only
        df_numbers = df_file.select_dtypes(include=['number'])

        # build into a new dataframe the max, min, average, and absolute values
        df_statistics = pd.DataFrame({
            'Maximum': df_numbers.max(),
            'Absolute_max': df_numbers.abs().max(),
            'Minimum': df_numbers.min(),
            'Absolute_min': df_numbers.abs().min(),
            'Average': df_numbers.mean(),
            'Absolute_ave': df_numbers.abs().mean()
        })
        return df_statistics
        

if __name__ == "__main__":

    file_path_csv = "Week3/Activity3/OnlineNewsPopularity.csv"
    file_path_parquet = "Week3/Activity3/OnlineNewsPopularity.parquet"
    print("*" * 20)

    # instantiate
    file_handler = FileProcessing(file_path_csv)

    # load source CSV file
    file_handler.load_csv_file()

    # convert into Parquet file format
    file_handler.convert_to_parquet(file_path_parquet)

    # read Parquet file and compute for column statistics
    df_output = file_handler.process_parquet(file_path_parquet)
    print("\n ----- Column Statistics -----")
    print(df_output)
    print("\n ----- E N D -----")