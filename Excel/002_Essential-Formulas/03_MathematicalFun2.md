
# Excel Lecture Notes

## SUMPRODUCT Formula
- **Purpose:** Calculates the sum of the product of individual elements of two or more series of numbers.
- **Example:**

  ```excel
  =SUMPRODUCT(A1:A3, B1:B3)
  ```

  - If `A1:A3` are `95, 83, 81` and `B1:B3` are `2, 1, 1.3`, the formula calculates `95*2 + 83*1 + 81*1.3`.
- **Steps:**
  1. Type `=SUMPRODUCT(`.
  2. Select the first series of numbers.
  3. Type `,` (comma).
  4. Select the second series of numbers.
  5. Press Enter.
- **Example Calculation:**
  - Result: `378.3` for `95*2 + 83*1 + 81*1.3`.
- **Tip:** Use dollar symbols for fixed references (e.g., weightages).

## RAND Function
- **Purpose:** Generates a random value between 0 and 1.
- **Usage:**
  ```excel
  =RAND()
  ```
  - No input parameters.
- **Applications:** Simulates chance events like tossing a coin or selecting a class representative.
- **Example:** Assigning the largest random value to choose a class representative.

## RANDBETWEEN Function
- **Purpose:** Generates a random value between a specified range.
- **Usage:**
  ```excel
  =RANDBETWEEN(40, 100)
  ```
  - Takes two parameters: the lower and upper limits of the range.
- **Example:** Randomly assigning marks between 40 and 100.

## Managing Random Values
- **Refreshing Issue:** Random values refresh on any operation in Excel.
- **Solution:** Use "Paste as Values" to fix the generated random values.
  1. Copy the cells with random values.
  2. Paste them using "Paste as Values" to retain the generated numbers without further refreshing.

## Additional Mathematical Functions
- Explore other mathematical functions available in Excel.
- **Access:** Go to the Formulas tab and select "Math & Trigonometry" to view a list of functions.

## Conclusion
- Practice using these functions on your own.
- Review the list of mathematical functions in Excel to expand your knowledge.
