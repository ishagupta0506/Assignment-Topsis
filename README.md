# TOPSIS Package

This package implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method for multi-criteria decision making.

---

## Author

**Isha Gupta**  
Roll Number: **102303007**

---

## Introduction

The **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)** is a well-established multi-criteria decision-making (MCDM) method.  
This Python implementation allows users to easily apply the TOPSIS methodology to a decision matrix and obtain a ranked list of alternatives based on multiple criteria.

The approach is widely used in engineering, management, and decision science problems where multiple conflicting criteria must be evaluated simultaneously.

---

## Key Concepts

- **Decision Matrix**  
  Represents the alternatives and their corresponding values for each criterion.

- **Weights**  
  Assign relative importance to each criterion based on user preference.

- **Impacts**  
  Indicate whether higher (`+`) or lower (`-`) values of a criterion are favorable.

- **Normalization**  
  Scales all criteria values to ensure comparability across different units.

- **Ideal Best and Ideal Worst Solutions**  
  Represent the best and worst possible values for each criterion.

- **Similarity and Dissimilarity Measures**  
  Compute the distance of each alternative from the ideal best and ideal worst solutions.

- **TOPSIS Score**  
  Combines similarity and dissimilarity measures to evaluate each alternative.

- **Ranking**  
  Alternatives are ranked based on their TOPSIS scores, where a higher score indicates a better alternative.

## Installation

Install the package using pip:

```bash
pip install topsis-isha-102303007
```

---

## PyPI Package

This project is also published as a Python package on **PyPI**.

### Package Name

topsis-isha-102303007


### PyPI Link
https://pypi.org/project/topsis-isha-102303007/

### Install from PyPI
```bash
pip install topsis-isha-102303007
```

---

## Usage

After installation, run the TOPSIS command from the terminal:

```bash
topsis <input_file.csv> "<weights>" "<impacts>" <output_file.csv>
```

---

## Example

```bash
topsis data.csv "1,1,1,1,1" "+,+,+,+,+" output.csv
```

---

## Input File Format

* The input file must be a **CSV file**
* It must contain **at least three columns**
* The **first column** should be an identifier (can be non-numeric)
* All remaining columns must contain **numeric values only**

---

## Input
<img width="414" height="389" alt="image" src="https://github.com/user-attachments/assets/12e8eeb5-d355-41bf-8fcc-cb32816ea50a" />

## Result
<img width="547" height="330" alt="image" src="https://github.com/user-attachments/assets/d8716f49-eba8-4ed0-9c6b-1d9e687c3c56" />



## Weights and Impacts

* Weights must be **numeric**
* Impacts must be either:
  * `+` for beneficial criteria
  * `-` for non-beneficial criteria
* Weights and impacts must be **comma-separated**
* The number of weights and impacts must match the number of criteria

---

## Output

The output CSV file will contain:
* All original columns
* A **Topsis Score** column
* A **Rank** column (Rank 1 indicates the best alternative)

---

## Web Service (Flask)

The web service implementation for TOPSIS is provided in the following file: topsis/app.py


### Features
- Upload CSV file
- Accept weights and impacts
- Validate inputs
- Execute TOPSIS on the server
- Email result CSV to user (configured locally using Gmail App Password)

### How to Run

```bash
pip install flask pandas
python topsis/app.py
```
---

## License

This project is developed for academic purposes.


