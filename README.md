# FPL Predictive Model-CAPSTONE Project
by Mu-izz Gbadamosi <br>

Welcome to the Fantasy Premier League (FPL) Data Analysis and Prediction project! This project is designed to provide insights into player performance, trends, and predictions for Fantasy Premier League enthusiasts. Whether you're a seasoned FPL manager looking for data-driven strategies or a beginner seeking guidance, this project has something for everyone.

## Overview
Fantasy Premier League is a popular online fantasy football game where participants assemble virtual teams of real-life Premier League players and compete based on their actual performances in the league. This project aims to analyze historical FPL data, uncover patterns, and build predictive models to assist managers in making informed decisions about player selection, transfers, and captain choices.

## Features
Data Exploration: Dive into detailed exploratory data analysis of FPL datasets, examining player statistics, team performance, and game-week trends.
Player Performance Analysis: Analyze player performance based on key metrics, such as total points, goals scored, assists, clean sheets, and more.
Predictive Modeling: Build and evaluate predictive models, including machine learning algorithms and neural networks, to forecast player performance in upcoming game weeks.
Feature Engineering: Explore various features, including lag variables, form, and player contributions, to enhance model accuracy.
Visualization: Visualize data trends and model predictions through interactive charts and plots.



The `notebooks` folder contains my jupyter notebooks:

1. `Mu-izz_Gbadamosi- Notebook #1 - Cleaning_and_EDA.ipynb` <br>
    - Contains data preprocessing and exploratory data analysis of my FPL dataset
2. `Mu-izz_Gbadamosi- Notebook #2 - Modelling.ipynb` <br>
    - Contains modelling techniques and final model selection
3. `FPL.py` <br>
    - Streamlit app showcasing the results from the final model

The `data` folder contains four comma separated files:

1. `merged-gw.csv` <br>
    - The original dataset for 2022/2023 FPL season from Vaastav's GitHub repository which i used for my analysis.
2. `merged_gw23/24.csv` <br>
    - The original dataset for 2022/2023 FPL season from Vaastav's GitHub repository which i might use later on for further comparison to my model
3. `cleaned.csv` <br>
    - cleaned dataset from my preliminary analysis which i will use for my modelling

The `slide` folder contains 3 presentation files:

1. `Capstone Project Sprint 1 Presentation.pdf` <br>
    - The presentation for sprint 1 of my project showcasing the topic and data analysis
2. `Capstone Project Sprint 2 Presentation.pdf` <br>
    - The presentation for sprint 2 of my project showcasing the topic, data analysis, preprocessing, model selection
3. `Capstone Project Sprint 3 Presentation.pdf` <br>
    - The final presentation of my project showing the model selection and product concept demo



**Data Dictionary**
| Column Name                | Description                                                                                                                                                                         |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name                       | A player's name                                                                                                                                                                     |
| position                   | A player's position                                                                                                                                                                 |
| team                       | The team a player belongs to                                                                                                                                                        |
|                         xP | Expected points calculated by FPL (what we will try to beat in modelling)                                                                                                           |
| assists                    | The number of passes in a game a player made that directly contributed to a goal                                                                                                    |
| bonus                      | The number of bonus points a player earned in a game                                                                                                                                |
| bps                        | The number of points earned through the bonus points system in FPL                                                                                                                  |
| clean_sheets               | Has a player successfully prevented the opposing team from scoring                                                                                                                  |
| creativity                 | Creativity assesses player performance in terms of producing goalscoring opportunities for others. It can be used as a guide to identify the players most likely to supply assists. |
| element                    | Indicates a player's position in ordinal format                                                                                                                                     |
| expected_assists           | A statistic that measures the number of assists that a player was expected to have returned in a match.                                                                             |
| expected_goal_involvements | A statistic that measures both the number of goals and assists that a team or player were expected to return in a Gameweek                                                          |
| expected_goals             | A statistic that measures both the quantity and quality of shots, based on how often each is normally a goal                                                                        |
| expected_goals_conceded    | This is the expected number of goals that a defence is expected to concede                                                                                                          |
| fixture                    | The game number in Premier League                                                                                                                                                   |
| goals_conceded             | The number of goals conceded by a player's team                                                                                                                                     |
| goals_scored               | The number of goals scored by a player's team                                                                                                                                       |
| ict_index                  | All three of influence, creativity, and threat scores are combined to create an overall ICT Index score                                                                             |
| influence                  | Influence evaluates the degree to which a player has made an impact on a single match or throughout the season                                                                      |
| kickoff_time               | The date and time that a match was played                                                                                                                                           |
| minutes                    | The number of minutes a player was on the pitch                                                                                                                                     |
| opponent_team              | The opposition team in number format                                                                                                                                                |
| own_goals                  | A goal scored inadvertently when the ball is struck into the goal by a player on the defensive team                                                                                 |
| penalties_missed           | The number of penalties that a player missed in a match                                                                                                                             |
| penalties_saved            | The number of penalties saved by a goalkeeper                                                                                                                                       |
| red_cards                  | If a player was sent off in a match by receiving a red card                                                                                                                         |
| round                      | The round or Gameweek that a match was played                                                                                                                                       |
| saves                      | The number of saves made by a goalkeeper                                                                                                                                            |
| selected                   | The number of FPL teams that have selected the player                                                                                                                               |
| starts                     | Indicating if the player was on the starting XI                                                                                                                                     |
| team_a_score               | The number of goals scored by the away team                                                                                                                                         |
| team_h_score               | The number of goals scored by the home team                                                                                                                                         |
| threat                     | This is a value that examines a player's threat on goal. It gauges the individuals most likely to score goals.                                                                      |
| total_points               | The number of FPL points earned in a gameweek                                                                                                                                       |
| transfers_balance          | The net transfers to FPL teams for a player                                                                                                                                         |
| transfers_in               | The number of transfers into FPL teams                                                                                                                                              |
| transfers_out              | The number of transfers out of FPL teams                                                                                                                                            |
| value                      | The cost of a player                                                                                                                                                                |
| was_home                   | If the player was playing at home or not                                                                                                                                            |
| yellow_cards               | The number of yellow cards received by a player                                                                                                                                     |
| GW                         | The round or Gameweek that a match was played                                                                                                                                       |

## Modeling
=============================================================

We transition to the modeling phase, where we'll employ various regression models such as Linear Regression, Non-Linear Regression, Neural Network, and Decision Tree. Our objective is to predict the `total_points`, treating it as the target variable.

Our approach is to use several individual models to predict the total points directly, considering all relevant independent variables.

Our model evaluation framework involves metrics like Mean Absolute Error (MAE), R-squared, and Adj-R-squared. K-fold cross-validation will assess the generalization performance of our models. By comparing different approaches, we aim to identify the most effective model for predicting FPL player performance.

As we progress, we'll refine our models and assess their robustness, ensuring their practical applicability in the dynamic world of Fantasy Premier League.

Here are the key insights from the Data Modeling:

Findings from R-squared and Adjusted R-squared:
- The R-squared and Adjusted R-squared of each model are almost equal. This suggest that the models are likely to generalize well and perform well with new and unseen data. This also indicates that the model does not overfit.
- The Neural Network models has the highiest Rsquared values followed by the Gradient Boost model meaning they exhibit the highiest performance when handling the test set and new unseen data.
- The least performing model is the Decision Tree Model with 80% of the variability in the dependent variable being explained by the independent variables in your model.

Findings from MAE of Test an Train set:
- Low MAE (close to zero) on both the train and test sets suggests that the model is making accurate predictions.
- If the difference between the MAE for test and train is significant, it is a good indication of overfitting.
- The Neural Network model has the lowest MAE values followed by the Gradient Boost model meaning the average magnitude of errors between predicted values and actual values are significantly low which is good for our dataset.
- There is not a significant difference between MAE of test and train set for the Neural Network
- Although the Gradient Boosting has low MAE, the MAE of test and train sets are significantly different which is a sign of overfitting or underfitting.
- The model with the highiest MAE for test and train set is the Linear Regression model with PCA which means it is the least performing out of all the models.

#### Conclusion:
- Neural Network model emerges as our most optimal model in predicting our target variable(`total_points`) based on its favorable MAE, R-squared and Adjusted R-squared values.
- The second pick from our models is the Gradient Boosting model based on performance. The model still shows signs of overfitting/underfitting so futher hyperparameter tuning will be needed to optimize the model.
- Feature performance varies between models so we could incorporate more models to see which features appear the most often.
- Since we are selecting the Neural Network as our optimal model, we can say that our most important features for predicting the target variable are `goals_scored` followed by `minutes` and `clean_sheets`.