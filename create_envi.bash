#Just a simple script to create a conda environment from a yml file
conda env create --file environment.yml
conda activate myenvTEST
conda env list
#conda env update --file environment.yml --prune #If you modify the environment.yml file and want to update an existing environment to reflect the changes, you can use the following command