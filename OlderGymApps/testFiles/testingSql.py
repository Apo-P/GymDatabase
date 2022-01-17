import sqlite3

#simple tutorial https://datatofish.com/create-database-python-using-sqlite3/
# 
# https://www.sqlitetutorial.net/sqlite-python/creating-database/
# https://www.sqlitetutorial.net/sqlite-python/create-tables/

connection = sqlite3.connect("test.db")
cursor = connection.cursor()


def execute_sql(cursor,sql):
    """Will execute the sql command given at the cursor given. It will return the cursor so we can do a quick fetch after the querry (i.e. execute_sql(cursor,sql).fetchall())"""

    return cursor.execute(sql)

execute_sql(cursor,"""DROP TABLE IF EXISTS products;""")
execute_sql(cursor,'''
            CREATE TABLE IF NOT EXISTS products 
            ([product_id] INTEGER PRIMARY KEY, 
            [product_name] TEXT)
            ;''')

execute_sql(cursor,"""DROP TABLE IF EXISTS prices;""")
execute_sql(cursor,'''
            CREATE TABLE IF NOT EXISTS prices
            ([product_id] INTEGER PRIMARY KEY, 
            [price] INTEGER)
            ;''')

execute_sql(cursor,'''
            INSERT INTO products (product_id, product_name) VALUES (1,'Computer'),(2,'Printer'),(3,'Tablet'),(4,'Desk'),(5,'Chair')
            ;''')

execute_sql(cursor,'''
            INSERT INTO prices (product_id, price) VALUES (1,800),(2,200),(3,300),(4,450),(5,150)
            ;''')

connection.commit()

results=execute_sql(cursor,'''
        SELECT
        a.product_name,
        b.price
        FROM products a
        LEFT JOIN prices b ON a.product_id = b.product_id
        ;''').fetchall()
print(results)
connection.close()