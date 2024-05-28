
# Macros in Excel

## Introduction
- **Macros** are a set of programming instructions stored as a procedure.
- Macros automate repetitive actions such as key presses or mouse clicks in Excel.
- Example: A macro to bold, center align, change format, and cell color of the active cell.

## Running a Macro
- Example macro with shortcut **Ctrl + Shift + A** performs:
  - Bold
  - Central alignment
  - Format change
  - Cell color change

## Creating Macros
### Enabling Developer Tab
- Right-click on the menu area and select "Customize the Ribbon."
- Check the Developer box and click OK.

### Recording a Macro
1. **Activate Developer Tab**: Click on it.
2. **Record Macro**:
   - Move to the desired sheet.
   - Use relative reference if needed (ensures the macro runs from the currently active cell).
   - Click "Record Macro."
   - Name the macro and set a shortcut key.
   - Provide a description (e.g., formatting a table).
   - Start recording and perform the desired actions.
3. **Perform Actions**:
   - Select cells, add borders, bold text, change cell color, etc.
4. **Stop Recording**: Click "Stop Recording" on the Developer tab.

### Using Recorded Macros
- Execute the macro using the assigned shortcut (e.g., **Ctrl + Shift + S**).
- Ensure actions like using **Ctrl + Shift + Right** for selection to accommodate different table sizes.

## Adding a Button to Run a Macro
1. **Insert Button**:
   - Go to Developer Tab → Insert → Button.
   - Draw the button and assign the macro to it.
2. **Rename Button**: Give it a meaningful name (e.g., "Exercise Macro").
3. **Run Macro via Button**: Click the button to execute the macro on the selected table.

## Saving Macros
- Save the workbook as an **Excel Macro-Enabled Workbook**:
  - Go to File → Save As.
  - Select the folder and choose "Excel Macro-Enabled Workbook (*.xlsm)."
  - Click Save.

### Error Handling
- If saving as a normal workbook, Excel will prompt that the workbook contains macros.
- Select "No" and save as a macro-enabled workbook instead.

## Viewing Macro Code
- Open the **Visual Basic for Applications (VBA)** window:
  - Go to Developer Tab → Visual Basic.
  - Expand Modules and select the appropriate module (e.g., Module1).
  - View the recorded macro code.

## Summary
- **Macros** automate repetitive tasks in Excel.
- **Recording and running macros** is straightforward, and adding buttons enhances usability.
- **Saving and viewing macros** ensures your work is preserved and editable.
- **Explore more**: Visit the Start Tech Academy YouTube channel for advanced Excel use cases.

## Conclusion
- This concludes the lecture and the course.
- With the basics of Excel, explore advanced use cases and implementations on our YouTube channel.
