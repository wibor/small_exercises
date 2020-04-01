# TODO
#  0. get all CSV files in folder
#  1. read with lazy iterator for file, create namedtuple from row, parse data
#  2. combine data to one namedtuple

def combine_header(filenames):
    def get_header(filename):
        with open(filename) as f:
            return f.readline().strip().split(',')
    header = []
    #TODO refactor without comprehension here
    [[header.append(column_name) for column_name in get_header(filename) if column_name not in header] for filename in filenames]
    return header
    
def parse(item):
    #TODO
    return  item
    
def get_row(filename):
    with open(filename) as f:
        f.readline()
        csv_reader = csv.reader(f, delimiter=',', quotechar = '"')
        yield from csv_reader
        
Combine = namedtuple('Combine', combine_header(filenames))

def combined_tuple_gen(filenames):
    gens = []
    for filename in filenames:
        gens.append(get_row(filename))

    while True:
        row = []
        try:
            for gen in gens:
                chunk = next(gen)
                for item in chunk:
                    if item not in row:
                        row.append(parse(item))
            yield Combine(*row)
        except StopIteration:
            print('ALL DATA PROCESSED')
            break

g = combined_tuple_gen(filenames)

for _ in range(5):
    print(next(g))
print()

import itertools
for row in itertools.islice(g, 5):
    print(row)
print()
