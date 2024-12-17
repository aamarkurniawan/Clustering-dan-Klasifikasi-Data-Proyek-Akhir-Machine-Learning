# -*- coding: utf-8 -*-
"""[Klasifikasi] Submission Akhir Mu'ammar Kurniawan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tLOrNBiAvsMB2XycXjzCnWj1IHSk4LI5

# **1. Import Library**

Pada tahap ini, Anda perlu mengimpor beberapa pustaka (library) Python yang dibutuhkan untuk analisis data dan pembangunan model machine learning.
"""

# Import library yang dibutuhkan
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
import joblib

"""# **2. Memuat Dataset dari Hasil Clustering**

Memuat dataset hasil clustering dari file CSV ke dalam variabel DataFrame.
"""

# Memuat dataset hasil clustering
file_path = 'clustering_result.csv'  # Ganti path sesuai lokasi file di Colab
data = pd.read_csv(file_path)
print("Dataset berhasil dimuat!")
print(data.head())

"""# **3. Data Splitting**

Tahap Data Splitting bertujuan untuk memisahkan dataset menjadi dua bagian: data latih (training set) dan data uji (test set).
"""

# Preprocessing Data
# Encode kolom kategorikal
categorical_columns = ['nama_variabel', 'nama_variabel_turunan', 'nama_turunan_tahun',
                       'nama_item_vertical_variabel', 'content_category']
encoder = LabelEncoder()
for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])

# Memilih fitur dan label
features = ['data_content', 'data_content_scaled', 'nama_tahun'] + categorical_columns
X = data[features]
y = data['Cluster']

# Standarisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Tampilkan bentuk data
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)

"""# **4. Membangun Model Klasifikasi**

## **a. Membangun Model Klasifikasi**

Setelah memilih algoritma klasifikasi yang sesuai, langkah selanjutnya adalah melatih model menggunakan data latih.

Berikut adalah rekomendasi tahapannya.
1. Pilih algoritma klasifikasi yang sesuai, seperti Logistic Regression, Decision Tree, Random Forest, atau K-Nearest Neighbors (KNN).
2. Latih model menggunakan data latih.
"""

# Model 1: Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# Model 2: Logistic Regression
lr_model = LogisticRegression(random_state=42, max_iter=1000)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

"""Tulis narasi atau penjelasan algoritma yang Anda gunakan.

## **b. Evaluasi Model Klasifikasi**

Berikut adalah **rekomendasi** tahapannya.
1. Lakukan prediksi menggunakan data uji.
2. Hitung metrik evaluasi seperti Accuracy dan F1-Score (Opsional: Precision dan Recall).
3. Buat confusion matrix untuk melihat detail prediksi benar dan salah.
"""

# Evaluasi Random Forest
print("Random Forest - Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Random Forest - F1 Score:", f1_score(y_test, y_pred_rf, average='weighted'))

# Evaluasi Logistic Regression
print("Logistic Regression - Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Logistic Regression - F1 Score:", f1_score(y_test, y_pred_lr, average='weighted'))

"""Tulis hasil evaluasi algoritma yang digunakan, jika Anda menggunakan 2 algoritma, maka bandingkan hasilnya.

## **c. Tuning Model Klasifikasi (Optional)**

Gunakan GridSearchCV, RandomizedSearchCV, atau metode lainnya untuk mencari kombinasi hyperparameter terbaik
"""

# Hyperparameter tuning untuk Random Forest
param_grid_rf = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}
grid_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=3, scoring='f1_weighted')
grid_rf.fit(X_train, y_train)
print("Best parameters for Random Forest:", grid_rf.best_params_)

"""## **d. Evaluasi Model Klasifikasi setelah Tuning (Optional)**

Berikut adalah rekomendasi tahapannya.
1. Gunakan model dengan hyperparameter terbaik.
2. Hitung ulang metrik evaluasi untuk melihat apakah ada peningkatan performa.
"""

# Menggunakan model terbaik dari GridSearchCV
best_rf_model = grid_rf.best_estimator_
y_pred_best_rf = best_rf_model.predict(X_test)

# Evaluasi ulang model Random Forest
print("Tuned Random Forest - Accuracy:", accuracy_score(y_test, y_pred_best_rf))
print("Tuned Random Forest - F1 Score:", f1_score(y_test, y_pred_best_rf, average='weighted'))

"""## **e. Analisis Hasil Evaluasi Model Klasifikasi**"""

# Confusion Matrix dan Classification Report untuk kedua model
print("\nConfusion Matrix - Random Forest")
print(confusion_matrix(y_test, y_pred_rf))
print("\nConfusion Matrix - Logistic Regression")
print(confusion_matrix(y_test, y_pred_lr))

# Analisis hasil dengan Classification Report
print("\nClassification Report - Random Forest")
print(classification_report(y_test, y_pred_rf))

print("\nClassification Report - Logistic Regression")
print(classification_report(y_test, y_pred_lr))

"""Berikut adalah **rekomendasi** tahapannya.
1. Bandingkan hasil evaluasi sebelum dan setelah tuning (jika dilakukan):
Sebelum tuning, Random Forest sudah menunjukkan hasil yang sangat baik dengan akurasi dan F1-Score mencapai 100%. Setelah tuning, hasilnya tetap sama, jadi tuning tidak memberikan perbedaan besar. Logistic Regression juga menunjukkan hasil yang sangat baik dengan akurasi dan F1-Score sekitar 98.26%.

2. Identifikasi kelemahan model:

* Precision atau Recall rendah untuk kelas tertentu:
Tidak ada masalah dengan precision atau recall yang rendah. Random Forest memberikan hasil yang sempurna untuk semua kelas, sementara Logistic Regression hanya memiliki sedikit kesalahan yang tidak terlalu signifikan.
*Apakah model mengalami overfitting atau underfitting?
Random Forest berpotensi mengalami overfitting karena hasilnya sempurna, terutama jika datasetnya kecil. Logistic Regression tampaknya lebih generalisasi dan stabil.

3. Berikan rekomendasi tindakan lanjutan:


*  Untuk mengatasi kemungkinan overfitting pada Random Forest, bisa mencoba membatasi kedalaman pohon atau menambahkan data baru.
*  Logistic Regression bisa ditingkatkan dengan menambahkan fitur baru atau mencoba algoritma lain seperti Gradient Boosting jika diperlukan.
*  Jika dataset dirasa terlalu kecil, ada baiknya mengumpulkan lebih banyak data agar model bisa lebih generalisasi dan stabil.


"""