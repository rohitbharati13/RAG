import pandas as pd 
import pdfplumber  # This is a Python library for extracting text, tables, and metadata from PDF files. It provides a simple interface to read and manipulate PDF documents, making it easier to work with PDF data in Python applications.
import re  # This is a built-in Python module that provides support for regular expressions. Regular expressions are a powerful tool for pattern matching and text manipulation. The re module allows you to search, match, and manipulate strings based on specific patterns, making it useful for tasks such as data cleaning, validation, and extraction.

from config import (pdf_path,attraction_csv , Event , stops , routes, trips, agency , NIAH)


#load all Files
def load_all_data() :
    Attraction_df = pd.read_csv(attraction_csv)
    Event_df = pd.read_csv(Event)
    Stops_df = pd.read_csv(stops)
    Trips_df = pd.read_csv(trips)
    Routes_df = pd.read_csv(routes)
    Agency_df = pd.read_csv(agency)
    NIAH_df = pd.read_csv(NIAH , encoding="latin1")

    #join routes with agency name 
    Routes_with_Agency = Routes_df.merge(                       # This line of code is performing a merge operation between the Routes_df DataFrame and the Agency_df DataFrame. The purpose of this merge is to combine information from both DataFrames based on a common column, which in this case is "agency_id". The result will be a new DataFrame that includes all columns from both original DataFrames, allowing for a more comprehensive view of the routes along with their corresponding agency names.
        Agency_df[["agency_id" , "agency_name"]],
        on="agency_id",
        how="left"
    )

    print("Attractions : " , Attraction_df.shape)
    print("Events : " , Event_df.shape)
    print("Stops   : " , Stops_df.shape)
    print("Routes : ", Routes_df.shape)
    print("Trips : " , Trips_df.shape)
    print("NIAH : ", NIAH_df.shape)

    return Attraction_df , Event_df , Stops_df , Agency_df , NIAH_df

# ── Load and clean PDF ────────────────────────────────────────────
def load_pdf():
    # Read text from PDF (same logic as your Colab code)
    pages = []
    with pdfplumber.open(pdf_path) as pdf:    # This line of code is opening the PDF file specified by the variable pdf_path using the pdfplumber library. The pdfplumber.open() function is used to create a context manager that allows you to work with the PDF file. The "with" statement ensures that the PDF file is properly opened and closed after the block of code is executed, preventing resource leaks and ensuring that the file is released when no longer needed.
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                pages.append(txt)    # This line of code is checking if the variable txt, which contains the extracted text from the current page of the PDF, is not empty or None. If txt contains valid text (i.e., it is not an empty string or None), the code appends this text to the pages list. This ensures that only pages with actual text content are added to the list, avoiding any empty entries.
    raw_text = "\n".join(pages)    # This line of code is joining all the extracted text from the individual pages of the PDF into a single string. The pages list contains the text from each page, and "\n".join(pages) concatenates these strings with a newline character ("\n") between each page's text. The result is a single string, raw_text, that contains the entire text content of the PDF, with each page's text separated by a newline.

    # Clean the text 
    text = re.sub(r"Ireland\s*–\s*Travel guide at Wikivoyage", " ", raw_text)
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"\[edit\]", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\[\d+\]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    print("PDF loaded and cleaned. Length:", len(text))
    return text

