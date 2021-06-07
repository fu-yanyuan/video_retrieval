2021 Jun. 7
---

use [PyRetri](https://github.com/PyRetri/PyRetri) to search one frame from a video

## use opencv to extract frames  
[extract_frames_v2.py](https://github.com/fu-yanyuan/video_retrieval/blob/main/code_training/extract_frames_v2.py)  
this will save the frames(1 fps) into the *gallery* as required:  
and press 's' to save the key frames that i want to search in the future into *query*  
```shell
# dataset need to be splited 
v_cars
├── gallery
│    └── honda
│         ├──xxx.jpg
│         └──···
└── query
     └── honda
          ├──xxx.jpg
          └──···
```  

## use PyRetri to do the single frame index  
```shell
# make data json
$ python3 main/make_data_json.py -d data/v_cars/gallery/ -sp data_jsons/v_cars_gallery.json -t general
$ python3 main/make_data_json.py -d data/v_cars/query/ -sp data_jsons/v_cars_query.json -t general
# extract features
$ CUDA_VISIBLE_DEVICES=4 python3 main/extract_feature.py -dj data_jsons/v_cars_gallery.json -sp data/features/v_cars/gallery/ -cfg configs/v_cars.yaml
$ CUDA_VISIBLE_DEVICES=4 python3 main/extract_feature.py -dj data_jsons/v_cars_query.json -sp data/features/v_cars/query/ -cfg configs/v_cars.yaml
# single image index
$ CUDA_VISIBLE_DEVICES=4 python3 main/test_video.py -cfg configs/v_cars.yaml
```   
## experiment results  
[v_cars.mp4](https://www.youtube.com/watch?v=q5PPNZiu52w)  
### query  
<img src="image_3706_q.jpg" width="224"/>  

### top 5 results  

<img src="55.png" width="224"/><img src="56.png" width="224">  
<img src="70.png" width="224"/><img src="72.png" width="224"/><img src="73.png" width="224"/>  

### query  
<img src="image_2812_q.jpg" width="224"/>

### top 5 results  
<img src="16.png" width="224"/><img src="17.png" width="224"/>  
<img src="61.png" width="224"/>   <img src="144.png" width="224"/><img src="145.png" width="224"/>  




