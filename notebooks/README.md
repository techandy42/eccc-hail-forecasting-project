# Notebooks

- The Colab notebooks can be found at [Hail Forecasting Google Drive/Notebooks Folder](https://drive.google.com/drive/folders/1Zt2RvmurvnNoFaNOgp3cNkqhztDKJNie?usp=drive_link).
- If you do not have access to the folder, please send an email at `techandy42@gmail.com` or `dominique.brunet@ec.gc.ca` to gain access.

### API Keys

- The LLM-related code at `azure_openai_api_demo_notebook.ipynb`, `hail_db_data_extraction.ipynb`, `hail_db_data_validation.ipynb`, and `hail_db_data_filtering.ipynb` notebooks require Azure API keys and Google Maps key. Please ask Dominique Brunet at `dominique.brunet@ec.gc.ca` or Stuart Spence at `stuart.spence@ec.gc.ca` to get the Azure API keys, and please create a project on Google Cloud Platform, enable Geocoding API, and get a credentials API to access Google Maps API [tutorial](https://developers.google.com/maps/get-started).

### About

- `hail_forecasting_v0.1.ipynb` notebook contains code to train XGBoost models for (1) Hail vs No Hail, (2) Severe vs Non-Severe, (3) Hail vs No Hail w/t Weights, and (4) categorical (No Hail, Non-Severe Hail, Severe Hail, and Seriously Severe Hail) classification. Should be ran as Colab notebook
- `azure_openai_api_demo_notebook.ipynb` notebook contains example code for running inferences on GPT-4 via Azure OpenAI API.
- `hail_db_data_extraction.ipynb` notebook contains code to extract fields from hail observation notes using LLM. Should be ran as Colab notebook. Already ran on all 7K observations.
- `hail_db_data_validation.ipynb` notebook contains code to validate the extracted fields using Google Maps API and LLM. Should be ran as Colab notebook. Already ran on all 7K observations.
- `hail_db_data_filtering.ipynb` notebook contains code to filter out confidential information (e.g. names, emails, phone numbers) from hail observation notes. Should be ran as Colab notebook. Haven't been ran yet on the 7K observations.
