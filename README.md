Diabetes Patient Readmission Problem
==============================

Author: Juan Echeverri<br>
Email: jecheverrigutierrez@gmail.com<br>
Resume: http://jecheverrigutierrez.s3-website-us-east-1.amazonaws.com/<br>

Classification with Diabetes readmission dataset<br>
source : https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008#<br>

The data are submitted on behalf of the Center for Clinical and Translational Research, Virginia Commonwealth University, a recipient of NIH CTSA grant UL1 TR00058 and a recipient of the CERNER data. John Clore (jclore '@' vcu.edu), Krzysztof J. Cios (kcios '@' vcu.edu), Jon DeShazo (jpdeshazo '@' vcu.edu), and Beata Strack (strackb '@' vcu.edu). This data is a de-identified abstract of the Health Facts database (Cerner Corporation, Kansas City, MO).

Data Set Information:<br>

The dataset represents 10 years (1999-2008) of clinical care at 130 US hospitals and integrated delivery networks. It includes over 50 features representing patient and hospital outcomes. Information was extracted from the database for encounters that satisfied the following criteria. (1) It is an inpatient encounter (a hospital admission). (2) It is a diabetic encounter, that is, one during which any kind of diabetes was entered to the system as a diagnosis. (3) The length of stay was at least 1 day and at most 14 days. (4) Laboratory tests were performed during the encounter. (5) Medications were administered during the encounter. The data contains such attributes as patient number, race, gender, age, admission type, time in hospital, medical specialty of admitting physician, number of lab test performed, HbA1c test result, diagnosis, number of medication, diabetic medications, number of outpatient, inpatient, and emergency visits in the year before the hospitalization, etc.

Problem Scope<br>
I have decided to solve the problem considering it as a binary classification problem, assuming that "No" = 0, otherwise 1. This was decided base ond the next description:

No readmission<br>
A readmission in less than 30 days (this situation is not good, because maybe your treatment was not appropriate); <br>
A readmission in more than 30 days (this one is not so good as well the last one, however, the reason could be the state of the patient. <br>

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebook: 01-JCEG-Diabetes Patient Readmission Problem.ipynb
    │
    ├── references         <- Data dictionaries, papers, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated PDF: 01-JCEG-Diabetes-Patient-Readmission-Problem-ipynb-2021-06-11-18_56_08.pdf
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis requirements.txt
    │
    ├── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
             └── get_raw_data.py
             └── variables_set.py
