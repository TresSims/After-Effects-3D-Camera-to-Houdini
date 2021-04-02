# After-Effects-3D-Camera-to-Houdini
This repository holds code for a plugin to import AfterEffects 3D Camera data into a Houdini Scene, with some customization

This repository is based on a gist by https://gist.github.com/howiemnet which can be found here: https://gist.github.com/howiemnet/8784cf04568c849271730965eaf35159

Installation Instructions:
1. Right Click on the shelf > New Tool
2. Copy and paste the contents of HPlugin.py into the script section of the new tool
3. Change the ui_file variable to point to the ui file in your cloned directory.

Usage instructions:
1. Copy keyframes from after effects, and paste them into a .txt file
2. Click on the tool in your shelf
3. Select the .txt file with your 3D camera keyframes
4. Select the camera object you want to apply the frames to (you can technically use any node with translate and rotate parameters)
5. Dial in your scale settings based on your scene in AE and houdini
6. Press Import

Roadmap:
1. Orientation modification options
2. After Effects plugin to create keyfame data
3. Installer
