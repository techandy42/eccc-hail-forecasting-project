# Datasets

- The original 10k hail dataset can be found at [Hail Forecasting Google Drive/Cleaned hackathon solutions Folder](https://drive.google.com/drive/folders/1gj-vg8DcYMMyHnD5eU1607hj44BSENVd?usp=drive_link).
- Other hail datasets can be found at [Hail Forecasting Google Drive/Hail_db Folder](https://drive.google.com/drive/folders/1y8UK8ykSIHgfYe71NA6tSEJVYJTz2vo0?usp=drive_link).
- The LLM-processed hail datasets can be found at [Hail Forecasting Google Drive/Datasets Folder](https://drive.google.com/drive/folders/1FLKqTb6U71Tvq16jiwE6Pln1e-xnfMV3?usp=drive_link).
- If you do not have access to the folder, please send an email at `techandy42@gmail.com` or `dominique.brunet@ec.gc.ca` to gain access.

### About

- [hail_predictors_10k.csv](https://drive.google.com/file/d/1FTxyOR41ZV3UFu0tMLZ1dvtppw0PtvLr/view?usp=drive_link) contains 10K samples of No Hail vs Hail observations used to train the hail forecasting models.
- [hail_db_with_size_v20230204.csv](https://drive.google.com/file/d/1fQDnHvHqs14DX1YudOSLIn3dPIyR3Mp-/view?usp=drive_link) contains 7K samples of hail observations, the dataset has been further processed with the LLM data extraction code.
- [HailReferenceObjects.csv](https://drive.google.com/file/d/195sLHmpYKRuOuSpfCQRrzZ7Xtal2HO_8/view?usp=drive_link) contains list of reference objects used to measure the size of hails.
- [extracted_info_combined.csv](https://drive.google.com/file/d/1U1amjrvaE1c-RchkBQwDPkOFry-YXuFk/view?usp=drive_link) contains fields extracted from `hail_db_with_size_v20230204.csv` observation notes using LLM.
- [extracted_info_with_validation.csv](https://drive.google.com/file/d/1_j22oW2Xk1w8goq3Qh43up_zalsQEtiK/view?usp=drive_link) contains `extracted_info_combined.csv` data with each row's fields validated using Google Maps API and LLM.
- [extracted_info_with_validation_and_link_status.csv](https://drive.google.com/file/d/19rJLGi3FIOYbI4jr632BhRHpjBjEWTib/view?usp=drive_link) contains `extracted_info_with_validation.csv` data with each social media link validated using the web scrapping scripts.
