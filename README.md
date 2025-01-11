# Gemini Spam Detector

This is a Django-based application that integrates with Google's Gemini API to check if a message is spam, fraudulent, or harmful. The application takes user input, processes it through the Gemini API, and provides a result indicating whether the message is spam.

---

## Features
- Detects spam or harmful messages using the Gemini API.
- Simple Django-based setup.
- Provides JSON responses for API calls.
- Includes a web interface to send messages for detection.

---

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.7 or above
- Django 3.2 or above
- Google Gemini API key
- pip for managing Python packages

---

## Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/tusharneje-07/spam-detector-django.git
cd spam-detector-django
```

### Step 2: Set Up a Virtual Environment
```bash
python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure API Key
1. Create a `.env` file in the root of your project.
2. Add your Google Gemini API key:
   ```
   API_KEY=your-google-gemini-api-key
   ```
3. Ensure the `API_KEY` is loaded in `settings.py`:
   ```python
   import os
   API_KEY = os.getenv('API_KEY')
   ```

### Step 5: Migrate the Database
Run the following command to set up the database:
```bash
python manage.py migrate
```

### Step 6: Run the Application
Start the Django development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

---

## Example `.env` File
```plaintext
API_KEY=your-google-gemini-api-key
```

---

## Troubleshooting
- **API Key Error**: Ensure the `.env` file exists and contains the correct API key.
- **Invalid Response**: Check the Gemini API documentation for updates or issues.
- **500 Internal Server Error**: Ensure the database is migrated, and the server is running.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Let me know if you’d like any further changes!
