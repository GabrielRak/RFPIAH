import numpy as np
import pandas as pd
import os  
import openpyxl
from utils.utils import check_if_path_exists

class Analyst:


	def __init__(self,ticker,input_folder,output_file):
		self.ticker = ticker
		self.output_file = output_file
		self.input_folder = input_folder

	def read_stock(self,):
		"""
			Reads the data from a JSON fie to a pandas DataFrame.
		"""
	
		filename = "data/json/" + self.ticker + ".json"
		check_if_path_exists("data/json")
	
		df = pd.read_json(filename)
		df = df.T
		columns_to_drop = [col for col in ['Dividends', 'Stock Splits'] if col in df.columns and (df[col] == 0).all()]
		
		df.drop(columns=columns_to_drop, errors="ignore", inplace=True)
	
		return df
	

	def read_folder(self,type="crypto",symbol="BTCUSDT"):
		"""
			Reads the data form folder 
		"""
		filenames = (os.listdir(f"{self.input_folder}/{symbol}" ))
		for filenames in filenames:
			filename = f"{self.input_folder}/{symbol}/{filenames}"
			check_if_path_exists('output/xlsx/')
			df = pd.read_json(filename)
			df.to_excel('output/xlsx/' + filenames + ".xlsx", index=False, engine="openpyxl")
			print(filename)
			print(df)
			print('\n]')

	def translate_to_xlsx(self):
		"""
			Saves the data frame to an 
		"""
		try:
			check_if_path_exists('output/xlsx/')
			self.read_data().to_excel("output/xlsx/" + self.ticker + ".xlsx", index=False, engine="openpyxl")
		except Exception as e:
			print(f"An error occurred while translating to xlsx: {e}")
			return None
		print(f"Generated xlsx:{self.ticker}")

