import os

# Jalankan preprocessing
print("\n[STEP 2] Preprocessing Text...")
os.system("python preprocessing/text_preprocessing.py")

# Jalankan konversi teks ke numerik
print("\n[STEP 3] Converting Text to Numerical Form...")
os.system("python vectorization/text_vectorization.py")

print("\nSemua proses selesai!")
