# Python-Notes

## Summary
- Python is widely used in different areas: Data Analysis, Web Application, Test API development
- Summary the python skills and projects according to the daily usage
## Tools:
- Python 3.6 or above https://www.python.org/downloads/
- Anaconda


## Python skills summary: How to be pythonic
- **Iterative**: For, While,etc., advanced usage: List comprehension
- **Slicing**:
- **Re**: Regular Expression, dealing with the text or words, normally filter, substitute,
- **Functions**:
- **Decorators**:
- **sys,os**: see my os_sys_usage.py
- **file read, write**:
- **data**: csv, json


## Python Application
### a. Data Analysis - Jupyter Notebook
#### Tools:
- Numpy, Pandas, Matplotlib, re(Regular Expression)
- Jupyter Notebook: for data analysis, jupyter notebook is better than the IDE - Anaconda
#### Steps:
1. Get the data
   - Web Scrapy (Terminal Project, BeautifulSoup Request)
   - Supplied by the consumer, or some data websites like Kraggle
2. Analyse the data
   - Import the data (Directly import, DataBase like MongoDB, MySQL)
   - Data Clean and Preprocessing (Dealing with the missing value, Wrangling)
   - Data Visualization (Matplotlib, Pyecharts)
3. Model fitting, Testing and Validation
   - Linear Regression, 
#### Projects:
- Douban Movie Top250 
- Amazon Food comments Analysis
### b. Web Application - Django
Build a blog website with Python Django

**Personal blog website based on Django-Framwork (Web_Development)**

#### Install the following apps on your machine
1. Git (optional)
2. virtualenv (pip install virtualenv)
3. Python

#### How to run on your local server
1. Firstly, clone the repository using the git shell <br>

2. Go to the base directory of the project <br>
<code>cd Web_Development </code> <br>
3. Create a virtual environment and activate it. <br>
<code>$ virtualenv venv</code> <br>
Windows: <code>$ venv\Scripts\activate</code> <br>
Linux/Mac: <code>$ source venv/bin/activate</code> <br>
4. Install the requirements for the project <br>
<code>$ pip install -r requirements.txt</code>  <br>
**This step will help you install the required apps/modules on your local machine automatically. That's also why we would create a requirements.txt for the project. Similarly you can use it when you deploy your project on a linux server**
5. Finally start the localhost server<br>
<code>$ python manage.py runserver</code> <br>

You can see built blog website on your localhost:8000

### c. Test Automation - API development
#### API: Application Programming Interface
Normally when we talk about API, it refers to the REST API.

**REST**: **Re**presentational **S**tate **T**ransfer

### d. OOP - Object-Oriented Programming
**class**: like java, class in python also has inheritance propertity


