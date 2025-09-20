import snowflake.connector

# Set your Snowflake credentials
conn = snowflake.connector.connect(
    user='<YOUR_USER>',
    password='<YOUR_PASSWORD>',
    account='<YOUR_ACCOUNT>',
    warehouse='<YOUR_WAREHOUSE>',
    database='<YOUR_DATABASE>',
    schema='<YOUR_SCHEMA>'
)

cs = conn.cursor()
try:
    # Create table (optional, if not already created)
    with open("create_table.sql") as sql_file:
        cs.execute(sql_file.read())

    # Load data from CSV (simple example)
    # You can use Snowflake's PUT and COPY INTO commands for large files
    import csv
    with open("sample_data.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cs.execute(
                "INSERT INTO my_table (id, name, created_at) VALUES (%s, %s, %s)",
                (row['id'], row['name'], row['created_at'])
            )
finally:
    cs.close()
    conn.close()
