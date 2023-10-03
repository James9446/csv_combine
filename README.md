# CSV Combiner

This is a Python3 script that combines multiple CSV files into one. It allows you to specify which columns to keep and you can also rename these specific columns in the combined CSV file.

## Installation

This script uses Python's built-in modules: argparse, os and glob, as well as pandas module. 

```bash
pip install pandas
```


## Usage

This script takes several command line arguments:

- `-i` or `--input_path` : The directory of the input CSV files. Default value is the current directory (`./`).
- `-n` or `--name` : The name of the combined output CSV file. Default value is `combined.csv`.
- `-k` or `--keep` : The names of the columns to keep from the original CSV files. If not supplied, all columns are kept.
- `-r` or `--rename` : The new names for the columns specified in `--keep`. This option can only be used in conjunction with `--keep` argument. The renaming is done in the provided order.
- `-o` or `--output_path` : The directory where the combined CSV file will be created. Default value is the current directory (`./`).

After running the script, it prints out the number of rows in the resulting combined CSV file.

Here are a few examples for using the script:

**Example 1**: Combine all CSV files in the current directory and keep all columns, with the default name 'combined.csv':

```bash
python csv_combine.py 
```

**Example 2**: Combine all CSV files in directory `data/`, keep only 'column1' and 'column2', rename them to 'rename1' and 'rename2', respectively. The output file named 'output.csv':

```bash
python csv_combine.py -i data/ -n output.csv -k column1 column2 -r rename1 rename2
```

**Example 3**: Combine all CSV files in directory `data/`, keep 'column1' and 'column2' as in the previous example, specify output directory `output_folder/`:

```bash
python csv_combine.py --input_path data/ --output_path output_folder/ --name output.csv --keep column1 column2 --rename rename1 rename2
```

Make sure to adjust the examples to match the columns present in your CSV files.