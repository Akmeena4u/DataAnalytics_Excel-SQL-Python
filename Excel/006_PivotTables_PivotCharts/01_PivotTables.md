
# Pivot Tables in Excel

## Introduction
- Pivot tables summarize data in the form of rows and columns.
- Provide counts and sums for different combinations of categories.
- Example: Furniture sales data.

## Data Example
- Columns: Salesperson, Product, Region, Customer, Date of Sale, Item Cost, Number of Items Sold, Total Cost.
- Each transaction by a salesperson is recorded in this table.

## Creating a Pivot Table
1. Go to the **Insert** menu and click on **Pivot Table**.
2. Ensure the entire table area is selected.
3. Choose whether to create the pivot table in the same worksheet or a new worksheet.
4. Click **OK**.

## Pivot Table Menu
- A new sheet is added with the pivot table menu on the right.
- Lists all column names.
- Four small boxes: Rows, Columns, Values, Filters.
- Drag and drop desired columns into these boxes to customize the report.

## Example: Sales Summary by Salesperson
1. Drag and drop **Salesperson** into the Rows box.
2. Drag and drop **Total Sales Value** into the Values box.
   - Shows the sum of total cost for each salesperson.
3. To identify sales to each customer, drag and drop **Customer Name** into the Columns box.

## Changing Value Field Settings
- To see the count of sales:
  1. Go to the Values box.
  2. Click on **Value Field Settings**.
  3. Select **Count** instead of **Sum**.
  4. Click **OK**.

## Sorting Data
- To sort data from largest to smallest:
  1. Go to the Grand Total column.
  2. Right-click on any value.
  3. Select **Sort > Largest to Smallest**.

## Applying Filters
- Use the Filters box to apply filters.
- Example: Filtering by region.
  1. Drag and drop **Region** into the Filters box.
  2. Click the small triangle to select desired regions.
  3. Tick the checkbox for multiple selections if needed.

## Viewing Monthly Sales
- Remove **Salesperson** from the table.
- Drag and drop **Date** into the Rows box.
- Grouping options:
  1. Right-click on the date field.
  2. Go to **Group**.
  3. Unselect **Years** and **Quarters**, leave **Months**.
  4. Click **OK**.

## Merging Values
- To group sales values for merged companies:
  1. Select the desired companies.
  2. Right-click and select **Group**.
  3. Click the minus button to see the combined sales.

## Using Slicers
- Slicers provide a convenient way to apply filters.
- To insert a slicer:
  1. Go to the **Analyze** option in the menu.
  2. Click on **Insert Slicer**.
  3. Select the column name for the filter (e.g., Region).
  4. Click **OK**.
- Use slicers to select one or multiple regions easily.

## Conclusion
- Pivot tables are powerful tools for summarizing and analyzing data.
- They allow quick and flexible data manipulation.
- Slicers enhance the user experience by providing easy filtering options.

