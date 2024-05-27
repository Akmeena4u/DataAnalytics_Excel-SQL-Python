
# Excel Lecture Notes

## Textual Functions

### TRIM Function
- **Purpose:** Removes extra spaces from text strings.
- **Usage:**
  ```excel
  =TRIM(text)
  ```
- **Example:**
  - If a cell contains "  student one  ", `=TRIM(A1)` will result in "student one".
- **Steps:**
  1. Type `=TRIM(`.
  2. Select the cell with the text string.
  3. Press Enter.
- **Notes:**
  - TRIM removes spaces from the beginning, end, and extra spaces between words.
  - To convert the formula result to a text value, use "Paste as Values" after copying the cells.

### CONCATENATE Function
- **Purpose:** Combines multiple text strings into one.
- **Usage:**
  ```excel
  =CONCATENATE(text1, text2, ...)
  ```
- **Example:**
  - Combine "Maths", "Science", and "English" in cells A1, B1, and C1: `=CONCATENATE(A1, B1, C1)` results in "MathsScienceEnglish".
  - To create a sentence: `=CONCATENATE(A1, " has scored ", B1, " in Maths")` might produce "Student 1 has scored 95 in Maths".
- **Steps:**
  1. Type `=CONCATENATE(`.
  2. Select the first text string.
  3. Type `,` (comma) and enter additional text strings or cell references.
  4. Close the bracket and press Enter.
- **Notes:**
  - To extend the formula for other rows, use the fill handle (drag the formula).

### Ampersand (&) for Concatenation
- **Purpose:** Combines multiple text strings into one using the `&` symbol.
- **Usage:**
  ```excel
  =text1 & text2 & ...
  ```
- **Example:**
  - Combine "Maths", "Science", and "English" in cells A1, B1, and C1: `=A1 & " has scored " & B1 & " in Maths"` results in "Student 1 has scored 95 in Maths".
- **Steps:**
  1. Select the first text string or cell reference.
  2. Type `&`.
  3. Enter the next text string or cell reference, surrounded by `&` symbols.
  4. Press Enter.
- **Notes:**
  - Ampersand performs the same function as CONCATENATE but is often quicker to type.

## Example Usage
- **TRIM Function:**
  - Corrects text with extra spaces: `=TRIM(A1)`
- **CONCATENATE Function:**
  - Combines first and last names: `=CONCATENATE(A1, " ", B1)`
  - Creates a sentence: `=CONCATENATE(A1, " has scored ", B1, " in Maths")`
- **Ampersand (&):**
  - Similar to CONCATENATE: `=A1 & " " & B1` for names, `=A1 & " has scored " & B1 & " in Maths"`

## Practical Examples
- **TRIM:** Clean text data from user input.
- **CONCATENATE/Ampersand:** Generate dynamic text strings for reports or summaries.

## Conclusion
- Practice using these functions to become familiar with their syntax and applications.
- Explore other textual functions in the Excel Formulas tab for more advanced text operations.

