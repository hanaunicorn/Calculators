# Store the table data as a dictionary of table names and their rows
tables = {}

def dojob(sql):
    global tables

    # Split the SQL command into parts
    parts = sql.strip().split()

    if parts[0].lower() == "create":
        # Create an empty list for the table to store rows
        tables[parts[2]] = []

    elif parts[0].lower() == "insert":
        table = parts[2]
        # Check if the table has reached its maximum capacity of 3 rows
        if len(tables.get(table, [])) >= 3:
            print("Table full")
        else:
            row = parts[-1].strip("();")
            # If the table does not exist, create it with an empty list
            tables.setdefault(table, []).append(row)

    elif parts[0].lower() == "select":
        # Print the rows joined as a string
        print(', '.join(tables.get(parts[2], [])))

    else:
        raise ValueError("Invalid SQL command.")

def main():
    try:
        # Create table a and insert values
        dojob("create table a (i int);")
        dojob("insert into a values(10);")
        dojob("insert into a values(2);")
        dojob("select i from a;")  # Output: 10, 2
        dojob("insert into a values(3);")
        dojob("select i from a;")  # Output: 10, 2, 3

        # Create table b and insert values
        dojob("create table b (i int);")
        dojob("insert into b values(1);")
        dojob("select i from b;")  # Output: 1

    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
