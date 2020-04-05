import csv

def data_reader(path, target):
    with open(path) as f:
        # auto config reader
        preview = f.read(1999)
        dialect = csv.Sniffer().sniff(preview)
        f.seek(0)
        # skip header
        if csv.Sniffer().has_header(preview):
            next(f)
        reader = csv.reader(f, dialect=dialect)
        while True:
            try:
                target.send(next(reader))
            except StopIteration:
                break

# coroutine wrapper
def coroutine(coro):
    def inner(*args, **kwargs):
        gen = coro(*args, **kwargs)
        next(gen)
        return gen
    return inner

@coroutine #pipeline final_part
def data_saver(path, header):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        while True:
            row = yield
            writer.writerow(row)

# biuld a filter
@coroutine
def filter_data(target, contains, position=0):
    while True:
        data = yield
        if contains in data[position]:
            target.send(data)

@coroutine
def filtrator(filter_predicate, target):
    while True:
        data = yield
        if filter_predicate(data):
            target.send(data)

def processing(path, target, *filters):
    header = ''
    with open(path) as f:
        header = f.readline()
    saver = data_saver(target, header.strip().split(','))
    target = saver
    for predicate in filters:
        filter_func = lambda x, v=predicate: v[0] in x[v[1]]
        target = filtrator(filter_func, target)

    data_reader(path, target)
    print("DONE")
    
    
if __name__=='__main__':
# read and filter data with some filters
  processing('car_data.csv', 'test.csv', ('B', 0), ('Green', 4), ('SL', 1))
