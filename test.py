import glob

data_dir = "clover_by_test"

filenames = glob.glob(f"{data_dir}/*.xml")

filename = filenames[0]
