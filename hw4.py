'''
This file is used to test the data type,NAN value and the numbers of the roll
Date: 11/6/2019
Author: Siting Wang

typePerColumnsVerify: test the is one type of the columns satisfy the desired type;
typeMeasureAll: go over every column
testNan: test if one column has NAN value and return the position of the value
VarifyNumberColumn:verify if the dataframe has at least one value;
'''
import numpy as np
import pandas as pd

df = pd.read_csv("https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv")

def type_per_columns_verify(df_column, desired_type):
    '''
    # :param df_column: the column you want to test for consistence
    # :param desired_type: Type
    # :return:If the Column's data type is consistent return true;else return false
    '''
    for data_in_column in df_column:
        if type(data_in_column) != desired_type:
            print(data_in_column)
            print(type(data_in_column))
            return False
        else:
            return True


def type_measure_all(data_frame):
    '''
    # :param data_frame: Data frame to be tested
    # :return: None
    '''


    for col in data_frame.columns:

        if type(df[col][1]) == str:
            type_name = str
        else:
            type_name = df[col][1].dtype

        if type_per_columns_verify(df[col], type_name):
            print("In columns %s, the column type is %s, it's consistant" % (col, type_name))
        else:
            print("In columns %s, the column type is %s, it's not consistant" % (col, type_name))


type_measure_all(df)

def test_nan(df_col):
    '''
    :param df_col: The column of a dataFrame
    :return: If there is NAN value in the column
    '''
    for i in range(len(df_col)):
        data_in_col = df_col[i]
        if np.isnan(data_in_col):
            print('NAN value at %d'%i)

test_nan(df['birthyear'])

def varify_number_column(data_frame):
    '''
    # :param data_frame: dataFrame to be tested
    # :return: if the data frame has over 1 column
    '''
    if data_frame.shape[1] >= 1:
        print("The data frame has at least one roll")
    return True

varify_number_column(df)
