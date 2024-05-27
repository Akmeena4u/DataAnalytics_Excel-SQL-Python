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

## Summary
- **Formulas vs. Functions:** Understand the difference and when to use each.
- **Using Functions:** Learn how to use SUM, MIN, MAX, and AVERAGE functions.
- **Ranking:** Use RANK.AVG to rank students based on their scores.

## Conclusion
- **Next Steps:** Explore other mathematical, textual, and logical functions in Excel to perform complex tasks efficiently.
