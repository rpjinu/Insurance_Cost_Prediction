# Insurance_Cost_Prediction
"Streamlit-based application to predict insurance costs using a trained Linear Regression model, taking user inputs like age, BMI, and region."

<img src=""width=800>
# Insurance Cost Prediction with Streamlit

This repository contains a Streamlit web application that predicts insurance costs based on user inputs.

## Features

*   **User-Friendly Interface:** A simple and interactive UI built with Streamlit.
*   **Dynamic Inputs:** Accepts user inputs such as age, sex, BMI, number of children, smoking habits, and region.
*   **Real-Time Predictions:** Uses a pre-trained Linear Regression model to predict insurance charges instantly.
*   **Extensible:** Easily customizable for additional features or different models.

## Dataset

The application is trained using a health insurance dataset containing the following columns:

*   `age`: Age of the individual
*   `sex`: Gender (encoded as 0 for male, 1 for female)
*   `bmi`: Body Mass Index
*   `children`: Number of children/dependents
*   `smoker`: Smoking habits (encoded as 0 for yes, 1 for no)
*   `region`: Geographic region (encoded as integers or one-hot encoded)
*   `charges`: Insurance charges (target variable)

## How It Works

1.  **Input Features:** Users provide inputs for age, sex, bmi, children, smoker, and region through the Streamlit app.
2.  **Feature Encoding:** Categorical features like sex, smoker, and region are encoded to match the model's training process.
3.  **Prediction:** The inputs are passed to a pre-trained Linear Regression model stored in a `model.pkl` file.
4.  **Output:** The model predicts the insurance charges based on the input data.

## Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/username/insurance-cost-prediction.git](https://github.com/username/insurance-cost-prediction.git)
    ```

2.  Navigate to the project directory:

    ```bash
    cd insurance-cost-prediction
    ```

3.  Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the Streamlit app:

    ```bash
    streamlit run insurance.py
    ```

2.  Open the app in your browser using the URL provided by Streamlit (e.g., http://localhost:8501).
3.  Input the required values, and the app will predict the insurance charges.

## Project Structure
2.0 Flash Experimental. Might not work as expected.
Markdown

# Insurance Cost Prediction with Streamlit

This repository contains a Streamlit web application that predicts insurance costs based on user inputs.

## Features

*   **User-Friendly Interface:** A simple and interactive UI built with Streamlit.
*   **Dynamic Inputs:** Accepts user inputs such as age, sex, BMI, number of children, smoking habits, and region.
*   **Real-Time Predictions:** Uses a pre-trained Linear Regression model to predict insurance charges instantly.
*   **Extensible:** Easily customizable for additional features or different models.

## Dataset

The application is trained using a health insurance dataset containing the following columns:

*   `age`: Age of the individual
*   `sex`: Gender (encoded as 0 for male, 1 for female)
*   `bmi`: Body Mass Index
*   `children`: Number of children/dependents
*   `smoker`: Smoking habits (encoded as 0 for yes, 1 for no)
*   `region`: Geographic region (encoded as integers or one-hot encoded)
*   `charges`: Insurance charges (target variable)

## How It Works

1.  **Input Features:** Users provide inputs for age, sex, bmi, children, smoker, and region through the Streamlit app.
2.  **Feature Encoding:** Categorical features like sex, smoker, and region are encoded to match the model's training process.
3.  **Prediction:** The inputs are passed to a pre-trained Linear Regression model stored in a `model.pkl` file.
4.  **Output:** The model predicts the insurance charges based on the input data.

## Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/username/insurance-cost-prediction.git](https://github.com/username/insurance-cost-prediction.git)
    ```

2.  Navigate to the project directory:

    ```bash
    cd insurance-cost-prediction
    ```

3.  Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the Streamlit app:

    ```bash
    streamlit run insurance.py
    ```

2.  Open the app in your browser using the URL provided by Streamlit (e.g., http://localhost:8501).
3.  Input the required values, and the app will predict the insurance charges.

## Project Structure

insurance-cost-prediction/
├── model.pkl              # Pre-trained Linear Regression model
├── insurance.py           # Main Streamlit application script
├── requirements.txt       # List of Python dependencies
├── README.md              # Project documentation
└── dataset.csv            # Original dataset (if applicable)

## Example

**Input:**

*   Age: 30
*   Sex: Male
*   BMI: 28.5
*   Children: 2
*   Smoker: No
*   Region: Northwest

**Output:**

Predicted Insurance Charges: $4500.23 (This is just an example, actual results may vary)

## Requirements

*   Python 3.7+
*   Libraries:
    *   streamlit
    *   numpy
    *   scikit-learn
    *   pandas

## Future Enhancements

*   Incorporate additional machine learning models for comparison.
*   Add more detailed error handling for user inputs.
*   Include data visualization and insights in the app.

## License

This project is licensed under the MIT License.

## Acknowledgments

*   Dataset sourced from Kaggle or similar platforms.
*   Inspired by various beginner machine learning projects.
