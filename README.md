<<<<<<< HEAD
# SecureTask API — DevSecOps P5

SecureTask API adalah aplikasi REST sederhana berbasis Flask untuk membuat, melihat, dan menghapus daftar tugas. Data disimpan di memori proses untuk kebutuhan praktikum; aplikasi ini bukan layanan produksi.

## Teknologi
- Python 3.12
- Flask untuk endpoint HTTP
- pytest untuk unit test
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk otomasi CI

## Struktur source code
- `app.py`: endpoint API.
- `tasks.py`: model Task.
- `validators.py`: validasi judul.
- `storage.py`: penyimpanan in-memory.
- `config.py`: konfigurasi aplikasi.
- `test_app.py`: unit test API.

## Menjalankan aplikasi secara lokal
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
API tersedia pada `http://127.0.0.1:5000`.

Contoh membuat tugas:
```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Belajar DevSecOps"}'
```

## Menjalankan test dan SAST
```bash
pytest -q
bandit -r . -x ./test_app.py,./.venv -ll -ii
```
Quality Gate menggunakan exit status Bandit: pipeline gagal jika Bandit menemukan isu dengan severity **medium/high** dan confidence **medium/high** sesuai filter `-ll -ii`. Tinjau hasil temuan dan perbaiki atau dokumentasikan sebelum mengubah kebijakan. Quality Gate ini adalah kebijakan praktikum berbasis ambang Bandit, bukan SonarQube Quality Gate.

## Overview pipeline CI/CD
Workflow `.github/workflows/devsecops.yml` berjalan pada `push` ke `main` dan `pull_request` yang menargetkan `main`. Job `build` berjalan di `ubuntu-latest`, memasang dependencies, dan menjalankan pytest. Job `sast-scan` juga berjalan di `ubuntu-latest`, bergantung pada `build` melalui `needs: build`, kemudian menjalankan Bandit. Jika build gagal, SAST tidak dijalankan.

## Batasan
- Data tugas hanya tersimpan dalam memori dan dihapus saat aplikasi berhenti.
- Gunakan `APP_SECRET_KEY` yang aman jika konfigurasi rahasia benar-benar digunakan; nilai bawaan hanya untuk pengembangan.
- Sebelum digunakan di produksi, tambahkan autentikasi, penyimpanan persisten, logging, rate limiting, dan konfigurasi deployment yang aman.
=======
# DevSecOps_0110223024_Rano-Alamsyah
Implementasi pipeline DevSecOps menggunakan GitHub Actions, SAST, dan Quality Gate.
>>>>>>> 149b7c16c479c1a3a074e833f903bc35a6cf4995
