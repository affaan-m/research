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

### Extension: Large Scale Research Proposal on Market Manipulation

**Title**: Investigating Market Manipulation in Cryptocurrencies through Advanced Sentiment Analysis and Machine Learning

**Objective**: To identify and mitigate market manipulation in the cryptocurrency sector through advanced sentiment analysis and machine learning techniques.

**Scope**:
- **Expanded Sample Size**: Increasing the sample size to 2000 microcap cryptocurrencies.
- **Enhanced Data Sources**: Incorporating additional social media platforms such as Telegram and Discord.
- **Advanced Analytical Techniques**: Using machine learning algorithms like LSTM for time series analysis and BERT for more nuanced sentiment analysis.
- **Collaborative Efforts**: Partnering with financial institutions and academic bodies to validate findings and explore practical applications.

**Expected Outcomes**:
1. A comprehensive understanding of market manipulation tactics in cryptocurrencies.
2. Development of predictive models to identify potential manipulation.
3. Policy recommendations for regulators to mitigate market manipulation.

**Methodology**:
1. **Data Collection**: Extensive data collection from multiple social media platforms and cryptocurrency exchanges.
2. **Sentiment Analysis**: Advanced sentiment analysis using state-of-the-art NLP techniques.
3. **Machine Learning Models**: Training and testing various machine learning models to predict price movements and identify manipulation.

**Collaborators**: Financial institutions, academic researchers, and regulatory bodies.

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

## Research Project 3: Enhancing Handwritten Quranic Arabic Recognition through Deep Learning: A Novel Approach Integrating Tajweed-Sensitive Convolutional Neural Networks

### Overview

This project embarks on an unprecedented exploration into the recognition of handwritten Quranic Arabic, with a special emphasis on integrating the complex rules of Tajweed. Utilizing a rich dataset of Arabic Handwritten Characters compiled by El-Sawy, Loey, and El-Bakry (2017), the research employs advanced convolutional neural networks (CNNs) architectures, particularly focusing on ResNet, to significantly advance the field of Arabic handwritten character recognition.

### Methodology

1. **Data Loading and Preprocessing**: Utilizing the Arabic Handwritten Characters Dataset, which contains 16,800 characters from 60 participants, the data undergoes augmentation, normalization, and reshaping to fit the model requirements.
2. **Model Architecture**: Adopting ResNet with modifications, including custom layers for Tajweed recognition, to handle the complexity of Quranic Arabic script.
3. **Hyperparameter Optimization**: Employing GridSearchCV and other techniques to fine-tune parameters for optimal performance.
4. **Training and Validation**: Utilizing an 80/10/10 split for training, validation, and testing, with a focus on accuracy, precision, recall, and F1 score.
5. **Comparative Analysis**: Conducting a detailed comparison between AlexNet and ResNet architectures to evaluate performance improvements.

### Findings

- **Accuracy**: Achieved an accuracy of over 91% in recognizing handwritten Quranic Arabic with integrated Tajweed rules using ResNet.
- **Model Robustness**: Enhanced through advanced data augmentation techniques and iterative refinement.
- **Comparative Analysis**: ResNet outperformed AlexNet in both accuracy and efficiency, demonstrating its superior capability in handling complex recognition tasks.

### Future Directions

- **Comprehensive Optimization**: Expanding hyperparameter tuning to include all conceivable combinations for maximal accuracy.
- **Advanced Architectures**: Further exploring deeper networks and hybrid models to push performance boundaries.
- **Real-world Applications**: Developing practical tools for educational and religious use, enhancing accessibility to Quranic texts.

### Conclusion

This project significantly contributes to the field of computational linguistics and artificial intelligence by addressing the complex task of Quranic Arabic recognition with integrated Tajweed rules. The insights gained lay the groundwork for further advancements and practical applications, aiming to enrich the educational and religious experiences of the global Muslim community.

---

**Note**: This repository is continuously updated with new research and findings. Please feel free to explore the content and contribute or provide feedback.

## License

This project is licensed under the MIT License - see the [LICENSE.md](license.md) file for details.

## Contact

For any inquiries or collaboration, please feel free to contact Affaan at [afmustafa@ucsd.edu](mailto:afmustafa@ucsd.edu).
