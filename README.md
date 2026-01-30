# 🏢 St. Petersburg Flat Price Predictor

> A machine learning application for estimating residential property values in St. Petersburg, Russia. This project leverages a CatBoost regression model trained on synthetic data to provide accurate market value predictions for 2026.

---

## 📋 Overview

The application employs a comprehensive feature set including spatial characteristics, building specifications, location data, utilities, and amenities to deliver precise price estimates. The interactive interface is built with Streamlit, enabling users to receive real-time predictions based on property attributes.

---

## ✨ Key Features

-  **Interactive Input Interface**: Comprehensive controls for property specifications including floor area, room configuration, building characteristics, and amenities
-  **Real-Time Predictions**: Instant market value estimation in Russian Rubles (₽)
-  **Modern UI Design**: Professional dark-themed interface with enhanced visual elements
-  **Complete Model Pipeline**: Includes Jupyter notebook for data exploration, model training, and evaluation
-  **Deployment Ready**: Configured for local execution or cloud deployment

---

## 📁 Project Structure
```
st-petersburg-flat-price-predictor/
├──  jupyter_notebook/
│   ├──  data.csv                                    # Training dataset
│   ├──  test.csv                                    # Test dataset
│   └──  ITMO Flat Price Prediction 2025-2026.ipynb  # Model development notebook
├──  streamlit_app/
│   ├──  app.py                                      # Main application
│   ├──  styles.css                                  # Custom styling
│   ├──  flat_price_model_2026_full.pkl              # Trained model
│   └──  .streamlit/
│       └──  config.toml                             # Application configuration
└──  screenshots/                                     # Application screenshots
```

> **📌 Note**: The `.streamlit` directory follows the standard Streamlit convention for configuration files. On Unix-like systems, this appears as a hidden folder.

---

## 📸 Screenshots

|  Space & Layout |  Building & Location |
|:---:|:---:|
| ![Space & Layout](screenshots/space_layout.png) | ![Building & Location](screenshots/building_location.png) |
|  **Utilities & Review** |  **Market Value Estimate** |
|:---:|:---:|
| ![Utilities & Review](screenshots/utilities_review.png) | ![Estimate](screenshots/estimate.png) |

---

## 🔧 Prerequisites

-  Python 3.8 or higher
-  PyCharm 
-  Jupyter Notebook

---

## 🛠️ Technology Stack

### ** Backend Logic**
- Python
- NumPy
- Pandas

### ** Machine Learning**
- CatBoost
- Scikit-learn

### ** Frontend**
- Streamlit
- CSS

### ** Deployment**
- Pickle (Model Serialization)

---

## 🚀 Installation & Usage

### 📦 Project Setup

1.  Download the **[Latest Release](https://github.com/yourusername/st-petersburg-flat-price-predictor/releases)**.
2.  Extract the contents of the ZIP file.
3.  Open PyCharm and navigate to the extracted project folder.

---

**📂 Project structure:**
```
jupyter_notebook/
   ├──  ITMO Flat Price Prediction 2025-2026.ipynb
   ├──  data.csv
   └──  test.csv
```

**🚀 Launch Jupyter Notebook:**
```bash
jupyter notebook
```

** Run the Notebook:**

1. Open `ITMO Flat Price Prediction 2025-2026.ipynb`
2. Modify or experiment with the parameters
3. Run all cells

The notebook will:
   -  Perform exploratory data analysis
   -  Train the CatBoost regression model
   -  Evaluate model performance
   -  Export the trained model as `flat_price_model_2026_full.pkl`
   -  Generate predictions on test data (output: `submission.csv`)

---

### Streamlit Web App


**📂 Project structure:**
```
streamlit_app/
   ├──  app.py
   ├──  flat_price_model_2026_full.pkl
   ├──  styles.css
   └──  .streamlit/
       └──  config.toml
```

**💻 Open in PyCharm:**

1. Run PyCharm and open `app.py`

**⌨️ Open Terminal**

**📦 Install dependencies:**
```bash
pip install streamlit pandas numpy catboost pickle5
```

**🎬 Run Streamlit:**
```bash
streamlit run app.py
```

>  Streamlit will automatically open in your default browser at: `http://localhost:8501`

**✅ Using the App:**

Input property specifications and click **"Calculate Market Value"** to generate predictions! 

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for St. Petersburg Real Estate**

</div>
