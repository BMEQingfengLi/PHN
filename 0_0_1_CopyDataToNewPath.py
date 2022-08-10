import pandas as pd
import os
import shutil
import numpy as np

def CopyData(save_rootdir,
             origin_data_dir,
             data_info_csvpth):
    '''

    :param save_rootdir:
    :param origin_data_dir:
    :param data_info_csvpth:
    :return:
    '''
    if not os.path.isdir(save_rootdir):
        os.mkdir(save_rootdir)

    # load dataset subjects
    data_info_csv = pd.read_csv(data_info_csvpth, dtype='str')
    subj_all_list_np = np.array(data_info_csv['name'])

    # copy data
    counter = 1
    for subj in subj_all_list_np:
        print('%s  %d/%d' % (subj, counter, len(subj_all_list_np)))
        currentsubj_orig_t1img_pth = os.path.join(origin_data_dir, subj, 't1_brain.nii.gz')
        currentsubj_save_dir = os.path.join(save_rootdir, subj)
        if os.path.isdir(currentsubj_save_dir):
            shutil.rmtree(currentsubj_save_dir)
        os.mkdir(currentsubj_save_dir)
        currentsubj_save_t1img_pth = os.path.join(save_rootdir, subj, 't1_brain.nii.gz')
        shutil.copyfile(currentsubj_orig_t1img_pth, currentsubj_save_t1img_pth)
        counter += 1


if __name__ == '__main__':
    # SMHC  COBRE  HBN  NPEMNSD  RCPDHP  SRPBS  TSRCPD  UCLA  WMHSI
    save_rootdir = '/HuaweiData/sharehome/yxpt/homeDocument/Documents/DL_trainingdata/20220809_PHN_Data/WMHSI'
    origin_data_dir = '/HuaweiData/sharehome/yxpt/homeDocument/Documents/DL_trainingdata/PublicDataforTest20210201/20210201copyforDLtest/WMHSI/data/'
    data_info_csvpth = './Files/WMHSI_AgeGenLabel.csv'
    CopyData(save_rootdir,
             origin_data_dir,
             data_info_csvpth)