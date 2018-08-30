# Multiple images generate HDRI 
## Project Description
Here you'll see two method to generate high dynamic range image. 
The one, first step, from multiple consistent images with different exposure time,  we can calibrate the camera response function curve. Second step, with this CRF, we can merge HDRI, but it can't be showed in your monitor. Thirdly, tonemapping LDRI so that you could see it.
The other one, from multiple images can be no exposure time, we can fusion HDRI directly.

## Toolbox Package Structure
* aux_lib, directory, contain some auxilliary library
* configure_file, directory, contain some configure file
* core_lib, directory, contain my hdr core library
* other, directory, contain some visual data
* result_img, directory, contain hdr result images
* test_img, directory, contain test source images
* demo.py, file, just a demo

## My Runtime Enviroment
```
System: Ubuntu14.04
Libraries: openCV3.2.0, matplotlib, FileInterfaceTool, etc.
```

## Running the tests
```
cd HDRTool/
python demo.py 
```
setting the configure file as following :
![alt text][configure_img]

calibrate crf curve:
![alt text][crf_img]

test_src_img:
![alt text][src_img0]
![alt text][src_img1]
![alt text][src_img2]

merge hdr result:
![alt text][hdr_merge]
fusion hdr result:
![alt text][hdr_fusion]

## Versioning
```
    1.0
```

## Authors
```
* **gimbu CUI** - *Initial work* - [gimbu][contributor]
```

## License

This project is licensed under the PI License 

## Acknowledgments

* you should know what HDR is
* etc

[src_img0]:https://cloud.githubusercontent.com/assets/20764967/24739132/fe58c770-1acc-11e7-8d89-3a41b0c3ae0b.png "src_img0"
[src_img1]:https://cloud.githubusercontent.com/assets/20764967/24739145/0fdebff4-1acd-11e7-92ee-0e045cb0ce61.png "src_img1"
[src_img2]:https://cloud.githubusercontent.com/assets/20764967/24739131/fe44fccc-1acc-11e7-9acb-30677f334c15.png "src_img2"
[crf_img]:https://cloud.githubusercontent.com/assets/20764967/24740985/79298850-1ad6-11e7-8f82-72f3357b082f.png "crf_img"
[configure_img]: https://cloud.githubusercontent.com/assets/20764967/24741073/f7f682dc-1ad6-11e7-9fca-00048ae12743.png "configure_img"
[hdr_merge]: https://cloud.githubusercontent.com/assets/20764967/24735525/ed42612e-1ab5-11e7-9904-f76591e6af42.png "Merge HDR"
[hdr_fusion]: https://cloud.githubusercontent.com/assets/20764967/24735538/fdc39a22-1ab5-11e7-8d59-1f3c2986b2c1.png "Fusion HDR"
[contributor]:https://github.com/

