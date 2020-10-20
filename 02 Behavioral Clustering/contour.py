import numpy as np
import cv2
import json
import math
import copy
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy
from tqdm import tqdm

import contour_utils


def get_samples(dir_name,video_name,json_name):

    data = contour_utils.load_json(json_name)
    contour_path = dir_name + 'contour_zexin'

    # ------------------- Read First Frame -----------------------

    # cap = cv2.VideoCapture(dir_name, video_name)
    cap = cv2.VideoCapture(dir_name+'/'+video_name)
    read_flag, frame = cap.read()
    width, height,depth = np.asarray(frame).shape

    i = 0
    if not os.path.exists(contour_path):
        os.mkdir(contour_path)


    # ----------------- Sample all the mouse mask ----------------------------
    while(read_flag):

        # 当前frame的pose信息
        mouses = data['frame_{}'.format(i)]
        pose1 = np.asarray(mouses[0]['keypoints']).reshape((4,3))
        pose2 = np.asarray(mouses[1]['keypoints']).reshape((4,3))

        # 当前frame中寻找contours
        frame = gaussian_filter(frame, sigma=3)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        ret,thre = cv2.threshold(gray,30,255,0)
        contours, hierarchy = cv2.findContours(thre,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]

        # 遍历每个contour，看是否符合要求
        for contour_id, contour in enumerate(contours):

            if (contour.size>150)and(contour.size<600):

                # 把contour以binary mask的形式呈现
                mask = np.zeros((width,height,depth),dtype = 'uint8')
                cv2.drawContours(mask, contours, contour_id, (255,255,255), -1)

                # 假设当前的contour符合要求，但发现有任意一个keypoint不在mask内，就放弃
                flag = True
                for j in [0,3]:
                    if (mask[int(pose1[j,1]),int(pose1[j,0]),0] == 0):
                        flag = False
                        continue

                if flag:

                    # 假设当前的contour符合要求，但发现有另一只老鼠的keypoint在mask内，就放弃
                    flag2 = True
                    for j in [0,3]:
                        if (mask[int(pose2[j,1]),int(pose2[j,0]),0] > 0):
                            flag2 = False
                            continue

                    if flag2:

                        # 首先把mask平移到中心
                        rows,cols,depth = mask.shape
                        x,y,w,h = cv2.boundingRect(contour)
                        M = np.float32([[1,0,640-(x+w/2)],[0,1,360-(y+h/2)]])
                        tra = cv2.warpAffine(mask,M,(cols,rows))

                        # 旋转到身体的轴在x轴上
                        body = pose1[3,0:2]-pose1[0,0:2]
                        rho,phi = contour_utils.cart2pol(body[0],body[1])
                        angle = math.degrees(phi)

                        M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
                        rot = cv2.warpAffine(tra,M,(cols,rows))

                        # 裁剪成 200 * 200
                        crop = rot[260:460,540:740].copy()

                        cv2.imwrite(contour_path+ '/mask_{}.png'.format(i),crop)
                        print(contour_path+ '/mask_{}.png'.format(i))

                        continue

        read_flag, frame = cap.read()
        i += 1

    cap.release()

# dir_name = '/Users/ruihan/Documents/clustering/Nancy/'
# video_name = 'e2_tra'

# dir_name = '/disk1/zexin/project/mice/clustering_sequencial/forZexin/results/0603/1929_black_two/'
# video_name = '1929_black_two.mov'
# json_name= '/disk1/zexin/project/mice/clustering_sequencial/forZexin/results/0603/1929_black_two/alphapose-results-forvis-tracked.json'

dir_name = '/disk1/zexin/project/mice/clustering_sequencial/forZexin/results/0603/1411_black_two/'
video_name = '1411_black_two.mov'
json_name= '/disk1/zexin/project/mice/clustering_sequencial/forZexin/results/0603/1411_black_two/alphapose-results-forvis-tracked.json'


get_samples(dir_name,video_name,json_name)

def create_dataframe_faces():

    # 取读所有的mask图，构成一个dataframe


    faces = pd.DataFrame([])
    i = 0

    ## 第一个视频
    img_dict = '/Users/ruihan/Documents/clustering/results/contour/'
    data = contour_utils.load_json('/Users/ruihan/Documents/clustering/results/0603/1411_black_two/alphapose-results-forvis-tracked.json')

    for img_name in os.listdir(img_dict):


        if not(img_name[-1] == 'g'):
            continue

        if np.random.randn()>1:
            print(img_dict + img_name)
            frame = plt.imread(img_dict + img_name)
            frame = np.asarray(frame[:,:,0],dtype = 'uint8')
            frame[frame == 255] = 1
            # flat = frame.flatten()

            # print(flat.shape)
            face = pd.Series(frame.flatten(),name = img_name)

            # print(face)
            faces = faces.append(face)
            i += 1

    ## 第二个视频
    img_dict = '/Users/ruihan/Documents/clustering/results/contour2/'
    data = contour_utils.load_json('/Users/ruihan/Documents/clustering/results/0603/1929_black_two/alphapose-results-forvis-tracked.json')

    for img_name in os.listdir(img_dict):
        if not(img_name[-1] == 'g'):
            continue

        if np.random.randn()>1:
            print(img_dict + img_name)
            frame = plt.imread(img_dict + img_name)
            frame = np.asarray(frame[:,:,0],dtype = 'uint8')
            frame[frame == 255] = 1
                # flat = frame.flatten()

            # print(flat.shape)
            face = pd.Series(frame.flatten(),name = img_name)
            # print(face)
            faces = faces.append(face)
            i += 1


    ## 可视化
    width, height = frame.shape
    fig, axes = plt.subplots(10,10,figsize=(9,9),
        subplot_kw = {'xticks':[], 'yticks':[]},
        gridspec_kw = dict(hspace=0.01, wspace=0.01))

    for i, ax in enumerate(axes.flat):
        ax.imshow(faces.iloc[i].values.reshape(height,width),cmap='gray')

    plt.savefig('love.png')

    import pickle

    with open('./utils_file/faces.pckl', 'wb') as f:
        pickle.dump(faces, f)

# create_dataframe_faces()


def pca_for_faces():

    import pickle
    with open('./utils_file/faces.pckl','rb') as f:
        faces = pickle.load(f)

    from sklearn.decomposition import PCA
    #n_components=0.80 means it will return the Eigenvectors that have the 80% of the variation in the dataset
    faces_pca = PCA(n_components=0.9)
    faces_pca.fit(faces)
    fig, axes = plt.subplots(2,5,figsize=(9,3),
        subplot_kw = {'xticks':[], 'yticks':[]},
        gridspec_kw = dict(hspace=0.01, wspace=0.01))

    for i, ax in enumerate(axes.flat):
        ax.imshow(faces_pca.components_[i].reshape(200,200),cmap='gray')

    plt.savefig('love_pc.png')
    plt.close()

    plt.figure()
    plt.plot(np.cumsum(faces_pca.explained_variance_ratio_))
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance');
    plt.savefig('love_variance.png')
    plt.close()

    with open('./utils_file/pca.pckl','wb') as f:
        pickle.dump(faces_pca,f)

    print(faces)
    components = faces_pca.transform(faces)


    # import pickle
    # with open('hc_single_temporal_small.pckl','rb') as f:  # Python 3: open(..., 'rb')
    # feature_allClip, feature_allClip_normal,select_info = pickle.load(f)
    # feature_allClip_normal = np.asarray(feature_allClip_normal)
    # feature_allClip = np.asarray(feature_allClip)

    # for k in range(len(components)):
    #     img_name = faces.index.values[k]
    #     frame_idx = img_name[0:-4].split('_')[-1]
    #     components[int(frame_idx)].append()
    #
    # Z = linkage(components, method ='ward',metric='euclidean')
    #
    # # print(components.shape)
    # # projected = faces_pca.inverse_transform(components)
    # # fig, axes = plt.subplots(10,10,figsize=(9,9), subplot_kw={'xticks':[], 'yticks':[]},
    # #         gridspec_kw=dict(hspace=0.01, wspace=0.01))
    # # for i, ax in enumerate(axes.flat):
    # #     ax.imshow(projected[i].reshape(200,200),cmap="gray")
    # #
    # # plt.savefig('love_ranked.png')
    #
    # f = plt.figure(figsize = (15,5))
    # g0 = plt.gca()
    # dn = hierarchy.dendrogram(Z,
    #     above_threshold_color='y',
    #     orientation='top',
    #     ax = g0)
    # plt.tight_layout()
    # plt.savefig('love_dendrogram.png')

    # # print(dn.keys())
    # leaves = np.asarray(dn['leaves'])
    # # print(leaves.size)

    # threshold = 100
    # cluster_idx = hierarchy.fcluster(Z,threshold,'distance')
    #
    # cluster_clips = [[] for i in range(np.max(cluster_idx)+1)]
    # for ii in range(len(cluster_idx)):
    #     cluster_clips[cluster_idx[ii]].append(ii)
    #
    #
    # # cluster_clips = np.asarray(cluster_clips)
    # for cluster_id in range(1,np.max(cluster_idx)+1):
    #
    #     fig, axes = plt.subplots(4,5,figsize=(9,7),
    #         subplot_kw = {'xticks':[], 'yticks':[]},
    #         gridspec_kw = dict(hspace=0.01, wspace=0.01))
    #
    #     for i, ax in enumerate(axes.flat):
    #         print(len(cluster_clips[cluster_id]))
    #         if i == len(cluster_clips[cluster_id]):
    #             break
    #         ax.imshow(faces.iloc[cluster_clips[cluster_id][i]].values.reshape(200,200),cmap='gray')
    #
    #     plt.savefig('love_cluster_{}.png'.format(cluster_id))
    #
    #     visualize_one_cluster(cluster_id,cluster_clips[cluster_id],leaves,g0,threshold,f)


# pca_for_faces()
