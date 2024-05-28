
# Excel Lecture Notes

## Logical Functions

### Single Argument Logical Test
- **Purpose:** Checks if a single condition is true or false.
- **Usage:**
  ```excel
  = (logical_test)
  ```
- **Example:** 
  - To check if a student scored 100 in Maths: `=B2=100`.
  - Extend the formula to other cells to see the results for all students.
  - Only one student (Student 4) scored 100 in Maths.

### AND Function
- **Purpose:** Checks if all conditions are true.
- **Usage:**
  ```excel
  =AND(condition1, condition2, condition3, ...)
  ```
- **Example:** 
  - To identify students with distinction (≥75 in all subjects): 
    ```excel
    =AND(B2>=75, C2>=75, D2>=75)
    ```
  - Extend the formula to other cells. 
  - Three students have more than 75 marks in all subjects.

### OR Function
- **Purpose:** Checks if any one or more conditions are true.
- **Usage:**
  ```excel
  =OR(condition1, condition2, condition3, ...)
  ```
- **Example:**
  - To identify students who failed any subject:
    ```excel
    =OR(B2<35, C2<35, D2<35)
    ```
  - Extend the formula to other cells.
  - Only one student (Student 5) failed (scored 30 in English).

### IF Function
- **Purpose:** Returns one value if a condition is true and another value if it's false.
- **Usage:**
  ```excel
  =IF(logical_test, value_if_true, value_if_false)
  ```
- **Example:**
  - To assign grades based on Maths scores:
    ```excel
    =IF(B2>=75, "A", "B")
    ```
  - Extend the formula to other cells.

### Nested IF
- **Purpose:** Allows multiple conditions by using multiple IF statements.
- **Usage:**
  ```excel
  =IF(condition1, value_if_true, IF(condition2, value_if_true, value_if_false))
  ```
- **Example:** 
  - To grade students based on scores:
    ```excel
    =IF(B2>=85, "A", IF(B2>=60, "B", "C"))
    ```
  - Extend the formula to other cells.
  - For more grades, add more nested IFs.

### Combining AND/OR with IF
- **Purpose:** Allows checking multiple conditions within an IF statement.
- **Example:** 
  - To check for distinction:
    ```excel
    =IF(AND(B2>=75, C2>=75, D2>=75), "Passed with Distinction", "")
    ```
  - To check if any subject is failed:
    ```excel
    =IF(OR(B2<35, C2<35, D2<35), "Failed", "Promoted to next class")
    ```
  - Extend the formula to other cells.

### COUNTIF Function
- **Purpose:** Counts the number of cells that meet a criterion.
- **Usage:**
  ```excel
  =COUNTIF(range, criteria)
  ```
- **Example:** 
  - To count students with grade A in Maths:
    ```excel
    =COUNTIF(B2:B6, "A")
    ```
  - Extend the formula to other grades.

### COUNTIFS Function
- **Purpose:** Counts the number of cells that meet multiple criteria.
- **Usage:**
  ```excel
  =COUNTIFS(range1, criteria1, range2, criteria2, ...)
  ```
- **Example:**
  - To count students with distinction:
    ```excel
    =COUNTIFS(B2:B6, ">75", C2:C6, ">75", D2:D6, ">75")
    ```
  - Changing the criteria cell dynamically adjusts the count.

### SUMIF Function
- **Purpose:** Sums the values in a range that meet a criterion.
- **Usage:**
  ```excel
  =SUMIF(range, criteria, sum_range)
  ```
- **Example:**
  - To sum Maths scores of students who passed:
    ```excel
    =SUMIF(E2:E6, "False", B2:B6)
    ```
  - Sum of Maths scores of students who passed is 349 (99 + 65 + 85 + 100).

### SUMIFS Function
- **Purpose:** Sums the values in a range that meet multiple criteria.
- **Usage:**
  ```excel
  =SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2, ...)
  ```
- **Example:** 
  - Similar to COUNTIFS, explore SUMIFS for multiple criteria.

## Conclusion
- Practice using these logical functions to understand their applications and syntax.
- Explore additional logical functions in the Formulas tab of the Excel menu for more advanced operations.

## Next Lecture
- In the next lecture, we will discuss Date-Time formulas.
