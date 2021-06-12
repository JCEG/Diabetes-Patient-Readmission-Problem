features_to_drop_v1 = [
'encounter_id', # inutil para el clasificador
'patient_nbr',# inutil para el clasificador
'weight', # 96,8% de missing values
'medical_specialty', # 49.0 % de missing values
'payer_code', # 39.0 % de missing values
'repaglinide', # drugs
'nateglinide', # drugs
'chlorpropamide', # drugs
'glimepiride', # drugs
'acetohexamide', # drugs
'glyburide', # drugs
'tolbutamide', # drugs
'pioglitazone', # drugs
'rosiglitazone', # drugs
'acarbose', # drugs
'miglitol', # drugs
'troglitazone', # drugs
'tolazamide', # drugs
'examide', # drugs
'citoglipton', # drugs
'glyburide-metformin', # drugs
'glipizide-metformin', # drugs
'glimepiride-pioglitazone', # drugs
'metformin-rosiglitazone', # drugs
'metformin-pioglitazone', # drugs
] 


# drugs list
drug_list = ['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 
           'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 
           'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 'tolazamide', 'examide', 
           'citoglipton', 'glyburide-metformin', 'glipizide-metformin', 'glimepiride-pioglitazone',
           'metformin-rosiglitazone', 'metformin-pioglitazone','insulin']


ordinal_features_to_keep_v1 = [
'age',
'max_glu_serum', # max_glu_serum test result. none significa no medida
'A1Cresult_v1', # A1c test result
'insulin', # drugs
'metformin',# drugs
'glipizide'# drugs
]

ordinal_features_to_keep_v2 = ['age']


categorical_features_to_keep_v1 = [
'age_grouped',
'race',
'gender',
'diag_1_v1', # from 716 clases to 9
'diag_2_v1', # 748 to 9
'diag_3_v1', # 789 to 9
'change', # si se hizo cambio en la medicacion
'diabetesMed', # binaria indica si hubo o no medicacion para la diabetes
'admission_type_id_v1',
'discharge_disposition_id_v1',
'admission_source_id_v1',
]

categorical_features_to_keep_v2 = [
'age_grouped',
'race',
'gender',
'diag_1_v1', # from 716 clases to 9
'diag_2_v1', # 748 to 9
'diag_3_v1', # 789 to 9
'change', # si se hizo cambio en la medicacion
'diabetesMed', # binaria indica si hubo o no medicacion para la diabetes
'admission_type_id_v1',
'discharge_disposition_id_v1',
'admission_source_id_v1',
'max_glu_serum', # max_glu_serum test result. none significa no medida
'A1Cresult_v1', # A1c test result
'insulin', # drugs
'metformin',# drugs
'glipizide'# drugs
]

categorical_features_to_keep_v3 = [
'age_grouped',
'race',
'gender',
'diag_1_v1', # from 716 clases to 9
'diag_2_v1', # 748 to 9
'diag_3_v1', # 789 to 9
'change', # si se hizo cambio en la medicacion
'diabetesMed', # binaria indica si hubo o no medicacion para la diabetes
'admission_type_id_v2',
'discharge_disposition_id_v2',
'admission_source_id_v2',
]

numerical_features_to_keep_v1 = [
'time_in_hospital',
'num_lab_procedures',
'num_procedures',
'num_medications', # validar pues la descripcion no es clara si es un numero o una clase
'number_outpatient', # Número de visitas ambulatorias
'number_emergency',
'number_inpatient', # Número de visitas hospitalarias
'number_diagnoses',
'count_change_meds', # variable nueva paper numero 8
'service_utilization' # variable nueva paper numero 9
]




output_original = ['readmitted'] 
output = ['binary_readmitted_v1'] #{'NO':0,'>30':1,'<30':1}
output_binary = ['binary_readmitted_v2'] # {'NO':0,'>30':0,'<30':1}


set_variables_v1 = {'drop': features_to_drop_v1, 
                    'ordinal': ordinal_features_to_keep_v1,
                    'categorical': categorical_features_to_keep_v1,
                    'numerical': numerical_features_to_keep_v1,
                    }

set_variables_v2 = {'drop': features_to_drop_v1, 
                    'ordinal': ordinal_features_to_keep_v2,
                    'categorical': categorical_features_to_keep_v2,
                    'numerical': numerical_features_to_keep_v1,
                    }
                    
set_variables_v3 = {'drop': features_to_drop_v1, 
                    'ordinal': ordinal_features_to_keep_v1,
                    'categorical': categorical_features_to_keep_v3,
                    'numerical': numerical_features_to_keep_v1,
                    }