SELECT date, (ai - chatgpt) AS us_diff
FROM {{ source('mage_demo', 'broken_dew_load_us_data') }}