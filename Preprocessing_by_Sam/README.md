# DS504-Divvy-Project

### Input Files:

**Pre-Processing.ipynb** - must do...

  0) Download Data and move to DS504-Divvy-Project folder:
  
  https://drive.google.com/open?id=1cd77zrTO8QGUvvK6UasZQHjPym5Kg8SL

  1) Change your root path:
```python
root_path='/Users/SamLongenbach/Desktop/DS504/project2/DS504-Divvy-Project/'
os.chdir(root_path)
```

  2) Pick the station file for creating output matrices (ex. S_2013, S_2014_Q34, ... S_2017_Q34):
```python
STATION_DATA = S_2013.sort_values(by=['id'])
```

**chi_town.shp** - Shape file for Chicago plot

**chi_town.shx** - Shx file for Chicago plot

### Output Files:

**distance_matrix.csv**  - Distances btw ordered 2013 Stations

**station_locations.csv**  - 2013 Stations ordered by Id 

**time_matrix.csv**  - Time btw ordered 2013 Stations


