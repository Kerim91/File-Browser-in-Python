# File-Browser-in-Python
Python Script Özeti:
Bu script, verilen bir dizindeki tüm dosya ve alt dizinleri tarar, yalnızca metin dosyalarını işler ve içeriklerini (ilk 100 karakter) yazdırır. Binary dosyalar atlanır. Hata oluştuğunda hata loglanır ve işlem devam eder.

Adımlar:
Dizini Tara: Script, verilen dizinin tüm alt dizinleri ve dosyalarını tarar.
Metin Dosyalarını İşle: Sadece metin dosyalarını okur, içeriklerinin ilk 100 karakterini yazdırır.
Binary Dosyaları Atlama: Binary dosyalar (örneğin .git dosyaları) tespit edilir ve atlanır.
Hata Yönetimi: Dosya okuma hataları loglanır ve işlem devam eder.


Kurulum:
Python 3 yüklü olmalıdır.
Repo'yu klonlayın:
git clone (https://github.com/Kerim91/File-Browser-in-Python.git)
cd dosya-tarayici


Kullanım:
Script’i çalıştırmak için:
bash
Kodu kopyala
python3 script.py /path/to/directory

