import unittest
import os
import sqlite3
from pipeline import main  # Adjust the import as per your file structure

class TestDataPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment before running any tests."""
        cls.db_path = '../data/MADE.sqlite'
        
        # Remove the database file if it exists
        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)
        
        # Run the main pipeline function to set up the database
        main()
        
        # Connect to the created database
        cls.conn = sqlite3.connect(cls.db_path)
        cls.cursor = cls.conn.cursor()

    def test_pipeline_execution(self):
        """Test the execution of the data pipeline."""
        # Check if the database file was created
        self.assertTrue(os.path.exists(self.db_path), "Database file was not created.")

        # Check if the traffic table was created
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='traffic_data';")
        traffic_table = self.cursor.fetchone()
        self.assertIsNotNone(traffic_table, "Table 'traffic_data' was not created in the database.")

        # Check if the weather table was created
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='weather_data';")
        weather_table = self.cursor.fetchone()
        self.assertIsNotNone(weather_table, "Table 'weather_data' was not created in the database.")

    def test_table_schema(self):
        """Test that the tables have the correct schema."""
        # Check the schema of the traffic_data table
        self.cursor.execute("PRAGMA table_info(traffic_data);")
        traffic_schema = self.cursor.fetchall()
        expected_traffic_schema = [
            (0, 'id', 'INTEGER', 0, None, 1),
            (1, 'month', 'TEXT', 0, None, 0),
            (2, 'traffic', 'INTEGER', 0, None, 0)
        ]
        self.assertEqual(traffic_schema, expected_traffic_schema, "Traffic table schema is incorrect.")

        # Check the schema of the weather_data table
        self.cursor.execute("PRAGMA table_info(weather_data);")
        weather_schema = self.cursor.fetchall()
        expected_weather_schema = [
            (0, 'id', 'INTEGER', 0, None, 1),
            (1, 'month', 'TEXT', 0, None, 0),
            (2, 'avg_temp', 'REAL', 0, None, 0),
            (3, 'snowfall', 'REAL', 0, None, 0),
            (4, 'precipitation', 'REAL', 0, None, 0),
            (5, 'wind_speed', 'REAL', 0, None, 0)
        ]
        self.assertEqual(weather_schema, expected_weather_schema, "Weather table schema is incorrect.")

    def test_data_content(self):
        """Test that the tables contain data."""
        # Check if the traffic_data table contains data
        self.cursor.execute("SELECT COUNT(*) FROM traffic_data;")
        traffic_count = self.cursor.fetchone()[0]
        self.assertGreater(traffic_count, 0, "Traffic table does not contain any data.")

        # Check if the weather_data table contains data
        self.cursor.execute("SELECT COUNT(*) FROM weather_data;")
        weather_count = self.cursor.fetchone()[0]
        self.assertGreater(weather_count, 0, "Weather table does not contain any data.")

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests."""
        cls.conn.close()
        # Optionally, remove the database file after testing
        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)

if __name__ == "__main__":
    unittest.main()
