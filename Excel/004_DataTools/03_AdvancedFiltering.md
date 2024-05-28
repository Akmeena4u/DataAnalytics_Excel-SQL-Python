
# Advanced Filters in Excel

## Introduction
In this video, we will learn about the advanced filters option available in the Data tab in Excel. These filters allow us to perform more complex operations than what's possible with basic filters. 

## Capabilities of Advanced Filters
1. **Multiple Conditions:** 
   - Specify multiple conditions or a combination of conditions (e.g., salesperson is Sara Johnson or region is North).

2. **Filtered Output in New Location:**
   - Retrieve the filtered data in a new location while keeping the original data intact.

3. **Filter Using Wildcards:**
   - Use wildcards for filtering data based on partial matches (e.g., customer IDs containing "AN").

4. **Unique Records:**
   - Retrieve unique records from the data, which can also be done using pivot tables but results in a smaller file size with advanced filters.

## Examples and Step-by-Step Guide

### Example 1: Simple Filter
**Objective:** Find all sales made by salesperson Sara Johnson.
1. **Specify Criteria:**
   - Write the column name (`Salesperson`) and the criteria (`=Sara Johnson`) in separate cells.
   - Format for exact text match: `="=Sara Johnson"`
   
2. **Apply Advanced Filter:**
   - Select the table, go to Data tab, and choose Advanced Filters.
   - Choose "Copy to another location."
   - Select the list range (the entire table including headers).
   - Select the criteria range (cells with criteria).
   - Specify the output location.
   - Click OK to view the filtered data.

### Example 2: Multiple AND Conditions
**Objective:** Find all sales by Jennifer Taylor in North region with debit card payment.
1. **Specify Criteria:**
   - Write the column names (`Salesperson`, `Payment Method`, `Region`) and their respective criteria.
   - Format criteria for exact matches.

2. **Apply Advanced Filter:**
   - Follow similar steps as in Example 1.

### Example 3: Multiple OR Conditions
**Objective:** Sales by Jennifer Taylor either in North region or with debit card payment.
1. **Specify Criteria:**
   - Write conditions in separate rows to indicate OR relationship.

2. **Apply Advanced Filter:**
   - Follow similar steps as in Example 1.

### Example 4: Numeric Range Filter
**Objective:** Retrieve sales data with selling price between 35K and 45K.
1. **Specify Criteria:**
   - Write the column name (`Selling Price`) and the range conditions (`>35000` and `<45000`).

2. **Apply Advanced Filter:**
   - Follow similar steps as in Example 1.

### Example 5: Using Wildcards
**Objective:** Filter transactions with customer IDs containing "AN" and payment method as bank transfer.
1. **Specify Criteria:**
   - Use wildcard (`*AN*`) for customer IDs.
   - Exact match for payment method.

2. **Apply Advanced Filter:**
   - Follow similar steps as in Example 1.

### Example 6: Retrieve Unique Records
**Objective:** Find names of all salespeople without duplicates.
1. **Apply Advanced Filter:**
   - Select the column containing salesperson names.
   - Specify the output location.
   - Check "Unique records only."
   - Click OK to view the unique names.

### Filtering Specific Columns
1. **Specify Desired Columns:**
   - List the column names you want in the output.
   
2. **Apply Advanced Filter:**
   - Select "Copy to another location."
   - In the "Copy to" field, select the cells with column names.
   - Follow similar steps as in Example 1.

## Conclusion
Advanced filters provide powerful options for complex data filtering in Excel, enabling you to apply multiple conditions, use wildcards, retrieve unique records, and get filtered data at a new location.
