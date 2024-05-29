
# Measures of Dispersion

Measures of dispersion tell us about the spread of the data. We will be discussing three measures of dispersion:

1. Range
2. Standard Deviation
3. Variance

Variance and standard deviation are related by a simple formula: variance is the square of the standard deviation.

## Range

Range is the largest value minus the smallest value.

### Example
In our example, the largest value is 34 and the smallest value is 7.

- Range = 34 - 7 = 27

Range is influenced by outliers. If your data has outliers, range should be avoided. For example, if one value is exceptionally high (e.g., 150):

- Range = 150 - 7 = 143

This range does not correctly represent the dispersion since only one value is exceptionally high. Most values are between 7 and 34. Remove outliers before calculating the range or use other measures of dispersion.

## Standard Deviation and Variance

Variance is the average of the squared differences from the mean. Standard deviation is the square root of the variance.

### Definitions
- **Population Mean (μ)**: The mean of the entire population.
- **Sample Mean (x̄)**: The mean of a sample from the population.

### Population Variance (σ²)
```
σ² = Σ (x - μ)² / N
```

### Sample Variance (s²)
```
s² = Σ (x - x̄)² / (n - 1)
```

### Population Standard Deviation (σ)
```
σ = √(σ²)
```

### Sample Standard Deviation (s)
```
s = √(s²)
```

### Example
Let's calculate the standard deviation for the following data:

Values: 10, 12, 23, 23, 16, 34, 7, 12, 22, 25, 27, 24, 17, 18, 15, 26, 29, 30, 28, 20, 19, 14, 18, 21

1. Calculate the mean (x̄):
```
x̄ = (10 + 12 + 23 + 23 + 16 + 34 + 7 + 12 + 22 + 25 + 27 + 24 + 17 + 18 + 15 + 26 + 29 + 30 + 28 + 20 + 19 + 14 + 18 + 21) / 24
  = 24.875
```

2. Calculate the variance (s²):
```
s² = Σ (x - x̄)² / (n - 1)
```

3. For each value, calculate the difference from the mean, square it, and sum these values:
```
s² = [(10-24.875)² + (12-24.875)² + ... + (21-24.875)²] / 23
   = 1624.625 / 23
   = 67.69
```

4. Calculate the standard deviation (s):
```
s = √(67.69)
  = 8.23
```

### Interpretation
A larger standard deviation indicates a wider dispersion of data from the mean. If another set of 24 observations has a similar mean but a lower standard deviation, it means that data has less dispersion and values are closer to the mean. Conversely, a larger standard deviation indicates that values are further from the mean.

## Conclusion
That's all for this video lecture on measures of dispersion. In the next video, we will discuss the measures of dispersion.
```

For more complex formulas, you can use a LaTeX editor to create images of the formulas and embed them in the Markdown file like this:

```markdown
![Population Variance](url_to_image)
```

