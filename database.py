from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

class Database:

    def __init__(self):

        self.uri = os.getenv("NEO4J_URI")
        self.user = os.getenv("NEO4J_USER")
        self.password = os.getenv("NEO4J_PASSWORD")

        self.driver = GraphDatabase.driver(
            self.uri,
            auth=(self.user, self.password)
        )

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):

        with self.driver.session() as session:

            result = session.run(query, parameters)

            return [record.data() for record in result]