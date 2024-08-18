import dask.dataframe as dd
import dask
dask.config.set({'dataframe.query-planning': True})
dask.config.set({'dataframe.query-planning-warning': False})



# Assuming 'final_sampled_user_ids.parquet' is the directory containing all the part files
# Load the entire dataset as one Dask DataFrame
df = dd.read_parquet('/labs/bharadwajlab/afmustafa/output/final_sampled_user_ids.parquet')
# Compute the count of rows in the DataFrame
row_count = df.shape[0].compute()

print(f"Total number of rows: {row_count}")

