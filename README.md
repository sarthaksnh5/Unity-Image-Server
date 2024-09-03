# Unity Image Loader

## Overview

This Unity project demonstrates how to fetch images from a Flask server and apply them to materials in Unity. The `ImageLoader` script handles the process of downloading images from a given API and updating materials on 3D objects in the scene.

## Prerequisites

- Unity (version compatible with the Newtonsoft.Json package or using Unity's JsonUtility)
- A running Flask server with an API endpoint providing image data
- Basic understanding of Unity’s UI and scripting

## Project Setup

### 1. Setting Up the Flask Server

Ensure that your Flask server is running and accessible at `http://127.0.0.1:5000/images`. The API should return a JSON response similar to:

```json
{
  "current_page": 1,
  "images": [
    {
      "created_on": "Tue, 03 Sep 2024 06:53:38 GMT",
      "id": "9e5c18a5-aa93-45d7-81d6-6ae1183bd0b8",
      "image_name": "Sarthak",
      "image_url": "http://localhost:5000/static/uploads/b2947a6f-a855-4c53-b5e7-df188dc278a8_DJI_0415.JPG"
    }
  ],
  "pages": 1,
  "total": 1
}
```

### 2. Setting Up the Unity Project

1. Create a New Unity Project:
    * Open Unity and create a new project.

2. Add the ImageLoader Script:
    * Create a new C# script named ImageLoader.cs and copy the provided code into this file.
    * Attach this script to an empty GameObject in your scene.

3. Configure the Script:
    * In the Unity Editor, select the GameObject with the ImageLoader script.
    * Assign the materials you want to update to the Materials list in the script component.    

### 3. Running the Project

* Ensure that your Flask server is running and serving image data.
* Press the Play button in Unity to start the scene.
* The script will fetch images from the API and apply them to the materials assigned in the Inspector.

## Troubleshooting

* `Server Not Responding`: Ensure your Flask server is running and accessible at the specified URL.
* `Image Not Applying`: Check the console for errors related to image fetching or texture application.
* `Material Not Updating`: Verify that the materials are correctly assigned to the materials list in the `ImageLoader` script.

## Contact

For questions or issues, please contact [Sarthak Lamba](emailto:sarthaksnh5@gmail.com).