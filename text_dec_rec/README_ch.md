## 简介
PP-OCR是一个由DB文本检测、检测框矫正和CRNN文本识别三部分组成的系统。

## 特性
- PPOCR系列高质量预训练模型，准确的识别效果
    - 通用ppocr_server系列：检测（47.1M）+方向分类器（1.4M）+ 识别（94.9M）= 143.4M
- 可运行于Linux、Windows、MacOS等多种系统

## 文档教程
- 算法介绍
    - [文本检测](./doc/doc_ch/algorithm_overview.md)
    - [文本识别](./doc/doc_ch/algorithm_overview.md)
## 快速安装
- 工作环境
- PaddlePaddle 2.0.0
- python3.7
- cuDNN 7.6+ (GPU)

**1. 环境配置**
  ```
  创建环境：
      conda creat --name ppocr python=3.7
  激活环境：
      conda activate ppocr    
  ```  
**2. 安装PaddlePaddle 2.0**
  ```
  pip install --upgrade pip
  
  如果您的机器安装的是CUDA9或CUDA10，请运行以下命令安装
  pip install paddlepaddle-gpu==2.0.0 -i https://mirror.baidu.com/pypi/simple
  
  如果您的机器是CPU，请运行以下命令安装
  
  pip install paddlepaddle==2.0.0 -i https://mirror.baidu.com/pypi/simple
  
  ```
  
**3. 安装第三方库**
  ```  
  pip install -r requirements.txt
  ```

  注意，windows环境下，建议从(https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely)下载shapely安装包完成安装，
  直接通过pip安装的shapely库可能出现`[winRrror 126] 找不到指定模块的问题`。
  如果是windows系统的话，首先把安装的shapely卸载：
  ```  
  pip uninstall shapely
  ```
  然后将上面链接下载的文件放到环境的Scripts文件夹中 如：D:\anaconda\envs\ppocr\Scripts
  ```  
  pip install somewhat.whl
  ```  
  somewhat.whl 为下载的文件名
## 运行
  
  ```
  python tools/infer/predict_system.py --image_dir="./doc/imgs/9.png" --det_model_dir="D:/Someprograms/text_dec_rec/inference/ch_ppocr_server_v2.0_det_infer/"  --rec_model_dir="D:/Someprograms/text_dec_rec/inference/ch_ppocr_server_v2.0_rec_infer/" --cls_model_dir="D:/Someprograms/text_dec_rec/inference/ch_ppocr_mobile_v2.0_cls_infer/" 
  ```
  同样可以在tools/infer/utility.py 中修改default值。 
  image_dir 为待检测的图片，部分实验图片存放在./doc/imgs/ ， 结果存放在tools/infer/inference_results/
## 更多信息

    https://github.com/PaddlePaddle/PaddleOCR
