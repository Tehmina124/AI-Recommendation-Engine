# ============================================================
# Task 4 - AI Recommendation Engine
# Internship: Interngrow AI
# Developed by: Tehmina Anwar
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Tehmina Anwar | AI Recommendation Engine",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f8f9fc;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    color: #6C2BD9;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
    margin-bottom: 20px;
}

.project-info {
    text-align: center;
    padding: 15px;
    border-radius: 15px;
    background: linear-gradient(135deg, #f3e8ff, #ede9fe);
    border: 1px solid #ddd;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.recommendation {
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(135deg, #f5f0ff, #faf8ff);
    border-left: 5px solid #7c3aed;
    margin: 12px 0;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
}

.feature-card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    text-align: center;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.07);
    margin-bottom: 15px;
}

.footer {
    text-align: center;
    margin-top: 50px;
    padding: 30px;
    color: #777;
    background: #f3f0f8;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">🤖 AI Recommendation Engine</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Personalized Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="project-info">

<h3>👩‍💻 Developed by Tehmina Anwar</h3>

<p>
🎓 <b>Interngrow AI Internship</b>
&nbsp; | &nbsp;
🚀 <b>Task 4 - Week 4</b>
</p>

<p>
An intelligent recommendation system inspired by
platforms such as Netflix and Amazon.
</p>

</div>
""", unsafe_allow_html=True)

# ============================================================
# DATASET
# ============================================================

data = {
    "Item": [
        "The Dark Knight",
        "Avengers",
        "Iron Man",
        "Spider-Man",
        "Black Panther",
        "Inception",
        "Interstellar",
        "The Matrix",
        "Avatar",
        "Jurassic Park",
        "Titanic",
        "The Notebook"
    ],

    "Genre": [
        "Action",
        "Action",
        "Action",
        "Action",
        "Action",
        "Sci-Fi",
        "Sci-Fi",
        "Sci-Fi",
        "Sci-Fi",
        "Adventure",
        "Romance",
        "Romance"
    ],

    "Action": [
        0.95,
        0.90,
        0.90,
        0.90,
        0.90,
        0.20,
        0.10,
        0.80,
        0.40,
        0.60,
        0.10,
        0.10
    ],

    "Adventure": [
        0.60,
        0.80,
        0.50,
        0.70,
        0.70,
        0.50,
        0.60,
        0.50,
        0.90,
        1.00,
        0.20,
        0.10
    ],

    "Romance": [
        0.10,
        0.20,
        0.10,
        0.20,
        0.10,
        0.10,
        0.10,
        0.10,
        0.20,
        0.10,
        0.95,
        1.00
    ],

    "Sci-Fi": [
        0.20,
        0.30,
        0.20,
        0.30,
        0.20,
        1.00,
        1.00,
        0.95,
        1.00,
        0.50,
        0.10,
        0.10
    ]
}

df = pd.DataFrame(data)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚙️ Recommendation Settings")

st.sidebar.markdown("### 👤 User Profile")

user_name = st.sidebar.text_input(
    "Your Name",
    value="Tehmina Anwar"
)

selected_genre = st.sidebar.selectbox(
    "❤️ Favorite Genre",
    ["Action", "Adventure", "Romance", "Sci-Fi"]
)

recommendation_count = st.sidebar.slider(
    "🎯 Number of Recommendations",
    1,
    8,
    5
)

recommendation_method = st.sidebar.selectbox(
    "🧠 Recommendation Method",
    [
        "Content-Based Filtering",
        "Collaborative Filtering",
        "Hybrid Recommendation Model"
    ]
)

# ============================================================
# USER PROFILE
# ============================================================

st.header("👤 User Profile Analysis")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👤 User", user_name)

with col2:
    st.metric("❤️ Favorite Genre", selected_genre)

with col3:
    st.metric("🎬 Available Items", len(df))

with col4:
    st.metric("🎯 Recommendations", recommendation_count)

# ============================================================
# USER PREFERENCE PROFILE
# ============================================================

st.subheader("📊 Your Preference Profile")

preference_values = {
    "Action": 0.9 if selected_genre == "Action" else 0.2,
    "Adventure": 0.9 if selected_genre == "Adventure" else 0.2,
    "Romance": 0.9 if selected_genre == "Romance" else 0.2,
    "Sci-Fi": 0.9 if selected_genre == "Sci-Fi" else 0.2
}

preference_df = pd.DataFrame(
    {
        "Genre": list(preference_values.keys()),
        "Preference Score": list(preference_values.values())
    }
)

st.bar_chart(
    preference_df.set_index("Genre")
)

# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

feature_columns = [
    "Action",
    "Adventure",
    "Romance",
    "Sci-Fi"
]

def content_based_recommendations(genre, count):

    result = df.sort_values(
        by=genre,
        ascending=False
    )

    return result.head(count)


def collaborative_recommendations(genre, count):

    # Simulated user-item interaction scores
    # representing collaborative filtering behaviour

    result = df.copy()

    result["CollaborativeScore"] = (
        result[genre] * 0.8
        + result["Adventure"] * 0.1
        + result["Action"] * 0.1
    )

    result = result.sort_values(
        by="CollaborativeScore",
        ascending=False
    )

    return result.head(count)


def hybrid_recommendations(genre, count):

    result = df.copy()

    content_score = result[genre]

    collaborative_score = (
        result[genre] * 0.8
        + result["Adventure"] * 0.1
        + result["Action"] * 0.1
    )

    result["HybridScore"] = (
        0.6 * content_score
        + 0.4 * collaborative_score
    )

    result = result.sort_values(
        by="HybridScore",
        ascending=False
    )

    return result.head(count)

# ============================================================
# PERSONALIZED RECOMMENDATIONS
# ============================================================

st.header("🎯 Personalized Recommendations")

if recommendation_method == "Content-Based Filtering":

    recommendations = content_based_recommendations(
        selected_genre,
        recommendation_count
    )

    score_column = selected_genre

elif recommendation_method == "Collaborative Filtering":

    recommendations = collaborative_recommendations(
        selected_genre,
        recommendation_count
    )

    score_column = "CollaborativeScore"

else:

    recommendations = hybrid_recommendations(
        selected_genre,
        recommendation_count
    )

    score_column = "HybridScore"

# ============================================================
# DISPLAY RECOMMENDATIONS
# ============================================================

for _, row in recommendations.iterrows():

    score = row[score_column] * 100

    st.markdown(
        f"""
        <div class="recommendation">

        <h3>🎬 {row['Item']}</h3>

        <p>
        <b>Genre:</b> {row['Genre']}
        </p>

        <p>
        <b>Recommendation Method:</b>
        {recommendation_method}
        </p>

        <p>
        <b>Match Score:</b>
        <span style="color:#7c3aed;font-size:20px;">
        {score:.1f}%
        </span>
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# SIMILAR ITEM DETECTION
# ============================================================

st.header("🔍 Similar Item Detection")

selected_item = st.selectbox(
    "🎬 Choose a movie to find similar items",
    df["Item"].tolist()
)

selected_index = df[
    df["Item"] == selected_item
].index[0]

features = df[feature_columns]

similarity_matrix = cosine_similarity(features)

similar_scores = similarity_matrix[selected_index]

similar_indices = np.argsort(
    similar_scores
)[::-1]

similar_items = []

for i in similar_indices:

    if i != selected_index:

        similar_items.append(
            (
                df.iloc[i]["Item"],
                df.iloc[i]["Genre"],
                similar_scores[i]
            )
        )

similar_items = similar_items[:5]

for item, genre, score in similar_items:

    st.markdown(
        f"""
        <div class="recommendation">

        🎬 <b>{item}</b>

        <br>

        Genre: {genre}

        <br>

        Similarity:
        <b>{score * 100:.1f}%</b>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# RECOMMENDATION HISTORY
# ============================================================

st.header("📜 Recommendation History")

if "history" not in st.session_state:

    st.session_state.history = []

if st.button("➕ Save Current Recommendation"):

    st.session_state.history.append(
        {
            "User": user_name,
            "Genre": selected_genre,
            "Method": recommendation_method,
            "Recommendations": ", ".join(
                recommendations["Item"].tolist()
            )
        }
    )

    st.success(
        "Recommendation saved successfully! ✅"
    )

if st.session_state.history:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:

    st.info(
        "No recommendation history yet. "
        "Save your recommendations to see them here."
    )

# ============================================================
# DATASET EXPLORER
# ============================================================

st.header("📊 Dataset Explorer")

with st.expander("🔎 View Movie Recommendation Dataset"):

    st.dataframe(
        df,
        use_container_width=True
    )

with st.expander("🤝 View Collaborative Filtering Matrix"):

    interaction_matrix = df[
        ["Item"] + feature_columns
    ].set_index("Item")

    st.dataframe(
        interaction_matrix,
        use_container_width=True
    )

# ============================================================
# PROJECT FEATURES
# ============================================================

st.header("🚀 Project Features")

project_features = [
    ("👤", "User Profile Analysis"),
    ("🔍", "Similar Item Detection"),
    ("🤝", "Collaborative Filtering"),
    ("📈", "User Preference Analysis"),
    ("🎬", "Movie Recommendation"),
    ("📜", "Recommendation History"),
    ("🔥", "Hybrid Recommendation Model"),
    ("⚡", "Interactive Streamlit Dashboard"),
    ("🎯", "Personalized Suggestions"),
    ("🧠", "Content-Based Filtering"),
    ("📊", "Cosine Similarity"),
    ("🧹", "Recommendation History Management")
]

cols = st.columns(3)

for i, (icon, feature) in enumerate(project_features):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="feature-card">

            <h2>{icon}</h2>

            <b>{feature}</b>

            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# HOW IT WORKS
# ============================================================

st.header("⚙️ How the Recommendation Engine Works")

steps = [
    (
        "1️⃣ User Profile",
        "The system collects the user's name and favorite genre."
    ),
    (
        "2️⃣ Content Analysis",
        "Movie characteristics are analyzed using genre-based features."
    ),
    (
        "3️⃣ Similarity Calculation",
        "Cosine similarity identifies items with similar characteristics."
    ),
    (
        "4️⃣ Collaborative Filtering",
        "User-item interaction patterns are used to generate recommendations."
    ),
    (
        "5️⃣ Hybrid Model",
        "Content and collaborative scores are combined."
    ),
    (
        "6️⃣ Personalized Results",
        "The system presents the highest-scoring recommendations."
    )
]

for title, description in steps:

    with st.expander(title):

        st.write(description)

# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.header("🛠️ Technology Stack")

tech_cols = st.columns(5)

technologies = [
    ("🐍", "Python"),
    ("🎈", "Streamlit"),
    ("🐼", "Pandas"),
    ("🔢", "NumPy"),
    ("🤖", "Scikit-Learn")
]

for i, (icon, tech) in enumerate(technologies):

    with tech_cols[i]:

        st.markdown(
            f"""
            <div class="feature-card">

            <h2>{icon}</h2>

            <b>{tech}</b>

            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    <h3>🤖 AI Recommendation Engine</h3>

    <p>
    Developed by <b>Tehmina Anwar</b>
    </p>

    <p>
    🎓 Interngrow AI Internship • 🚀 Task 4 • Week 4
    </p>

    <p>
    AI/ML Engineer • Python Developer • Generative AI Enthusiast
    </p>

    <p>
    Built with Python, Streamlit, Pandas, NumPy & Scikit-Learn ❤️
    </p>

    </div>
    """,
    unsafe_allow_html=True
)
