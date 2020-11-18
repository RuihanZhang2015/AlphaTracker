
######################################################################
###                        general setting                         ###
######################################################################
# gpu_id is the id of gpu that will be used
gpu_id = 0


######################################################################
###                         code path setting                      ###
######################################################################
AlphaTracker_root = '/gdrive/AlphaTracker/01_Tracking/AlphaTracker'


######################################################################
###                        data related setting                    ###
######################################################################

# image_root_list is a list of image folder paths to the RGB image for training
image_root_list=['/gdrive/TRAINING_DATA_2020-11-17/']

# json_file_list is a list of paths to the json file that contain labels of the images for training
json_file_list = ['/gdrive/TRAINING_DATA_2020-11-17/ATjsonCOLAB.json']

# num_mouse is a list the specify the number of mouse in the images in each image folder path
num_mouse = [2]

# exp_name is the name of the experiment
exp_name = 'Mouse_SampleData'

# num_pose is the number of the pose that is labeled
## note!! remember to change self.nJoints in train_sppe/src/utils/dataset/coco.py
num_pose = 4
pose_pair = [ [0,1], [0,2],[0,3]]

# image_root_list is a list of image folder paths to the RGB image for training
#image_root_list=[\
#                 'E:\Data\Animal_tracking\marmoset\marmFramesForTyeLab\data\Oliver20191205_GoPro1\',
#                 'E:\Data\Animal_tracking\marmoset\marmFramesForTyeLab\data\Oliver20191205_GoPro2',
#                 'E:\Data\Animal_tracking\marmoset\marmFramesForTyeLab\data\Oliver20191205_GoPro3',
#                 'E:\Data\Animal_tracking\marmoset\marmFramesForTyeLab\data\Oliver20191205_GoPro4',
#                ]
# json_file_list is a list of paths to the json file that contain labels of the images for training
#json_file_list = [\
#                 'E:\Data\Animal_tracking\marmoset\marmFramesForTyeLab\data\Oliver20191205_GoPro1\CollectedData_sms.json',
#                 'E:\Data\Animal_tracking\marmoset\marmFramesForTyeLab\data\Oliver20191205_GoPro2\CollectedData_sms.json',
#                 'E:\Data\Animal_tracking\marmoset\marmFramesForTyeLab\data\Oliver20191205_GoPro3\CollectedData_sms.json',
#                 'E:\Data\Animal_tracking\marmoset\marmFramesForTyeLab\data\Oliver20191205_GoPro4\CollectedData_sms.json',
#	]
# num_mouse is a list the specify the number of mouse in the images in each image folder path
#num_mouse = [1,1,1,1]
# exp_name is the name of the experiment
#exp_name = 'Oliver_train1234'
# num_pose is the number of the pose that is labeled
## note!! remember to change self.nJoints in train_sppe/src/utils/dataset/coco.py
#pose_pair = [\
#	[0,1],[0,8],[0,2],[0,9],       # nose to eyes, ears
#	[0,15], [15, 16], [16,17], # spine and tail
#	[15,3],[3,4],[4,5],             # left arm
#	[15, 10], [10,11], [11,12], # right arm
#	[16,6], [6,7], [16,13],[13,14], # legs
#	]
#####################
# monkey bodyparts (x,y) are organized as: 
#nose,nose,lEye,lEye,lEar,lEar,lShoulder,lShoulder,lElbow,lElbow,lHand,lHand,lKnee,lKnee,lFoot,lFoot,rEye,rEye,rEar,rEar,rShoulder,rShoulder,rElbow,rElbow,rHand,rHand,rKnee,rKnee,rFoot,rFoot,backMid,backMid,tailBase,tailBase,tailTip,tailTip
# grand total of 17 body segments: 
# nose-Leye,  nose_Reye, nose_Lear, nose-Rear, nose-Midback, midback-tailbase, tailbase-tailtip, midback-Lshoulder, midback-Rshoulder, Lshoulder-Lelbow, Rshoulder-Relbow, Lelbow-Lhand, Relbow-Rhand, tailtip-Lknee, tailtip-Rknee, Lknee-Lfoot, Rknee-Rfoot

# train_val_split is ratio of data that used to train model
train_val_split = 0.90
# image_suffix is the suffix of the image
image_suffix = 'jpg'



######################################################################
###               training hyperparameter setting                  ###
######################################################################
sppe_lr=1e-4
sppe_epoch=10
# sppe_pretrain = '/disk4/zexin/project/mice/AlphaTracker/train_sppe/exp/coco/labeled_byCompany_0204050607_split90_ori/model_10.pkl'
sppe_pretrain = ''
sppe_batchSize = 10
yolo_lr=0.0005
yolo_iter=2000  ## if use pretrained model please make sure yolo_iter to be large enough to garantee finetune is done
#yolo_iter=20000+20000  ## if use pretrained model please make sure yolo_iter to be large enough to garantee finetune is done
# yolo_pretrain = '/disk4/zexin/project/mice/AlphaTracker/train_yolo/darknet/backup/labeled_byCompany_0204050607_split90_ori/yolov3-mice_final.weights'
yolo_pretrain = ''
yolo_batchSize = 4


######################################################################
###                    demo video setting                          ###
######################################################################
### note video_full_path is for track.py, video_paths is for track_batch.py
# video_full_path is the path to the video that will be tracked
#video_full_path = '/home/zexin/project/mice/datasets/interaction/2019-11-19_2femalespost8hrisolation.mp4'
video_full_path = '/gdrive/Sample_Data/sample_video.mp4'
# start_frame is the id of the start frame of the video
start_frame = 0
# end_frame is the id of the last frame of the video
end_frame = 3000000
# max_pid_id_setting is the number of mice in the video
max_pid_id_setting = 2

# result_folder is the path to the folder used to save the result
result_folder = '/gdrive/Mouse_SampleResults'

# remove_oriFrame is whether remove the original frame that generated from video
remove_oriFrame = False
vis_track_result = 1 # 1=show annotation on video; 0=does not show

# weights and match are parameter of tracking algorithm, following setting should work fine, no need to change
weights = '0 6 0 0 0 0 '
match = 0
