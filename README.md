# YOLO Essential Functions

This repository contains essential functions and scripts for managing YOLO object detection workflows, including label creation, image conversion, and label reclassification.

## Features

- **Convert Annotations**: Scripts for converting label formats.
- **Image Processing**: Convert images for YOLO training.
- **Reclassification**: Update class IDs for annotations.
- **Missing Labels Handling**: Create missing labels for images.
- **File Renaming**: Batch rename images and labels for consistency.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/burakpekisik/yolo_essential_functions.git
   ```

2. Run the desired script:
   - For converting labels:
     ```bash
     python convert.py
     ```

## Available Scripts

- `convert.py`: Converts YOLO labels between different formats.
- `convert_to_image.py`: Converts annotations into labeled images for visualization.
- `create_labels.py`: Generates new labels for missing annotations.
- `reclassify.py`: Reclassifies labels by changing class IDs.
- `rename_images.ipynb`: Renames images based on specified patterns.
- `rename_labels.ipynb`: Renames labels to match image names.

## How to Use

Each script is designed to perform specific tasks related to YOLO annotations and image preparation. Modify parameters as needed within the scripts before execution.

## License

This project is licensed under the MIT License.
