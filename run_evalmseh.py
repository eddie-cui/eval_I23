import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import subprocess

# 根路径
method_path = 'D:\chz\output'
gt_im_tree_path = 'D:\potterylike_dataset_meshes_transformed_images'
gt_mesh_tree_path = 'D:\potterylike_dataset_meshes_transformed'

# 设置 num_images 常量
num_images = 35

# 获取文件夹下的所有子文件夹
def get_subdirectories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

for i in range(1,56):
    subdir=str(i)
    pr_mesh = os.path.join(method_path, subdir,'0','mesh.obj')
    camera_info_dir = os.path.join(gt_im_tree_path, subdir,'model')
    gt_mesh = os.path.join(gt_mesh_tree_path, subdir, 'model.obj')
    command = f'python eval_mesh.py --pr_mesh {pr_mesh} --name TripoSR_{subdir} --camera_info_dir {camera_info_dir} --num_images {num_images} --gt_mesh {gt_mesh} --output TripoSR'
    # 打印并执行命令
    
    print(f'执行命令: {command}')
    subprocess.run(command, shell=True)
print("TripoSR finished")

method_path = 'D://chz/free3d_output/mesh'
for i in range(1,56):
    subdir=str(i)
    pr_mesh = os.path.join(method_path, subdir, 'it30000-mc512.obj')
    camera_info_dir = os.path.join(gt_im_tree_path, subdir,'model')
    gt_mesh = os.path.join(gt_mesh_tree_path, subdir, 'model.obj')
    command=f'python postprocess_mesh.py --input {pr_mesh} --num_cluster 1'
    # 构建终端命令
    print(f'执行命令: {command}')
    subprocess.run(command, shell=True)
    pr_mesh = os.path.join(method_path, subdir,'it30000-mc512')
    # 构建终端命令
    command = f'python eval_mesh.py --pr_mesh {pr_mesh}_post.ply --name Free3D_{subdir} --camera_info_dir {camera_info_dir} --num_images {num_images} --gt_mesh {gt_mesh} --output Free3d'
    
    # 打印并执行命令
    print(f'执行命令: {command}')
    subprocess.run(command, shell=True)
print("Free3D finished")
method_path = 'D://chz/sync_output/mesh'
for i in range(1,56):
    subdir=str(i)
    pr_mesh = os.path.join(method_path, subdir, 'it30000-mc512.obj')
    camera_info_dir = os.path.join(gt_im_tree_path, subdir,'model')
    gt_mesh = os.path.join(gt_mesh_tree_path, subdir, 'model.obj')
    command=f'python postprocess_mesh.py --input {pr_mesh} --num_cluster 1'
    # 构建终端命令
    print(f'执行命令: {command}')
    subprocess.run(command, shell=True)
    pr_mesh = os.path.join(method_path, subdir,'it30000-mc512')
    # 构建终端命令
    command = f'python eval_mesh.py --pr_mesh {pr_mesh}_post.ply --name SyncDreamer_{subdir} --camera_info_dir {camera_info_dir} --num_images {num_images} --gt_mesh {gt_mesh} --output Syncdreamer'
    
    # 打印并执行命令
    print(f'执行命令: {command}')
    subprocess.run(command, shell=True)
print("SyncDreamer finished")