import pandas as pd


@data_loader
def load_data_from_api(*args, **kwargs):
    url = "https://gist.githubusercontent.com/khuyentran1401/a9d89e42624c0a3ec78df5e824c4806a/raw/98fb02ed0150a3e029e404da45e5bda680409aa0/india_chatgpt_ai.csv"
    data = pd.read_csv(url)
    return data


@test
def test_output(output, *args) -> None:
    assert output["chatgpt"].dtype == object
    assert output["ai"].dtype == int
