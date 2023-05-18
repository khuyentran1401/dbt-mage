columns = df_1.columns
cols = list(filter(lambda x: df_1[x].dtype == float or df_1[x].dtype == int, columns))
x = df_1[cols[0]]
y = [df_1[cols[1]]]
