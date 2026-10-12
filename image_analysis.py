
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def analyze_image(image_path):
    path = Path(image_path)

    if not path.is_file():
        print(f"ERROR: File tidak ditemukan: {path}")
        return

    # 1. Membuka gambar asli
    with Image.open(path) as original:
        print("=" * 60)
        print("PROJECT IMAGE ANALYSIS")
        print("Pembuktian Citra Digital sebagai Susunan Angka")
        print("=" * 60)

        print("\n[1] INFORMASI GAMBAR")
        print(f"Nama file       : {path.name}")
        print(f"Format file     : {original.format}")
        print(f"Ukuran gambar   : {original.width} x {original.height}")
        print(f"Mode asli       : {original.mode}")

        # 2. Mengubah gambar menjadi RGB
        rgb_image = original.convert("RGB")
        pixels = np.array(rgb_image)

    height, width, channels = pixels.shape

    print("\n[2] REPRESENTASI NUMERIK")
    print(f"Tipe data       : {pixels.dtype}")
    print(f"Bentuk array    : {pixels.shape}")
    print(f"Jumlah channel  : {channels}")
    print(f"Jumlah piksel   : {width * height:,}")
    print(f"Jumlah nilai    : {pixels.size:,}")
    print(f"Nilai minimum   : {pixels.min()}")
    print(f"Nilai maksimum  : {pixels.max()}")
    print(f"Rata-rata nilai : {pixels.mean():.2f}")

    print("\n[3] PEMBUKTIAN NILAI PIXEL")
    print("Contoh 5 piksel pertama pada baris pertama:")

    for x in range(min(5, width)):
        r, g, b = pixels[0, x]
        print(f"Piksel (x={x}, y=0): R={r}, G={g}, B={b}")

    # 3. Menampilkan matriks channel RGB
    # Maksimal 5 baris x 5 kolom agar output terminal ringkas
    rows = min(5, height)
    cols = min(5, width)

    print("\n[4] MATRIKS ANGKA CHANNEL MERAH (R)")
    print(pixels[:rows, :cols, 0])

    print("\n[5] MATRIKS ANGKA CHANNEL HIJAU (G)")
    print(pixels[:rows, :cols, 1])

    print("\n[6] MATRIKS ANGKA CHANNEL BIRU (B)")
    print(pixels[:rows, :cols, 2])

    # 4. Menghitung jumlah nilai unik
    print("\n[7] ANALISIS NILAI")
    for i, channel_name in enumerate(["Merah", "Hijau", "Biru"]):
        values = pixels[:, :, i]
        print(
            f"Channel {channel_name:5s}: "
            f"{len(np.unique(values))} nilai intensitas unik"
        )

    # 5. Mengubah RGB menjadi grayscale secara matematis
    rgb_float = pixels.astype(np.float64)

    grayscale = (
        0.299 * rgb_float[:, :, 0]
        + 0.587 * rgb_float[:, :, 1]
        + 0.114 * rgb_float[:, :, 2]
    ).round().astype(np.uint8)

    print("\n[8] MATRIKS GRAYSCALE")
    print("Contoh 5 x 5 nilai intensitas:")
    print(grayscale[:rows, :cols])

    # 6. Menghitung ukuran data array
    print("\n[9] UKURAN DATA")
    print(f"Ukuran array RGB di memori : {pixels.nbytes:,} byte")
    print(f"Ukuran array grayscale     : {grayscale.nbytes:,} byte")
    print(f"Ukuran file asli           : {path.stat().st_size:,} byte")

    # 7. Rekonstruksi gambar dari data angka
    reconstructed = Image.fromarray(pixels, mode="RGB")
    reconstructed.save("hasil_rekonstruksi.png")

    grayscale_image = Image.fromarray(grayscale, mode="L")
    grayscale_image.save("hasil_grayscale.png")

    # 8. Membuktikan bahwa RGB yang direkonstruksi sama
    reconstructed_pixels = np.array(reconstructed)
    identical = np.array_equal(pixels, reconstructed_pixels)

    print("\n[10] UJI REKONSTRUKSI")
    print(f"Apakah data RGB identik? {identical}")
    print("Gambar hasil: hasil_rekonstruksi.png")
    print("Gambar grayscale: hasil_grayscale.png")

    print("\nKESIMPULAN")
    print(
        "Gambar digital dapat direpresentasikan sebagai array angka. "
        "Setiap piksel memiliki nilai intensitas warna, dan array tersebut "
        "dapat digunakan untuk membentuk kembali citra."
    )
    print("=" * 60)


def analyze_metadata(image_path):
    from PIL import Image, ExifTags
    from pathlib import Path
    import json

    path = Path(image_path)

    print("\n" + "=" * 60)
    print("ANALISIS METADATA GAMBAR")
    print("=" * 60)

    print("\n[1] INFORMASI FILE")
    print(f"Nama file       : {path.name}")
    print(f"Ekstensi        : {path.suffix}")
    print(f"Ukuran file     : {path.stat().st_size:,} byte")

    with Image.open(path) as img:
        print("\n[2] INFORMASI FORMAT DAN DIMENSI")
        print(f"Format          : {img.format}")
        print(f"Lebar           : {img.width} piksel")
        print(f"Tinggi          : {img.height} piksel")
        print(f"Mode warna      : {img.mode}")
        print(f"Jumlah piksel   : {img.width * img.height:,}")
        print(f"Format animasi  : {getattr(img, 'is_animated', False)}")
        print(f"Jumlah frame    : {getattr(img, 'n_frames', 1)}")

        print("\n[3] INFO YANG TERSIMPAN DI FILE")
        if img.info:
            for key, value in img.info.items():
                if isinstance(value, bytes):
                    print(f"{key}: data biner ({len(value)} byte)")
                else:
                    text = repr(value)
                    print(f"{key}: {text[:300]}")
        else:
            print("Tidak ada info tambahan yang terbaca.")

        print("\n[4] METADATA EXIF")
        exif = img.getexif()

        if exif:
            for tag_id, value in exif.items():
                tag_name = ExifTags.TAGS.get(
                    tag_id, f"Tag_{tag_id}"
                )

                # Hindari mencetak data biner yang sangat besar
                if isinstance(value, bytes):
                    value = f"Data biner ({len(value)} byte)"

                print(f"{tag_name}: {value}")
        else:
            print("Metadata EXIF tidak tersedia.")

        print("\n[5] PROFIL WARNA ICC")
        icc = img.info.get("icc_profile")

        if icc:
            print(f"Profil ICC tersedia: {len(icc):,} byte")
        else:
            print("Profil ICC tidak ditemukan.")

    print("\n[6] PEMISAHAN METADATA DAN DATA PIXEL")
    print("Metadata menjelaskan informasi file atau gambar.")
    print("Data pixel menyimpan nilai numerik pembentuk citra.")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Cara penggunaan:")
        print("py image_analysis.py gambar.jpg")
    else:
        analyze_image(sys.argv[1])
        analyze_metadata(sys.argv[1])
