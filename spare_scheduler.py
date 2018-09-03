import os
import subprocess
import GPUtil


deviceIDs = GPUtil.getAvailable(order='first', limit=3, maxLoad=0.5, maxMemory=0.5)

print(','.join(str(e) for e in deviceIDs))

task_queue_file = os.path.join(os.environ.get("HOME", None), "task_queue.txt")

if not os.path.isfile(task_queue_file):
	sys.exit(0)

task_list = open(task_queue_file).readlines()

print(task_list)

for i in range(min(len(deviceIDs), len(task_list))):
	task = task_list[i].strip() + " --gpu-id=%d" % i
	print(task)
	subprocess.Popen(task, shell=True, cwd="/home/xyang22/project/research/active-learning-dnn")
