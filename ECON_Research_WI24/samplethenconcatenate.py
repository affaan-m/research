import dask.dataframe as dd
from dask.diagnostics import ProgressBar
import os, argparse, logging, psutil
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Argument parsing
parser = argparse.ArgumentParser(description='Sample and merge Parquet files using Dask.')
parser.add_argument('--folder_path', type=str, required=True, help='Path to the folder containing Parquet files')
parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the output Parquet file')
parser.add_argument('--sample_fraction', type=float, default=0.1, help='Fraction of data to sample (e.g., 0.1 for 10%)')
args = parser.parse_args()

# Memory usage function
def print_memory_usage():
    process = psutil.Process(os.getpid())
    logging.info(f"Current memory usage: {process.memory_info().rss / 1024 ** 2:.2f} MB")

def sample_and_merge_optimized_dask(folder_path, output_dir, sample_fraction=0.1):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'final_sampled_user_ids.parquet')
    
    ddf = dd.read_parquet(os.path.join(folder_path, '*.parquet'))
    ddf_sampled = ddf.sample(frac=sample_fraction)
    
    with ProgressBar():
        ddf_sampled.to_parquet(output_file)
    
    logging.info(f"Output saved to {output_file}")

if __name__ == "__main__":
    print_memory_usage()  # Before execution
    sample_and_merge_optimized_dask(args.folder_path, args.output_dir, args.sample_fraction)
    print_memory_usage()  # After execution

