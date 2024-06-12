import unittest
import os
import sqlite3
from pipeline import main


class TestDataPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment before running any tests."""
        cls.db_path = '../data/MADE.sqlite'
        
       
        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)
        
       
        main()
        
        
        cls.conn = sqlite3.connect(cls.db_path)
        cls.cursor = cls.conn.cursor()

        
        cls.passed_messages = []

    def test_pipeline_execution(self):
        """Test the execution of the data pipeline."""
        
        self.assertTrue(os.path.exists(self.db_path), "Database file was not created.")

        
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='traffic';")
        traffic_table = self.cursor.fetchone()
        self.assertIsNotNone(traffic_table, "Table 'traffic' was not created in the database.")

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='weather';")
        weather_table = self.cursor.fetchone()
        self.assertIsNotNone(weather_table, "Table 'weather' was not created in the database.")

    def test_table_schema(self):
        """Test that the tables have the correct schema."""
        
        self.cursor.execute("PRAGMA table_info(traffic);")
        traffic_schema = self.cursor.fetchall()
        expected_traffic_schema = [
            (0, 'id', 'INTEGER', 0, None, 1),
            (1, 'month', 'TEXT', 0, None, 0),
            (2, 'traffic', 'INTEGER', 0, None, 0)
        ]
        self.assertEqual(traffic_schema, expected_traffic_schema, "traffic table schema is Wrong.")

        
        self.cursor.execute("PRAGMA table_info(weather);")
        weather_schema = self.cursor.fetchall()
        expected_weather_schema = [
            (0, 'id', 'INTEGER', 0, None, 1),
            (1, 'month', 'TEXT', 0, None, 0),
            (2, 'tavg', 'REAL', 0, None, 0),
            (3, 'snow', 'REAL', 0, None, 0),
            (4, 'prcp', 'REAL', 0, None, 0),
            (5, 'wspd', 'REAL', 0, None, 0)
        ]
        self.assertEqual(weather_schema, expected_weather_schema, "Weather table schema is Wrong.")

    def test_data_content(self):
        """Test that the tables contain data."""
        
        self.cursor.execute("SELECT COUNT(*) FROM traffic;")
        traffic_count = self.cursor.fetchone()[0]
        self.assertGreater(traffic_count, 0, "Traffic table does not contain any data.")

        
        self.cursor.execute("SELECT COUNT(*) FROM weather;")
        weather_count = self.cursor.fetchone()[0]
        self.assertGreater(weather_count, 0, "Weather table does not contain any data.")

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests."""
        cls.conn.close()
        
        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)
if __name__ == "__main__":
    unittest.main()
