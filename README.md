# Udemy Streamlit Github Repository

--> [Link to the udemy course on Streamlit 🎉](https://www.udemy.com/course/streamlit-deployer-son-app-de-machine-learning-sur-le-web/)

## 1️⃣ Presentation

This project is part of the [Streamlit.io](https://streamlit.io/) training course that I propose with a double objective:

1) Learn how to use Streamlit.io, a Python framework that allows to develop data/ML applications and commonly used by Data Scientists. 
2) Develop a web application to analyze the stock prices of S&P500 companies.

Here is a preview of the final version of the application developed in this directory : 

*Step 1 : S&P500 Screener*

<img width="600" alt="Streamlit web app stock forecasting" src="https://user-images.githubusercontent.com/67114372/193663427-d34271f8-df9f-4d4c-8041-c83bcd39b26c.png">


*Step 2 : S&P500 Stock Analysis*

<img width="600" alt="Streamlit web app stock forecasting" src="https://user-images.githubusercontent.com/67114372/193663471-5b35daf3-5be3-41e9-832b-94ed748cd8b6.png">

If you want to see the final application in production, click [here](https://pierre-louis-danieau-u-final-versionprojectfinal-project-mh4one.streamlit.app/) !

## 2️⃣ Presentation of the directory

Here is the architecture of the course directory :

<img width="600" alt="repository tree" src="https://user-images.githubusercontent.com/67114372/197332282-a9f17712-5c54-4b50-9e01-67b0bbe814b3.png">

The `initial_version` directory contains the same files as the `final_version` directory. The difference is that the files in the `initial_version` directory are empty and will be completed with the explanations during the training.

You will find all the answers in the `final_version` directory.

Then, within these 2 folders, you will find :
- An `exercise` folder: With all the exercises of the course.
- A `project` folder in which you will find the 3 successive steps of the final project (the S&P500 screener and stock analysis application) : `final_project_basics.py` / `final_project_interactions.py` / `final_project.py`

## 3️⃣ How to work with this directory

In order to work on this directory, you have to download it locally on your own computer. 

To do this, open a terminal and place yourself in the folder of your choice in order to store the project folder (with the `cd` command) then clone the folder by executing the command :

`git clone https://github.com/pierre-louis-danieau/udemy_streamlit.git`

Congratulations, you should see the directory appear locally on your computer. You can now open the project with your favorite editor (VScode, Pycharm, Spyder...)!

## 4️⃣ Exercices folder

The `exercises` folder is composed of 4 subfolders:
- streamlit_basics : Python file on the basics of streamlit + input files (an audio recording, a photo, a video)
- streamlit_interactions : Python file for training on streamlit widgets which allow to interact with the user.
- streamlit_visualizations : Python file for training on how to create graphics in streamlit.
- streamlit_advanced_features : Python file for training on the more advanced components of streamlit.


## 5️⃣ Projects folder

The `project` folder is composed of 5 subfiles:

You will find :
- `final_project_basics.py` : The first step of the application with what was seen in the streamlit_basics training part.
- `final_project_interactions.py` : The second step of the application with what was seen in the streamlit_interactions training part.
- `final_project.py`: The third and last step of the application with what was seen in the streamlit_visualizations and streamlit_advanced_features training part.
- **s&p500.csv**: The csv file of most of the S&P500 companies with some indicators like market capitalization, dividend ratio...
- **stock.jpeg**: A picture used in the layout of the application.

## 6️⃣ How to execute the streamlit applications

In order to run the all the python files, you need to create a virtual environment and install the dependencies that are in the `requirements.txt` file.

To do this:
1) Open a terminal and go to the repository folder: 

`cd udemy_streamlit`

2) Install virtualenv : 

`pip install virtualenv`

3) Create the virtual environment : 

`virtualenv env`

4) Activate it : 

`source env/bin/activate`

5) Install dependencies : 

`pip install -r requirements.txt`

Once the installation of the dependencies is finished, you can run all the python files with the command : `streamlit run path_to_file/file_name.py`.

For example, to run the final application, execute :

`streamlit run final_version/project/final_project.py`

And to run the first code exercice (the streamlit foundation in the `streamlit_basics` repository):

`streamlit run final_version/exercices/streamlit_basics/basic.py`

You should then see a web window with the streamlit application!

PS : The version of Python used during this training is : 3.9.6 



----------------------------------

🎉🎉 That's it, you normally have all the elements to work on this repository yourself ! 🎉🎉

--> [Link to the udemy course on Streamlit](https://www.udemy.com/course/streamlit-deployer-son-app-de-machine-learning-sur-le-web/)

Happy training !
