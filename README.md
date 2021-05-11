# PCBS-Stroop-Effect
This repository contains an implementation to test the Stroop effect in individuals. 

## Table of Contents
- [Getting started](#getting-started)
- [How to run](#how-to-run)
- [Analyse the results](#analyse-the-results)


## Getting started
To get started, you must first make sure that you have all the dependencies installed for the project to run. The easiest way to do this is to clone this repository and create a conda environment using the configuration file provided. To do this, change your location to the root of the cloned repository and run the following command: 
```
conda env create -n NAME_OF_ENV -f psychopy-env.yml
```

where ```NAME_OF_ENV``` is replaced by your preferred environment name. After this, you can active the conda environment by running the following command:
```
conda activate NAME_OF_ENV
```

## How to run
The trials are based on a configuration file, which is located in ```json_files\trials.json```. Here, a list of trials can be specified. Each trial consists of an object with the following properties: 

- ```center_stimulus_color```
- ```left_stimulus_word```
- ```center_stimulus_word```
- ```right_stimulus_word```

An example configuration file has already been made, which can be used as inspiration. 

Once the trials have been configured, the program can be executed by running:
```
python stroop_test.py
```

This will prompt the user to enter their name and guide them through the experiment. Once all the trials as specified in the ```trials.json``` have been completed, the results of the experiment will be exported to a ```.csv``` file that can later be analysed.

## Analyse the results
To analyse the results obtained, 
