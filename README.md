# SCT_DS_TrackCode_Task02 - Titanic Data Cleaning and Visualization

## 📌 Overview
This project analyzes the famous Titanic dataset to explore survival patterns based on passenger demographics and other features.  
It involves:
- Handling missing data
- Removing duplicates
- Performing exploratory data analysis (EDA)
- Creating professional visualizations

---

## 📂 Dataset
The dataset used is **trained.csv**, which contains passenger details such as:
- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

---

## ⚙️ Steps Performed
1. **Data Cleaning**
   - Filled missing `Age` values with median
   - Filled missing `Embarked` values with mode
   - Dropped `Cabin` column due to too many missing values
   - Removed duplicate rows

2. **Exploratory Data Analysis (EDA)**
   - Plotted survival counts
   - Visualized survival by gender
   - Plotted age distribution
   - Analyzed class vs survival rates

3. **Visualization**
   - Used **Seaborn** and **Matplotlib**
   - Graphs are displayed in fullscreen for better readability

---

## 📊 Key Visuals
- **Survival Count**
- **Survival by Gender**
- **Age Distribution**
- **Class vs Survival**

---

## 📦 Requirements
```bash
pip install pandas numpy matplotlib seaborn
