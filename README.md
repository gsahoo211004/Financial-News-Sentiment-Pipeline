# FinancialInsight — AI-Driven Market Sentiment Pipeline

**FinancialInsight** is a full-stack Data Engineering and AI platform built to automate the extraction, transformation, and analysis of unstructured financial news data. It leverages Natural Language Processing (NLP) to provide real-time sentiment scores, transforming raw headlines into actionable, predictive business insights.

## 🚀 Key Features
* **Automated Data Ingestion:** Connects to external News APIs to gather real-time data on specific market sectors.
* **AI-Driven Sentiment Analysis:** Utilizes NLP (`TextBlob`) to quantify market mood through Polarity and Subjectivity scores, categorizing news as Positive, Negative, or Neutral.
* **Interactive Dashboard:** A responsive web interface built with **Bootstrap 5** and **Chart.js** for visualizing sentiment distribution and communicating findings to stakeholders.
* **Data Integrity & Governance:** Implemented a relational database schema using Django ORM to ensure data validation, quality, and duplicate prevention.
* **Enterprise Security:** Utilizes environment variables (`python-dotenv`) to securely manage API keys and application secrets.

## 🛠️ Tech Stack
* **Backend Framework:** Django (Python)
* **Database:** SQLite / PostgreSQL
* **AI & NLP:** TextBlob
* **Frontend:** HTML5, CSS3, Bootstrap 5, Chart.js
* **Data Tools & Security:** Requests, Pandas, python-dotenv

## 📂 Project Structure
```text
├── financial_insight_hub/
│   ├── dashboard/
│   │   ├── models.py      # Relational Data Schema
│   │   ├── utils.py       # AI Logic, Data Transformation & API Integration
│   │   ├── views.py       # Query Optimization & Context Rendering
│   │   └── templates/     # Interactive UI/UX Dashboard
│   ├── .env               # Secure Environment Variables (Ignored by Git)
│   └── settings.py        # Core Configuration
```

## ⚙️ Setup & Installation

**1. Clone the Repository:**
```bash
git clone https://github.com/yourusername/Financial-News-Sentiment-Pipeline.git
cd Financial-News-Sentiment-Pipeline
```

**2. Install Dependencies:**
```bash
pip install django requests textblob pandas python-dotenv
```

**3. Configure Environment Variables:**
Create a `.env` file in the root directory (where `manage.py` is located) and add your keys:
```text
NEWS_API_KEY=your_newsapi_org_key_here
DJANGO_SECRET_KEY=your_django_secret_key_here
```

**4. Run Database Migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Start the Server:**
```bash
python manage.py runserver
```
*Navigate to `http://127.0.0.1:8000/` in your browser to view the live dashboard.*
