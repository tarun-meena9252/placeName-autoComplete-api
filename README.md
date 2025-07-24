# 📍 Autocomplete Places API

This is a simple and lightweight API built with FastAPI to provide **autocomplete suggestions** and **place details** using Google Places API.

It is designed to work seamlessly with frontend apps (like React Native/Expo) and supports local development with [ngrok](https://ngrok.com/).

---

## 📦 Setup Instructions

### 1. Create a Virtual Environment

From inside the `placeName-autoComplete-api
` directory, create a virtual environment:

```bash
python -m venv venv
```
This will create a venv/ folder with an isolated Python environment.

2. Activate the Virtual Environment
On macOS/Linux:

```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```
3. Install Dependencies
Make sure you're in the same folder as requirements.txt, then run:

```bash
pip install -r requirements.txt
```
This will install all the required packages inside the virtual environment.

🚀 Running the API
4. Start the FastAPI Server Locally
Navigate to the places_api directory:

```bash
cd places_api
uvicorn main:app --reload --port 8000
```
5. Expose API to the Internet using ngrok
Option 1: Temporary ngrok tunnel
```bash
ngrok http 8000
```
Option 2: Use a reserved ngrok domain
```bash
ngrok http --domain=some-name.ngrok-free.app 8000
```
Update your frontend to call APIs using this ngrok URL.

🌐 API Endpoints
You can use these endpoints from a browser or app (e.g., with fetch()):

🔤 Autocomplete
```bash
GET /autocomplete?input=pune
```
Example:

```bash
http://localhost:8000/autocomplete?input=pune
```
🗺️ Place Details
```bash
GET /place-details?place_id=ChIJrTLr-GyuEmsRBfy61i59si0
```
Example:

```bash
http://localhost:8000/place-details?place_id=ChIJrTLr-GyuEmsRBfy61i59si0
```
📲 Using with Fetch in Frontend
```bash
fetch('https://your-ngrok-subdomain.ngrok-free.app/autocomplete?input=mumbai')
```
Replace your-ngrok-subdomain with your actual ngrok domain.

🛠 Tech Stack
FastAPI

Uvicorn

Python 3.x

Google Places API

ngrok

📁 Project Structure
bash
Copy
Edit
autoCompleteApi/
│
├── venv/                   # Virtual environment
├── requirements.txt        # Python dependencies
└── places_api/
    └── main.py             # FastAPI app with autocomplete and details endpoints
