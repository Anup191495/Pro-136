import pandas as pd

df = pd.read_csv("cv.csv")

star_names = df['Star_name'].tolist()
mass_values = df['Mass'].tolist()
radius_values = df['Radius'].tolist()
distance_values = df['Distance'].tolist()

star_data_list = []

for i in range(len(star_names)):
    star_data_list.append({
        'Star_name': star_names[i],
        'Mass': mass_values[i],
        'Radius': radius_values[i],
        'Distance': distance_values[i]
    })

print(star_data_list)

