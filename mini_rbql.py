import csv, re
input_reader = csv.reader(open('input.csv'))
query = input('Please enter a query. Example: SELECT a1, a2 WHERE a2 != \'foobar\'\n> ')
query = re.sub('(?<=[^a-zA-Z0-9_])a([0-9]+)', r'row[\1]', query) # Replaces a1 with row[1], a2 with row[2], etc
query = re.sub('SELECT', '', query, flags=re.IGNORECASE)
query_parts = re.split('WHERE', query, flags=re.IGNORECASE)
select_part = query_parts[0]
where_part = query_parts[1] if len(query_parts) > 1 else 'True'
main_loop = '''
for NR, row in enumerate(input_reader):
    row.insert(0, NR)
    if ({}):
        print(','.join(str(v) for v in [{}]))
'''.format(where_part, select_part)
exec(main_loop)
