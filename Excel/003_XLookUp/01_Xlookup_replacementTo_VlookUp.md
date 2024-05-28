
# Introduction to XLOOKUP

## Overview
- **XLOOKUP** is a powerful new addition to the lookup functions in Excel.
- It has more features than VLOOKUP and HLOOKUP.
- Available only in Excel 2021, Excel 365, and later versions.

## Practical Example with Employee Data
- The data includes employee serial number, role, college, city, CTC, and experience in months.
- Download the sheet from the resources of this video to follow along.

## Simple XLOOKUP Example (Replacing VLOOKUP)
- **Objective**: Find the CTC of a specified employee serial number.
- **Example**:
  ```excel
  =XLOOKUP(B3, B2:B1339, G2:G1339)
  ```
  - `B3`: Lookup value (serial number).
  - `B2:B1339`: Lookup array (serial numbers).
  - `G2:G1339`: Return array (CTC values).
- **Steps**:
  1. Enter the formula.
  2. Check the returned CTC value.

## Returning Multiple Values with XLOOKUP
- **Objective**: Return multiple values (City type, CTC, and experience) for a given serial number.
- **Example**:
  ```excel
  =XLOOKUP(B3, B2:B1339, D2:F1339)
  ```
  - `B3`: Lookup value.
  - `B2:B1339`: Lookup array.
  - `D2:F1339`: Return array (multiple columns).
- **Steps**:
  1. Enter the formula.
  2. Observe the multiple returned values.

## Looking Up Values to the Left with XLOOKUP
- **Objective**: Retrieve the role of an employee, even if the role column is to the left of the lookup column.
- **Example**:
  ```excel
  =XLOOKUP(B3, B2:B1339, C2:C1339)
  ```
  - `B3`: Lookup value.
  - `B2:B1339`: Lookup array.
  - `C2:C1339`: Return array (roles).
- **Steps**:
  1. Enter the formula.
  2. Verify the returned role.

## Key Features of XLOOKUP
- Can return multiple values from an array.
- Can look up values to the left of the lookup array, unlike VLOOKUP.
- Simplifies and improves lookup efficiency in Excel.

## Conclusion
- XLOOKUP offers significant advantages over traditional lookup functions like VLOOKUP and HLOOKUP.
- Its ability to return multiple values and look up to the left makes it a versatile tool in data analysis.

