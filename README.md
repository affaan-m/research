# Research Work by Affaan - UCSD

Welcome to Affaan's research repository, housing various research projects conducted at UCSD and personally. This repository is a testament to the commitment towards pushing the boundaries of knowledge and innovation, particularly in the fields of quantitative finance, economics, and the intersection with cutting-edge technology. Below is an overview of the current projects and their corresponding descriptions.

## Research Project 1: Discovering Market Manipulation Using Sentiment Analysis in Microcap Cryptocurrencies

### Overview

This project aims to explore the relationship between Reddit discussions and the price movements of microcap cryptocurrencies. Leveraging various APIs, including CoinMarketCap, Twitter, and Reddit, the study focuses on identifying correlations, understanding sentiment, and attempting to infer causality.

### Methodology

The project follows a systematic approach, divided into multiple steps:

1. **Sample Selection**: Selecting 500 microcap cryptocurrencies with a market capitalization of under 1 million USD.
2. **Data Collection**: Gathering mentions from Reddit posts and constructing a rich dataset.
3. **Data Preprocessing**: Cleaning and aggregating the data, including sentiment analysis.
4. **Correlation Analysis**: Investigating linear relationships between post counts and price.
5. **Statistical Significance Testing**: Confirming the statistical significance of the correlations.
6. **Multivariate Regression Analysis**: Conducting a panel data regression model to understand influences on price, including lagged price, Reddit posts, and total market cap.

### Findings

- **Positive Sentiment**: An overwhelmingly positive sentiment across the posts.
- **Strong Correlations**: A few microcaps showed strong positive correlations between Reddit discussions and price.
- **Statistical Significance**: The significant correlations suggest potential underlying relationships.

### Limitations and Future Work

- **Model Complexity**: A more complex model could refine insights.
- **Data Scope**: Additional data sources and variables may enhance the analysis.
- **Focused Analysis**: Further studies could explore the mechanisms driving specific correlations.

### Conclusion

This project offers valuable insights into the dynamic interplay between social media and financial markets, particularly within the realm of microcap cryptocurrencies. It serves as a foundation for further research and innovation in the field of financial technology and market behavior.

---

## Research Project 2: Comparing Neural Networks with Newton’s Method Gradient Descent, SVM, and Random Forest for Max-Flow Optimization in Supply Chain Networks

### Overview

This study embarks on a comparative analysis of machine learning techniques for optimizing supply chain networks, focusing on the max-flow problem. Utilizing three key datasets - "Daily Demand Forecasting Orders" from Ferreira et al. (2017), "Wholesale Customers" from Cardoso (2014), and "Online Retail" (2015) - the research aims to model and predict critical factors influencing supply chain efficiency.

### Methodology

The project is systematically structured as follows:

1. **Data Preparation**: Initial Exploratory Data Analysis (EDA) for understanding dataset characteristics, followed by data cleaning and preprocessing.
2. **Model Selection**: Employing Neural Networks using Newton's Method Gradient Descent, Support Vector Machines (SVM), and Random Forests (RF) for the analysis.
3. **Data Splitting**: Dividing datasets into different training-testing splits (80/20, 50/50, 20/80) to evaluate model performance.
4. **Model Training and Evaluation**: Training each classifier and assessing performance based on accuracy, F-score, Lift, ROC Area, average precision, and other metrics.
5. **Visualization and Analysis**: Plotting convergence rates and performance metrics to compare classifiers visually.
6. **Hyperparameter Tuning and Cross-Validation**: Using GridSearchCV to optimize hyperparameters for each classifier.

### Findings

- **Neural Networks**: Demonstrated high accuracy but required substantial computational resources for convergence.
- **SVM**: Showed consistent and robust performance across different datasets.
- **Random Forest**: Achieved high training accuracy, indicating proficiency in capturing complex data patterns but also a potential for overfitting.

### Insights and Future Work

- **Computational Efficiency**: Logistic Regression and SVM are preferable for limited computational power, while Neural Networks are suitable with ample computational resources.
- **Model Stability**: Further investigation into feature relationships and model stability is necessary for robust predictive performance.
- **Future Research**: Exploring hybrid models or ensemble techniques combining the strengths of these classifiers could enhance supply chain optimization.

### Conclusion

The study provides a nuanced understanding of how different machine learning models can optimize various aspects of supply chain management. While Random Forest stands out for handling complex datasets, Neural Networks show promise for future applications with sufficient computational support. Logistic Regression and SVM offer accessible alternatives for scenarios with computational or data limitations.

---

**Note**: This repository is continuously updated with new research and findings. Please feel free to explore the content and contribute or provide feedback.

## License

This project is licensed under the MIT License - see the [LICENSE.md](license.md) file for details.

## Contact

For any inquiries or collaboration, please feel free to contact Affaan at [afmustafa@ucsd.edu](mailto:afmustafa@ucsd.edu).
