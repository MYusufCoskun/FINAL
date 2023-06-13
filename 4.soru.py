import pandas as pd

yaslar = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 16
c2 = 22
iterations = 4

columns = ['xi', 'c1', 'c2', 'Distance 1', 'Distance 2', 'Nearest Cluster', 'New Centroid']
df = pd.DataFrame(columns=columns)

for i in range(iterations):
    temp_df = pd.DataFrame(columns=columns)

    for xi in yaslar:
        distance1 = abs(xi - c1)
        distance2 = abs(xi - c2)

        if distance1 < distance2:
            nearest_cluster = 1
        else:
            nearest_cluster = 2

        temp_df = pd.concat([temp_df, pd.DataFrame({'xi': [xi], 'c1': [c1], 'c2': [c2], 'Distance 1': [distance1],
                                                    'Distance 2': [distance2], 'Nearest Cluster': [nearest_cluster],
                                                    'New Centroid': [None]})])

    c1 = temp_df[temp_df['Nearest Cluster'] == 1]['xi'].mean()
    c2 = temp_df[temp_df['Nearest Cluster'] == 2]['xi'].mean()

    temp_df.loc[temp_df['Nearest Cluster'] == 1, 'New Centroid'] = c1
    temp_df.loc[temp_df['Nearest Cluster'] == 2, 'New Centroid'] = c2

    df = pd.concat([df, temp_df])

    print(f"Iteration {i+1}:")
    print()
    print(temp_df.to_string(index=False))
    print()

pd.set_option('display.max_rows', None)
print(df.to_string(index=False))
print("")
print("Örnekteki 19 kişinin hangi kümeye ait oldukları:")

for xi, nearest_cluster in zip(yaslar, df['Nearest Cluster']):
    cluster_name = 'c1' if nearest_cluster == 1 else 'c2'
    print(f"{xi} yaşındaki kişi {cluster_name} kümesindedir.")
