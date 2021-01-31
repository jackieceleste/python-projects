# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# updated damages function
updated_damages = []
def update_damages(lst):
  for cost in lst:
    if cost[-1] == "M":
      cost = cost[:-1]
      cost = float(cost) * 1000000
      updated_damages.append(cost)
    elif cost[-1] == "B":
      cost = cost[:-1]
      cost = float(cost) * 1000000000
      updated_damages.append(cost)
    else:
      updated_damages.append(cost)
update_damages(damages)
#print(updated_damages)


# dictionary function for hurricane info
def hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane_info = {}
  for i in range(0, len(names)):
    hurricane_info[names[i]] = {
      'Name': names[i],
      'Month': months[i],
      'Year': years[i],
      'Max Sustained Wind': max_sustained_winds[i],
      'Areas Affected': areas_affected[i],
      'Damage': damages[i],
      'Death': deaths[i]
      }
  return hurricane_info
hurricane_info = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
#print(hurricane_info)


#organize hurricanes by year
def sort_by_year(names, years):
  for i in range(0, len(names)):
    hurricane_info[years[i]] = hurricane_info[names[i]]
    del hurricane_info[names[i]]
  return(hurricane_info)
hurricane_info = sort_by_year(names, years)
#print(hurricane_info)


#count how often each area is listed as an affected area
#return results in a dictionary 
def count_areas_affected(hurricane_info):
  times_areas_affected = {}
  all_areas = []
  for lst in hurricane_info:
    for area in lst:
      all_areas.append(area)
  for area in all_areas:
      times_areas_affected = dict((area, all_areas.count(area)) for area in all_areas)
  return times_areas_affected
times_areas_affected = count_areas_affected(areas_affected)
#print(times_areas_affected)


#find area affected by the most hurricanes
#find how often this area was hit
def area_most_affected(times_areas_affected):
  max_key = max(times_areas_affected, key=times_areas_affected.get)
  max_value = max(times_areas_affected.values())
  most_affected_area = [max_key, max_value]
  most_affected_area = {
  max_key: max_value
  }
  return most_affected_area
most_affected_area = area_most_affected(times_areas_affected)
#print(most_affected_area)


#find hurricane with greatest number of deaths
#find number of deaths it caused
def find_deadliest_hurricane(hurricane_info):
  deadliest_hurricane = {}
  max_value = max(val['Death'] for val in hurricane_info.values())
  for val in hurricane_info.values():
    if val['Death'] == max_value: 
      deadliest_name = val['Name']
  deadliest_hurricane = {'Name': deadliest_name, 'Death': max_value}
  return deadliest_hurricane
deadliest_hurricane = find_deadliest_hurricane(hurricane_info)
#print(deadliest_hurricane)


#rate hurricanes on mortality scale
def create_mortality_ratings(hurricane_info):
  mortality_ratings = {}
  rating0 = []
  rating1 = []
  rating2 = []
  rating3 = []
  rating4 = []
  for val in hurricane_info.values():
    if val['Death'] == 0:
      rating0.append(val['Name'])
    elif val['Death'] > 0 and val['Death'] <= 100:
      rating1.append(val["Name"])
    elif val['Death'] > 100 and val['Death'] <= 500:
      rating2.append(val['Name'])
    elif val['Death'] > 500 and val['Death'] <= 1000:
      rating3.append(val['Name'])
    else:
      rating4.append(val['Name'])
  mortality_ratings = {
    0: rating0, 
    1: rating1, 
    2: rating2, 
    3: rating3, 
    4: rating4
    }
  return mortality_ratings
mortality_ratings = create_mortality_ratings(hurricane_info)
#print(mortality_ratings)





    