# 04 Training and Tracking with Colab

## Introduction

AlphaTracker is tested in Linux systems broadly and those systems that have GPUs. However, if you would do not have Linux-compatible system or do not have access to consumer GPUs, you can use Google Colab for the purposes of training and tracking Alphatracker!

## An Important Notice Before You Continue:

Google Colab is only useful for training and inference purposes. If you have a fully-labeled set of data using the Alphatracker annotation tool, continue on...if you have NOT labeled your data, **please complete this step first!**

### Step 1:

Find your folder/folders of data that contain the training images and the JSON annotated files. 

Open your Google Drive, and upload the folder/folders, and the videos you want to label, into the Drive under the main `My Drive` folder. Ensure that your Drive has ample storage after uploading the files!!

### Step 2: 

Open the `alphatrackerCOLAB.ipynb`, which can be found at this [link here]. You have now opened your Python session

### Step 3:

Click `Runtime` and then `Change runtime type`...from the dropdown menu, select `GPU`. 

### Step 4: 

Now, we will connect our Python session to our Google Drive. Press the play button next to the code block to run the first cell. You will be prompted with an authorization link. Click this link and follow the instructions...select the Google Drive account to which you have uploaded your data from `Step 1`. Paste the authorization code back into the prompt box. 

Run the second code block...**this is an important note**: The main `My Drive` folder has the following path: `/content/drive/My Drive`. We are now inside this main folder

### Step 5:

Run the following code block to download `Alphatracker` into your Google Drive...Wait a minute or two, then go to your `My Drive` folder...you should notice a new folder by the name `Alphatracker` has appeared. 

#### **THIS FOLLOWING IS CRUCIAL:**

Go into the newly created `Alphatracker` folder. Find the subfolder entitled `01 Tracking`. **Rename this folder to `01_Tracking`...add an underscore between the "01" and "Tracking"**

### Step 6:

In the following code block, in the variable `image_root_list`, enter the path to all your image folders...

Remember, the main `My Drive` folder has the path `/content/drive/My Drive`...therefore, a folder named `Images` that is under the main `My Drive` folder would have the path `/content/drive/My Drive/Images`. This is what you should type. For example, `image_root_list = ['/content/drive/My Drive/Folder1', '/content/drive/My Drive/Folder2']` and etc...

### Step 7: 

Now, find the `setting.py` file inside the `Alphatracker` directory: The file should be located in `/Alphatracker/01_Tracking/Alphatracker/setting.py`.

**Open this file using the `Text Editor` and NOT Google Docs!!**


