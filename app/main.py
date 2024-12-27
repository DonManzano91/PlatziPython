import utils
import read_csv
import charts
import pandas as panda



def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''

  df = panda.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages) 

  country = input('Type Country => ')
  print(country)

  data = read_csv.read_csv('data.csv')  #Esta esta viva solo para que no truene el programa
  results = utils.population_by_country(data, country)

  if len(results) > 0:
    country = results[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()