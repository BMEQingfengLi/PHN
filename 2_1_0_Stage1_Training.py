from Utils.Stage1_PFENTrainingProcess import
import argparse


def main():
    '''

    :return:
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgrootpth',
                        default="/HuaweiData/sharehome/yxpt/homeDocument/Documents/DL_trainingdata/20220809_PHN_Data/SMHC",
                        type=str,
                        help='input image rootpath ( including training and validation data)')
    parser.add_argument('--gpuidx',
                        default=0,
                        type=int,
                        help='Index of GPU. The training process uses a single GPU.')
    parser.add_argument('--savepth',
                        default='./Save_stage1/',
                        type=str,
                        help='model and results save path')
    parser.add_argument('--epoch',
                        default=500,
                        type=int,
                        help='training epoch')
    parser.add_argument('--batchsize',
                        default=24,
                        type=int,
                        help='training batchsize')
    parser.add_argument('--threadnum',
                        default=10,
                        type=int,
                        help='number of thread')




    args = parser.parse_args()

     # basic setting
    input_image_rawpth = args.imgpth
    input_subjname = args.patientname
    input_applicnum = args.applicnum
    input_age = args.age
    input_gender = args.gender
    save_rootpath = args.saverootpth

    # project setting
    gpu_flag = args.gpuflag
    hcfeaturecsv_pth = "/home/yxpt/Desktop/Projects/PHIDiagReport_V3/Codes/DatasetFeatureTable_removeWJHMDD_T1.csv"
    stage1modelrootpth = "/home/yxpt/Desktop/Projects/PHIDiagReport_V3/Models/Stage1"
    stage2modelrootpth = "/home/yxpt/Desktop/Projects/PHIDiagReport_V3/Models/Stage2"
    fiveclfmodelrootpth = "/home/yxpt/Desktop/Projects/PHIDiagReport_V3/Models/FiveCLF"
    tidycode_pth = "/home/yxpt/Desktop/Projects/PHIDiagReport_V3/Codes/CODEBASE/TIDY/TDv1.0.0"
    phipipecode_pth = "/home/yxpt/Desktop/Projects/PHIDiagReport_V3/Codes/CODEBASE/PHIPIPE/PPv1.0.0"
    otherutilscode_pth = "/home/yxpt/Desktop/Projects/PHIDiagReport_V3/Codes/"
    taskname = args.taskname

    # Start Analysis process
    DiagReportPipeline(input_image_rawpth,
                       input_subjname,
                       input_applicnum,
                       input_age,
                       input_gender,
                       gpu_flag,
                       save_rootpath,
                       hcfeaturecsv_pth,
                       stage1modelrootpth,
                       stage2modelrootpth,
                       fiveclfmodelrootpth,
                       tidycode_pth,
                       phipipecode_pth,
                       otherutilscode_pth,
                       taskname)


if __name__ == '__main__':
    main()
