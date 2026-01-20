# TOPSIS Package

This package implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method for multi-criteria decision making.

---

## Author

**Isha Gupta**  
Roll Number: **102303007**

---

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


