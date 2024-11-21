import os

def is_text_file(file_path):
    """
    Bir dosyanın metin dosyası olup olmadığını kontrol eder.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read(512)  # İlk 512 baytı oku
        return True
    except:
        return False

def process_file(file_path):
    """
    Dosya üzerinde işlem yapar (örneğin içeriği yazdırır).
    """
    print(f"İşleniyor: {file_path}")
    if not is_text_file(file_path):
        print(f"Binary veya okunamayan dosya atlandı: {file_path}")
        return
    
    # Örnek işlem: Dosya içeriğini okuma
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read(100))  # İlk 100 karakteri yazdır
    except Exception as e:
        print(f"Hata: {e}")

def traverse_directory(directory):
    """
    Belirtilen dizindeki tüm dosyaları gezer ve işler.
    """
    if not os.path.isdir(directory):
        print("Geçersiz dizin!")
        return

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Kullanım: python3 script.py <dizin>")
    else:
        directory = sys.argv[1]
        traverse_directory(directory)
