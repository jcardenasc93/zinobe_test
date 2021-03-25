""" Thi smodules generate the reports from the current data """
import sqlite3
import json


class DBManager:
    """ This class implements the SQLite manager """

    def __init__(self):
        self.create_table_query = """CREATE TABLE IF NOT EXISTS report
                                     (total_time, average_time, max_time, min_time)"""
        self.insert_query = "INSERT INTO report VALUES (?,?,?,?)"
        self.create_connection()
        self.create_table()

    def create_connection(self):
        """ Creates sqlite3 connection """
        self.connection = sqlite3.connect('db_app.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        """ Creates report table in db """
        self.cursor.execute(self.create_table_query)
        self.connection.commit()

    def insert_row(self, data):
        """ Inserts a new row """
        print("Inserting row to database")
        self.cursor.executemany(self.insert_query, data)
        self.connection.commit()


class JSONManager:
    """ This class is used to create a json file """

    @classmethod
    def create_json(cls, data, filename="data.json"):
        """ Creates JSON file """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
