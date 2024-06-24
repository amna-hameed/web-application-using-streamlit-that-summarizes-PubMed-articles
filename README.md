# web-application-using-streamlit-that-summarizes-PubMed-articles
it is a web application created using streamlit that summarizes PubMed articles. It uses r T5 (Hugging Face) for text summarization.
This project involves creating a web application to summarize PubMed articles. The web application is built using Streamlit, and the summarization is performed using a pre-trained T5 model from Hugging Face.

Table of Contents
Data Exploration and Preparation
Model Selection and Fine-Tuning
Web Application Development
Running the Application
Data Exploration and Preparation
Dataset
The dataset used in this project is the PubMed Summarization dataset from Hugging Face. It contains scientific papers and their abstracts.

Loading the Dataset
The dataset is available in a zip file containing three CSV files: train.csv, test.csv, and validate.csv.
Preprocessing
Preprocess the dataset to clean and prepare the text for summarization. This involves removing unwanted characters, links, and unnecessary spaces.
Model Selection and Fine-Tuning
Model Selection
We use the pre-trained T5 model from Hugging Face for text summarization.

Tokenization
Tokenize the dataset for input to the model.
Web Application Development
Streamlit App
Develop a Streamlit web application to allow users to input or upload PubMed articles and display the summarized version.
Load Model and Tokenizer
Running the Application
Setup
Install Dependencies:
Ensure you have the necessary packages installed. You can use pip to install them.
pip install pandas torch transformers streamlit
for my machine this wasn't working so i created another virtual enviroment by using following commands
conda create -n summarizer_env python=3.8
conda activate summarizer_env
conda install pytorch torchvision torchaudio cpuonly -c pytorch
pip install streamlit transformers
Download Model:
The pre-trained T5 model will be downloaded automatically when you run the app.
Running the App
To run the Streamlit app, use the following command:
streamlit run app.py
Replace app.py with the name of your Python file containing the Streamlit code.

Additional Notes
Ensure you have Python and the required libraries installed on your machine.
The summarization is performed using a pre-trained T5 model from Hugging Face. If you wish to fine-tune the model on your dataset, follow the Hugging Face documentation for fine-tuning instructions.
