
# Lecture on Date and Time Functions in Excel

Hello everyone, in this lecture we will be covering date and time related functions in Excel. We all mention date and time in different formats, sometimes we use date month and year which is DDMMYY or sometimes it is Month date year MMDDYY, or sometimes the month are written in words instead of numbers.

Excel supports all these formats and it even identifies the input in cells to see if those are dates or not.

## Date and Time Functions

### Today's Date
To see today's date in default format, use the `TODAY` function:
```excel
=TODAY()
```
This function returns today's date and refreshes whenever the sheet is refreshed.

### Current Date and Time
For the current date and time, use the `NOW` function:
```excel
=NOW()
```
This includes the time along with the date.

### Number Format for Dates
Excel stores dates and times as numbers:
- The integer part represents the number of days since 1st Jan 1900.
- The decimal part represents the time (fraction of a day).

For example:
- 1st Jan 1900 is 1.
- 30th Dec 1900 is 365.
- 12th Nov 2018 is 43,416.

### Date and Time Formats
To format dates and times:
1. Right-click the cell.
2. Select "Format Cell".
3. In the category menu, select "Date" or "Time" to choose a predefined format, or select "Custom" to create a custom format.

For example, a custom format:
- `DD` for day
- `mmmm` for full month name
- `YY` for year
- `h:mm` for time

### Extracting Day, Month, and Year
- To get the day:
  ```excel
  =DAY(A1)
  ```
- To get the month:
  ```excel
  =MONTH(A1)
  ```
- To get the year:
  ```excel
  =YEAR(A1)
  ```

### Calculating Date Differences
- To find the number of days between two dates:
  ```excel
  =DAYS(end_date, start_date)
  ```
  or simply subtract the dates:
  ```excel
  =end_date - start_date
  ```
- To convert the difference to hours:
  ```excel
  =(end_date - start_date) * 24
  ```
- To convert to minutes:
  ```excel
  =(end_date - start_date) * 24 * 60
  ```

### DATEDIF Function
This function calculates the difference between two dates in days, months, or years:
```excel
=DATEDIF(start_date, end_date, "d")  // for days
=DATEDIF(start_date, end_date, "m")  // for months
=DATEDIF(start_date, end_date, "y")  // for years
```

## Conclusion
That's all for this lecture. In the next lecture, we will discuss the `INDEX MATCH` and `LOOKUP` functions.

---
