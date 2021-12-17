# AI vs Real Face Neural Network Detector
Can a neural network model distinguish the faces of real people from those generated by another neural network?

![alt text](https://images.theconversation.com/files/168081/original/file-20170505-21003-zbguhy.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=926&fit=clip)

This project is a part of Ironhack Data Analytics Full Time Bootcamp course. 

## 1. Project Description

The project consists of two inter-connected elements:
* A Jupyter notebook where a CNN Neural Network model has been compiled, fit & trained using 20k images of both real human faces as well as fake, AI-generated human faces.
* A second Jupyter notebook (and a .py exectuable) which serve as a GUI (using streamlit.io) to use the model to recognize new & unseen data.

## 2. Tools used

The main technologies used here are Python, using the libraries such as Tensorflow, Keras (for the AI model) as well as stremalit.io to build a simple web-interface for GUI.

## 3. Challenges identified

There have been three major challenges during this project:
* Finding a dataset of images that was large enough ( > few thousand different images), split between two categories of fake & real faces, that was also pretty balanced.
*  Constructing a model in terms of layer number, layer type, parameters (learning rate, epochs, number of steps, etc). to maximize the model accuracy.
*  Shifting from the Jupyter environment to streamlit GUI - there have been issues related to saving the model data & using it for predictions using the web interface.

## 4. How to use & install

The project is straightforward to install, use & modify:
* Fork & clone the entire repo on your hard-drive
* Download the main dataset from author's private OneDrive (it is too large to fit in Github/LFS), unzip and include it in the same folder as other files
   * https://1drv.ms/u/s!ArCfuIIvBRcVgZsyCDTpZGcYW5zSig?e=hGhYoy
* Run the Jupyter app.py from your terminal to see the streamlit GUI, or any of the two Jupyter notebooks (model2.ipynb, app.ipynb) to see the Python code.
* Explore the the Microsoft Powerpoint presentation to get quick insights on the project & work done.

## 5. Copyright

While the data used & tools are free-to-use & open-source, I will appreciate if the below credits are mentioned if you find using my work & time devoted to this project useful, and you intend to share it in full/parts publicly:

* **Author:** Arek Tarnawski
* **LinkedIn:** https://www.linkedin.com/in/arek-tarnawski/
* **Github:** https://github.com/arektarnawski/

*Amsterdam, 2021*
