import re

# Store the table data as a dictionary of table names and their rows
tables = {}

def dojob(sql):
    global tables

    # Regular expression patterns to match SQL commands
    create_match = re.match(r'create table (\w+) \((\w+) int\);', sql, re.IGNORECASE)
    insert_match = re.match(r'insert into (\w+) values\((\d+)\);', sql, re.IGNORECASE)
    select_match = re.match(r'select (\w+) from (\w+)(?: where \((.*?)\))?;', sql, re.IGNORECASE)

    if create_match:
        # If it's a "CREATE TABLE" command, extract table_name and column_name
        table_name, column = create_match.groups()
        # Create an empty list for the table to store rows
        tables.setdefault(table_name, [])

    elif insert_match:
        # If it's an "INSERT INTO" command, extract table_name and value
        table_name, value = insert_match.groups()
        # Check if the table has reached its maximum capacity of 3 rows
        if len(tables.get(table_name, [])) < 3:
            # If not full, append the value as an integer to the table
            tables.setdefault(table_name, []).append(int(value))
        else:
            # If full, print a message indicating the table is full
            print(f"Table {table_name} is full")

    elif select_match:
        column, table_name, conditions = select_match.groups()
        rows = tables.get(table_name, [])
        
        if conditions:
            # Split the conditions using 'or' as the separator
            or_conditions = re.split(r'\s+or\s+', conditions, flags=re.IGNORECASE)
            results = []
            for condition in or_conditions:
                # Extract the individual components of each condition
                condition_column, condition_operator, condition_value = re.match(r'(\w+)\s*([><=]+)\s*(\d+)', condition).groups()
                condition_value = int(condition_value)
                # Process each condition and filter the rows accordingly
                if condition_operator == ">":
                    result = [row for row in rows if row > condition_value]
                elif condition_operator == "<":
                    result = [row for row in rows if row < condition_value]
                elif condition_operator == "=":
                    result = [row for row in rows if row == condition_value]
                elif condition_operator == ">=":
                    result = [row for row in rows if row >= condition_value]
                elif condition_operator == "<=":
                    result = [row for row in rows if row <= condition_value]
                results.extend(result)

            # Remove duplicates while preserving the original order
            rows = list(dict.fromkeys(results))

        # Print the table name and the entire row list
        print(f"Table {table_name}:")
        print(rows)
        # Return the rows as a list of integers
        return rows

    else:
        # If the command is not recognized, raise an error
        raise ValueError("Invalid SQL command.")


def main():
    try:
        sql_commands = [
            "create table a (i int);",
            "insert into a values(10);",
            "insert into a values(2);",
            "insert into a values(3);",
            "create table b (i int);",
            "insert into b values(1);",
            "insert into b values(4);",
            "insert into b values(5);",
            "select i from a;",
            "select i from b;",
            "select i from a where i=3;",
            "select i from b where i=4;",
            "select i from b where i<6 and i>2;",
            # Test with the OR operator and bracketed expression
            "select i from b where (i<6 and i>2) or (i=4 and 1<5);"
        ]

        # Collect the values for each table
        table_values = {}
        for sql in sql_commands:
            values = dojob(sql)
            if values is not None:
                table_name = re.search(r'from (\w+)', sql, re.IGNORECASE).group(1)
                table_values.setdefault(table_name, []).append(values)

        # Print the collected values for each table
        for table_name, values_list in table_values.items():
            print(f"Table {table_name}:")
            print(values_list)

    except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
