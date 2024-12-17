# 📊 Proyek Akhir Machine Learning: Clustering & Klasifikasi

Proyek ini adalah implementasi tugas akhir mata kuliah *Machine Learning* di Universitas Pamulang. Tujuan dari proyek ini adalah membangun model *Clustering* dan *Klasifikasi* menggunakan dataset yang telah diproses, serta menganalisis hasil evaluasi model.

---

## 📌 **Deskripsi Proyek**
1. **Clustering**:  
   - Menggunakan metode *KMeans* untuk mengelompokkan data menjadi 3 cluster.
   - Dataset terdiri dari kolom numerikal dan kategorikal yang telah diproses.
   - Evaluasi dilakukan menggunakan **Silhouette Score**.

2. **Klasifikasi**:  
   - Menggunakan algoritma **Random Forest** dan **Logistic Regression**.
   - Dataset yang digunakan adalah hasil dari clustering, di mana label cluster menjadi target klasifikasi.
   - Evaluasi dilakukan dengan metrik **Accuracy** dan **F1-Score**.
   - Model dievaluasi sebelum dan setelah tuning hyperparameter.

---

## 🛠 **Teknologi yang Digunakan**
- Python 3.x
- Scikit-learn
- Pandas
- Numpy
- Matplotlib & Seaborn
- Google Colab

---

## 🗂 **Struktur Proyek**
📁 Proyek_Machine_Learning │ ├── clustering_result.csv # Dataset hasil Clustering ├── README.md # Dokumentasi proyek ini ├── RandomForest_Model.pkl # Model Random Forest terbaik setelah tuning │ └── Notebooks: ├── Clustering.ipynb # Notebook untuk implementasi Clustering └── Classification.ipynb # Notebook untuk implementasi Klasifikasi
