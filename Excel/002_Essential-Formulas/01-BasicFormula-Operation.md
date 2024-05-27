# Basic Mathematical Operations in Excel

## Introduction
In this , we will cover basic mathematical operations in Excel, demonstrating how Excel simplifies repetitive calculations.

## Workbook Setup
- **Workbook Description:** A table with two columns containing numbers.
- **Tasks:**
  1. Add two numbers and write the sum in the "Sum" column.
  2. Add two numbers and a constant in the fourth column.
  3. Multiply these three numbers in the fifth column.
  4. Find the average of the three numbers in the last column.

## Adding Numbers
1. **Formula Basics:**
   - Formulas in Excel start with an `=` symbol.
   - Example: `=A2 + B2`.
   - The result will be displayed in the cell, while the formula remains visible in the formula bar.

2. **Using Cell References:**
   - **Dynamic Updates:** If cell values change, the formula updates automatically.
   - **Extending Formulas:**
     - Drag the formula from the bottom right corner to apply it to other cells.
     - Excel adjusts cell references automatically (e.g., `A2 + B2` becomes `A3 + B3`).

## Adding Constants
1. **Formula Example:**
   - Add a constant to the sum of two numbers: `=A2 + B2 + $B$13`.
   - **Using Dollar Symbols:**
     - `$` before a row number (e.g., `$B$13`) locks the reference, preventing it from changing when dragged.

2. **Extending Formulas with Locked References:**
   - Extend the formula down the column; `$B$13` remains constant.

## Multiplying Numbers
1. **Formula Example:**
   - Multiply three numbers: `=A2 * B2 * $B$13`.
   - Use `$` to lock the constant reference.

## Calculating Averages
1. **Formula Example:**
   - Add three numbers and divide by three: `=(A2 + B2 + $B$13) / 3`.
   - Alternatively, use the sum from the "Sum" column: `=D2 / 3`.

2. **Extending Formulas:**
   - Double-click the bottom right corner of the cell to fill the formula down the entire column automatically.

## Summary
- **Key Points:**
  - Formulas in Excel start with an `=` symbol.
  - Use cell references for dynamic updates.
  - Extend formulas by dragging or double-clicking the bottom right corner.
  - Use `$` to lock cell references.
  - Excel simplifies repetitive calculations and increases productivity.

## Next Steps
- **Upcoming Topics:**
  - Mathematical, textual, and logical functions in Excel.

---

