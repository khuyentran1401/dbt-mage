import pandas as pd


@data_loader
def load_data(*args, **kwargs):
    url = "https://gist.githubusercontent.com/khuyentran1401/d492492d1ba73dacf77b65f468420f06/raw/39adfc1f65a76aa4f09b445267bff8292bdd4f3a/us_chatgpt_ai.csv"
    return pd.read_csv(url)


@test
def test_output(output, *args) -> None:
    assert output["chatgpt"].dtype == object
    assert output["ai"].dtype == int
