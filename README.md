# 🚀 Fraud Transaction Detection

Detect fraudulent transactions using machine learning! This project leverages advanced data analysis techniques to distinguish between genuine and fraudulent transactions, helping in financial security and fraud prevention.

## 📌 Dataset

The dataset used in this project is sourced from Kaggle:  
🔗 [Fraud Transaction Detection Dataset](https://www.kaggle.com/code/llabhishekll/fraud-transaction-detection/input)  

It contains anonymized financial transaction records labeled as **fraudulent** or **genuine**.

## 🏗️ Project Structure

```
📂 Fraud-Transaction-Detection/
│── 📂 models/          # Saved trained models
│── 📂 templates/       # HTML templates for web interface
│── 📜 app.py          # Flask application for the web interface
│── 📜 train.ipynb     # Jupyter Notebook for data analysis & model training
│── 📜 requirements.txt # Required dependencies
│── 📜 README.md        # Project documentation
```

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rupeshbharambe24/Fraud-Transaction-Detection.git
cd Fraud-Transaction-Detection
```

### 2️⃣ Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download the Dataset
- Access the dataset from the Kaggle link above.
- Place the dataset file in the project directory.

---

## 🚀 Usage

### 🔹 Train the Model
- Open `train.ipynb` in Jupyter Notebook.
- Run all the cells to preprocess the data and train the model.
- The trained model will be saved in the `models/` directory.

### 🔹 Run the Web Application
```bash
python app.py
```
- Open a browser and visit: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**  
- Upload transaction data and check for fraud detection results.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, improve the project, and submit a pull request. 🚀

