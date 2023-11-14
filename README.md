# Energy Prediction by the Hour
Danayt Aman. November 17,2023
![image_info](header_articles_(11)-2.png)
# Project Overview
This project aims to predict energy consumption by the hour using machine learning techniques. Matching supply to demand is of utmost importance in the energy sector, it ensures the stability and reliability of power grid. The goal is to develop a model that can accurately forecast energy usage, which can be valuable for various applications such as energy management, demand planning, and cost optimization. 

## Data Understanding 

The project utilizes a dataset containing historical energy consumption by the hour. The dataset includes features such as date, time, weather conditions, and other relevant variables that were engineered from the time stamp and calendar such as holidays, working days and lag variables as time series prediction are influenced by previes times with certain weigh assigned to each historical lag. The dataset is preprocessed and cleaned to handle missing values, outliers, and other data quality issues. Weather data was retrieved from [NOVA](https://www.ncei.noaa.gov) and consumption data was retrieved from [CAISO](http://www.caiso.com/planning/Pages/ReliabilityRequirements/Default.aspx), the website has data from 2019, and that was the starting point of this timeseries project ending at the end of 2022 with posibly using 2023 data as a fresh testing set.


## Project Structure

The project is structured as follows:

1. Data Cleaning and EDA: Load data and Perform exploratory data analysis to gain insights into the dataset, understand the distribution of variables, and identify any patterns or trends.

2. Feature Engineering: Create new features or transform existing ones to enhance the predictive power of the model. This may involve techniques such as lagging variables, creating interaction terms, or encoding categorical variables.

3. Model Development: Train and evaluate various machine learning models to predict energy consumption. This includs regression models such as Random forest, elastic net, decision tree-based models such as XGBoost. Timeseries models such as SARIMAX and FB Prophet were also used in this project along with advanced techniques like LTSM neural networks.

4. Model Evaluation: To evaluate the performance of our models, we have employed several evaluation metrics. These metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and R-squared (R^2). These metrics provide us with a comprehensive understanding of the accuracy and precision of our predictions, enabling us to compare and select the best-performing mode

5. Model Deployment: Once a satisfactory model is selected, deploy it in a production environment to make real-time predictions. This may involve creating an API or integrating the model into an existing system.

## Conclusion

By accurately predicting energy consumption by the hour, this project aims to provide valuable insights for energy management and planning. The developed model can be used to optimize energy usage, reduce costs, and improve overall efficiency. Using time series forcasting this project was able to predict hourly energy consumption at 7.97% MAPE, which is on average 168.27 MWH off the actual consumption, which has a minimum consumption of 5768.62 MWH and max 22379.07 MWH. These results were obtained by using a 24h lag variables for each hour with XGBoosting model. Other models such as elasticnet and randomforest also performed well with a 24h lags included. Our data had high seasonality and timeseries models such SARIMAX, even after decomposition and taking out noices were not able to pick on the trend as well as the linear models with lags.


# Limitations
This project did not account for solar energy and the time used being during covid where lockdown had an effect on energy consumption and might not be an appropriate representation of the county's usual data as yearly trend decreses from 2019 to 2022 and picks up from there. The data set used also doen't include all forcasting requirements such as solar, EV ownership or economic condition. 

# Next Steps
* Include solar, EV, and economic condition for long term forcasting.
* Account for residential and industrial presence 
* Deploy Model

## Dependencies

The project relies on the following libraries:

- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## Usage

To run the project, follow these steps:

1. Clone the repository:

git clone git@github.com:Danayt09/Phase_5_Energy.git

2. Install the required dependencies:

pip install -r requirements.txt

3. Run the Jupyter notebook or Python scripts in the specified order:

* [CleaningNotebook]()
* [PreprocessingNotebook]()
* [ModelingNotebook]()


# LinkdIn
Danayt Aman <a href = "https://github.com/Danayt09"><img src='https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png' width = '25' height='25'></a><a href="https://www.linkedin.com/in/danayt-aman/"><img src='https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg' width = '25' height='25'></a>  


