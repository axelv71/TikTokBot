# Delete all mp4 files in the current directory and all subdirectories

import os
import glob

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".mp4"):
            os.remove(os.path.join(root, file))

