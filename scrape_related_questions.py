# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
import sys
from bs4 import BeautifulSoup
import numpy as np
import json
import unittest, time, re
import xlsxwriter
import pandas as pd
import numpy as np
import sys
import os
import fetch_answer_and_related_questions








topics = ["Personal-Finance","Loans","Personal-Loans-1","Bank-Loans","Financial-Services-1",
			"Finance","Finance-in-India", "Finance-and-Investments", "Investing-in-the-Stock-Market-1",
			"Hedge-Funds", "Investing", "Mutual-Fund-Investment-Strategies", "The-Economics-of-Investing","Stock-Markets-2",
			"Investment-Advice","Mutual-Fund-Investment-Advice-1","Stocks-finance"]

for topic in topics:
	topic_dir = os.path.join(os.getcwd(),"data",str(topic))
	if os.path.isdir(topic_dir):
		print("------------------------------topic----------------------------------------------")
		answer_related_questions_getter = fetch_answer_and_related_questions.fetch_answer_and_related_questions(topic_dir,topic)
		answer_related_questions_getter.fetch_related_questions_and_links()
		print("------------------------------changing topic----------------------------------------------")
		print("\n")
		print("+++++++++++++++++++++++++++++++related complete++++++++++++++++++++++++++++++++++++++++")