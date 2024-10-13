import os
import subprocess

# 定义基础路径
gt_base_path = r"D:\chz\free3d_output\free3d_orginal"  # Ground truth 的基础路径
pr_base_path = r"D:\potterylike_dataset_meshes_transformed_images"  # Predicted/rendered images 的基础路径

# 定义图像数量
num_images = 35

# 遍历每一个任务目录
for task_id in range(1, 56):
    # 构建 Ground Truth 和 Predictions 的路径
    gt_path = os.path.join(gt_base_path, str(task_id))  # 对应 ground truth 的路径
    pr_path = os.path.join(pr_base_path, str(task_id), "model")  # 对应 predicted/rendered 的路径
    
    # 定义任务名称，动态根据任务编号变化
    case_name = f"free3d_{task_id}"
    
    # 构建命令
    command = f'python eval_nvs.py --gt {pr_path} --pr {gt_path} --name {case_name} --num_images {num_images}'
    
    # 执行命令
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # 输出执行结果
    print(f"Evaluating Task {task_id}:")
    print(result.stdout)
    if result.stderr:
        print(f"Errors: {result.stderr}")
