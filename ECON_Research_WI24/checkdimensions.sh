#!/bin/bash

#SBATCH --job-name=check_dimensions
#SBATCH --output=check_dimensions_%j.out
#SBATCH --error=check_dimensions_%j.err

# Activate your Python environment if you have one
# source /path/to/your/environment/bin/activate

# Navigate to the directory containing your Python script
cd /labs/bharadwajlab/afmustafa/

# Run your Python script
python checkdimensions.py

