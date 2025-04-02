import sqlite3
from datetime import datetime


def replace_neg_999_with_null(conn, table_name):
    """
        Replace all occurrences of -999 in a specified table with NULL values.
        This function iterates over each column in the given table and updates the column,
        replacing any instance of '-999' with NULL. It handles potential errors during
        the update process, such as unsupported data types, by skipping the problematic
        columns and printing an error message.
        Args:
            conn: The SQLite database connection object.
            table_name (str): The name of the table to update.
    """
    print("Start replacement from -999 to null")
    
    cursor = conn.cursor()

    # Get column names from the table
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = [column[1] for column in cursor.fetchall()]

    for column in columns:
        print(f"processing: {column}")
        try:
            # Update the column, setting -999 to NULL
            cursor.execute(f"UPDATE {table_name} SET {column} = NULL WHERE {column} = '-999'")
            conn.commit()
        except sqlite3.OperationalError as e:
            print(f"Skipping column {column} due to error: {e}")
            
    print("Finisched the replacement from -999 to null")