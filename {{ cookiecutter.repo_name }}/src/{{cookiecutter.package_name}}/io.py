import os
import pandas as pd


class IO:
    local_data_path = '.'

    def __init__(self, local_data_path: str):
        """
        Constructor that can set the data path from where we will access local data..

        Args:
        """
        self.local_data_path = local_data_path

    def load_cleaned_file(self, download_always: bool = True):
        """
        Example function that loads a file from the data lake and returns a dataframe.
        """

        df = pd.read_csv(local_path,
                         dtype={'Well_name': 'category'},
                         parse_dates=['start'])
        return df
