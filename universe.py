search_engines = ['Yeehaw',
'NSM',
'Dont Ask',
'B9',
'Googol']
queries = [
'Yeehaw',
'Yeehaw',
'Googol',
'B9',
'Googol',
'NSM',
'B9',
'NSM',
'Dont Ask',
'Googol']

def what_engines(engines, queries):
    remaining = set(engines)
    result = []

    for index, query in enumerate(reversed(queries)):
        if index == len(queries) - 1:
            if query in remaining:
                remaining.remove(query)

            if len(remaining) == 0:
                result.insert(0, queries[0])
            else:
                result.insert(0, list(remaining)[0])

        elif len(remaining) > 1 and query in remaining:
            remaining.remove(query)

        elif len(remaining) == 1 and query in remaining:
            result.insert(0, query)
            remaining = set(queries)

    return result

print(what_engines(search_engines, queries))
print(what_engines(['G', "B", "D", "A"], "GDA"))
