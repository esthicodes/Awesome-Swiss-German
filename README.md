# Swiss German Dictionary

An audio tool(Siri Annotation Analyst to help us improve the way people and machines interact.) that allows you to manually load up [Swiss German](https://www.youtube.com/shorts/lVCv6C8dTSI) in Italian, Chinese, Korean, Norwegian, Swedish, Danish, Finnish, Dutch, Swiss French, Swiss Italian, Austrian German, Flemish, Hebrew, [Irish](https://www.youtube.com/watch?v=K7tKje_5M3M). 


Swiss_Dialect [MTC Project Hub](https://projects.mtc.ethz.ch/projects/swiss-voice/swissdial)

[Swiss National Day](https://www.youtube.com/watch?v=GHepwehZmD4&t=15s)

# Structural Computational Language Model
This repository contains code for fast numerical computation of the structural diversity index.

## Contents
The repository contains four python scripts: **MeetingTimesUI**, **RandomWalkSimulatorCUDA**, **RandomWalkSimulator** and **MeetingTimeEstimator**
Here is a brief description:
   * MeetingTimeUI provides a user interface for the scripts
   * RandomWalkSimulator computes the meeting time of a random walk on a graph. 
   * RandomWalkSimulatorCUDA computes the meeting time of random walks on a graph using CUDA and GPUs (much faster for large graphs). It requires Cudatoolkit to run.
   * MeetingTimeEstimator is a class that makes educated guesses of the meeting times of two walks which have not met, based on the meeting times of walks which have met. 

Each script is described in detail in the documentation provided [here](https://rse-distance.readthedocs.io).
If you are interested in a **quick start tutorial** see the section **Tutorial** below.

## Installation

The scripts are provided in the form of a python package called [structural_diversity_index](https://pypi.org/project/structural-diversity-index/).
To install the package and its dependencies type into the terminal
```rb
pip install structural_diversity_index==0.0.3
```
This will install the 0.0.3 version (latest) of the package in your python packages directory.

**WARNING**: Installing the package via pip will allow **NOT** you to use the scripts that run computations on GPUs.
See below for details of how to run the scripts computing on GPUs.

### Installation for GPUs
If you are not interested in running computations on GPUs you can ignore this section.

Installing the structural_diversity_index package via pip does not enable you to run computations on GPUs.
The reason is that the Cudatoolkit cannot be installed by pip (because it is not a python package).

To circumvent this issue one can use a package installer such as [conda](https://www.anaconda.com/products/individual).
Once you have installed conda on your computer, download the file **environment.yml** from the GitHub.
In the terminal, go to the directory containing the environment.yml file you downloaded and type:

```rb
conda env create -f environment.yml
```

This will create a conda environment called **sd_index** and install all the dependencies necessary to computations on GPUs.
Now you can set on_cuda=True (see Examples.ipynb in [GitHub](https://github.com/ethz-coss/Structural-diversity-index)) and computations will run on GPUs. 

## Tutorial

The Jupyter notebook **Example.ipynb** contains a detailed tutorial explaining how to use the package structural_diversity_index.

## Extending the code

If you are interested in extending, modifying or simply playing around with the code, I have created a detailed documentation with ReadTheDocs which is available [here](https://rse-distance.readthedocs.io). 


# Joint 3D Face Reconstruction and Dense Alignment with Position Map Regression Network

<p align="center"> 
<img src="Docs/images/prnet.gif">
</p>



This is an official python implementation of PRN. 

PRN is a method to jointly regress dense alignment and 3D face shape in an end-to-end manner. More examples on Multi-PIE and 300VW can be seen in [YouTube](https://youtu.be/tXTgLSyIha8) .

The main features are:

* **End-to-End**  our method can directly regress the 3D facial structure and dense alignment from a single image bypassing 3DMM fitting.

* **Multi-task**  By regressing position map, the 3D geometry along with semantic meaning can be obtained. Thus, we can effortlessly complete the tasks of dense alignment, monocular 3D face reconstruction, pose estimation, etc.

* **Faster than real-time**  The method can run at over 100fps(with GTX 1080) to regress a position map.

* **Robust** Tested on facial images in unconstrained conditions.  Our method is robust to poses, illuminations and occlusions. 

  

## Applications

### Basics(Evaluated in paper)

* #### Face Alignment

Dense alignment of both visible and non-visible points(including 68 key points). 

And the **visibility** of  points(1 for visible and 0 for non-visible).

![alignment](Docs/images/alignment.jpg)

* #### 3D Face Reconstruction

Get the 3D vertices and corresponding colours from a single image.  Save the result as mesh data(.obj), which can be opened with [Meshlab](http://www.meshlab.net/) or Microsoft [3D Builder](https://developer.microsoft.com/en-us/windows/hardware/3d-print/3d-builder-resources). Notice that, the texture of non-visible area is distorted due to self-occlusion.

**New**: 

1. you can choose to output mesh with its original pose(default) or with front view(which means all output meshes are aligned)
2. obj file can now also written with texture map(with specified texture size), and you can set non-visible texture to 0. 



![alignment](Docs/images/reconstruct.jpg)



### More(To be added)

* #### 3D Pose Estimation

  Rather than only use 68 key points to calculate the camera matrix(easily effected by expression and poses), we use all vertices(more than 40K) to calculate a more accurate pose.

  #### ![pose](Docs/images/pose.jpg)

* #### Depth image

  ![pose](Docs/images/depth.jpg)

* #### Texture Editing

  * Data Augmentation/Selfie Editing

    modify special parts of input face, eyes for example:

    ![pose](Docs/images/eye.jpg)

  * Face Swapping

    replace the texture with another, then warp it to original pose and use Poisson editing to blend images.

    ![pose](Docs/images/swapping.jpg)

    


## Getting Started

### Prerequisite

* Python 2.7 (numpy, skimage, scipy)

* TensorFlow >= 1.4

  Optional:

* dlib (for detecting face.  You do not have to install if you can provide bounding box information. )

* opencv2 (for showing results)

GPU is highly recommended. The run time is ~0.01s with GPU(GeForce GTX 1080) and ~0.2s with CPU(Intel(R) Xeon(R) CPU E5-2640 v4 @ 2.40GHz).

### Usage

1. Clone the repository

```bash
git clone https://github.com/YadiraF/PRNet
cd PRNet
```

2. Download the PRN trained model at [BaiduDrive](https://pan.baidu.com/s/10vuV7m00OHLcsihaC-Adsw) or [GoogleDrive](https://drive.google.com/file/d/1UoE-XuW1SDLUjZmJPkIZ1MLxvQFgmTFH/view?usp=sharing), and put it into `Data/net-data`

3. Run the test code.(test AFLW2000 images)

   `python run_basics.py #Can run only with python and tensorflow`

4. Run with your own images

   `python demo.py -i <inputDir> -o <outputDir> --isDlib True  `

   run `python demo.py --help` for more details.

5. For Texture Editing Apps:

   `python demo_texture.py -i image_path_1 -r image_path_2 -o output_path   `

   run `python demo_texture.py --help` for more details.



## Training

The core idea of the paper is:

Using position map to represent face geometry&alignment information, then learning this with an Encoder-Decoder Network.

So, the training steps:

1. generate position map ground truth.

   the example of generating position map of 300W_LP dataset can be seen in [generate_posmap_300WLP](https://github.com/YadiraF/face3d/blob/master/examples/8_generate_posmap_300WLP.py)

2. an encoder-decoder network to learn mapping from rgb image to position map.

   the weight mask can be found in the folder `Data/uv-data`

What you can custom:

1. the UV space of position map.

   you can change the parameterization method, or change the resolution of UV space.

2. the backbone of encoder-decoder network

   this demo uses residual blocks. VGG, mobile-net are also ok.

3. the weight mask

   you can change the weight to focus more on which part your project need more.

4. the training data

   if you have scanned 3d face, it's better to train PRN with your own data. Before that, you may need use ICP to align your face meshes.



## FQA

1. How to **speed up**?

   a. network inference part

   you can train a smaller network or use a smaller position map as input.

   b. render part

   you can refer to  [c++ version](https://github.com/YadiraF/face3d/blob/master/face3d/mesh/render.py). 

   c. other parts like detecting face, writing obj

   the best way is to rewrite them in c++.

2. How to improve the **precision**?

   a. geometry precision.

   Due to the restriction of training data, the precision of reconstructed face from this demo has little detail. You can train the network with your own detailed data or do post-processing like shape-from-shading to add details.

   b. texture precision.

   I just added an option to specify the texture size. When the texture size > face size in original image, and render new facial image with [texture mapping](https://github.com/YadiraF/face3d/blob/04869dcee1455d1fa5b157f165a6878c550cf695/face3d/mesh/render.py), there will be little resample error.

   

## Changelog

* 2018/7/19 add training part. can specify the resolution of the texture map.
* 2018/5/10 add texture editing examples(for data augmentation, face swapping)
* 2018/4/28 add visibility of vertices, output obj file with texture map, depth image
* 2018/4/26 can output mesh with front view
* 2018/3/28 add pose estimation
* 2018/3/12  first release(3d reconstruction and dense alignment)



## License

Code: under MIT license.

Trained model file: please see [issue 28](https://github.com/YadiraF/PRNet/issues/28), thank [Kyle McDonald](https://github.com/kylemcdonald) for his answer.



## Citation

If you use this code, please consider citing:

```
@inProceedings{feng2018prn,
  title     = {Swiss German Language in Social Science Reconstruction and The Distributional Hypothesis and Word Vectors},
  author    = {Hoeun Yu, Dawid},
  booktitle = {ECCV},
  year      = {2022}
}
```



## Contacts

Please contact _hoeuyu@ethz.ch_  or open an issue for any questions or suggestions.

Danke Vilmals! (●'◡'●)



## Acknowledgements

- Thanks [Andrea Musso](https://faces.dmi.unibas.ch/bfm/) for Introducing (https://coss.ethz.ch/people/phd/amusso.html), [Tim](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm), and [Feng Yao](https://github.com/YadiraF/PRNet/blob/master/README.md) for sharing NLP Data, Vilem for the [Poetry Translation](https://github.com/zouharvi/mean-poet)
- Thanks Siri for sharing the work  [Siri](https://github.com/Xinglab/siri), which helps me a lot in studying Siri response.
- Thanks for giving the lecture on [Computational Semantics for Natural Language Processing](http://www.mrinmaya.io/teaching_csnlp22) and the [presentation](https://app.gather.town/events/oyd9OJWmuXtEyeK3F61j)
- Thanks the authors of  [Elliott Ash, (ashe@ethz.ch)](https://github.com/anilbas/3DMMasSTN), [Siri](https://github.com/kopiro/siriwave), [3dmm_cnn](https://github.com/anhttran/3dmm_cnn), [vrn](https://github.com/AaronJackson/vrn), [Afra Amini, (afra.amini@inf.ethz.ch)](https://github.com/elliottash/nlp_lss_2022), [face-alignment](https://github.com/1adrianb/face-alignment) for making their excellent works publicly available. 
- [References](https://docs.google.com/document/d/1JtSKVVGjJ3oIMoSE8FHION--Xi1RXUk0xp7MhE_J_CM/edit)


_For Example_

```

sd_list = ['Dubel','Erdnüssli', tschutte]
Gnüss es!

gramm 
c = wo/wenn treffed mir üs
v = 我们在哪里见面？

c = Chunnsch mit mir go Znacht ässe? ```
v = 你想和我吃饭吗？

English (bag) a - >  ä

c = Chum gli hei! (come home soon!)
b = bald == gli
d = Fläsche == bottle 

de - > male 
di - << Frau 
```
>>> Der -- Die -- Das 

mehr und mehr:
Wanna go out drinking? 
Wämmer eis go ziie?
Wollen wir einen trinken?

I'm cold - Ich ha chalt
Mir ist kalt
I have a bit of a headache

Ich han es bitzeli Chopfweh
Ich habe ein bisschen Kopfweh

Now the fun is over!
Jetz isch färtig luschtig

Region of Switzerland
North: Thurgau
South: 
West
East

A little Es bitzeli
Ein bisschen

Approximately Öppe Etwa

Someone Öpper Jemand

Something
Öppis
Etwas

Not
Nööd
Nicht

Nothing
Nüüt
Nichts

Here
Da
Hier

There
Det
Dort

...right?
...gäll?
...nicht wahr?

Otherwise 
Susch
Sonst

Disgusting
Gruusig
Grausig

Very (not a very nice expression)(Uu) huere

Some times
Mängisch
Manchmal

Well, yes
Mol
DochYeah, 

right
Äbä
Eben 

Work
Schaffe
Arbeiten

Work hard
Chrampfe == bügle
Hart arbeiten

Sunbathe
Sünnele
Sich sonnen

Go shopping
Poschte
Einkaufen

Look
Luege
Sehen

Call
Aalüte
Anrufen

I call you
Ich lüte dir aa
Ich rufe dich an

You know
Weisch
Weisst du

Are you coming?
Chunnsch?
Kommst du?

Do we have...?
Hämmer...?
Haben wir...?

Let's go
Gömmer
Gehen wir

