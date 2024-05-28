
# Importing Data from PDF to Excel

## Introduction
In this video, we will learn how to import data from a PDF file into an Excel file. This feature is new and available in Excel 2021 or Office 365. Users of Excel 2019 or earlier versions will need to copy-paste manually.

## Importance of the Feature
- Importing data tables from a PDF file is common in business scenarios.
- Example: As a finance manager, you might want to analyze balance sheets or profit and loss statements available in PDF format by importing them into Excel for further analysis.

## Steps to Import Data from PDF to Excel

### Step 1: Open the PDF
- Example PDF: Quarterly balance sheet report of Apple.
- Goal: Import the data of current assets from the balance sheet.

### Step 2: Use Excel’s Data Tab
1. Go to the `Data` tab.
2. Click on `Get Data`.
3. Select `From File` > `From PDF`.

### Step 3: Select PDF File
- Choose the PDF file and click on `Import`.
- Excel identifies all tables present in the PDF.
- Select the table you want to import (e.g., Table 1: Current Assets).

### Step 4: Transform Data Using Power Query
- Click on `Transform Data` to open Power Query.
- Use Power Query to clean and format the data:
  - Remove unnecessary columns (e.g., Column 2 and Column 4).
  - Rename columns (e.g., Column 3 to "Current Quarter" and Column 5 to "Q4 Last Year").
- Steps added in Power Query are remembered and applied each time the data is refreshed.

### Step 5: Load Data into Excel
- Click on `Close and Load` to load the transformed data into Excel.

## Updating Data
- Replace the old PDF file with a new one (e.g., new quarter data).
- Refresh data in Excel:
  - Go to `Table Design` > `Refresh`.
- Data and calculations will update automatically.

## Advanced Features
### Automatic Refresh
- Set refresh settings:
  - Go to `Connection Properties`.
  - Set the refresh interval (e.g., every hour, day, week).

### Handling Multiple Pages in PDF
1. Import data from multi-page PDFs (e.g., employee salary data).
2. Combine data from multiple tables using Power Query:
  - Filter to show only tables.
  - Remove unnecessary columns.
  - Expand data columns.
  - Use the first row as headers.
  - Apply transformations if needed.
3. Load combined data into Excel.

## Conclusion
- Importing data from a PDF to Excel using this new feature is efficient and saves time.
- Power Query allows for powerful data transformation and formatting.
- This feature is particularly useful in business scenarios where data analysis is frequently performed.

