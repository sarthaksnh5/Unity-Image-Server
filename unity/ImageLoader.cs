using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System;

public class ImageLoader : MonoBehaviour
{
    public List<Material> materials; // Assign this from the Unity Editor
    private readonly string url = "http://127.0.0.1:5000/images";
    private int materialIndex = 0;

    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(FetchAndApplyImages());
    }

    IEnumerator FetchAndApplyImages()
    {
        using (UnityWebRequest request = UnityWebRequest.Get(url))
        {
            yield return request.SendWebRequest();

            if (request.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError("Error fetching images: " + request.error);
            }
            else
            {
                ProcessResponse(request.downloadHandler.text);
            }
        }
    }

    void ProcessResponse(string jsonResponse)
    {
        ImageApiResponse response = JsonUtility.FromJson<ImageApiResponse>(jsonResponse);

        if (response.images != null && response.images.Length > 0)
        {
            foreach (var image in response.images)
            {
                if (materialIndex < materials.Count)
                {
                    StartCoroutine(LoadImageAndApply(image.image_url, materials[materialIndex]));
                    materialIndex++;
                }
                else
                {
                    break;
                }
            }
        }
    }

    IEnumerator LoadImageAndApply(string imageUrl, Material material)
    {
        using (UnityWebRequest request = UnityWebRequestTexture.GetTexture(imageUrl))
        {
            yield return request.SendWebRequest();

            if (request.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError("Error loading image: " + request.error);
            }
            else
            {
                Texture2D texture = ((DownloadHandlerTexture)request.downloadHandler).texture;
                material.SetTexture("_MainTex", texture); // Apply the texture to the material
            }
        }
    }

    [Serializable]
    public class ImageApiResponse
    {
        public int current_page;
        public ImageData[] images;
        public int pages;
        public int total;
    }

    [Serializable]
    public class ImageData
    {
        public string created_on;
        public string id;
        public string image_name;
        public string image_url;
    }
}
