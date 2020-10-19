python train.py --frame_folders_str='./1411_black_two/annotation/;./1929_black_two/annotation/'   --Annotation_files_str='./1411_black_two/annotation/annotation.json;./1929_black_two/annotation/annotation.json' --pretrian_folder='./model/version1/'  --save_folder='./model/version2/'





python track.py --video_paths_str='./1411_black_two.mov;1859_black_two.mov' \
	--save_jsons_str='./1411_black_two/alpha_pose.json;./1411_black_two/alpha_pose2.json' \
	--nums_mice_str='2;3' \
	--model_path_str='./model/version1/'


env CUDA_VISIBLE_DEVICES=2 python train.py


CUDA_VISIBLE_DEVICES=2 python train.py \
             --dataset coco \
             --img_folder_train /disk2/zexin/project/mice/AlphaTracker//train_yolo/darknet//data/labeled_byCompany_05_split90_ori/color/ \
             --annot_file_train /disk2/zexin/project/mice/AlphaTracker//train_sppe//data/labeled_byCompany_05_split90_ori/data_newLabeled_01_train.h5 \
             --img_folder_val /disk2/zexin/project/mice/AlphaTracker//train_yolo/darknet//data/labeled_byCompany_05_split90_ori/color/ \
             --annot_file_val /disk2/zexin/project/mice/AlphaTracker//train_sppe//data/labeled_byCompany_05_split90_ori/data_newLabeled_01_val.h5 \
             --expID labeled_byCompany_05_split90_ori \
             --nClasses 4 \
             --LR 0.0001 --trainBatch 10 \
             --nEpochs 10 \
             --nThreads 6 \
             --loadModel /disk2/zexin/project/mice/AlphaTracker//models/sppe/duc_se.pth