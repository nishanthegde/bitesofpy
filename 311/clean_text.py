# -*- coding: utf-8 -*-v

import os
from pathlib import Path
import string
import sys
from urllib.request import urlretrieve

from zipfile import ZipFile

import pandas as pd

# import stop_words
from tf_idf import TFIDF

stop_words = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "you're",
    "you've",
    "you'll",
    "you'd",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "she's",
    "her",
    "hers",
    "herself",
    "it",
    "it's",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "that'll",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "don't",
    "should",
    "should've",
    "now",
    "d",
    "ll",
    "m",
    "o",
    "re",
    "ve",
    "y",
    "ain",
    "aren",
    "aren't",
    "couldn",
    "couldn't",
    "didn",
    "didn't",
    "doesn",
    "doesn't",
    "hadn",
    "hadn't",
    "hasn",
    "hasn't",
    "haven",
    "haven't",
    "isn",
    "isn't",
    "ma",
    "mightn",
    "mightn't",
    "mustn",
    "mustn't",
    "needn",
    "needn't",
    "shan",
    "shan't",
    "shouldn",
    "shouldn't",
    "wasn",
    "wasn't",
    "weren",
    "weren't",
    "won",
    "won't",
    "wouldn",
    "wouldn't",
]

# local = os.getcwd()
TMP = Path(os.getenv("TMP", "/tmp"))

# TMP = Path(os.getenv("TMP", local))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"

df_samples = pd.read_pickle(TMP / "samples.pkl")


def get_df_column(column_name):
    return df_samples[[column_name]].rename(columns={column_name: "text"})


def _setup():
    data_zipfile = '311-data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(TMP)


_setup()


def load_data():
    # Load the text and populate a Pandas Dataframe
    # The order of the sample text strings should not be changed
    # Return the Dataframe with the index and 'text' column
    df = pd.read_csv(f'{TMP}/samples.txt', index_col=None, header=0)
    return df


def strip_url_email(x_df):
    # Strip all URLs (http://...) and Emails (somename@email.address)
    # The 'text' column should be modified to remove
    #   all URls and Emails
    x_df['text'] = x_df['text'].replace(to_replace=r'(?i)http\S+', value='', regex=True)
    x_df['text'] = x_df['text'].replace(to_replace=r'\S+@\S+', value='', regex=True)
    return x_df


def to_lowercase(x_df):
    # Convert the contents of the 'text' column to lower case
    # Return the Dataframe with the 'text' as lower case
    x_df['text'] = x_df['text'].str.lower()
    return x_df


def strip_stopwords(x_df):
    # Drop all stop words from the 'text' column
    # Return the Dataframe with the 'text' stripped of stop words
    x_df["text"] = x_df["text"].str.split()
    x_df['text'] = x_df['text'].apply(lambda x: [word for word in x if word not in stop_words])
    x_df["text"] = x_df["text"].str.join(" ")
    return x_df


def strip_non_ascii(x_df):
    # Remove all non-ascii characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of non-ascii characters
    x_df['text'] = x_df['text'].replace(to_replace=r'[^\x00-\x7F]+', value='', regex=True)
    return x_df


def strip_digits_punctuation(x_df):
    # Remove all digits and punctuation characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of all digit and punctuation characters
    x_df['text'] = x_df['text'].replace(to_replace=r'[^\w\s]', value='', regex=True)
    x_df['text'] = x_df['text'].replace(to_replace=r'[\_]', value='', regex=True)
    x_df['text'] = x_df['text'].replace(to_replace=r'[\d]', value='', regex=True)
    return x_df


def calculate_tfidf(x_df):
    # Calculate the 'tf-idf' matrix of the 'text' column
    # Return the 'tf-idf' Dataframe
    tfidf_obj = TFIDF(x_df["text"])
    return tfidf_obj()


def sort_columns(x_df):
    # Depending on how the earlier functions are implemented
    #   it's possible that the order of the columns may be different
    #   Sort the 'tf-idf' Dataframe columns
    #   This ensure the tests are compatible
    x_df = x_df.reindex(sorted(x_df.columns), axis=1)
    return x_df

def get_tdidf():
    # Pandas’ pipeline feature allows you to string together
    # Python functions in order to build a pipeline of data processing.
    # Complete the functions above in order to produce a 'tf-idf' Dataframe
    # Return the 'tf-idf' Dataframe
    df = (
        load_data()
            .pipe(strip_url_email)
            .pipe(to_lowercase)
            .pipe(strip_stopwords)
            .pipe(strip_non_ascii)
            .pipe(strip_digits_punctuation)
            .pipe(calculate_tfidf)
            .pipe(sort_columns)
    )
    return df


# def main():
#     print('thank you for looking after my family...')
#     # print(get_df_column("text"))
#     # print(get_df_column("strip_url_email"))
#     # print(load_data())
#     # print(strip_url_email(load_data()))
#     # d = pd.DataFrame(
#     #             [
#     #                 "i me my myself we our ours ourselves you",
#     #                 "i me my myself we our ours ourselves you hello world",
#     #                 "lorem ipsum dolor sit amet, consectetur adipiscing elit",
#     #             ]
#     #     ,columns = ["text"]
#     # )
#     # print(strip_stopwords(d))
#     print(get_tdidf())
#
#
# if __name__ == '__main__':
#     main()
