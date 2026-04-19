# 🏏 IPL Predictive Analytics — Batsman Run Prediction


## 📌 Project Overview
This project predicts IPL batsman runs using machine 
learning techniques. By analyzing historical IPL data 
from 2008 to 2020, we built models that can predict 
how many runs a batsman will score based on match 
conditions and player statistics.

## 👥 Team Members
| Member | Name | Contribution |
|--------|------|-------------|
| Member 1 | Adithyan Biju | Problem Statement, Feature Engineering, SHAP, Deployment |
| Member 2 | Fidal Govind | EDA, Model Building, README |
| Member 3 | Archana Das | Preprocessing, Model Evaluation, PPT |

## 🎯 Problem Statement
Cricket is one of the most popular sports in the world 
and IPL is its biggest tournament. Predicting batsman 
performance can help teams make better decisions about 
team selection and match strategy. This project uses 
machine learning to predict batsman runs based on 
historical IPL data from 2008 to 2020.

## 📂 Dataset
- **Source:** Kaggle — IPL Complete Dataset 2008-2020
- **Files:** deliveries.csv and matches.csv
- **Size:** 179,078 deliveries across 816 matches
- **Features:** Batsman, bowler, venue, batting team, bowling team, runs scored

## 🔄 Project Pipeline

## 📊 Data Science Life Cycle

### Stage 1 — Problem Definition and Literature Review
Defined the problem of predicting IPL batsman runs 
using machine learning. Reviewed 5 research papers 
on cricket match prediction using ML techniques.

### Stage 2 — Data Collection and Understanding
Used IPL Complete Dataset 2008-2020 from Kaggle 
containing 179,078 deliveries across 816 matches.

### Stage 3 — Data Preprocessing and Cleaning
The dataset was cleaned by removing null values 
and irrelevant columns. Categorical variables were 
encoded using label encoding. The final dataset 
had no missing values and was ready for training.

### Stage 4 — Exploratory Data Analysis
- 55.6% of innings fall in flop category (0-15 runs)
- Virat Kohli is the highest run scorer with 8000+ runs
- Average runs per innings increased from 2008 to 2024
- Punjab Cricket Association Stadium has highest average runs

### Stage 5 — Feature Engineering and Selection
Features selected include batting average, strike rate, 
venue, batting team, bowling team and toss decision. 
These features directly impact batsman performance.

### Stage 6 — Model Building and Training
Three models were trained:
- Simple Linear Regression
- Multiple Linear Regression
- Logistic Regression

### Stage 7 — Model Evaluation and Comparison
| Model | Accuracy |
|-------|----------|
| Simple Linear Regression | 68% |
| Multiple Linear Regression | 74% |
| Logistic Regression | 71% |

Multiple Linear Regression performed best with 
lowest error rate and highest accuracy.

### Stage 8 — Model Interpretation and Explainability
SHAP analysis shows that batting average is the most 
important feature. Strike rate and venue also have 
significant impact on predictions. The model makes 
logical predictions based on cricket domain knowledge.

### Stage 9 — Deployment
Model deployed on Streamlit Community Cloud.
Live App: Member1: added Streamlit deployment link to README

### Stage 10 — Documentation
Full documentation available in this README, 
PPT presentation and Jupyter notebook.

## 🤖 Models Used
| Model | Accuracy |
|-------|----------|
| Simple Linear Regression | 68% |
| Multiple Linear Regression | 74% |
| Logistic Regression | 71% |

## 📊 Key Findings
- Virat Kohli is the highest run scorer with 8000+ runs
- 55.6% of innings are flop scores (0-15 runs)
- Batting average is the most important feature
- Average runs per innings has increased from 2008 to 2024
- Punjab Cricket Association Stadium has highest average runs

## 🚀 Deployment
- **Platform:** Streamlit Community Cloud
- **Live App:**https://ipl-predictive-analytics-ghf3nh6np9wdrhcckgopxi.streamlit.app/

## ⚙️ How to Run Locally
1. Clone the repository:
git clone https://github.com/adithyanbijuds25-eng/ipl-predictive-analytics.git

2. Install requirements:
pip install -r requirements.txt

3. Open notebook:
jupyter notebook ipl_project.ipynb

4. Upload deliveries.csv and matches.csv

5. Run all cells

## 📁 Repository Structure

## 📚 References
1. Pathak et al. (2016) - Predicting outcomes of IPL cricket matches using machine learning
2. Sankaranarayanan et al. (2014) - Cricket analytics using decision tree and random forest
3. Kampakis & Thomas (2015) - Using machine learning to predict cricket match outcomes
4. Manage & Scariano (2013) - Statistical analysis of cricket using logistic regression
5. Shah et al. (2020) - Deep learning approaches for cricket match outcome prediction
