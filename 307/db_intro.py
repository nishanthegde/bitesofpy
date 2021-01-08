import sqlite3
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

NINJAS = [
    ("taspotts", 906),
    ("Tomade", 896),
    ("tasoak", 894),
    ("clamytoe", 890),
]


class SQLiteType(Enum):
    """Enum matching SQLite data types to corresponding Python types.
   
    Supported SQLite types:
        https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types.
    
    This Enum is uses in the definition of a table schema to define 
        the allowed data type of a column.

    Example: SQLiteType.INTEGER is the ENUM, 
        SQLiteType.INTEGER.name is "INTEGER",
        SQLiteType.INTEGER.value is int.     
    """

    NULL = None
    INTEGER = int
    REAL = float
    TEXT = str
    BLOB = bytes


class SchemaError(Exception):
    """Base Schema error class if a table schema is not respected."""

    pass


class DB:
    """SQLite Database class.

    Supports all major CRUD operations.
    This DB operates in-memory only by default.

    Attributes:
        location (str): The location of the database.
            Either a .db file or the special :memory: value for an
            in-memory database connection.
        connection (sqlite3.Connection): Connection object used to interact with
            the SQLite database.
        cursor (sqlite3.Cursor): Cursor object used to send SQL statements
            to a SQLite database.
        table_schemas (dict): The table schemas of the database.
            The key is the table name and the value is a list of pairs of 
            column name and column type.
    """
    connection = None
    cursor = None
    table_schemas = {}
    rows_affected = 0

    def __init__(self, location: Optional[str] = ":memory:"):
        self.location = location

    def __enter__(self):
        self.connection = sqlite3.connect(self.location)
        self.cursor = self.connection.cursor()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def create(
            self, table: str, schema: List[Tuple[str, SQLiteType]], primary_key: str
    ):
        """Creates a new table.

        Makes use of the SQLiteType enum class.
        Updates the table_schemas attribute.

        You can declare any column of the schema to serve as the primary key by adding
            'primary key' after the column name in the SQL statement.

        If the primary key is not part of the schema,
            a SchemaError should be raised with the message:
            "The provided primary key must be part of the schema."

        Args:
            table (str): The table's name.
            schema (list): A list of columns and their SQLite data types.
                Example: [("make", SQLiteType.TEXT), ("year": SQLiteType.INTEGER)].
            primary_key (str): The primary key column of the provided schema.

        Raises:
            SchemaError: If the given primary key is not part of the schema.
        """

        if not [c for c in schema[0] if c == primary_key]:
            raise SchemaError('The provided primary key must be part of the schema.')

        create_str = f'CREATE TABLE {table} ('

        for column, data_type in schema:
            if column == primary_key:
                create_str += f'{column} {data_type.name} PRIMARY KEY, '
            else:
                create_str += f'{column} {data_type.name}, '

        create_str = create_str[:-2]
        create_str += ')'

        self.cursor.execute(create_str)

        self.table_schemas[table] = schema

    def delete(self, table: str, target: Tuple[str, Any]):
        """Deletes rows from the table.

        Args:
            table (str): The table's name.
            target (tuple): What to delete from the table. The tuple consists
                of the column name and the actual value. For example, if you
                wanted to remove the row(s) with the year 1999, you would pass it
                ("year", 1999). Only supports "=" operator in this bite.
        """
        raise NotImplementedError("You have to implement this method first.")

    def insert(self, table: str, values: List[Tuple]):
        """Inserts one or multiple new records into the database.

        Before inserting a value, you should make sure
            that the schema for the table is respected.

        If there are more or less values than columns,
            a SchemaError should be raised with the message:
            "Table <table-name> expects items with <table-columns-count> values."

       If the type of a value does not respect the type of the column,
            a SchemaError should be raised with the message:
            "Column <column-name> expects values of type <column-type>."

        To add several values with a single command, you might want to look into
            [executemany](https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.executemany)

        Args:
            table (str): The table's name.
            values (list): A list of values to insert.
                Values must respect the table schema.
                The tuple consists of the values for each column in the table.
                Example: [("VW", 2001), ("Tesla", 2020)]

        Raises:
            SchemaError: If a value does not respect the table schema or
                if there are more values than columns for the given table.
        """

        # check if number of values to insert is equal to number of columns in table
        col_query = "PRAGMA table_info(%s)" % table
        self.cursor.execute(col_query)
        num_columns = len(self.cursor.fetchall())
        num_values = [len(t) for t in values]

        for val_length in num_values:
            if val_length != num_columns:
                raise SchemaError(f'Table {table} expects items with {num_columns} values.')

        # check if type of value respects schema type
        for value in values:
            for i in range(len(value)):
                if not isinstance(value[i], self.table_schemas[table][i][1].value):
                    raise SchemaError(
                        f'Column {self.table_schemas[table][i][0]} expects values of type {self.table_schemas[table][i][1].value.__name__}.'
                    )
        # insert values
        for value in values:
            insert_str = f'INSERT INTO {table} ('

            for column, data_type in self.table_schemas[table]:
                insert_str += f'{column}, '

            insert_str = insert_str[:-2]
            insert_str += ') VALUES ('

            for i in range(len(value)):
                if isinstance(value[i], str):
                    insert_str += f"'{value[i]}', "
                else:
                    insert_str += f"{value[i]}, "

            insert_str = insert_str[:-2]
            insert_str += ')'

            self.cursor.execute(insert_str)
            self.rows_affected += self.cursor.rowcount

    def select(
            self,
            table: str,
            columns: Optional[List[str]] = None,
            target: Optional[Tuple[str, Optional[str], Any]] = None,
    ) -> List[Tuple]:
        """Selects records from the database.

        If there are no columns given, select all available columns as default.

        If a target is given, but no operator (length of target < 3), assume equality check.

        Args:
            table (str): The table's name.
            columns (list, optional): List of the column names that you want to retrieve.
                Defaults to None.
            target (tuple, optional): If you want to narrow down the records returned,
                you can specify the column name, the operator and a value to look for.
                Defaults to None. Example: ("year", 1999) <-> ("year", "=", 1999).

        Returns:
            list: The output returned from the sql command
        """

        if columns is None:
            rows = self.cursor.execute(f'SELECT * FROM {table}').fetchall()
        else:
            select_str = f'SELECT '
            for col_name in columns:
                select_str += f'{col_name}, '

            select_str = select_str[:-2]
            select_str += f' FROM {table}'
            print(select_str)
            rows = self.cursor.execute(select_str).fetchall()

        return rows

    def update(self, table: str, new_value: Tuple[str, Any], target: Tuple[str, Any]):
        """Update a record in the database.

        Args:
            table (str): The table's name.
            new_value (tuple): The new value that you want to enter. For example,
                if you wanted to change "year" to 2001 you would pass it ("year", 2001).
            target (tuple): The row/record to modify. Example ("year", 1991)
        """
        raise NotImplementedError("You have to implement this method first.")

    @property
    def num_transactions(self) -> int:
        """The total number of changes since the database connection was opened.

        Returns:
            int: Returns the total number of database rows that have been modified.
        """
        return self.rows_affected


def main():
    print('thank you for looking after my mama!')
    DB_SCHEMA = [("ninja", SQLiteType.TEXT), ("bitecoins", SQLiteType.INTEGER)]
    #
    # for s in DB_SCHEMA:
    #     print(s[1].name)
    # db = DB()
    # print(db.location)
    # print(db.cursor)

    with DB() as db:
        db.create("ninjas", DB_SCHEMA, "ninja")
        # print(db.table_schemas)
        db.insert("ninjas", NINJAS)
        # print(db.num_transactions)
        # print(db.select("ninjas", None))
        print(db.select("ninjas", ["ninja"]))
        print(db.select("ninjas", ["bitecoins"]))

    print(sorted([(e[0],) for e in NINJAS]))
    print([(e[1],) for e in NINJAS])

if __name__ == '__main__':
    main()
