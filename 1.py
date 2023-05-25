import subprocess

def kill_explorer():
  # Open Task Manager
  task_manager = subprocess.Popen("taskmgr")

  # Wait for Task Manager to open
  while not task_manager.poll():
    pass

  # Right-click on "Windows Explorer"
  subprocess.Popen(["taskmgr", "/f", "/im", "explorer.exe"])

  # Click "End Task"
  subprocess.Popen(["taskmgr", "/i", "/t", "explorer.exe"])

  # Close Task Manager
  task_manager.terminate()

if __name__ == "__main__":
  kill_explorer()
