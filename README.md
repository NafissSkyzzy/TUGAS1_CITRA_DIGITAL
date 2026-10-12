# Laporan Project Image Analysis

## Pembuktian bahwa Citra Digital Merupakan Susunan Angka Menggunakan Python

**Nama:** Muhammad Nafis Abdillah\
**NIM:** 24260026\
**Mata kuliah:** Pengolahan Citra Digital\
**Bahasa pemrograman:** Python\
**Library:** Pillow dan NumPy\
**File yang dianalisis:** `gambar.jpg`

------------------------------------------------------------------------

## 1. Pendahuluan

Citra digital yang ditampilkan di layar komputer bukan hanya gambar
visual, tetapi juga data yang direpresentasikan secara numerik. Pada
citra raster, gambar tersusun atas piksel-piksel. Setiap piksel memiliki
posisi dan nilai tertentu yang menentukan warna atau tingkat
kecerahannya.

Project ini bertujuan membuktikan bahwa citra digital dapat dibaca
sebagai susunan angka menggunakan Python. Program membaca informasi
gambar, mengubah piksel menjadi array numerik, menampilkan sebagian
matriks nilai warna, menghitung statistik dasar, mengonversi gambar
menjadi grayscale, dan merekonstruksi gambar dari data piksel.

Selain itu, program membaca metadata yang tersedia pada file, seperti
format, dimensi, informasi kamera, tanggal, resolusi, dan informasi
frame.

## 2. Tujuan

1.  Membuktikan bahwa gambar digital dapat direpresentasikan sebagai
    array angka.
2.  Menjelaskan hubungan antara piksel, channel RGB, dan matriks
    numerik.
3.  Menghitung jumlah piksel dan jumlah nilai warna dalam gambar.
4.  Menampilkan nilai piksel dan sebagian matriks channel merah, hijau,
    dan biru.
5.  Mengubah citra RGB menjadi grayscale menggunakan operasi matematika.
6.  Menguji apakah citra yang direkonstruksi dari array memiliki nilai
    piksel yang identik dengan array awal.
7.  Membaca metadata file untuk memperoleh informasi tambahan tentang
    gambar.

## 3. Perangkat dan Library

-   **Python:** menjalankan program analisis.
-   **Pillow (`PIL`):** membuka, membaca, mengonversi, dan menyimpan
    gambar serta membaca sejumlah metadata.
-   **NumPy:** mengubah gambar menjadi array numerik dan melakukan
    perhitungan.
-   **Terminal/CMD:** menjalankan program tanpa antarmuka grafis.

Instalasi library:

``` bat
py -m pip install pillow numpy
```

## 4. Cara Menjalankan Program

Letakkan `image_analysis.py` dan `gambar.jpg` di folder yang sama. Buka
terminal pada folder tersebut, kemudian jalankan:

``` bat
py image_analysis.py gambar.jpg
```

Jika nama atau ekstensi gambar berbeda, sesuaikan argumen perintah
dengan nama file yang digunakan.

## 5. Ringkasan Hasil Analisis

Berdasarkan output program, diperoleh hasil berikut:

  Parameter                                            Hasil
  ------------------------------------- --------------------
  Nama file                                     `gambar.jpg`
  Format yang dikenali Pillow                            MPO
  Dimensi gambar yang dianalisis          7952 × 5304 piksel
  Mode warna yang digunakan                              RGB
  Tipe data array                                    `uint8`
  Bentuk array RGB                         `(5304, 7952, 3)`
  Jumlah piksel                                   42.177.408
  Jumlah nilai RGB                               126.532.224
  Nilai minimum                                            0
  Nilai maksimum                                         255
  Rata-rata seluruh nilai RGB                         106,09
  Nilai intensitas unik channel merah                    256
  Nilai intensitas unik channel hijau                    254
  Nilai intensitas unik channel biru                     256
  Ukuran array RGB di memori                126.532.224 byte
  Ukuran array grayscale                     42.177.408 byte
  Ukuran file asli                           19.660.800 byte
  Hasil uji rekonstruksi                              `True`

**Catatan penting:** file terdeteksi sebagai MPO (*Multi-Picture
Object*) dan memiliki dua frame. Kode analisis utama menggunakan gambar
yang dibuka oleh Pillow, lalu mengonversinya ke RGB. Pada implementasi
ini, array yang dianalisis adalah frame yang sedang dibuka secara
default---umumnya frame pertama. Program belum menganalisis kedua frame
MPO secara terpisah.

## 6. Penjelasan Konsep

### 6.1 Piksel dan channel RGB

Piksel adalah unit terkecil pada citra raster. Dalam representasi RGB
8-bit, setiap piksel memiliki tiga nilai:

-   **R (Red):** intensitas merah.
-   **G (Green):** intensitas hijau.
-   **B (Blue):** intensitas biru.

Setiap channel mempunyai nilai 0 sampai 255. Sebagai contoh,
`(255, 0, 0)` berarti merah murni, `(0, 0, 0)` berarti hitam, dan
`(255, 255, 255)` berarti putih.

Secara matematis, sebuah piksel dapat ditulis:

\[ P(x,y) = \[R(x,y), G(x,y), B(x,y)\] \]

`x` menunjukkan posisi kolom dan `y` menunjukkan posisi baris.

### 6.2 Array tiga dimensi

Program menghasilkan array dengan bentuk `(5304, 7952, 3)`. Artinya:

-   5304 baris piksel;
-   7952 kolom piksel;
-   3 channel warna pada setiap piksel.

Jumlah piksel dihitung dengan:

\[ 7952 `\times 5304`{=tex} = 42.177.408 \]

Jumlah nilai RGB adalah:

\[ 42.177.408 `\times 3`{=tex} = 126.532.224 \]

Dengan demikian, satu gambar berukuran tersebut memiliki lebih dari 42
juta piksel dan lebih dari 126 juta nilai channel RGB.

### 6.3 Tipe data `uint8`

`uint8` adalah tipe bilangan bulat 8-bit tanpa tanda, dengan rentang
0--255. Karena setiap nilai membutuhkan satu byte, array RGB memerlukan:

\[ 126.532.224 `\times 1`{=tex} = 126.532.224 `\text{ byte}`{=tex} \]

Sementara array grayscale hanya memiliki satu nilai per piksel, sehingga
ukurannya:

\[ 42.177.408 `\times 1`{=tex} = 42.177.408 `\text{ byte}`{=tex} \]

Angka tersebut adalah kebutuhan memori array mentah, bukan ukuran file
gambar terkompresi.

### 6.4 Statistik intensitas

Nilai minimum, maksimum, dan rata-rata digunakan untuk merangkum
distribusi nilai dalam array RGB. Nilai minimum 0 dan maksimum 255
menunjukkan bahwa data memiliki nilai pada kedua ujung rentang
intensitas 8-bit.

Jumlah nilai unik menunjukkan banyaknya intensitas berbeda yang
benar-benar ditemukan pada masing-masing channel. Channel merah dan biru
memiliki 256 nilai unik, sedangkan channel hijau memiliki 254 nilai unik
pada citra yang dianalisis.

### 6.5 Konversi grayscale

Program menghitung intensitas grayscale dengan rumus pendekatan
luminansi:

\[ Y = 0{,}299R + 0{,}587G + 0{,}114B \]

Nilai hasil perhitungan dibulatkan dan disimpan sebagai `uint8`.
Grayscale menghasilkan satu nilai intensitas untuk setiap piksel, bukan
tiga nilai RGB.

### 6.6 Rekonstruksi gambar

Array RGB diubah kembali menjadi objek gambar, kemudian disimpan sebagai
`hasil_rekonstruksi.png`. Program membaca kembali gambar hasil tersebut
menjadi array dan membandingkannya menggunakan `np.array_equal()`.

Output `True` berarti nilai array RGB yang dibandingkan identik. Hal ini
membuktikan bahwa data numerik yang dibaca program dapat digunakan untuk
membentuk kembali citra dengan nilai piksel yang sama. Pengujian ini
membandingkan array RGB hasil pembacaan dengan array RGB hasil
rekonstruksi, bukan membandingkan byte file PNG dengan byte file
MPO/JPEG.

## 7. Penjelasan Kode Program

### 7.1 Mengimpor library

``` python
import sys
from pathlib import Path
import numpy as np
from PIL import Image
```

-   `sys` digunakan untuk membaca argumen dari terminal.
-   `Path` memeriksa keberadaan file dan membaca informasi ukuran file.
-   `numpy` digunakan untuk mengolah data numerik.
-   `Image` dari Pillow digunakan untuk membaca dan menyimpan gambar.

### 7.2 Memeriksa dan membuka file

``` python
path = Path(image_path)

if not path.is_file():
    print(f"ERROR: File tidak ditemukan: {path}")
    return

with Image.open(path) as original:
    ...
```

Kode memeriksa apakah file tersedia. Jika file tidak ditemukan, program
menampilkan pesan kesalahan. `Image.open()` membuka file gambar agar
properti dan pikselnya dapat dibaca.

### 7.3 Mengubah gambar menjadi array RGB

``` python
rgb_image = original.convert("RGB")
pixels = np.array(rgb_image)
```

Konversi ke RGB memastikan gambar yang dianalisis memiliki tiga channel
warna. `np.array()` mengubah data piksel menjadi array NumPy sehingga
nilainya bisa dihitung dan ditampilkan.

### 7.4 Membaca bentuk array dan statistik

``` python
height, width, channels = pixels.shape

print(pixels.dtype)
print(pixels.shape)
print(pixels.size)
print(pixels.min())
print(pixels.max())
print(pixels.mean())
```

-   `shape` memberikan dimensi array.
-   `dtype` menunjukkan tipe data.
-   `size` menghitung seluruh elemen array.
-   `min()` dan `max()` mencari nilai terendah dan tertinggi.
-   `mean()` menghitung rata-rata semua nilai channel RGB.

### 7.5 Menampilkan nilai piksel

``` python
for x in range(min(5, width)):
    r, g, b = pixels[0, x]
    print(f"Piksel (x={x}, y=0): R={r}, G={g}, B={b}")
```

Kode mengambil lima piksel pertama pada baris teratas. `pixels[0, x]`
mengakses piksel pada baris nol dan kolom `x`. Ketiga nilainya kemudian
ditampilkan sebagai R, G, dan B.

### 7.6 Menampilkan matriks setiap channel

``` python
print(pixels[:rows, :cols, 0])
print(pixels[:rows, :cols, 1])
print(pixels[:rows, :cols, 2])
```

Indeks terakhir menunjukkan channel yang diambil:

-   `0` untuk merah;
-   `1` untuk hijau;
-   `2` untuk biru.

Program hanya menampilkan maksimal 5 × 5 nilai agar output terminal
tetap ringkas. Seluruh data gambar tetap tersimpan dalam array `pixels`.

### 7.7 Menghitung nilai intensitas unik

``` python
for i, channel_name in enumerate(["Merah", "Hijau", "Biru"]):
    values = pixels[:, :, i]
    print(len(np.unique(values)))
```

`np.unique()` mencari nilai berbeda dalam sebuah channel. Hasilnya
menunjukkan jumlah intensitas unik yang ditemukan, bukan jumlah piksel.

### 7.8 Menghitung grayscale

``` python
rgb_float = pixels.astype(np.float64)

grayscale = (
    0.299 * rgb_float[:, :, 0]
    + 0.587 * rgb_float[:, :, 1]
    + 0.114 * rgb_float[:, :, 2]
).round().astype(np.uint8)
```

Array diubah sementara menjadi `float64` agar perhitungan desimal
dilakukan dengan baik. Ketiga channel dikalikan bobot masing-masing,
dijumlahkan, dibulatkan, lalu diubah menjadi `uint8`.

### 7.9 Menghitung kebutuhan memori

``` python
pixels.nbytes
grayscale.nbytes
path.stat().st_size
```

`nbytes` menghitung ukuran array di memori. `st_size` menghitung ukuran
file yang tersimpan di penyimpanan. Kedua ukuran dapat berbeda karena
file gambar dapat dikompresi dan mengandung struktur atau metadata
tambahan.

### 7.10 Menguji rekonstruksi

``` python
reconstructed = Image.fromarray(pixels, mode="RGB")
reconstructed.save("hasil_rekonstruksi.png")

reconstructed_pixels = np.array(reconstructed)
identical = np.array_equal(pixels, reconstructed_pixels)
```

`Image.fromarray()` membentuk objek gambar dari array numerik. Setelah
disimpan dan dibaca kembali, `np.array_equal()` menguji apakah semua
elemen kedua array sama.

## 8. Penjelasan Metadata

Output metadata memberikan informasi tambahan di luar nilai piksel:

  -----------------------------------------------------------------------
  Metadata                Hasil                   Penjelasan
  ----------------------- ----------------------- -----------------------
  Format                  MPO                     Format *Multi-Picture
                                                  Object*, yang dapat
                                                  menyimpan beberapa
                                                  gambar/frame dalam satu
                                                  file.

  Dimensi                 7952 × 5304             Lebar dan tinggi frame
                                                  yang dibuka untuk
                                                  analisis.

  Mode                    RGB                     Piksel dikonversi
                                                  menjadi tiga channel
                                                  warna untuk analisis.

  Jumlah frame            2                       Pillow mendeteksi dua
                                                  frame dalam file MPO.

  DPI                     350 × 350               Informasi resolusi yang
                                                  tersimpan pada file;
                                                  bukan jumlah piksel
                                                  gambar.

  Make                    SONY                    Merek perangkat yang
                                                  tercatat dalam EXIF.

  Model                   ILCE-7RM3A              Model kamera yang
                                                  tercatat dalam EXIF.

  Software                ILCE-7RM3A v1.00        Informasi software yang
                                                  tersimpan pada
                                                  metadata.

  DateTime                2026:10:01 08:40:09     Nilai tanggal/waktu
                                                  yang tersimpan pada tag
                                                  EXIF.

  Orientation             1                       Tag orientasi
                                                  menunjukkan orientasi
                                                  normal.

  Profil ICC              Tidak ditemukan         Program tidak menemukan
                                                  profil ICC pada
                                                  informasi gambar yang
                                                  diperiksa.
  -----------------------------------------------------------------------

Metadata merupakan informasi yang menyertai file, sedangkan data piksel
adalah nilai numerik yang digunakan untuk merepresentasikan tampilan
citra. Metadata dapat tidak tersedia, dihapus, atau berubah saat gambar
diproses.

## 9. Batasan Analisis

1.  Program mengonversi gambar ke RGB. Jika file awal memiliki mode
    warna atau transparansi lain, representasi array yang dianalisis
    adalah hasil konversi, bukan selalu representasi asli file.
2.  File yang digunakan terdeteksi sebagai MPO dengan dua frame.
    Analisis utama belum membandingkan atau memproses setiap frame
    secara terpisah.
3.  Matriks yang ditampilkan hanya sebagian kecil dari keseluruhan array
    karena jumlah data sangat besar.
4.  Ukuran array di memori tidak sama dengan ukuran file karena file
    dapat dikompresi dan memiliki metadata.
5.  Metadata kamera dan tanggal merupakan nilai yang tercatat dalam
    file; program tidak memverifikasi secara independen apakah nilai
    tersebut benar secara historis.
6.  Tidak ditemukannya profil ICC tidak berarti gambar tidak memiliki
    warna; program tetap dapat membaca dan menganalisis nilai RGB.

## 10. Kesimpulan

Hasil project menunjukkan bahwa citra digital dapat direpresentasikan
sebagai array numerik. Gambar yang dianalisis memiliki dimensi 7952 ×
5304 piksel, menghasilkan 42.177.408 piksel dan 126.532.224 nilai RGB.
Setiap channel menyimpan nilai intensitas numerik dalam rentang 0--255.

Program juga menunjukkan bahwa nilai-nilai tersebut dapat dipisahkan
menjadi matriks channel, dihitung statistiknya, dikonversi menjadi
grayscale, dan direkonstruksi menjadi citra dengan array RGB yang
identik. Informasi metadata memberikan konteks tambahan mengenai format,
dimensi, kamera, waktu, dan karakteristik file.

Dengan demikian, project ini membuktikan bahwa citra digital raster
bukan sekadar tampilan visual, melainkan data numerik terstruktur yang
dapat dibaca, dihitung, diolah, dan dibentuk kembali melalui
pemrograman.

------------------------------------------------------------------------

## Lampiran: File yang Dihasilkan

-   `image_analysis.py` --- kode Python untuk analisis citra dan
    metadata.
-   `gambar.jpg` --- file gambar yang dianalisis.
-   `hasil_rekonstruksi.png` --- hasil rekonstruksi dari array RGB.
-   `hasil_grayscale.png` --- hasil konversi grayscale.

**Catatan:** angka dan informasi pada laporan ini mengikuti output
terminal yang diberikan untuk file `gambar.jpg`.
