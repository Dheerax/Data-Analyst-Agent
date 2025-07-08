import tempfile
import sqlite3
import pandas as pd
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase

class DataAnalysisAgent:
    def __init__(self, llm):
        self.llm = llm
        self.db_connection = None
        self.sql_database = None
    
    def init_agent(self, df: pd.DataFrame, table_name: str="Uploaded_table"):
        try:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
            temp_file.close()

            conn = sqlite3.connect(temp_file.name)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.commit()
            conn.close()

            self.sql_database = SQLDatabase.from_uri(f"sqlite:///{temp_file.name}")
            toolkit = SQLDatabaseToolkit(db=self.sql_database, llm=self.llm)
            self.sql_agent = create_sql_agent(
                llm=self.llm,
                toolkit=toolkit,
                verbose=True
            )
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def run_query(self, query):
        if not hasattr(self, 'sql_agent'):
            raise RuntimeError("Agent not created")
        
        return self.sql_agent.run(query)
    