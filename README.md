# [Swiss German Dictionary](https://www.apple.com/chde/)
![](https://i.imgur.com/dLI4HYM.jpg)

[App Demo](https://www.swiss-german-online.com/app.html)


Used Tools: 

Cloud Run, BigQuery, Virtual Machines with GPUs and Machine Learning APIs, Google Cloud [Speech-to-Text](https://cloud.google.com/speech-to-text)

You can find an overview [here](https://cloud.google.com/products)

Design: 

[Figma](https://www.figma.com/)

Collaboration: 
[FigJam](https://www.figma.com/figjam/)

[wonder.me](http://wonder.me/)

[conceptboard.com](http://conceptboard.com) 

[jamboard.google.com](http://jamboard.google.com/) 

[menti.com](http://menti.com/) 

[retrotool.io](http://retrotool.io/) 

[kahoot.it](http://kahoot.it/)

https://meta.stackexchange.com/questions/38915/creating-an-image-link-in-markdown-format
An audio tool(Siri Annotation Analyst to help us improve the way people and machines interact.) that allows you to manually load up [Swiss German](https://www.youtube.com/shorts/lVCv6C8dTSI) in Italian, Chinese, Korean, Norwegian, Swedish, Danish, Finnish, Dutch, Swiss French, Swiss Italian, Austrian German, Flemish, Hebrew, [Irish](https://www.youtube.com/watch?v=K7tKje_5M3M). 

## Interacting with your Devices

Once your device has been added to SwissGermanBot, you should be able to tell Siri to control your devices. However, realize that Siri is a cloud service, and iOS may need some time to synchronize your device information with iCloud.

One final thing to remember is that Siri will almost always prefer its default phrase handling over SwissGermanBot devices. For instance, if you name your Sonos device "Radio" and try saying "Siri, turn on the Radio" then Siri will probably start playing an iTunes Radio station on your phone. Even if you name it "Esthi" and say "Siri, turn on Esthi", Siri will probably just launch the Esthi app instead. This is why, for instance, the suggested `name` for the Esthi accessory is "Speakers".


Swiss 8 Different Dialects Project on [MTC Project Hub](https://projects.mtc.ethz.ch/projects/swiss-voice/swissdial)

[Have a look at Swiss National Day](https://www.youtube.com/watch?v=GHepwehZmD4&t=15s)

# Structural Computational Language Model
This repository contains code for fast numerical computation of the structural diversity index.

## Contents
The repository contains four python scripts: **MeetingTimesUI**, **ANTLR (ANother Tool for Language Recognition)**, **RandomWalkSimulator** and **MeetingTimeEstimator**
Here is a brief description:
   * ANTLR (ANother Tool for Language Recognition) is a powerful parser generator for reading, processing, executing, or translating structured text or binary files. It's widely used to build languages, tools, and frameworks. From a grammar, ANTLR generates a parser that can build and walk parse trees.
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

### Usage

1. Clone the repository

```bash
git clone https://github.com/Estheryu991/SwissGerman_Dictionary
cd SwissGerman_Dictionary
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
 

## FQA

1. How to **speed up**?

   a. network inference part

   you can train a smaller network or use a smaller position map as input.

   b. render part

   you can refer to  [c++ version](https://github.com/YadiraF/face3d/blob/master/face3d/mesh/render.py). 

   c. other parts like detecting face, writing obj

   the best way is to rewrite them in c++.

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
Jetzt isch färtig luschtig

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
Doch
Yeah, 

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

<p align="center"> 
<img src="Docs/images/ihanfrag.jpeg">
</p>



Let's go
Gömmer
Gehen wir

# Hack Zürich [![HackZürich 2022](https://user-images.githubusercontent.com/78131082/190856349-20963f78-1e1b-4589-8242-828d8fbc66e1.jpeg)](https://www.youtube.com/watch?v=dQQG-GhMxSI)

# Repository for [![Repo](https://github.com/f-dangel/hackzurich2022/blob/main/doc/videos/2228D31D-BE67-4A3C-B093-39E0C4F02F93.mov)](https://github.com/amirrezaeian/Individual-household-electric-power-consumption-Data-Set-/blob/master/data_e_power.ipynb)


# Power Consumption Leverage 

Libraries that we used: 

## Django 

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, it helps to focus on writing our app without needing to reinvent the wheel. ^^

# Base Django 

Django ist ein in Python geschriebenes, quelloffenes Webframework, das einem Model-View-Presenter-Schema folgt. Es wurde ursprünglich entwickelt, um die News-Seite „Lawrence Journal-World“ zu verwalten, und wurde im Juli 2005 unter einer BSD-Lizenz veröffentlicht.

## Run it on you local Machine

### Run it with Django-Admin (manage.py)

1. venv
2. pip install -r requirements
3. makemigrations
4. migration
5. runserver
6. makesuperuser
7. makemessage (i18n)
8. compilemessage (i18n)

### Run with Docker

This Repo is completly SIP ready and for a local testing you can start this app with docker-compose:  
``
$ docker-compose up --build
``

explane variables

### what can be removed

example app ...
1. folder
2. urls
3. installed_apps
4. maybe migration (try it out)

## HackZürich Theme

### Settings

There are in the just two variables that you can set for customizing the VSETH Theme.
- `HackZürich_GROUP`
- `HackZürich`

With `HackZürich` you can define the group from those it will take all static files from https://static.HackZürich.ch/assets/{HackZürich}.

`HackZürich_SECONDARY_NAVBAR` is a array of dicts.It define the entries of the secondary navbar. At the moment this template does not support dropdowns. You have some options for a menu entry.
- `title` (string): The title of the menu entry.
- `href` (string): URL path where the link goes
- `icon` (string) (optional): on mobile device, the menu bar goes to the botton and there will be shown this icons. If you don't set this option, there will be no icon but you cann find the entry still in the collapseble menu.
- `withoutLanguagePrefix` (boolean) (optional): Default all menu links would completed with the i18n language path but if this value is true it don't do it.
- `justSuperUser` (boolean) (optional): If the menu entry should just shown to superusers.
- `groups` (string) (optional): An array of existings groups, for those groups the menu entry is shown.

### base.html

## OIDC

We are trying to solve a problem related with Household Electric Power Consumption. 

## maybe an instruction for integration the HackZürich_HighSix app into existing project


[NLP](https://cloud.google.com/natural-language/docs/samples/language-entity-sentiment-text?hl=de)


This repository would contain a prototype and the pitch material for our solution to the challenge
["#9 Winter is coming — Are we ready?"](https://hackzurich.com/workshops#workshops).

The idea would be to reduce peak consumption in electricity by using notebook batteries. 
To do that, we would implement a smart power mode that enables a device to charge when
electricity demand is low, and avoid charging during hours of high deman.

# HackZurich 2022 Challenge —  #9 Winter is coming — Are we ready?

**Workshops**
- 20:00-20:35          Workshops Round 1  - Newton 1012, (1. OG)
- 20:45-21:20          Workshops Round 2 - Newton 1012, (1. OG)

<br>

## Short description

This winter, power shortages can be expected across Switzerland and will affect households and companies alike. How can innovation help us to use the energy smarter and avoid the risk of blackouts? We have made something about project management. 

> Do you have questions? Contact us on Discord. Channel: #9 - Zühlke

## Datasets
To better unterstand the power consumption in Switzerland, we provide you with some sample datasets/statistics. **It is not obligatory to use the datasets.**

* Swiss Federal Office of Energy
  * [Analysis of energy consumption by specific use](https://www.bfe.admin.ch/bfe/en/home/supply/statistics-and-geodata/energy-statistics/analysis-of-energy-consumption-by-specific-use.html#kw-98566) (General information page)
  * Analysis of the Swiss energy consumption 2000-2020 according to specific use (all Stakeholders) ([German](./datasets/10695-DE-Stromverbrauch_Verwendungszwecke_2000-2020.xlsx) | [English](./datasets/10695-EN-Energy_Consumption_By_Purpose_2000-2020.xlsx))
  * Analysis of the Swiss energy consumption by households 2000-2020 ([German](./datasets/10711-DE-Stromverbrauch_Haushalte_2000-2020.xlsx) | [English](./datasets/10711-EN-Energy_Consumption_By_Households_2000-2020.xlsx))

<br>

* OpenData.Swiss
  * [Swiss exports and imports by tariff number and country - monthly data since 1988](https://opendata.swiss/en/dataset/schweizerische-exporte-und-importe-nach-tarifnummer-und-land-monatliche-daten-ab-1988)


<br>
<br>
<br>

> 👉 Let's Focus on the Process! [Do work that matters – From ideation to implementation and beyond](https://www.zuehlke.com/en/careers)

|          |  |
:-------------------------:|:-------------------------:
<a href="https://www.zuehlke.com/en/careers">![](./resources/zuehlke-image1.png)</a> |  <a href="https://www.zuehlke.com/en/careers">![](./resources/zuehlke-image2.png)</a> 



The purpose of limiting the battery's max charge is to prolong battery health and to prevent damage to the battery. Various sources show that the optimal charge range for operation of lithium-ion batteries is between 40% and 80%, commonly referred to as the 40-80 rule [[1]](https://www.apple.com/batteries/why-lithium-ion/)[[2]](https://www.eeworldonline.com/why-you-should-stop-fully-charging-your-smartphone-now/)[[3]](https://www.csmonitor.com/Technology/Tech/2014/0103/40-80-rule-New-tip-for-extending-battery-life). This project is especially helpful to people who leave their Macs on the charger all day, every day.

## Installation

The easiest method to install BCLM is through `brew`.

BCLM is written in Swift and is also trivial to compile. Currently, it can only be compiled on macOS Catalina (10.15) or higher but it can run on OS X Mavericks (10.9) or higher.

A release zip is also provided with a signed and notarized binary for those who do not have development tools or are on an older macOS version.

### Brew

```
$ brew tap zackelia/formulae
$ brew install bclm
```

### From Source

```
$ swift build
$ sudo swift test
$ cp .build/debug/bclm /usr/local/bin
```

### From Releases

```
$ unzip bclm.zip
$ cp bclm /usr/local/bin
```

## Usage

```
$ bclm
OVERVIEW: Battery Charge Level Max (BCLM) Utility.

USAGE: bclm <subcommand>

OPTIONS:
  --version               Show the version.
  -h, --help              Show help information.

SUBCOMMANDS:
  read                    Reads the BCLM value.
  write                   Writes a BCLM value.
  persist                 Persists bclm.
  unpersist               Unpersists bclm.

  See 'bclm help <subcommand>' for detailed help.
```

When writing values, macOS charges slightly beyond the set value (~3%). In order to display 80% when fully charged, it is recommended to set the BCLM value to 77%.

```
$ sudo bclm write 77
$ bclm read
77
```

Note that in order to write values, the program must be run as root. This is not required for reading values.

## Persistence

The SMC can be reset by a startup shortcut or various other technical reasons. To ensure that the BCLM is always at its intended value, it should be persisted.

This will create a new plist in `/Library/LaunchDaemons` and load it via `launchctl`. It will persist with the current BCLM value and will update on subsequent BCLM writes.

```
$ sudo bclm persist
```

 Likewise, it can be unpersisted which will unload the plist.

```
$ sudo bclm unpersist
```

## References

![jhg](https://user-images.githubusercontent.com/78131082/190860072-1ebbbcf8-f508-48a8-8446-d8598c08cea4.jpeg)


![seoul_nighttime_timelapse__gif__by_clarissaask_d5esusr](https://user-images.githubusercontent.com/78131082/190858349-6689eaba-ee08-4d23-80ce-c5208efacfa9.gif)

[Household-electric-power-consumption-Data-Set](https://github.com/amirrezaeian/Individual-household-electric-power-consumption-Data-Set)

## Acknowledgements

- Thanks [High-Sixs](https://github.com/f-dangel/hackzurich2022), [Kaggle](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set), and [AreaChart](https://recharts.org/en-US/api) for sharing relevant data.

- Thanks Kolja for sharing his work [Kolja](https://github.com/kolja-esders), which helped us a lot in studying Household Electric Power Consumption.

- Thanks the organizers of [HackZürich](https://hackzurich.com/), [ReChart](https://github.com/ralpguler/DenseReg), [Alex Erfurt](https://github.com/alexerfurt) for providing [Google Cloud Developer's Cheat Sheet](https://github.com/priyankavergadia/google-cloud-4-words), [vrn](https://github.com/AaronJackson/vrn), [Hexagon](https://github.com/hexagon-geo-surv/hackzurich-2022), [Schindler](https://developer.schindler.com/) for making their excellent works publicly available. 




# Citation: 

@inproceedings{aepli2018parsing,
  title={{Parsing Approaches for Swiss German}},
  author={No\"emi Aepli and Simon Clematide},
  booktitle={{Proceedings of the 3rd Swiss Text Analytics Conference (SwissText), Winterthur, Switzerland}},
  year={2018}
}

* The Language Interpretability Tool: Interactively analyze NLP models for model understanding in an extensible and framework agnostic interface.
