import os
import os.path
import sys
import numpy as np
import scipy as sp
from run_AROMA_config import *

def source_fsl5():
  try:
    os.system('setenv FSLDIR /home/fmri/fmrihome/fsl5.csh')
    os.system('${source /home/qinlab/Toolbox/fsl/etc/fslconf/fsl.csh}')
    os.system('setenv PATH ${/home/qinlab/Toolbox/fsl/bin:${PATH}')
  except:
    print('Cannot source fsl')

def ReadSubjectList(filename):
  try:
    f = open(filename, 'r')
    subjectIDs = f.read()
    f.close()
    subjectlist = subjectIDs.split()
  except:
    print('Cannot read subject list')
  return subjectlist

def Run_ICA_AROMA_nonaggr(input_file, output_folder, mc_file, brain_mask_fname):
  try:
    cmd = 'python /home/xujiahua/Scripts/AROMA/ICA-AROMA-master/ICA-AROMA-master/ICA_AROMA.py -in ' + input_file + ' -out ' + output_folder + ' -mc ' + mc_file + ' -tr 2 ' + ' -m ' + brain_mask_fname
    print(cmd)
    os.system(cmd)
  except :
    print('Cannot run AROMA nonaggr')

def Run_ICA_AROMA_aggr(input_file, output_folder, mc_file, brain_mask_fname):
  try:
    cmd = 'python /home/xujiahua/Scripts/AROMA/ICA-AROMA-master/ICA-AROMA-master/ICA_AROMA.py -in ' + input_file + ' -out ' + output_folder + ' -mc ' + mc_file + ' -tr 2 ' + ' -m ' + brain_mask_fname + ' -den aggr'
    print(cmd)
    os.system(cmd)
  except:
    print('Cannot run AROMA aggr')

def main():
    source_fsl5 # aggr needs fsl5

    subjectList = ReadSubjectList(subjectlist_file)

    for aggr_sign in aggr_signs:
      for isubj in subjectList:
          print('Running Subject %s for AROMA %s'%(isubj, aggr_sign))

          for task_folder in task_dirs:

                try:
                  interim_path_src = '/fmri/' + task_folder + '/smoothed_spm12/'
                  interim_path_des = '/fmri/' + task_folder + '/AROMA'
                  #yearid = '20' + isubj[0:2]
                  tmp1_input_file = raw_dir + '/' + isubj + interim_path_src + pipeline + 'I.nii.gz'
                  tmp2_input_file = raw_dir + '/' + isubj + interim_path_src + pipeline + 'I.nii'

                  if os.path.isfile(tmp2_input_file):
                    input_file = tmp2_input_file
                  elif os.path.isfile(tmp1_input_file):
                     input_file = tmp1_input_file
                  else:
                     print('error: file path does not exist')
                     sys.exit(1)
                  output_folder = raw_dir  + '/' + isubj + interim_path_des + '_' + aggr_sign
                  mc_file = raw_dir  + '/' + isubj + interim_path_src + 'rp_arI.txt'

                  if aggr_sign == 'nonaggr':
                    Run_ICA_AROMA_nonaggr(input_file, output_folder, mc_file, brain_mask_fname)
                  elif aggr_sign == 'aggr':
                    Run_ICA_AROMA_aggr(input_file, output_folder, mc_file, brain_mask_fname)
                  else:
                    print('error: aggr sign does not match')
                    sys.exit(1)
                except:
                    pass
if __name__ == '__main__':
  main()
