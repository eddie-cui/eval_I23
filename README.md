# Evaluation of Image to 3D Methods

## Introduction
This repository is used to evaluate the performance of various methods for generating 3D models from a single image in a small dataset with diversity. 

First of all, we need to have a division of labor to run the results of various methods, and then run the evaluation indicators of the corresponding methods. 

We hope that you will try to complete it by **July 24, 2024**. 

The following are the methods that need to be assessed, with parentheses representing the members responsible for the methodology:
## Methods to evaluate
### Image to 3D Methods
- [] [Zero-1-to-3 ++](https://github.com/SUDO-AI-3D/zero123plus) (ckq)
- [] [CRM](https://github.com/thu-ml/CRM) (yl)
- [] [Era3D](https://github.com/pengHTYX/Era3D) (xf)
- [] [InstantMesh](https://github.com/TencentARC/InstantMesh) (yl)
- [] [SyncDreamer](https://github.com/liuyuan-pal/SyncDreamer/tree/main) (ckq)
- [] [ViVid-1-to-3](https://github.com/ubc-vision/vivid123) (wyh)
- [] [Wonder3d](https://github.com/xxlong0/Wonder3D) (xf)
- [] [Free3D](https://github.com/ubc-vision/vivid123) (wyh)

## Dataset
We use datasets including 30 objects in SyncDreamer and 70 objects which randomly chosen. [link](https://drive.google.com/file/d/1-2vuKdzsV44z_g86pFBs-lLxu6-hh55a/view?usp=drive_link)

The dataset can be rendered according to the following content to specify the viewing angle, if necessary, you can render it yourself.

### Render the result of the specified perspective
0. Download blender script from [utl](https://download.blender.org/release/Blender3.2) and unzip it at current path.
1. Replace the desired degrees in [view_ls.txt](view_ls.txt). The first column points to elevation and the second column points to azimuth. 
2. Run 
```
blender-3.2.2-windows-x64\blender.exe --background --python blender_script.py -- --object_path <Path to mesh> --output_dir <Path to outputs>  --num_images <Number of rendered images>
```
You can set cammera distance through ```--camera_dist <float>``` which default is 2. 

    eg. 
    ``` 
    blender-3.2.2-windows-x64\blender.exe --background --python blender_script.py -- --object_path \\tsclient\F\kaogu\ti_dataset_mesh\Ecoforms_Cup_B4_SAN\meshes\model.obj --output_dir \\tsclient\F\kaogu\ti_dataset_mesh\Ecoforms_Cup_B4_SAN  --num_images 7
    ```

3. Organize the files in following format:
    ```
    <case_name>
    |-- <case_name>-gt (rendered by yourself)
        |-- 000-depth.png        # target depth map for each view
        |-- 000.png        # target image for each view
        |-- 001-depth.png 
        |-- 001.png
        ...
        |-- meta.pkl     # camera infomation
    |-- <case_name>-mesh           
        |-- materials    
        |-- meshes 
            |-- models.mtl    
            |-- models.obj    # target mesh
            |-- texture.png    
        |-- thumbnails
        ...
    ...
    ```

### Batch rendering 
You can batch render cases in the dataset via script `render_datasets.py`. A version of the 35 views rendered by WYH is provided [here](https://drive.google.com/file/d/1SUUY9CS3WCnx4V5Q8Axc-DZZ2hXvgd7B/view?usp=drive_link), and the details of the views are in `view_ls.txt`. This dataset also has a copy on the server `D:\GSO_render_datasets`.
### Prompts generation
For methods can use text prompts, you can get text prompts in `prompts.csv` which are collected from object description.    



## Evaluation Metrics
0. Run specific method and *tuning hyperparameters*  (set voxel_size=0.5 if possible)
tips：
- If you encounter some problems in the installation, please google it first. Most of the issues have a solution in github issues.
- It is recommended to install the repository on the Windows system, most methods use Open3d, which is not feasible in the Liunx system of the Shanghai science and technology cluster.

### Evaluation for rendered images 
```
python eval_nvs.py --gt <Path to ground truth> --pr <Path to rendered images>  --name <Case Name> --num_images <Number of evaluated images>
```
For example
```
python eval_nvs.py --gt D:\wyh\eval_I23\Ecoforms_Plant_Container_FB6_Tur\Ecoforms_Plant_Container_FB6_Tur-gt --pr D:\wyh\InstantMesh\outputs\instant-mesh-large\images\Ecoforms_Plant_Container_FB6_Tur  --name InstantMesh --num_images 6

```
Before running teh command, please read these items:
1. GT images are named as format: 000.png, 001.png 002.png ... 
2. The result will be saved in ```./logs/metrics/nvs.log```
3. Both GT images and predicted images will be preprocessed and saved in preprocessed folder in <Path to rendered images>
4. Download SAM checkpoint [here](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth) and mode to ```./ckpts```

### Evaluation for mesh
This version need to be tested. Please wait for updating.
```
# Optional (If encounter "DistutilsPlatformError", use it)
SET DISTUTILS_USE_SDK=1
SET MSSdk=1

python eval_mesh.py --pr_mesh <Path to predicted mesh directory> --pr_type "mesh" or "pcd"   --gt_mesh <Path to ground truth directory> --gt_mesh_colmap <Path to ground truth colmap directory> --gt_mesh_mask <Path to ground truth mesh> --downsample
```
For example
```
python eval_mesh.py --pr_mesh D:\wyh\InstantMesh\outputs\instant-mesh-large\meshes\Ecoforms_Plant_Container_FB6_Tur.obj --name instantmesh --camera_info_dir Ecoforms_Plant_Container_FB6_Tur\Ecoforms_Plant_Container_FB6_Tur-gt --num_images 12 --gt_mesh Ecoforms_Plant_Container_FB6_Tur\Ecoforms_Plant_Container_FB6_Tur-mesh\meshes\model.obj --output logs
```

## Reporting Results
Present the evaluation results in a clear and concise manner. The visualization results and tables should be illustrated in [slides](./res.pptx). 
The slides should include:
1. Method name
2. Hyperparameters of method (iterations, training dataset size, tese dataset size)
3. Visualization rendered color results, normal map  (GT and rendered)
4. Visualization of mesh (if the format can be inserted in slides)

## Conclusion
Please communicate in a timely manner

## Related projects
We collect code from following projects. We thanks for the contributions from the open-source community!
[SyncDreamer](https://github.com/liuyuan-pal/SyncDreamer/tree/main)

[DTUeval-python](https://github.com/jzhangbs/DTUeval-python)

[TanksAndTemples](https://github.com/isl-org/TanksAndTemples/tree/master)