if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from pytrends.request import TrendReq


@custom
def transform_custom(data, *args, **kwargs):
    """
    Args:
        data: The output from the upstream parent block (if applicable)
        args: The output from any additional upstream blocks

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here

    pt = TrendReq(hl="en-US", tz=360)

    # set the keyword & timeframe
    pt.build_payload(["chatgpt", "ai"], geo='IN')

    # get the interest over time
    return pt.interest_over_time()

