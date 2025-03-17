import csv

def merge_csv_files(file1, file2, output_file):
    """
    Menggabungkan dua file CSV menjadi satu file output.
    
    Args:
        file1 (str): Path ke file CSV pertama.
        file2 (str): Path ke file CSV kedua.
        output_file (str): Path untuk file CSV output gabungan.
    """
    # List untuk menyimpan semua baris dari kedua file
    combined_rows = []

    # Menaikkan batas maksimum ukuran field
    import sys
    max_int = sys.maxsize
    while True:
        try:
            csv.field_size_limit(max_int)
            break
        except OverflowError:
            max_int = int(max_int / 10)

    # Membaca file CSV pertama
    try:
        with open(file1, 'r', encoding='utf-8') as f1:
            reader1 = csv.reader(f1)
            header1 = next(reader1)  # Simpan header dari file pertama
            combined_rows.extend(reader1)  # Tambahkan semua baris dari file pertama
    except FileNotFoundError:
        print(f"File {file1} tidak ditemukan.")
        return
    except Exception as e:
        print(f"Error saat membaca {file1}: {e}")
        return

    # Membaca file CSV kedua
    try:
        with open(file2, 'r', encoding='utf-8') as f2:
            reader2 = csv.reader(f2)
            header2 = next(reader2)  # Simpan header dari file kedua
            
            # Pastikan header kedua file sama
            if header1 != header2:
                print("Header kedua file tidak cocok. Penggabungan dibatalkan.")
                return
            
            combined_rows.extend(reader2)  # Tambahkan semua baris dari file kedua
    except FileNotFoundError:
        print(f"File {file2} tidak ditemukan.")
        return
    except Exception as e:
        print(f"Error saat membaca {file2}: {e}")
        return

    # Menyimpan hasil gabungan ke file output
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header1)  # Tulis header sekali saja
            writer.writerows(combined_rows)  # Tulis semua baris gabungan
        print(f"File berhasil digabungkan. Total baris: {len(combined_rows)}")
        print(f"Hasil disimpan di {output_file}")
    except Exception as e:
        print(f"Error saat menulis file output: {e}")

# Jalankan fungsi
file1 = "webdev_text_samples.csv"  # Ganti dengan path file CSV pertama
file2 = "webdev_text_samples2.csv"  # Ganti dengan path file CSV kedua
output_file = "datasets/merged_TextSample.csv"  # Ganti dengan nama file output
merge_csv_files(file1, file2, output_file)