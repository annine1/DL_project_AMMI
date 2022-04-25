 # #####Problem understanding: Cat vs. dog classifier #

 In this project, we are going to build a classifier that classifies whether an image is cat or dog. </br>

 Cat      | Dog
 :--------:|:---------:
 ![](figures/cat.0.jpg)  | ![](figures/dog.0.jpg)

 # Run the project
 git config --global user.name ""
 git config --global user.email ""

<!-- <br> -->
Refer to this [link](https://www.kaggle.com/competitions/dogs-vs-cats/data) to get the data.

# Run the project #
In this project, we have two steps: training and predicting. In the predict step, you can upload any image from your laptop and predict it. Let's show you how to run the project.

If you do not have venv package, please refer to this [link](https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/)
</br>

## Create virtual environment ##

```
$ python3 -m venv ENV_NAME
```
## Activate your environment ##

```
$ source ENV_NAME/bin/activate
```

## Requirement installations ##
To run this, make sure to install all the requirements by:

```
$ pip install -r requirements.txt 
```
# Training the model #

```
$ python3 main.py --model MODEL_NAME --num_epochs
```
## Example of running models ##

```
$ python3 main.py --model resnet --10
```