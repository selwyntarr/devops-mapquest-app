# MapQuest WebApp

# Description
The **MapQuest Explorer** project is a web application that leverages the MapQuest API to provide users with an intuitive and interactive mapping experience. Our goal is to create a user-friendly interface that allows individuals to explore maps, obtain directions, and access location-based information effortlessly.

# Team Members
- Tarriela
- Teope
- Agpaoa

# Tech Stack
- Python StreamLit
- API (MapQuest)

# Installation

1. Create Virtual Environment
```
python -m venv mapquest-app
```

2. Activate Virtual Environment
```
.\mapquest\Scripts\activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Create Environment Variables
- Create a new file named `.env`
- Add an entry for `API_KEY`
```
API_KEY = "your-mapquest-api-key-here"
```

4. Run Streamlit App
```
streamlit run app.py
```