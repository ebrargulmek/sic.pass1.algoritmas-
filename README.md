ASSEMBLER KODUNUN ÇALIŞTIRILMASI 
1- Python resmi sitesine (https://www.python.org) gidin.
2-"Downloads" sekmesine tıklayın ve işletim sisteminize uygun Python sürümünü seçin. 
3-İndirilen yükleyiciyi çalıştırın ve kurulum talimatlarını takip edin. 
Kodumuzu çalıştırabilmemiz için bir metin editörü kullanrak kaynak kod dosyasını (input.txt) hazırlanması gerekir.
Ayrıca projede bulunan python kodunu '.py'uzantılı bir dosya olarak oluşturmanız gerekir. ( örnk : pass1.py) 

[file_name = 'input.txt'
# Kaynak kod satırlarını dosyadan okur
source_lines = read_source_file(file_name) ] kodumuzdaki bu kod blogu ise kaynak kod dosyasını okuyacak ve sembol tablosu ile bazı temel assembler çıktılarını üretecektir.

PROJEYE GENEL BAKIŞ 
Bu proje, belirli bir assembly dilini makine koduna dönüştüren bir derleyicidir. Düşük seviyeli programlamanın anlaşılmasını ve uygulanmasını amaçlar. Derleyici, kaynak kodunu işler, semboller ve adresler üzerinde çözümlemeler yaparak çoklu geçişlerde işlem yapar ve sonunda yürütülebilir makine kodu üretir.

PROJE NASIL ÇALIŞIR ? 
-Derleyici, kaynak kodunu içeren (input.txt) dosyayı açar ve içeriğini satır satır okur. Bu aşamada, yorum satırları ve gereksiz boşluklar atılır, böylece sadece kod içeren satırlar işleme alınır.
-->SEMBOL TABLOSUNUN OLUŞTURULMASI
-Derleme işleminin başında, LOCCTR (konum sayacı), programın başlangıç adresi(eğer bir START direktifi girilmediyse 0 )ile başlatılır. Eğer kaynak kodda START direktifi varsa, bu direktifte belirtilen değer başlangıç adresi olarak kullanılır.
-Kaynak kod satırları sırayla ayrıştırılır. Her bir satır için, etiket (varsa), işlem kodu (opcode) ve operand (varsa) ayrıştırılır.
-Bir satırda etiket varsa, bu etiket ve mevcut LOCCTR değeri sembol tablosuna eklenir. 
-İşlem kodu, bir direktif (START, END, BYTE, WORD, RESB, RESW gibi) veya bir makine talimatı olabilir. Direktifler genellikle bellek tahsis etme, program başlangıç ve bitiş adreslerini belirleme işlevlerine sahiptir. Makine talimatları ise, derleyicinin çıktı dosyasında belirli bir makine kodu üretmesini sağlar.
- Her işlenen satırın ardından, LOCCTR güncellenir. Bu güncelleme, mevcut satırın talimat veya veri büyüklüğüne bağlıdır. Örneğin, WORD için 3 byte, RESW için belirtilen sayıda kelime kadar (kelime başına 3 byte) artırılır.
--> MAKİNE KODUNUN OLUŞTURULMASI
-Derleyici kaynak kodu tekrar işler ve sembol tablosunu kullanarak tüm etiket ve sembollerin adreslerini çözümler. Bu, talimatların ve veri referanslarının doğru adresleme bilgisiyle makine koduna dönüştürülmesini sağlar.
-->SONLANDIRMA
-'END' direktifi görüldüğünde, derleme işlemi tamamlanır. Derleyici, gerekli son işlemleri gerçekleştirir ve çıktı dosyalarını oluşturur. Bu aşamada, sembol tablosu ve üretilen makine kodu gibi çıktılar kullanıcıya sunulur.

PROJEDE KULLANILAN FONKSİYONLAR:
-read_source_file(file_name): Bir dosyadan assembly kaynak kodunu okur, yorumları ve boş satırları filtreler. Bu projede bu fonksiyon input.txt kaynak dosyasını okumak, yorumları ve boş satırları filtrelemek için kullanılmıştır.
-parse_line(line): Tek bir assembly kod satırını bileşenlerine ayrıştırır: etiket, opcode ve operand. Bu projede bu fonksiyon kaynak kod dosyasındaki satırları etiket, opcode ve operand olarak ayırmıştır.
-pass1(source_lines): Derleyicinin birinci geçişi, sembol tablosunu oluşturur ve başlangıç adreslerini hesaplar.
