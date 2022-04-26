"""So, why do we want to use a database instead of a file?  Here's an example
of a (relatively) simple SQL query:
SELECT melon_type,
       COUNT(*) AS num_melons,
       MIN(price) AS cheapest,
       AVG(price) AS avg_price
FROM melons
WHERE price < 5
GROUP BY melon_type
HAVING COUNT(*) > 1
ORDER BY num_melons DESC;

Here's what that would look like using Python and a .csv file:"""

from csv import DictReader
from pprint import pprint

# get all melons from file
with open('melons.csv') as f:
    reader = DictReader(f)
    melons = []

    # cast data types
    for melon in reader:
        melon['id'] = int(melon['id'])
        melon['price'] = float(melon['price'])

        if melon['seedless'] == 'TRUE':
            melon['seedless'] = True
        else:
            melon['seedless'] = False

        # add the melon dict to the list
        melons.append(melon)

# there are several pprints sprinkled throughout, feel free to uncomment them
# to see what the data structures look like at different points in the code.
# pprint(melons)

# start building the query
melon_query = {}

for melon in melons:
    ### WHERE price < 5
    if melon['price'] >= 5:
        continue

    ### SELECT melon_type
    m_type = melon['melon_type']

    ### GROUP BY melon_type
    if m_type not in melon_query:
        melon_query[m_type] = {'num_melons': 0,
                               'cheapest': None,
                               'avg_price': 0}

    ### SELECT COUNT(*) as num_melons
    melon_query[m_type]['num_melons'] += 1

    ### SELECT MIN(price) as cheapest
    if (melon_query[m_type]['cheapest'] is None or
        melon['price'] < melon_query[m_type]['cheapest']):
       melon_query[m_type]['cheapest'] = melon['price']

    ### SELECT AVG(price) as avg_price
    melon_query[m_type]['avg_price'] += melon['price']

# pprint(melon_query)

# continue building query
low_counts = []

for m_type, results in melon_query.items():
    ### HAVING COUNT(*) > 1
    if results['num_melons'] < 2:
        low_counts.append(m_type)

    ### SELECT AVG(price) as avg_price #(continued)
    results['avg_price'] /= results['num_melons']

### HAVING COUNT(*) > 1 #(continued)
for m_type in low_counts:
    melon_query.pop(m_type)

# pprint(melon_query)

# get query results as a list
melon_results = list(melon_query.items())

### ORDER BY num_melons DESC
melon_results.sort(key=lambda r: r[1]['num_melons'], reverse=True)


# format and output results
print('melon_type | num_melons | cheapest | avg_price')
print('-----------+------------+----------+-------------------')

for result in melon_results:
    melon_type = result[0]
    spaces = ' ' * (len('melon_type') - len(melon_type))
    print(f'{melon_type}{spaces}', end=' | ')

    num_melons = str(result[1]['num_melons'])
    spaces = ' ' * (len('num_melons') - len(num_melons))
    print(f'{spaces}{num_melons}', end=' | ')

    cheapest = str(result[1]['cheapest'])
    spaces = ' ' * (len('cheapest') - len(cheapest))
    print(f'{spaces}{cheapest}', end=' | ')

    avg_price = result[1]['avg_price']
    print(avg_price)
