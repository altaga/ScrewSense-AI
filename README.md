# ScrewSense AI
 This project is a screw defect detection system inspired by the defect detection kit project.

<img src="https://i.ibb.co/h1p7nRp/image.png" width="1000">

# Fast Links:

### Video Demo:

Video Demo: Click on the image
[![ScrewVideo](https://i.ibb.co/h1p7nRp/image.png)](pending...)

# Introduction:

In the realm of modern manufacturing, precision and quality are essential. The process of screw manufacturing involves intricate steps, from the initial material selection to the final threading and coating. With the rise of automation and Industry 4.0, Artificial Intelligence (AI) has emerged, the efficiency and accuracy of various manufacturing processes can be possible.

<img src="https://i.ibb.co/6sHtKZr/image.png" width="1000">

# Problem:

There are several problems associated with bad manufacturing, and these issues can have far-reaching consequences. Here are some key problems:

- Product Quality Issues: Poor manufacturing can result in defects, irregularities, or inconsistencies in the final product. This compromises the quality of the product and can lead to malfunctions or failures, impacting customer satisfaction and brand reputation.

- Higher Costs: Correcting defects or replacing faulty components can be expensive. Increased production costs, combined with potential warranty claims and recalls, can have a significant financial impact on a company.

- Damaged Reputation: Poor manufacturing practices can tarnish a company's reputation. Word of mouth, online reviews, and negative publicity can spread quickly, leading to a loss of trust among customers and partners. Rebuilding a damaged reputation can be a lengthy and challenging process.

- Legal Consequences: If defective products lead to harm or violate safety regulations, manufacturers may face legal consequences. This can result in lawsuits, regulatory fines, and long-term damage to the company's legal standing.

This solution focuses on leveraging the power of AI to revolutionize screw manufacturing by developing an advanced defect detection system. 

<img src="https://i.ibb.co/cNthVKS/image.png" width="1000">

# Solution:

This innovative solution harnesses the power of OpenVino anomalib python module, using the advanced padim model to seamlessly detect defects in screws This project extends its capabilities to deployment on hardware, particularly utilizing the versatility of a Raspberry Pi. This integration provides a compact and efficient solution for real-time screw inspection, this could be much better on a NUC device.

<img src="https://i.ibb.co/RybNj95/20231216-015712.jpg" width="1000">

## Materials:

Hardware:
- RaspberryPi 4 (4Gb) - x1.
https://www.raspberrypi.com/products/raspberry-pi-4-model-b/
- HD webcam - x1.
https://www.logitech.com/en-eu/products/webcams.html
- LCD Screen - x1.
https://www.alibaba.com/product-detail/Original-3-5-7-10-1_1600479875551.html
- Servo - x1.
https://www.amazon.com/Deegoo-MG996R-digital-engranaje-Helic%C3%B3ptero/dp/B07MFK266B?th=1

Software:
- OpenVino:
https://docs.openvino.ai/2023.2/home.html
- Anomalib
https://github.com/openvinotoolkit/anomalib
- OpenCV:
https://opencv.org/
- Miniconda:
https://docs.conda.io/projects/miniconda/en/latest/
- Raspberry Pi OS:
https://www.raspberrypi.com/software/
  
Online Platforms:
- Google Colab:
https://colab.research.google.com/

## Connection Diagram:

<img src="https://i.ibb.co/N70FDdH/scheme-drawio-1.png" width="1000">

This general connection diagram shows how through a camera we can obtain images of the screws, pass them to the anomalib neural network, make a decision about the state of the screw and display the result on the screen.

# Online Train:

Para poder realizar el entrenamiento y el testing de los modelos de anomalib de la forma mas sencilla posible para liberarlo de forma open source, lo mejor qe se me ocurrio fue realizar un notebook de google colab para que cualquiera pueda entrenar este modelo.

<img src="https://i.ibb.co/TTmk2Qv/image.png" width="1000">

Todo el notebook esta comentado y viene con los ultimos outputs que yo realice, sin embargo si realizas un run all a todo el notebook obtendras los mismos resultados.

[NOTEBOOK](./)

# Board Setup:

In this particular scenario, configuring the Raspberry Pi with Anomalib posed a slight challenge. The Raspberry Pi 4, with Raspberry OS 64 bits, comes with Python 3.11, this version is incompatible with Anomalib (12/16/1994). 

When we complete the configuration of the board we get the following error.

    ValueError: mutable default <class 'timm.models.maxxvit.MaxxVitConvCfg'> for field conv_cfg is not allowed: use default_factory

My solution was to create a virtual environment with [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) and install Python3.10 in this environment, which according to the Anomalib documentation is compatible with this version of Python.

- Install Raspbian in its 64-bit version. https://www.raspberrypi.com/software/


<img src="https://i.ibb.co/SV17s6T/image.png"> 

- Install miniconda and create python3.10 env.

        wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh
        bash Miniforge3-Linux-aarch64.sh
        yes | conda create -n anomalib_env python=3.10

- Install anomalib, openvino and download the main repo.

        git clone https://github.com/openvinotoolkit/anomalib.git
        pip install -e .
        pip install -r anomalib/requirements/openvino.txt

- Once this is done, you can use any inference model you have trained in Colab. The files used in the demo are located in the [ScrewsClassifier](./ScrewsClassifier/).

# The Final Product:

### Complete System:

<img src="https://i.ibb.co/Cvv8dQF/20231216-015652.jpg" width="49%"> <img src="https://i.ibb.co/4t2xtXC/20231216-015712.jpg" width="49%">

# EPIC DEMO:

Video: Click on the image
[![ScrewVideo](https://i.ibb.co/h1p7nRp/image.png)](pending...)

# Table of contents

- [ScrewSense AI](#screwsense-ai)
- [Fast Links:](#fast-links)
    - [Video Demo:](#video-demo)
- [Introduction:](#introduction)
- [Problem:](#problem)
- [Solution:](#solution)
  - [Materials:](#materials)
  - [Connection Diagram:](#connection-diagram)
- [Online Train:](#online-train)
- [Board Setup:](#board-setup)
- [The Final Product:](#the-final-product)
    - [Complete System:](#complete-system)
- [EPIC DEMO:](#epic-demo)
- [Table of contents](#table-of-contents)
