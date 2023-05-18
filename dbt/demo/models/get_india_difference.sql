SELECT date, (ai - chatgpt) AS india_diff
FROM {{ source('mage_demo', 'broken_dew_load_india_data') }}