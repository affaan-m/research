#!/bin/bash

#SBATCH --job-name=affaan_userID_sample
#SBATCH --output=affaan_userID_sample_%j.out

# Load any necessary modules
# module load python/3.7

# If you have a specific Python environment, activate it
# source activate myenv

# Navigate to the directory containing your script
cd /sphere/bharadwajlab/afmustafa/

# Execute your Python script
python samplethenconcatenate.py --folder_path "/sphere/bharadwajlab/linkedin/individual_user" --output_dir "/sphere/bharadwajlab/afmustafa/output"
