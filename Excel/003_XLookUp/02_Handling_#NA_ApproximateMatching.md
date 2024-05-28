
# XLOOKUP Features and Advanced Examples

## Handling Errors with XLOOKUP
- **Problem**: VLOOKUP/HLOOKUP returns `#NA` when a value isn't found.
- **Solution**: Use the fourth parameter of XLOOKUP to handle missing values.

### Example
- **Scenario**: Lookup for a serial number not in the data (e.g., 2000).
- **Formula**:
  ```excel
  =XLOOKUP(B3, B2:B1339, G2:G1339, "Not Found")
  ```
  - `B3`: Lookup value.
  - `B2:B1339`: Lookup array.
  - `G2:G1339`: Return array.
  - `"Not Found"`: Value to display if not found.

## Replacing HLOOKUP with XLOOKUP
- **Objective**: Find the CTC of a serial number using a horizontal lookup.
- **Example**:
  ```excel
  =XLOOKUP(B3, B1:M1, B2:M2)
  ```
  - `B3`: Lookup value.
  - `B1:M1`: Horizontal lookup array.
  - `B2:M2`: Horizontal return array.

## Advanced Matching Modes
- **Problem**: VLOOKUP by default does approximate matching; XLOOKUP provides more refined matching options.
- **Default Behavior**: XLOOKUP performs exact matching.
- **Advanced Matching**: Use the fifth parameter for match mode.

### Example: Approximate Match for Bonuses
- **Scenario**: Assign bonuses based on experience.
- **Data**:
  - `0-11 months`: 1%
  - `12-23 months`: 2.5%
  - `24-35 months`: 5%
  - ...

#### Finding the Largest Number Less Than or Equal To
- **Objective**: Find the largest experience less than or equal to the lookup value.
- **Formula**:
  ```excel
  =XLOOKUP(B3, A2:A10, B2:B10, , -1)
  ```
  - `B3`: Lookup value.
  - `A2:A10`: Experience array.
  - `B2:B10`: Bonus array.
  - `-1`: Exact match or next smaller item.

#### Finding the Smallest Number Greater Than or Equal To
- **Objective**: Find the smallest experience greater than or equal to the lookup value.
- **Formula**:
  ```excel
  =XLOOKUP(B3, A2:A10, B2:B10, , 1)
  ```
  - `B3`: Lookup value.
  - `A2:A10`: Experience array.
  - `B2:B10`: Bonus array.
  - `1`: Exact match or next larger item.

### Example Data
- **Table 1**: Lower limits given.
  - `0-11`: 1%
  - `12-23`: 2.5%
  - ...

- **Table 2**: Upper limits given.
  - `1-12`: 2.5%
  - `13-24`: 5%
  - ...

### Example Formulas
#### Lower Limits
```excel
=XLOOKUP(B3, A2:A10, B2:B10, , -1)
```
#### Upper Limits
```excel
=XLOOKUP(B3, A2:A10, B2:B10, , 1)
```

## Conclusion
- XLOOKUP enhances lookup capabilities in Excel.
- Handles errors gracefully with custom messages.
- Replaces both VLOOKUP and HLOOKUP with a unified function.
- Provides refined approximate matching options.

---

