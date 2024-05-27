# Basic Mathematical Functions in Excel

## Introduction
In this lecture, we will cover some basic mathematical functions in Excel. 

## Difference Between Formulas and Functions
- **Formulas:** An expression that calculates the value of a cell (e.g., `=A1 + B1`).
- **Functions:** Predefined formulas with descriptive names (e.g., `SUM`, `AVERAGE`).

## Data Setup
- **Data:** Scores of five students in three subjects (Maths, Science, English).
- **Objective:** Calculate total marks, minimum and maximum scores, average scores, and ranks.

## Using the SUM Function
1. **Manual Addition:**
   - Example: `=A2 + B2 + C2`
2. **SUM Function:**
   - Example: `=SUM(A2, B2, C2)`
   - Using range: `=SUM(A2:C2)`

3. **Extending Formulas:**
   - Use the bottom right corner to drag the formula to other cells.

## Auto-Complete Feature
- **Excel Suggestions:** As you type, Excel suggests functions.
- **Using Tab Key:** Press Tab to auto-complete the function name.

## Other Mathematical Functions
1. **MIN Function:**
   - Example: `=MIN(A2:A6)`
   - Finds the minimum value in a range.

2. **MAX Function:**
   - Example: `=MAX(A2:A6)`
   - Finds the maximum value in a range.

3. **AVERAGE Function:**
   - Example: `=AVERAGE(A2:A6)`
   - Calculates the mean value of a range.

## Ranking Students
1. **RANK.AVG Function:**
   - Example: `=RANK.AVG(A2, $A$2:$A$6, 0)`
   - First parameter: value to rank.
   - Second parameter: range of values.
   - Third parameter: ranking order (0 for highest rank 1, 1 for lowest rank 1).

2. **Maintaining Reference Range:**
   - Use dollar symbols (`$`) to lock cell references.
   - Shortcut: Select cell and press `F4` to add dollar symbols.

3. **Extending RANK.AVG Formula:**
   - Drag to apply the ranking formula to other cells.


## Difference between RANK, RANK.AVG and RANK.EQ
There are three versions of the RANK formula that you can use in MS Excel

RANK was available in the older versions of excel. We can still use it, probably it will not be available in the coming versions of Excel. There are two new versions of Rank now - RANK.EQ and RANK.AVG. Below example may clear the difference between these two -

For values 5,6,6,7 -RANK and RANK.EQ will return ranks as 1,2,2,4 (Same rank for same values) and RANK.AVG will return ranks as 1 ,2.5 ,2.5 ,4. (Average of 2nd and 3rd rank). Because RANK.AVG takes average of the ranks where values are same, we often see decimal digits in ranks calculated using this formula.

If all the values in the list are unique, all the three formulas assign same ranks in that case.

## Summary
- **Formulas vs. Functions:** Understand the difference and when to use each.
- **Using Functions:** Learn how to use SUM, MIN, MAX, and AVERAGE functions.
- **Ranking:** Use RANK.AVG to rank students based on their scores.

## Conclusion
- **Next Steps:** Explore other mathematical, textual, and logical functions in Excel to perform complex tasks efficiently.
