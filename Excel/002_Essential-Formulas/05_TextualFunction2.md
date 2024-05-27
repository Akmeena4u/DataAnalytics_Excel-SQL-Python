
# Excel Lecture Notes

## Textual Functions

### SUBSTITUTE Function
- **Purpose:** Replaces occurrences of a specified text within a string with another text.
- **Usage:**
  ```excel
  =SUBSTITUTE(text, old_text, new_text)
  ```
- **Example:**
  - To change "Stubent" to "Student": `=SUBSTITUTE(A1, "b", "d")` results in "Student".
  - To change a score from 38 to 95 in a sentence: `=SUBSTITUTE(A2, "38", "95")`.
  - To change "science" to "English" in a string: `=SUBSTITUTE(A3, "science", "English")`.
- **Notes:**
  - The SUBSTITUTE function is case-sensitive.
  - To display formulas as text, add a space before the equal sign.

### UPPER and LOWER Functions
- **Purpose:** Converts text to uppercase or lowercase.
- **Usage:**
  ```excel
  =UPPER(text)
  =LOWER(text)
  ```
- **Example:**
  - To convert to uppercase: `=UPPER(A1)` converts "student one" to "STUDENT ONE".
  - To convert to lowercase: `=LOWER(A2)` converts "Student One" to "student one".
- **Steps:**
  1. Type `=UPPER(` or `=LOWER(`.
  2. Select the text string.
  3. Press Enter.
  - To fill the table, drag the formula down using the fill handle.

### LEN Function
- **Purpose:** Returns the number of characters in a text string, including spaces.
- **Usage:**
  ```excel
  =LEN(text)
  ```
- **Example:**
  - To find the length of "student one": `=LEN(A1)` results in 11.
- **Steps:**
  1. Type `=LEN(`.
  2. Select the text string.
  3. Press Enter.
  - To extend the function to other cells, use the fill handle.

### LEFT, RIGHT, and MID Functions
- **Purpose:** Extracts specified characters from a text string.
- **Usage:**
  - **LEFT:** Extracts characters from the left.
    ```excel
    =LEFT(text, num_chars)
    ```
  - **RIGHT:** Extracts characters from the right.
    ```excel
    =RIGHT(text, num_chars)
    ```
  - **MID:** Extracts characters from the middle.
    ```excel
    =MID(text, start_num, num_chars)
    ```
- **Example:**
  - **LEFT:**
    - To extract the first 4 characters: `=LEFT(A1, 4)` results in "2018".
  - **RIGHT:**
    - To extract the last 2 characters: `=RIGHT(A1, 2)` results in "GR".
  - **MID:**
    - To extract 5 characters starting from the 5th position: `=MID(A1, 5, 5)` results in "12345".
- **Steps:**
  1. Type `=LEFT(`, `=RIGHT(`, or `=MID(`.
  2. Select the text string.
  3. Specify the number of characters or the starting point and number of characters.
  4. Press Enter.
  - To complete the table, use the fill handle.

## Practical Examples
- **SUBSTITUTE:** Correct typos or update text within a string.
- **UPPER/LOWER:** Standardize text case.
- **LEN:** Validate the length of input strings.
- **LEFT/RIGHT/MID:** Extract specific parts of a text, such as product codes or dates.

## Conclusion
- Practice using these functions to understand their applications and syntax.
- Explore additional textual functions in the Formulas tab of the Excel menu for more advanced text operations.
