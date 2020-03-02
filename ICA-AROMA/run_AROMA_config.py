'''
#############################################################################
#################### Config file for run_AROMA.py ###########################
#############################################################################

To run:

1) copy both run_AROMA.py and run_AROMA_config.py 
2) fill out config and run: python run_AROMA.py

Note: If you get "ImportError: libgfortran.so.*: cannot open shared object file: No such file or directory"
Then you need to add this the libgfortran library to your path. To do this, run:

    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:/home/kochalka/lib64/

'''

# Location of the raw data directory (should be musk1)
raw_dir = '/home/xujiahua/Data'

# List of your task folders (should be a list not a txt file)
task_dirs = ['RS']

# 'nonaggr' to run the nonaggressive version of the algorithm and 'aggr' to run the aggressive version
aggr_signs = ['nonaggr']

# .txt file holding your subject list
subjectlist_file = 'twins_test.txt'

# specify which preliminary pipeline you have run (should be either 'swar' or 'swfar')
pipeline = 'swcar'

# File with brain mask
brain_mask_fname = '/home/qinlab/Toolbox/fsl/data/standard/MNI152_T1_2mm_brain_mask.nii.gz'
