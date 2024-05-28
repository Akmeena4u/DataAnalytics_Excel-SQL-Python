
# Importing Data from Websites to Excel

## Introduction
In this video, we will learn how to import data from websites into Excel. This is useful when you find a data set on a website in the form of a table and want to analyze it in Excel. For example, if you want to analyze the unemployment rates of different countries from a Wikipedia table.

## Limitations
- The feature to import data from web pages is available only in Excel 2019 and above versions.
- Users with Excel 2016 or older versions will not see this option but can manually copy-paste the data.

## Steps to Import Data from a Web Page
1. **Go to the Data Tab:**
   - Click on `Get Data`.
   - Select `From Online Sources`.
   - Choose `From Web`.

2. **Enter the URL:**
   - Copy the URL of the web page containing the table.
   - Paste it in the URL box and click OK.

3. **Navigator Window:**
   - Excel processes the page and identifies data tables.
   - Select the desired table by previewing it on the right side.

4. **Edit in Power Query (if needed):**
   - Click on `Edit` to open the Power Query window.
   - Apply transformations (e.g., removing unnecessary columns, setting headers, sorting, filtering).

5. **Load Data:**
   - Click on `Close and Load` to import the data into Excel in a tabular format.

## Example 1: Importing Data from Wikipedia
1. **URL:**
   - Example URL with a table of unemployment rates by country.

2. **Transformations:**
   - Remove unnecessary columns.
   - Set the first row as headers.
   - Sort by unemployment rate.
   - Filter data to show only countries with unemployment rates between 4% and 8%.

3. **Load Data:**
   - Click `Close and Load`.

## Example 2: Importing Data from Worldometer
1. **URL:**
   - Example URL with COVID-19 data by country.

2. **Transformations:**
   - Filter out non-country rows.
   - Remove extra columns.
   - Keep only top 20 countries by total cases.

3. **Load Data:**
   - Click `Close and Load`.

## Automatic Refresh
- Set refresh frequency by going to `Connection Properties`.
- Check the box and enter the refresh interval (default is 60 minutes).

## Practice Assignment
- **Yahoo Finance:**
   - Go to Yahoo Finance.
   - Search for a company (e.g., Apple Inc.).
   - Navigate to historical data.
   - Import historical stock prices into Excel.

## Conclusion
- Importing data from web pages allows for dynamic updates.
- Power Query helps format data and apply necessary transformations.
- Practice with different web pages to get comfortable with the process.

