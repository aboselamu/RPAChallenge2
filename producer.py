from RPA.Browser.Selenium import Selenium 
import re
import time
import requests
import logging
from pathlib import Path
from robocorp import vault
from robocorp import excel
from robocorp import storage
from datetime import datetime
from robocorp.tasks import task
from robocorp import workitems
# from robocorp.workitems import WorkItems
from datetime import datetime, timedelta
from robocorp.tasks import get_output_dir
from browser_manager import BrowserManager as BM 
from data_retriever import DataRetriever 

@task
def producer():

    
    bm = BM()
    url = "https://www.aljazeera.com/"
    bm.opening_the_news_Site(url)
    bm.search_the_phrase("Business")
    dr = DataRetriever()
    dr.retrive_data(1, "Business", bm)

    # Close the browser
    # bm.close_browser()


    # save_data_to_Excel(workbook, sheet_name)
    # workbook.save(excel_file_path)

    # Saving the workbook
    # workbook.save(excel_file_path)
    
