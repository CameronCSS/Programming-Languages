import sqlite3

try:
    conn = sqlite3.connect('PY4E.sqlite')
    cur = conn.cursor()

    # Query to list all tables in the DB
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    if tables:
        print("Tables in the database:")
        for table in tables:
            print(table[0])
    else:
        print("No tables found in the database.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# Delete table if we have already run this code
cur.execute(
    '''
    DROP TABLE IF EXISTS Counts
    ''')

# Create the Counts table
cur.execute(
    '''
    CREATE TABLE Counts (org TEXT, count INTEGER)
    ''')
print(f"Counts table created")

filename = input('Enter file name: ')
if (len(filename) < 1):
    filename = 'mbox-short.txt'

handle_file = open(filename)
for line in handle_file:
    # Skip the files that Dont start with From: 
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')
    org = domain[1]

    # Find that org in our DB
    cur.execute('''
    SELECT count FROM  Counts WHERE org = ?
    ''', (org,))

    row = cur.fetchone()

    # If there are no records for that org, insert that org and set count to 1
    if row is None:
        cur.execute('''
        INSERT INTO Counts (org, count) 
            VALUES (?, 1)
        ''', (org,))
    else:
        cur.execute('''
        UPDATE Counts SET count = count + 1 WHERE org = ?
        ''', (org,))
    conn.commit()

sqlstr = ''' 
SELECT
    org,
    count
FROM
    Counts
ORDER BY
    count DESC
LIMIT 10
'''

# Print the org and their count
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])


cur.close()
