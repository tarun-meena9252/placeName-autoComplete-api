useful commands:
1) Create a virtual environment
(Inside autoCompleteApi directory):
Pick a name for your environment (commonly .venv, env, or venv):
    -> python -m venv venv
This will create a folder venv/ containing an isolated Python environment.

2) Activate virtual environment-
(activate from inside autoCompleteApi directory):
    -> source venv/bin/activate

3) Install dependencies from requirements.txt
(Make sure you're in the same folder as requirements.txt, then run):
    -> pip install -r requirements.txt
This will install all packages listed in the file into the virtual environment.

4) Run the API on local host-
(first navigate to places_api directory)
    -> cd places_api
    -> uvicorn main:app --reload --port 8000

5) Run ngrok server over public internet -
    -> ngrok http 8000

    OR 
    
    Use a reserved domain :
    -> ngrok http --domain=some-name.ngrok-free.app 8000 

6) Using the API-
    #(from a webbrowser)
    Autocomplete: 
        http://localhost:8000/autocomplete?input=pune
    Details:
        http://localhost:8000/place-details?place_id=ChIJrTLr-GyuEmsRBfy61i59si0

    #(from app use fetch() method)
        fetch('https://<your-ngrok-url>.ngrok.io/autocomplete?input=mumbai')
