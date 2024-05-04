import sqlite3
import unittest

def is_table_empty(cursor, table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]
    return row_count == 0

class TestIsTableEmpty(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")

    def test_empty_table(self):
        self.assertFalse(is_table_empty(self.cursor, 'test_table'))

    def test_non_empty_table(self):
        self.cursor.execute("INSERT INTO test_table (name) VALUES ('John')")
        self.conn.commit()

        self.assertTrue(is_table_empty(self.cursor, 'test_table'))

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
