
# Text to Columns and Removing Duplicates in Excel

## Text to Columns
- **Purpose**: Split text data in a single cell into separate columns based on a delimiter.
- **Delimited**: Use when data is separated by a specific character (e.g., comma, star).
- **Fixed Width**: Use when data columns have a set length with no separator.

### Example: Comma Separated Data
1. **Select Cells**: Choose the cell or cells containing the data.
2. **Text to Columns**: Go to `Data > Text to Columns`.
3. **Delimited Option**: Choose the delimited option and select the separator (e.g., comma).
4. **Preview and Finish**: Excel will preview the split and allow adjustments before finalizing.

### Handling Different Separators
- **Star Symbol Separator**: Similar process with the delimited option, selecting the star symbol as the separator.
- **Fixed Width**: For data without a separator but with known column lengths, use the fixed width option to manually set column boundaries.

## Removing Duplicates
- **Purpose**: Eliminate duplicate entries from a dataset.
- **Steps**:
  1. **Select Data**: Choose the data range.
  2. **Remove Duplicates**: Go to `Data > Remove Duplicates`.
  3. **Checkbox for Headers**: Check if the data includes headers.
  4. **Select Columns**: Choose columns for duplicate comparison.
  5. **Remove Exact Duplicates**: Excel removes rows with identical values in the selected columns.
  6. **Custom Criteria**: Optionally, apply custom criteria (e.g., keeping unique entries based on specific column values).

### Example: Removing Duplicates with Custom Criteria
1. **Sorting Data**: Sort data based on a specific column (e.g., marks in English).
2. **Remove Duplicates**: Select data and remove duplicates, choosing only the relevant column for comparison.
3. **Result**: Excel removes duplicates based on specified criteria, keeping unique entries.

---
