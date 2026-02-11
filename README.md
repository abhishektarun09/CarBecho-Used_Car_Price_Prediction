# 🚗 [CarBecho - Sell your Old Car](https://carbecho-used-car-price-prediction.onrender.com/)

<p align="center">
  <img src="static\images\index.jpg" alt="Screenshot" width="400"/>
</p>


This project is an **end-to-end machine learning solution** that predicts the **resale price of a used car** based on key vehicle and ownership attributes. It features a robust backend ML pipeline, a user-friendly frontend, secure user authentication, and modern deployment practices — all wrapped in a modular and production-ready architecture.

---
🖼️ Screenshots

<p align="center">
  <img src="static\images\homepage.jpg" alt="Screenshot" width="400"/>
</p>
<p align="center">
  <img src="static\images\predict.jpg" alt="Screenshot" width="400"/>
</p>
<p align="center">
  <img src="static\images\predicted.jpg" alt="Screenshot" width="400"/>
</p>

#### Video Demo:  [CarBecho - YouTube](https://youtu.be/k5T6ypmNjPs?si=1DvXttIk1cQfrWD6)

## 📊 Features

- **Machine Learning**: Regression models trained and tuned to predict car prices.
- **Best Model**: GradientBoostingRegressor with hyperparameter tuning via GridSearchCV.
- **Modular Code**: Structured into pipelines, custom exceptions, and logging.
- **Web App**: Built using Flask with HTML, CSS, and JavaScript.
- **Authentication**: Secure login, register, change password, logout.
- **Database**: PostgreSQL Server on Neon.
- **Deployment**: Dockerized app deployed on Render.

---

## 🧠 Model Information

### 🎯 Target
- `selling_price` (in currency units)

### 🧾 Features Used
- `km_driven`, `fuel`, `seller_type`, `transmission`, `owner`,  
  `mileage`, `engine`, `max_power`, `seats`, `age`

### 🔍 Models Trained
- `LinearRegression`
- `DecisionTreeRegressor`
- `RandomForestRegressor`
- `GradientBoostingRegressor` ✅ Best
- `AdaBoostRegressor`
- `KNeighborsRegressor`
- `XGBRegressor`
- `CatBoostRegressor`

### ✅ Best Performing Model
- **GradientBoostingRegressor**  
  - Selected via **GridSearchCV**  
  - Saved as `.pkl` model artifact

### 📈 Evaluation Metric
- `R² Score`

---

## 🧰 Tech Stack

| Layer         | Tools/Frameworks                                       |
|---------------|--------------------------------------------------------|
| Backend (ML)  | `sklearn`, `xgboost`, `catboost`                       |
| Data Prep     | `pandas`, `sklearn.Pipeline`, `OneHotEncoder`         |
| Frontend      | `Flask`, `HTML`, `CSS`, `JavaScript`                              |
| Auth & DB     | `Flask-Login`, `PostgreSQL Database on Neon`                     |
| Python Ver    | `3.8`                                                  |





---

## 🚀 Deployment

The entire application is **containerized with Docker** and deployed to **Render**. Deployment is automated, which handles:

- Building the Docker image
- Managing environment secrets securely

Link: https://carbecho-used-car-price-prediction.onrender.com/

---

## 🔒 Authentication

- User registration & login system
- Passwords stored securely using hashing
- Session-based authentication
- Features: Register, Login, Logout, Change Password

---

## 🖥️ Web App UI

The prediction form includes fields like:

- Fuel type
- Owner type
- Seller type
- Transmission
- KM Driven
- Mileage
- Engine
- Max Power
- Seats
- Age

Users input the car's details and receive an **instant resale price prediction**.

---

## 📦 Setup Instructions

1. **Clone the Repository**  
    ```bash
    git clone https://github.com/abhishektarun09/CS50x_Project.git

2. **Create and run Docker Image**  
    ```bash
    docker-compose up --build

3. **Go to browser**
    ```bash
    localhost:5000

---

## 🛠 Future Improvements

- Add confidence interval to predictions
- Enable CSV batch uploads
- Implement model performance dashboard
- Add admin role for user management

---

## 📬 Contact

Created as part of **Harvard University CS50x Final Project**  
- Author: Abhishek Tarun
- Email: abhishek.tarun09@gmail.com 