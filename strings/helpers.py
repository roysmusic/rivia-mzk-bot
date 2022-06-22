HELP_1  =  """✅**<u>Yönetici Komutları:</u>**
/pause - Çalan müziği duraklatın.
/resume - Duraklatılan müziği devam ettirir.
/mute - Çalan müziğin sesini kapatır.
/unmute - Sesi kapatılan müziğin sesini açar.
/skip - Çalmakta olan müziği atla.
/stop - Çalan müziği durdurur.
/shuffle - Sıraya alınmış çalma listesini rastgele karıştırır.
✅<u>**Belirli Atlama:**</u>
/atla [Sayı(örnek: 3)]
    - Müziği belirtilen sıraya alınmış numaraya atlar. Örnek: /skip 3, müziği sıraya alınan üçüncü müziğe atlayacak ve sıradaki 1 ve 2 müziği yok sayacaktır.
✅<u>**Döngü Oyna:**</u>
/loop [etkin/devre dışı] veya [1-10 arası sayılar]
    - Etkinleştirildiğinde, bot sesli sohbette çalmakta olan müziği 1-10 kez döngüye alır. Varsayılan olarak 10 kez.
✅<u>**Yetkili Kullanıcılar:**</u>
Yetkilendirme Kullanıcıları, sohbetinizde yönetici hakları olmadan yönetici komutlarını kullanabilir.
/auth [Kullanıcı adı] - Grubun YETKİ LİSTESİ'ne bir kullanıcı ekleyin.
/unauth [Kullanıcı adı] - Bir kullanıcıyı grubun YETKİ LİSTESİ'nden kaldırın.
/authusers - Grubun YETKİ LİSTESİ'ni kontrol edin.
NOT: BOT TÜRKÇE KOMUT SİSTEMİ İLE ÇALIŞABİLİR """

HELP_2  =  """✅<u>**Çal Komutları:**</u>
/play veya /vplay [Müzik Adı veya Youtube/Spotify/Apple/Resso/SoundCloud Bağlantısı]
    - Bot, verilen sorguyu sesli sohbette çalmaya başlayacaktır.
/stream [m3u8 veya dizin bağlantıları]
    - Sesli sohbetlerde canlı bağlantılar yayınlayın.
/channelplay [Kanal Kullanıcı Adı veya Kimliği] veya [bağlı]
    - Kanalı bir gruba bağlayın ve grubunuzdan kanalın sesli sohbetinde müzik akışı yapın. Bağlamak için kanalın **Sahibi** olmanız gerekir. Alternatif olarak, grubunuzu o kanala bağlayabilir ve ardından `/channelplay bağlantılı` ile bağlanmayı deneyebilirsiniz"
Kanalı bağladıktan sonra, oynatma modunu / oynatma modu aracılığıyla gruptan kanala değiştirin
✅<u>**Desteklenen Platform:**</u>
Bot yalnızca YouTube, AppleMusic, Spotify, Resso, Soundcloud, M3u8 ve Index Links'i destekler
✅**<u>Bot'un Sunucu Oynatma Listeleri:</u>**
/playlist - Sunucularda Kaydedilmiş Oynatma Listenizi Kontrol Edin.
/deleteplaylist - Çalma listenizde kayıtlı tüm müzikleri silin
/play - Kayıtlı Oynatma Listenizi Sunuculardan oynatmaya başlayın.
✅<u>**Oyun Ayarları:**</u>
/playmode - Grubunuzun oynatma ayarlarını ayarlayabileceğiniz düğmeler içeren eksiksiz bir oynatma ayarları paneli edinin.
🔗 **Oynatma modundaki seçenekler:** [Buradaki düğmeyi tıklayarak daha fazla bilgi alın]
1️⃣ **Arama Modu** [ Doğrudan veya Satır İçi] : - /oynatma modu verirken arama modunuzu değiştirir.
2️⃣ **Oynat Modu** [Grup veya Kanal] :- Oynatma modunuzu kanal veya grup olarak değiştirir ve yalnızca orada müzik akışı sağlar.
3️⃣ **Oyun Türü** [ Herkes veya Yöneticiler] : - Yöneticilerse, yalnızca grupta bulunan yöneticiler sesli sohbette müzik çalabilir.
NOT: BOT TÜRKÇE KOMUT SİSTEMİ İLE ÇALIŞABİLİR"""


HELP_3  =  """✅<u>**Bot Komutları:**</u>
/stats - En İyi 10 Parçayı Al Global İstatistikler, Botun En İyi 10 Kullanıcısı, Botta En İyi 10 Sohbet, Sohbette Oynanan En İyi 10 vb.
/sudolist - Yukki Music Bot'un Sudo Kullanıcılarını kontrol edin
/lyrics [Müzik Adı] - Web'de belirli bir Müzik için Şarkı Sözleri arar.
/song [Parça Adı] veya [YT Bağlantısı] - youtube'dan herhangi bir parçayı mp3 veya mp4 formatında indirin.
/queue- Müzik Sıra Listesini Kontrol Edin.
NOT: BOT TÜRKÇE KOMUT SİSTEMİ İLE ÇALIŞABİLİR"""


HELP_4  =  """✅<u>**Ek Komutlar:**</u>
/start - Yukki Music Bot'u başlatın.
/help - Komutların ayrıntılı açıklamalarını içeren Komutlar Yardımcısı Menüsü alın.
/ping- Bot'a ping atın ve Yukki'nin Ram, Cpu vb. istatistiklerini kontrol edin.
✅<u>**Grup Ayarları:**</u>
/settings - Satır içi düğmelerle tam bir grubun ayarlarını alın
🔗 **Ayarlardaki Seçenekler:**
1️⃣ Sesli sohbette yayın yapmak istediğiniz **Ses Kalitesini** ayarlayabilirsiniz.
2️⃣ Sesli sohbette yayın yapmak istediğiniz **Video Kalitesini** ayarlayabilirsiniz.
3️⃣ **Yetkili Kullanıcılar**:- Yönetici komutları modunu buradan herkese veya yalnızca yöneticilere değiştirebilirsiniz. Grubunuzda bulunan herkes yönetici komutlarını kullanabilecekse (/atla,/durdur vb.)
4️⃣ **Oynatma Modu Ayarları** : Oynatma komutları bölümünden yardım alın.
5️⃣ **Temiz Mod:** Etkinleştirildiğinde, sohbetinizin temiz ve iyi kalmasını sağlamak için 5 dakika sonra botun mesajlarını grubunuzdan siler.
6️⃣ **Komut Temizleme** : Etkinleştirildiğinde, Bot yürütülen komutları (/play, /pause, /shuffle, /stop vb.) hemen siler.
NOT: BOT TÜRKÇE KOMUT SİSTEMİ İLE ÇALIŞABİLİR"""
