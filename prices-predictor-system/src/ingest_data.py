""""Using the factory function to create a automation in loading of all kinds of data maybe it, 
    csv, json, XML, Database (Modifications required ahead), etc. [Other formats are not well exception handled. 
    TODO:Add exception handler and more automation for database ingestion]
"""

import os 
import zipfile 
from abc import ABC, abstractmethod 
import json 
import sqlite3
import pandas as pd 

#Define an abstract class for data-Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self , file_path: str) -> pd.DataFrame: 
        pass 
 
#implementing concrete class for ZIP Ingestion    
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """" Extracts a .zip file and returns the content as a pandas DataFrame"""
        #Ensure the file is a zip file. 
        if not file_path.endswith(".zip"): 
            raise ValueError("Expected a .zip file. Provided is of another format.")
        
        #Extract the zip file 
        with zipfile.ZipFile(file_path, "r") as zip_ref: 
            zip_ref.extractall("extracted_data")
            
        #Find the extracted CSV file (assuming there is only one csv file inside the zip ) 
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        
        if len(csv_files) == 0 : 
            raise FileNotFoundError("No CSV file found in the extracted data.")
        
        if len(csv_files) == 1 : 
            raise ValueError("Multiple CSV files found Please specify which one to use.")
        
        # read CSV into the DataFrame 
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)
        
        # return the DataFrame
        return df 
    
""""Implementig custom concrete class for JSON Ingestion"""
class JSONDataIngestor(DataIngestor): 
    def ingest(self, file_path : str) -> pd.DataFrame : 
        """Reads a JSON file and returns a pandas DataFrame"""
        #Ensure the file is JSON file. 
        if not file_path.endswith(".json"):
            raise ValueError("Expected a.json file. Provided is of another format.")
        
        #load JSON into pandas DataFrame 
        with open(file_path, 'r') as json_ref : 
            data = json.load(json_ref) 
        
        #Convert JSON to pandas DataFrame
        df = pd.DataFrame(data)
        return df 
        
""""Implementing Custom concrete class for Excel format data"""        
class ExcelDataIngestor(DataIngestor):
    def ingest(self, file_path : str) -> pd.DataFrame: 
           """Reads a excel file (assuming there is only one sheet associated with the file) return pandas DataFrame"""
           # Ensure the file is Excel file. 
           if not file_path.endswith(".xlsx"): 
               raise ValueError("Expected an.xlsx file. Provided is of another format.")
               
           # Load excel into pandas DataFrame 
           df = pd.read_excel(file_path) 
           return df

"""Implementing Custom concrete class for XML Data"""
class XMLDataIngestor(DataIngestor): 
    def ingest(self, file_path: str) -> pd.DataFrame:
        """ Reads a XML file and returns a pandas DataFrame"""
        #Ensure the file is a XMl file. 
        if not file_path.endswith(".xml"): 
            raise ValueError("Expected an.xml file. Provided is of another format.")
        
        #Load XML data into pandas DataFrame 
        return  pd.read_xml(file_path) 
    
"""Implementing Custom concrete class for TextFiles"""
class TextDataIngestor(DataIngestor): 
    """Read's text data and return's pandas DataFrame"""
    def ingest(self , file_path: str) -> pd.DataFrame: 
         #ensure the file is a text file. 
        if not file_path.endswith(".txt"): 
            raise ValueError("Expected a.txt file. Provided is of another format.")
    
        # Load text data into pandas DataFrame
        return pd.read_csv(file_path, delimiter='\t')
    
"""Implementing Custom concrete class for Database files(SQLite)"""
class SQLDataIngestor(DataIngestor): 
    """Reads data from a SQLite database and return's pandas DataFrame"""
    def ingest(self, file_path : str) -> pd.DataFrame:
        #Ensure the file is SQLite file. 
        if not file_path.endswith(".sqlite"): 
            raise ValueError("Expected a.sqlite file. Provided is of another format.")
        
        # Connect to SQLite database and load data into pandas DataFrame
        conn = sqlite3.connect(file_path)
        df = pd.read_sql_query("SELECT * FROM table_name", conn)
        
        # Close the connection
        conn.close()
        
        return df
    
#Implement the Factory to create DataIngestor: 
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension : str) -> DataIngestor: 
        if file_extension.lower() == ".zip":
            return ZipDataIngestor()
        elif file_extension.lower() == ".json" : 
            return JSONDataIngestor()
        elif file_extension.lower() in [".xls", ".xlsx"] : 
            return ExcelDataIngestor()  # Assuming.xls and.xlsx are Excel files 
        elif file_extension.lower() == ".txt" :
            return TextDataIngestor()
        elif file_extension.lower() == ".xml" : 
            return XMLDataIngestor()
        elif file_extension.lower() == ".sqlite" :
            return SQLDataIngestor()
        else:
            raise ValueError(f"No ingestor available for the file extension: {file_extension}")
                    
#Sample usage 
if __name__ == "__main__": 
    #specify the file path
    file_path = " "
    
    #Determine the file extension 
    file_extension = os.path.splitext(file_path)[1]
    
    # Get the appropriate DataIngestor 
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    
    # Ingest the data and load it into dataframe 
    df = data_ingestor.ingest(file_path)
    
    # print the dataframe
    print(df)
    print(f"Shape of the DataFrame: {df.shape}")
    pass 

    