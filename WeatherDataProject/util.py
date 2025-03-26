import sqlite3
from datetime import datetime


def replace_neg_999_with_null(conn, table_name):
    cursor = conn.cursor()

    # Get column names from the table
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]

    for column in columns:
        try:
            # Update the column, setting -999 to NULL
            cursor.execute(f"UPDATE {table_name} SET {column} = NULL WHERE {column} = '-999'")
        except sqlite3.OperationalError as e:
            print(f"Skipping column {column} due to error: {e}")

    conn.commit()