from pytrends.request import TrendReq

def load_data(country: str):
    # Specify your data loading logic here
    pt = TrendReq(hl="en-US", tz=360)

    # set the keyword & timeframe
    pt.build_payload(["chatgpt", "ai"], geo=country)

    # get the interest over time
    return pt.interest_over_time().reset_index()