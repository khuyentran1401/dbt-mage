SELECT us.date, us_diff, india_diff
FROM {{ ref('get_us_difference') }} AS us
JOIN {{ ref('get_india_difference') }} AS india 
ON us.date = india.date
