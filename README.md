<p align="center"><img src="./AI RECOMMANDATION.png" width="100%" alt="AI Recommendation Engine Banner"></p>

<h1 align="center">🤖 AI Recommendation Engine</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-purple?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/InternGrow-Internship-purple?style=for-the-badge" alt="InternGrow Internship">
</p>

<p align="center">
  <b>🤖 An AI-powered personalized movie recommendation system built with Python and Streamlit.</b>
</p>

<p align="center">
  Developed as part of the <b>InternGrow Internship – Task 4 (Week 4)</b>.
</p>

<p align="center">
  <a href="https://ai-recommendation-engine-y7ptm7oeavn9hh9cfna2xq.streamlit.app/">
    🚀 <b>View Live Demo</b>
  </a>
</p>

---

## 📌 About The Project

**AI Recommendation Engine** is a Machine Learning based recommendation system inspired by popular platforms such as **Netflix and Amazon**.

The application analyzes user preferences and movie characteristics to generate personalized movie recommendations.

The system demonstrates important recommendation system concepts including:

- 👤 User Profile Analysis
- 🎬 Movie Recommendation
- 🎯 Personalized Suggestions
- 🔍 Similar Item Detection
- 🧠 Content-Based Filtering
- 🤝 Collaborative Filtering
- 🔥 Hybrid Recommendation Model
- 📜 Recommendation History
- 📊 Cosine Similarity

This project was developed as part of the **InternGrow Internship – Task 4, Week 4** to gain practical experience in Recommendation Systems, Data Processing and Machine Learning.

---

## 🎯 Project Scenario

Build a recommendation system similar to **Netflix or Amazon**.

The goal of this project is to develop an intelligent recommendation engine that analyzes user preferences and recommends relevant movies/items.

---

## ✨ Key Features

### 👤 User Profile Analysis

Users can enter their name and select their favorite movie genre.

The system uses the selected preference to generate personalized recommendations.

### 🎬 Movie Recommendation

The application recommends movies according to the user's selected genre.

Supported genres include:

- ⚔️ Action
- 💕 Romance
- 🚀 Sci-Fi
- 🦖 Adventure

### 🎯 Personalized Suggestions

The system analyzes the user's preferences and ranks movies according to their match scores.

### 🔍 Similar Item Detection

Users can select a movie and find other movies with similar characteristics using **Cosine Similarity**.

### 🧠 Content-Based Filtering

Movies are recommended based on their characteristics and genre-related feature values.

### 🤝 Collaborative Filtering

The project demonstrates collaborative filtering concepts using user-item interaction patterns.

### 🔥 Hybrid Recommendation Model

The system demonstrates the concept of combining content-based and collaborative recommendation approaches.

### 📜 Recommendation History

Users can save their current recommendations and view their recommendation history inside the application.

### 📊 Interactive Dashboard

The complete recommendation system is presented through an interactive **Streamlit dashboard**.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Application Development |
| 🎈 Streamlit | Interactive Web Interface |
| 🐼 Pandas | Data Processing |
| 🔢 NumPy | Numerical Computing |
| 🤖 Scikit-Learn | Machine Learning |
| 🧮 Cosine Similarity | Similar Item Detection |
| 🐙 GitHub | Version Control |
| ☁️ Streamlit Community Cloud | Deployment |

---

## 🧠 Recommendation Approaches

### 1️⃣ Content-Based Filtering

Content-Based Filtering recommends items based on their characteristics.

The system compares movie features such as:

- Action
- Romance
- Sci-Fi
- Adventure

Movies with similar feature profiles receive higher similarity scores.

### 2️⃣ Collaborative Filtering

Collaborative Filtering uses user-item interaction patterns to identify recommendation preferences.

It is inspired by recommendation systems used by platforms such as Netflix and Amazon.

### 3️⃣ Hybrid Recommendation

A Hybrid Recommendation Model combines multiple recommendation approaches to improve personalized results.

text
🧠 Content-Based Filtering
          +
🤝 Collaborative Filtering
          ↓
🔥 Hybrid Recommendation Model
          ↓
🎯 Personalized Suggestions
🔄 How The Application Works

👤 User

↓

📝 Enter Name

↓

❤️ Select Favorite Genre

↓

📊 Analyze User Preference

↓

🎬 Analyze Movie Features

↓

🔍 Calculate Similarity

↓

🧠 Recommendation Model

↓

📈 Calculate Match Scores

↓

🎯 Rank Recommendations

↓

🎬 Display Personalized Movies

📊 User Profile Analysis

The application displays important information about the current user.

Example:

👤 User
Tehmina Anwar


❤️ Favorite Genre
Action


🎬 Available Items
12


🎯 Recommendations
5

The application also provides a preference profile based on the selected genre.

🎯 Personalized Recommendations

Example recommendation results:

🎬 The Dark Knight

Genre: Action

Recommendation Method: Content-Based Filtering

Match Score: 95%

🎬 Avengers

Genre: Action

Recommendation Method: Content-Based Filtering

Match Score: 90%

🎬 Iron Man

Genre: Action

Recommendation Method: Content-Based Filtering

Match Score: 90%

🎬 Spider-Man

Genre: Action

Recommendation Method: Content-Based Filtering

Match Score: 90%

🎬 Black Panther

Genre: Action

Recommendation Method: Content-Based Filtering

Match Score: 90%

🔍 Similar Item Detection

The application allows users to select a movie and discover similar movies.

The system uses Cosine Similarity to compare movie feature vectors.

🎬 Select Movie
       ↓
📊 Extract Features
       ↓
🧮 Create Feature Vector
       ↓
🔍 Calculate Cosine Similarity
       ↓
📈 Generate Similarity Scores
       ↓
🎯 Rank Similar Movies
       ↓
🎬 Display Results
📜 Recommendation History

Users can save their current recommendations.

The recommendation history stores information such as:

👤 User Name
❤️ Favorite Genre
🎬 Recommended Movies

Example:

User	Favorite Genre	Recommendations
Tehmina Anwar	Action	The Dark Knight, Avengers, Iron Man
🚀 Project Features
👤 User Profile Analysis
🎬 Movie Recommendation
🎯 Personalized Suggestions
🔍 Similar Item Detection
🤝 Collaborative Filtering
🧠 Content-Based Filtering
🔥 Hybrid Recommendation Model
📜 Recommendation History
📈 User Preference Analysis
🧮 Cosine Similarity
⚡ Interactive Streamlit Dashboard
📊 Recommendation Match Scores
🎯 Personalized Results
📂 Project Structure

AI-Recommendation-Engine/

├── app.py
├── requirements.txt
├── AI RECOMMANDATION.png
├── screenshots/
└── README.md

📄 app.py

Contains the complete Streamlit application and recommendation engine.

📄 requirements.txt

Contains the Python packages required to run the application.

🖼️ AI RECOMMANDATION.png

Project banner displayed at the top of the GitHub README.

📁 screenshots/

Contains screenshots of the application interface and major features.

📄 README.md

Contains complete project documentation.

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Tehmina124/AI-Recommendation-Engine.git
2️⃣ Open the Project Folder
cd AI-Recommendation-Engine
3️⃣ Install Dependencies
py -3.12 -m pip install -r requirements.txt
4️⃣ Run the Application
py -3.12 -m streamlit run app.py
5️⃣ Open in Browser
http://localhost:8501
🌐 Live Demo

🚀 Try the AI Recommendation Engine:

<a href="https://ai-recommendation-engine-y7ptm7oeavn9hh9cfna2xq.streamlit.app/"> https://ai-recommendation-engine-y7ptm7oeavn9hh9cfna2xq.streamlit.app/ </a>

The application is deployed online using Streamlit Community Cloud.

☁️ Deployment

The application deployment workflow:

Python Development

↓

AI Recommendation Engine

↓

Streamlit Application

↓

GitHub Repository

↓

Streamlit Community Cloud

↓

🌐 Live Web Application

🎓 Internship Information
InternGrow Internship

Project: AI Recommendation Engine

Task: Task 4

Week: Week 4

Scenario

Build a recommendation system similar to Netflix or Amazon.

Required Features
👤 User Profile Analysis
🎬 Product/Movie Recommendation
🔍 Similar Item Detection
🎯 Personalized Suggestions
📜 Recommendation History
Upgrade Features
🤝 Collaborative Filtering
🧠 Content-Based Filtering
🔥 Hybrid Recommendation Model
Skills
Recommendation Systems
Data Processing
Machine Learning
🎯 Project Objectives

The main objectives of this project were:

Build a practical recommendation system.
Understand recommendation system concepts.
Analyze user preferences.
Implement content-based recommendations.
Implement similar item detection.
Explore collaborative filtering.
Understand hybrid recommendation models.
Use cosine similarity for item comparison.
Build an interactive Streamlit dashboard.
Deploy a Python application online.
Gain practical Machine Learning experience.
💡 What I Learned

Through this project, I gained practical experience in:

🐍 Python Development
🤖 Machine Learning
🧠 Recommendation Systems
📊 Data Processing
🔍 Cosine Similarity
👤 User Profile Analysis
🎯 Personalized Recommendations
🤝 Collaborative Filtering
🧠 Content-Based Filtering
🔥 Hybrid Recommendation Concepts
🎈 Streamlit Application Development
🐙 GitHub Repository Management
☁️ Streamlit Cloud Deployment
🧪 Application Testing and Debugging
📸 Screenshots
🏠 Home Dashboard
<p align="center"> <img src="./screenshots/Home.png" width="90%" alt="AI Recommendation Engine Home Dashboard"> </p>
🎯 Personalized Recommendations
<p align="center"> <img src="./screenshots/recommendations.png" width="90%" alt="Personalized Movie Recommendations"> </p>
🔍 Similar Item Detection
<p align="center"> <img src="./screenshots/similar-items.png" width="90%" alt="Similar Item Detection"> </p>
📜 Recommendation History
<p align="center"> <img src="./screenshots/history.png" width="90%" alt="Recommendation History"> </p>
🚀 Project Features
<p align="center"> <img src="./screenshots/features.png" width="90%" alt="AI Recommendation Engine Features"> </p>
🔮 Future Improvements

Future versions can include:

🤖 Advanced recommendation algorithms
👥 Multiple user accounts
🤝 Advanced Collaborative Filtering
🔥 Improved Hybrid Recommendation
🎬 Larger real-world movie datasets
⭐ Movie ratings
❤️ Like/Dislike functionality
📜 Permanent recommendation history
🗄️ Database integration
🎬 Movie posters
🔎 Movie search
🎯 Advanced personalization
📊 Recommendation analytics
☁️ Production-level deployment
👩‍💻 About Me
Tehmina Anwar

BSAI Student | AI/ML Engineer | Python Developer

I am a Bachelor of Science in Artificial Intelligence student passionate about building practical Artificial Intelligence and Machine Learning applications.

Areas of Interest
🐍 Python
🤖 Machine Learning
🧠 Deep Learning
✨ Generative AI
🧠 Large Language Models
🔍 Retrieval-Augmented Generation
📝 Natural Language Processing
👁️ Computer Vision
🚀 AI Application Development
🔗 Connect With Me
💻 GitHub
<a href="https://github.com/Tehmina124"> GitHub Profile </a>
💼 LinkedIn
<a href="https://www.linkedin.com/in/tehmina-anwar-77b8a8414/"> LinkedIn Profile </a>
🌐 Portfolio
<a href="https://tehmina-portfolio-five.vercel.app/"> Portfolio Website </a>
🚀 Live Project
<a href="https://ai-recommendation-engine-y7ptm7oeavn9hh9cfna2xq.streamlit.app/"> AI Recommendation Engine </a>
⭐ Support

If you found this project useful or interesting, please consider giving the repository a ⭐ Star on GitHub.

<p align="center"> <b>🤖 AI Recommendation Engine</b> </p> <p align="center"> Developed by <b>Tehmina Anwar</b> </p> <p align="center"> 🎓 InternGrow Internship • 🚀 Task 4 • 📅 Week 4 </p> <p align="center"> <b>Built with ❤️ using Python, Streamlit, Pandas, NumPy & Scikit-Learn</b> </p> <p align="center"> © 2026 Tehmina Anwar </p>
