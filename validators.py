MAX_TITLE_LENGTH = 120


def validate_task_title(title):
    if not isinstance(title, str):
        return "Judul tugas wajib berupa teks"
    cleaned = title.strip()
    if not cleaned:
        return "Judul tugas tidak boleh kosong"
    if len(cleaned) > MAX_TITLE_LENGTH:
        return f"Judul tugas maksimal {MAX_TITLE_LENGTH} karakter"
    return None
