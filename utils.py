import pandas as pd

def convert_to_dataframe(tweets):

    data = {
        "Generated Tweets": tweets
    }

    df = pd.DataFrame(data)

    return df