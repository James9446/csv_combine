import pandas as pd
import os
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_path', type=str, default='./', help='directory of input files')
parser.add_argument('-o', '--output_path', type=str, default='./', help='directory of output file')
parser.add_argument('-n', '--name', type=str, default='combined.csv', help='name of combined file')
parser.add_argument('-k', '--keep', nargs='+', default=[], help='columns to keep')
parser.add_argument('-r', '--rename', nargs='+', default=[], help='new column names')
args = parser.parse_args()

path = args.input_path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
  df = pd.read_csv(filename, dtype=str)
  
  # Select only specified columns
  if args.keep:
    df = df[args.keep]
  
  # Rename columns
  if args.rename:
    df.columns = args.rename
  
  li.append(df)

# Concatenate all dataframes in list
df = pd.concat(li, ignore_index=True)

# Save combined dataframe to csv
df.to_csv(os.path.join(args.output_path, args.name), index=False)

print(f"Created {args.name} in {args.output_path} with {len(df)} rows.")