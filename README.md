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

## ECON_Research_WI24: Large-Scale User ID Sampling and Analysis

### Project Overview
This project, developed for the Economics Department Research Lab Winter 2024, focuses on efficient sampling and analysis of large-scale user ID datasets. It's designed to work with the San Diego Supercomputer Center, specifically for research on the economic impact of return migrants. The project combines econometric techniques with Natural Language Processing (NLP) and leverages advanced computing methods for data handling and analysis.

### Key Components

#### 1. samplethenconcatenate.py
This Python script is the core of the sampling process. It uses Dask for distributed computing to efficiently sample and merge large Parquet files.

Key functions and features:
- `sample_and_merge_optimized_dask(folder_path, output_dir, sample_fraction=0.1)`:
  - Reads Parquet files from a specified folder
  - Samples a fraction (default 10%) of the data
  - Saves the sampled data as a new Parquet file

Arguments:
- `--folder_path`: Path to the folder containing Parquet files
- `--output_dir`: Directory to save the output Parquet file
- `--sample_fraction`: Fraction of data to sample (default: 0.1)

Additional features:
- Memory usage tracking using `psutil`
- Progress bar for visual feedback during processing

#### 2. Bash Script (SLURM Job Submission)
This script is used to submit the sampling job to the SLURM workload manager on the supercomputer.

Key features:
- Sets job name and output file
- Navigates to the correct directory
- Executes the Python script with appropriate arguments

#### 3. Data Verification Script
This script verifies the sampled dataset by counting the total number of rows.

Key features:
- Uses Dask for efficient processing of large Parquet files
- Configures Dask for optimized query planning
- Loads the sampled dataset and computes the total row count

### Workflow
1. The bash script submits the job to SLURM, which executes `samplethenconcatenate.py`.
2. `samplethenconcatenate.py` reads the Parquet files, samples 10% of the data, and saves the result.
3. The data verification script then loads the sampled dataset and computes the total number of rows.

### Results
- Original dataset: 763,504,805 User IDs
- Sampled dataset: 76,350,473 User IDs (approximately 10%)
- Runtime reduced from 2.5 hours to 26 minutes

### Technical Proficiencies Demonstrated
- Unix/Terminal: Used for job submission and cluster interaction
- Python: Core language for script development
- Dask: Utilized for distributed computing and efficient data handling
- SLURM: Workload manager for job submission on the supercomputer
- Parquet: Efficient columnar storage format for large datasets

### Key Achievements
- Developed a Parallelized Computing Algorithm for efficient data sampling
- Significantly reduced runtime from 2.5 hours to 26 minutes
- Achieved 10% sampling of an 800 million user dataset without increasing storage and memory costs
- Set a new benchmark for processing scalability and speed in large-scale data analysis

### Usage
1. Ensure all dependencies are installed (Dask, psutil).
2. Submit the job using the provided bash script: sbatch job_submission_script.sh
3. Once the job completes, verify the results using the data verification script.

### Future Directions
- Further optimization of the sampling algorithm for even larger datasets
- Integration with NLP techniques for in-depth analysis of migration trends
- Development of advanced econometric models leveraging the sampled data

Note: This project is part of ongoing research on the economic impact of return migrants, blending econometric techniques with NLP and leveraging advanced computing resources for comprehensive migration analysis.

## ECON_Research_SS24: O Globo Violence Article Scraper

### Project Overview
This project, developed for the Economics Department Undergraduate Research Lab Summer 2024, is designed to scrape and analyze articles from O Globo's Rio de Janeiro section, focusing on violence-related news. The scraper collects articles, processes their content, and classifies them based on their likelihood of being related to violent events.

### File Structure and Functionality

#### 1. main.py
This is the entry point of the application. It orchestrates the entire scraping and data processing pipeline.

Key functions:
- `main()`: Coordinates the scraping process, data saving, and output generation.
  - Sets up scraping parameters (start page, max pages, time range)
  - Initializes CSV file for data storage
  - Calls `scrape_oglobo()` from scraper.py
  - Handles exceptions and keyboard interrupts
  - Provides a summary of scraped data
  - Saves data to CSV and DataFrame formats

#### 2. scraper.py
Contains the core logic for scraping articles from O Globo's website.

Key functions:
- `scrape_oglobo(days=365, start_page=1, max_pages=None)`: 
  - Scrapes articles from specified pages
  - Utilizes BeautifulSoup for HTML parsing
  - Extracts basic article information (title, URL, publication date)
  - Calls `get_article_content()` to fetch full article text
  - Uses `ViolenceClassifier` to predict violence likelihood
  - Extracts various data points using functions from data_processors.py
  - Yields a dictionary of extracted and processed data for each article

#### 3. content_extractor.py
Handles the retrieval and parsing of full article content.

Key functions:
- `get_article_content(url, max_retries=3)`:
  - Fetches the full text of an article from its URL
  - Implements retry logic for failed requests
  - Uses various CSS selectors to locate article content
  - Cleans the extracted text by removing unwanted elements and whitespace

#### 4. data_processors.py
Contains functions for processing and extracting specific data from article content.

Key functions:
- `extract_location(text)`: Identifies mentioned locations in the article
- `extract_police_involvement(text)`: Determines if police are mentioned
- `extract_gang_involvement(text)`: Checks for mentions of gang activity
- `extract_victims(text)`: Attempts to count the number of victims mentioned
- `extract_gender(text)`: Extracts gender information of individuals mentioned
- `determine_violence_level(text)`: Categorizes the level of violence (High/Medium/Low)
- `determine_violence_type(text)`: Identifies the type of violent event
- `is_violence_related(text)`: Determines if the article is related to violence
- `extract_journalist(text)`: Extracts the name of the journalist

#### 5. utils.py
Provides utility functions used across the project.

Key functions:
- `extract_date(text)`: Extracts dates mentioned in the text
- `get_coordinates(location)`: Geocodes location names to coordinates
- `clean_text(text)`: Cleans and normalizes text
- `format_date(date)`: Formats datetime objects to standard string format
- `extract_important_metadata(content)`: Extracts key metadata from article content

#### 6. violence_classifier.py
Implements machine learning models to classify articles based on their likelihood of being related to violent events. This file offers two classification approaches: a simpler scikit-learn based model and a more robust BERT-based transformer model.

Key classes:

1. `SimpleViolenceClassifier`:
   - Uses scikit-learn's TfidfVectorizer and MultinomialNB for classification
   - `train_classifier()`: Trains the model on a predefined set of examples
   - Suitable for quick classification with lower computational requirements

2. `RobustViolenceClassifier`:
   - Utilizes a pre-trained Portuguese BERT model ("neuralmind/bert-base-portuguese-cased")
   - Capable of fine-tuning on domain-specific data for improved accuracy
   - Key methods:
     - `fine_tune(texts, labels)`: Fine-tunes the model on a manually labeled dataset of violence and non-violence related articles
     - `predict_violence_likelihood(text)`: Predicts the likelihood of an article being violence-related

Usage notes:
- The BERT-based classifier requires pre-training or fine-tuning on a manual sample of marked violence and non-violence articles before use in the main scraping process.
- Fine-tuning process:
  1. Collect a diverse set of articles from O Globo or similar sources
  2. Manually label these articles (1 for violence-related, 0 for non-violence)
  3. Use the `fine_tune` method with this labeled dataset
  4. The fine-tuned model can then be used for predictions during the scraping process

Choosing between classifiers:
- SimpleViolenceClassifier: Use for faster processing and when computational resources are limited
- RobustViolenceClassifier: Prefer for higher accuracy, especially when dealing with nuanced or context-dependent violence references in Portuguese text

Note: The BERT-based classifier requires more computational resources, especially during the fine-tuning process. GPU acceleration is recommended for efficient fine-tuning and faster inference.

### How It All Ties Together
1. `main.py` initiates the scraping process by calling `scrape_oglobo()` from `scraper.py`.
2. `scraper.py` fetches article listings, extracts basic info, and calls `get_article_content()` from `content_extractor.py` to get full article text.
3. The scraped content is then processed using various functions from `data_processors.py` and `utils.py` to extract relevant information.
4. `violence_classifier.py` is used to predict the likelihood of each article being related to a violent event.
5. All extracted and processed data is compiled into a dictionary for each article and yielded back to `main.py`.
6. `main.py` saves this data to CSV and DataFrame formats, providing a summary of the scraped articles.

### Usage
To run the scraper:
1. Ensure all dependencies are installed (requests, beautifulsoup4, pandas, numpy, scikit-learn, geopy).
2. Run `python main.py` from the command line.
3. The script will start scraping articles, processing them, and saving the results to 'violence_data.csv' and 'violence_data_df.csv'.

Note: Respect O Globo's robots.txt and terms of service when using this scraper. Implement appropriate delays between requests to avoid overloading their server.

---

**Note**: This repository is continuously updated with new research and findings. Please feel free to explore the content and contribute or provide feedback.

## License

This project is licensed under the MIT License - see the [LICENSE.md](license.md) file for details.

## Contact

For any inquiries or collaboration, please feel free to contact Affaan at [afmustafa@ucsd.edu](mailto:afmustafa@ucsd.edu).
