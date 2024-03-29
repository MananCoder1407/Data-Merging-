import pandas as pd;
import numpy as np;

data = pd.read_csv('dwarf_stars.csv');

final_data = data.dropna();

solar_radius = [];
solar_mass = [];

for i in final_data['Radius'].tolist():
    val = float(i) * 0.102763;
    solar_radius.append(val);
    
for i in final_data['Mass'].tolist():
    val = float(i) * 0.000954588;
    solar_mass.append(val);
    
dict = {'solar_mass' : solar_mass, 'solar_radius' : solar_radius};

df = pd.DataFrame(dict);

df.to_csv('/Users/mananjain/Desktop/web scraping 2/solMR.csv');

merged_csv = pd.concat(
    map(pd.read_csv, ['bright_stars.csv', 'solMR.csv']), ignore_index=True);

print(merged_csv)