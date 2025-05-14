
# AI-Based Insight Generator App

This is a Python-based web application that leverages OpenAI's GPT-4 to analyze CSV data, generate insights, and create visualizations. Built with **Streamlit**, **Plotly**, and the **OpenAI API**, the app helps users understand their data through a user-friendly interface.

## Features

- **CSV Upload**: Upload your dataset in CSV format.
- **Data Preview**: View the first few rows of your uploaded dataset.
- **Basic Summary Statistics**: Get a quick summary of the dataset.
- **AI-Generated Insights**: Get insights such as trends, anomalies, and suggestions for visualizations using GPT-4.
- **Visualization Options**: Create charts such as:
  - Scatter Plot
  - Histogram
  - Line Chart
  - Bar Chart
  - Box Plot

## Installation

### Prerequisites

To run the app, you'll need:

- **Python 3.x** (recommended version: 3.8+)
- **OpenAI API Key**: You can obtain an API key by creating an account on [OpenAI](https://beta.openai.com/signup/).

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ai-insight-dashboard.git
   cd ai-insight-dashboard
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API Key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. Run the app:

   ```bash
   streamlit run app.py
   ```

   This will open the app in your browser, and you can start interacting with it!

## Usage

1. Upload your **CSV file** through the file uploader in the app.
2. You will see a preview of your dataset and summary statistics.
3. Select the chart type you wish to generate (e.g., Scatter Plot, Histogram).
4. Select the columns for the X and Y axes to create visualizations.
5. Get **AI-generated insights** about the dataset, including trends, anomalies, and potential visualizations.

## Contributing

Contributions are welcome! If you would like to improve the app or fix any issues, feel free to fork the repository and submit a pull request.

### To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is open-source.

## Acknowledgements

- **OpenAI** for providing the GPT-4 model for generating insights from data.
- **Streamlit** for enabling easy creation of interactive web applications.
- **Plotly** for the interactive visualizations in the app.
