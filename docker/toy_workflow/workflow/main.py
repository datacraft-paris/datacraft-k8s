import os
import pandas as pd
import numpy as np
from environs import Env

if __name__ == "__main__":
    # Parse configuration from environment variables
    print("Parsing configuration")
    env = Env()
    env.read_env()
    
    number_rows = env.int("NUMBER_ROWS", 10)
    output_directory_path = env.str("OUTPUT_DIRECTORY_PATH", "/data")
    output_file_name = env.str("OUTPUT_FILE_NAME", "toy_data.csv")

    # Generate random dataframe
    print("Generating random dataframe...")
    df = pd.DataFrame(np.random.randint(0,number_rows,size=(number_rows, 4)), columns=list('ABCD'))
    
    # Create output directory
    print("Creating output directory")
    try:
        os.makedirs(output_directory_path)
    except FileExistsError:
        print("Directory already exists.")
        pass

    # Write output csv to disk
    print("Saving result to disk.")
    df.to_csv(os.path.join(output_directory_path, output_file_name))