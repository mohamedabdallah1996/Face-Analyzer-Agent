# 😉 Face Analyzer Agent 

Face Analyzer Agent is a Streamlit-based web application that allows users to analyze facial images using advanced AI models. The app provides three main functionalities: selecting example images, uploading custom images, and capturing images via a camera. The analysis is powered by the Gemini model and Tavily Tools, offering detailed insights into the visual features of the provided images.

## 🌟 Features

* **Example Faces**: Pre-loaded examples for the app.
* **Image Upload**: Upload your own face images.
* **Camera Capture**: Take photos directly through the app.
* **AI Analysis**: Powered by Google's Gemini 2.0 Flash and Tavily Search.
* **Ingredient Insights**: Get a detailed analysis of human traits, mood and feelings.

## 🚀 Installation 

1. Clone the repository:
   ```bash
    git clone https://github.com/yourusername/Product-Ingredient-Agent.git
    cd Product-Ingredient-Agent
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up API key
   Add your `TAVILY_API_KEY` and `GOOGLE_API_KEY` to the `secrets.toml` file in the `.streamlit` directory or update it from the streamlit UI
   ```bash
   TAVILY_API_KEY = "your_tavily_api_key"
   GOOGLE_API_KEY = "your_google_api_key"
    ```

## 💡 Usage 

1. Run the Streamlit app:
    ```python
    streamlit run app.py
    ```

2. Open your browser and navigate to http://localhost:8501

3. Choose one of three options to analyze a product:

    * Select from example faces
    * Upload your own image
    * Take a photo using your camera

