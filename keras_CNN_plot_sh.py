#! /usr/bin/env python2 

import subprocess
import sys
import os 
import write_class_plotin as wcp
#Set the tfrecords directory of sys.argv[1]
sys_tfrecords_subdirecotry = sys.arg[1]
#Set the tfrecords name of sys.argv[2]
sys_tfrecords_name = sys.argv[2]

#####Searching the *.tfrecords is existed or not#####
dir_root = '/home/wehuang/work2/new_workspace/CMSSW_10_2_6/root6_space/HGCAL_Testing_Deep_Learning/Test_Beam_build_graph/python/tfrecord_dir/'

os.mkdir(dir_root + sys_tfrecords_subdirecotry)
for_tfrecord = wcp.plotin_class(sys_tfrecords_subdirecotry)
for_tfrecord.find_path_name()

tfrecord_filename = sys_tfrecords_name

###disappear at 12/12 15:13####
#if(os.listdir(dir_root) == sys_tfrecords_subdirecotry):
#    tmp_path = os.join(dir_root,sys_tfrecords_subdirecotry)
#    if(os.listdir(tmp_path) == sys_tfrecords_name):
#        pass
#    else:
#        subprocess.call("python","tmp_keras_for_HGCAL_CNN_plot.py",sys_tfrecords_subdirecotry,sys_tfrecords_name)
#else:
#    os.mkdir(os.join(dir_root,sys_tfrecords_subdirecotry))
#    subprocess.call("python","tmp_keras_for_HGCAL_CNN_plot.py",sys_tfrecords_subdirecotry,sys_tfrecords_name)
####End of existed *.tfrecords###################
#number_plot_subdirctory = subprocess.call("ls","|","wc" "-l")
#print(number_plot_subdirctory)
#subprocess.call(


