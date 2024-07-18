# AQI Prediction

Welcome to the AQI Prediction project repository!

## About

This project aims to provide users with real-time Air Quality Index (AQI) data for any city they search, along with a forecast of the AQI for the next five days. The goal is to help individuals and communities make informed decisions about outdoor activities and health precautions based on air quality predictions.

## Features

- **Real-Time AQI Data:** Users can search for any city worldwide and receive the current AQI data instantly.
- **5-Day AQI Forecast:** The project predicts the AQI for the next five days, offering users a glimpse into future air quality trends.
- **User-Friendly Interface:** The interface is designed to be intuitive and easy to use, ensuring accessibility for all users.

## Methodology

- **Data Sources:** The project utilizes data from reliable sources such as government environmental agencies and trusted weather services.
- **Forecasting Model:** The AQI forecast is powered by TimeGPT integrated with MindsDB, leveraging advanced machine learning algorithms and time series analysis techniques. The model is trained on historical AQI data and various meteorological parameters to enhance prediction accuracy.
- **Technology Stack:**
  - **Ozon3:** Used for data processing and integration.
  - **MindsDB:** Utilized for developing and deploying machine learning models, including the integration with TimeGPT for forecasting.
  - **React + Vite:** Provides a fast and responsive user interface.
  - **Flask:** Serves as the backend framework to handle API requests and connect the frontend with the data and models.

## Unique Aspects

- **Comprehensive Coverage:** The project covers a wide range of cities globally, making it useful for users across different regions.
- **High Accuracy:** By leveraging advanced machine learning techniques and extensive datasets, the project aims to provide highly accurate AQI forecasts.
- **User-Centric Design:** The focus is on delivering valuable insights in an easy-to-understand format, catering to users' needs for actionable air quality information.

## Intended Audience

This project is intended for anyone interested in monitoring air quality, including:
- General public concerned about air pollution and its health effects
- Environmental researchers and analysts
- Policy makers and government agencies
- Health professionals and organizations
- Outdoor enthusiasts and athletes

We hope this tool will empower users with critical air quality information, helping them to take necessary precautions and plan their activities accordingly.

## Getting Started

### Prerequisites

- Node.js and npm
- Python and pip

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/AQI-Prediction.git
    cd AQI-Prediction
    ```

2. Install frontend dependencies:
    ```sh
    cd frontend
    npm install
    ```

3. Install backend dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Getting API Keys

#### Ozon3 API Key

1. Visit the Ozon3 website and sign up for an account.
2. Navigate to the API section in your account settings.
3. Generate a new API key and copy it.

#### TimeGPT API Key

1. Visit the TimeGPT website and sign up for an account.
2. Navigate to the API section in your account settings.
3. Generate a new API key and copy it.

### Running the Project

1. Set up environment variables for your API keys. Create a `.env` file in the root directory with the following content:
    ```
    OZON3_API_KEY=your_ozon3_api_key
    TIMEGPT_API_KEY=your_timegpt_api_key
    ```

2. Start the backend server:
    ```sh
    py app.py
    ```

3. Start the frontend server:
    ```sh
    cd frontend
    npm run dev
    ```

4. Open your browser and navigate to `http://localhost:5000` to use the application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgements

- Thanks to the developers of Ozon3, MindsDB, React, Vite, and Flask for their excellent tools and libraries.

---
