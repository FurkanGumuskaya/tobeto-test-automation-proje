TOBETO TEST

Test Senaryosu 1

Adı : Giriş Paneli Kontrolü

Açıklama : Kullanıcılar e-posta ve şifrelerini girerek sisteme giriş yapabilmelidir.

Ön Koşul : Test ortamı çalışır ve hazır durumda olmalıdır. Tobeto giriş sayfasına girilmiş olmalıdır. 

Input: https://tobeto.com/giris

Case 1 : Başarılı Giriş Kontrolü

Adım 1: Sitenin giriş sayfasına gir.

Input: https://tobeto.com/giris


Adım 2: E-posta bölümüne kayıtlı bir mail adresi gir.

Input: aaa@gmail.com


Adım 3: Şifre bölümüne kayıtlı bir şifre gir.

Input: 123456


Adım 4: Giriş yap butonuna tıkla.

Beklenen Sonuç : Kullanıcı başarılı bir şekilde anasayfaya geçiş yapabilmelidir ve ekranda “Giriş başarılı.” mesajı çıkmalıdır.


![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/9d6c0d73-feae-453a-b60f-39b237fa10b5)


Case 3 :  E-posta veya Şifre Hatalı Girildiğinde

Adım 1: E-posta veya şifre bölümündeki bilgileri hatalı gir.

Input:

e-posta: abc@gmail.com(geçersiz) şifre:123456

e-posta: aaa@gmail.com şifre: 12378(geçersiz)

e-posta: abc@gmail.com (geçersiz) şifre: 12378(geçersiz)


Adım 2: Giriş yap butonuna tıkla.

Beklenen Sonuç: Kullanıcı bilgilerini hatalı girdiyse bir sonraki sayfaya geçiş sağlanmamalıdır. Pop-up şeklinde "Geçersiz e-posta veya şifre" uyarısı verilmelidir. 

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/6cd4a694-101b-40a6-b14c-39230fb9a28d)


Test Senaryosu 2

Adı : Kayıt Ol Paneli Kontrolü

Açıklama : Kullanıcılar henüz sisteme üye değilse e-posta ve şifrelerini girerek sisteme kayıt yapabilmelidir.

Ön Koşul : Test ortamı çalışır ve hazır durumda olmalıdır. Tobeto kayıt sayfasına girilmiş olmalıdır.

Input: https://tobeto.com/kayit-ol

Case 1 : Başarılı Kayıt Ol Kontrolü

Adım 1: Sitenin kayıt sayfasına gir.

Input: https://tobeto.com/kayit-ol

Adım 2: “Ad” bölümüne adını gir.

Input: Doğukan 

Adım 3: “Soyad” bölümüne soyadını gir.

Input: Arslan

Adım 4: “E-posta” bölümüne geçerli bir mail adresi gir.

Input: aaa@gmail.com

Adım 5: “Şifre” bölümüne en az 6 karakterli bir şifre gir.

Input: 123456

Adım 6: “Şifre Tekrar” bölümüne ilk girilen şifreyi gir.

Input: 123456

Adım 7: “Kayıt ol” butonuna tıkla.

Beklenen Sonuç : Kayıt ol butonuna tıkladıktan sonra kayıt oluşturmak için sözleşmeler başlıklı bir pop-up açılmalıdır.
![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/e5c17ee1-c65c-41bf-b216-283a3a63f2d4)

Adım 8 :Açılan pop-up’da aydınlatma metnine tıkla.

Adım 9 : Açılan pop-up’da “Açık Rıza Metni’ni okudum ve anladım .” linkine tıkla. Checkbox’ını işaretle.

Adım 10: Açılan pop-up’da “Üyelik Sözleşmesi ve Kullanım Koşulları’nı okudum ve anladım.” Checkbox’ını işaretle.

Adım 11: Açılan pop-up’da “E-posta gönderim izni.”  Checkbox’ını işaretle.

Adım 12: Açılan pop-up’da “Arama izni.”  Checkbox’ını işaretle.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/3f815f2a-74e4-4ea9-8aee-d13a47ed2362)

Adım 13: Arama iznine tıklandıktan sonra açılan telefon numarası alanını doldur. 

Input: 05062202020

Adım 14: Açılan pop-up’da “Ben robot değilim” Checkbox’ını işaretle.

Adım 15: “Devam Et” butonuna tıkla.

Beklenen Sonuç : Kayıt başarıyla gerçekleşti bildirimi alınmalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/8a34cd6b-a46c-4393-8751-4c7d9b33e40a)

Case 2: Kayıt Ol Sırasında İstenen Telefon Numarası Karakter Kontrolü

Adım 1: Sitenin kayıt sayfasına gir.

Input: https://tobeto.com/kayit-ol

Adım 2: “Ad” bölümüne adını gir.

Input: Doğukan

Adım 3: “Soyad” bölümüne soyadını gir.

Input: Arslan

Adım 4: “E-posta” bölümüne geçerli bir e-mail adresi gir.

Input: aaa@gmail.com

Adım 5: “Şifre” bölümüne en az 6 karakterli bir şifre gir.

Input: 123456

Adım 6: “Şifre Tekrar” bölümüne ilk girilen şifreyi gir.

Input: 123456

Adım 7: “Kayıt ol” butonuna tıkla.

Adım 8: Açılan pop-up’da aydınlatma metnine tıkla.

Adım 9: Açılan pop-up’da “Açık Rıza Metni’ni okudum ve anladım.” linkine tıkla ve Checkbox’ını işaretle.

Adım 10: Açılan pop-up’da “Üyelik Sözleşmesi ve Kullanım Koşulları’nı okudum ve anladım.” Checkbox’ını işaretle.

Adım 11: Açılan pop-up’da “E-posta gönderim izni.”  Checkbox’ını işaretle.

Adım 12: Açılan pop-up’da “Arama izni.”  Checkbox’ını işaretle.

Adım 13: Açılan textarea da bir Ülke adı seçimi yap.

Input:Türkiye

Adım 14: Açılan textarea kısmına 10 karakterden az bir numara gir.

Input: +90 1234

Adım 15: Açılan pop-up’da “Ben robot değilim” Checkbox’ını işaretle.

Adım 16: “Devam Et” butonuna tıkla.

Beklenen Sonuç: “En az 10 karakter girmelisiniz.” uyarısı gelmelidir.

Adım 17: Açılan textarea kısmına 10 karakterden fazla bir numara gir.

Input: +90 4357653794753

Beklenen Sonuç: “En fazla 10 karakter girmelisiniz.” uyarısı gelmelidir.

Adım 18: Açılan textarea kısmına yazılan telefon numarasını sil.

Beklenen Sonuç: “Doldurulması zorunlu alan” uyarısı gelmelidir.

Adım 19: Açılan textarea kısmına rakamdan farklı bir karakter gir.

Beklenen Sonuç: Rakamdan farklı bir karaktere izin verilmemelidir.

Case 3 : Geçersiz E-posta Kontrolü

Adım 1: E-posta kutusuna geçersiz bir E-posta adresi yaz.

Input: E-posta = e

Beklenen Sonuç :“Geçersiz e-posta adresi*” uyarısı görülmelidir.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/e9764f2b-d56f-456b-9f2c-0413832f7321)

Adım 2: Adım 1’de girilen geçerli veya geçersiz E-postayı sil.

Beklenen Sonuç: "Doldurulması zorunlu alan*" uyarısı görünmelidir.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/6aaae5b9-8c48-4d83-8e56-995eb3b3b447)

Case 4 : Girdiğiniz E Posta Adresi İle Kayıtlı Üyelik Bulunmaktadır Uyarısının Alınması

Adım 1: Sitenin kayıt sayfasına gir.

Input: https://tobeto.com/kayit-ol

Adım 2: “Ad” bölümüne adını gir.

Input: Doğukan

Adım 3: “Soyad” bölümüne soyadını gir.

Input: Arslan

Adım 4: “E-posta” bölümüne kayıtlı bir mail adresi gir.

Input: kayıtlı@gmail.com

Adım 5: “Şifre” bölümüne en az 6 karakterli bir şifre gir.

Input: 12345

Adım 6: “Şifre Tekrar” bölümüne ilk girilen şifreyi gir.

Input: 123456

Adım 7: “Kayıt ol” butonuna tıkla.

Adım 8: Açılan pop-up’da “Açık Rıza Metni’ni okudum ve anladım.” Checkbox’ını işaretle.

Adım 9: Açılan pop-up’da “Üyelik Sözleşmesi ve Kullanım Koşulları’nı okudum ve anladım.” Checkbox’ını işaretle.

Adım 10: Açılan pop-up’da “E-posta gönderim izni.”  Checkbox’ını işaretle.

Adım 11: Açılan pop-up’da “Arama izni.”  Checkbox’ını işaretle.

Adım 12: Arama iznine tıklandıktan sonra açılan telefon numarası alanını doldur.

Adım 13: Açılan pop-up’da “Ben robot değilim” Checkbox’ını işaretle.

Adım 14: “Devam Et” butonuna tıkla.

Beklenen Sonuç : “Girdiğiniz e posta adresi ile kayıtlı üyelik bulunmaktadır.” uyarısı alınmalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/6fc019d9-65bf-4bff-805b-36e7d4943b9a)

Case 5: Şifrenin Karakter Sayı Kontrolü

Adım 1: Sitenin kayıt sayfasına gir.

Input: https://tobeto.com/kayit-ol

Adım 2: “Ad” bölümüne adını gir.

Input: Doğukan

Adım 3: “Soyad” bölümüne soyadını gir.

Input: Arslan

Adım 4: “E-posta” bölümüne geçerli bir mail adresi gir.

Input: aaa@gmail.com

Adım 5: “Şifre” bölümüne 6 karakterden az bir şifre gir.

Input: 12345

Adım 6: “Şifre Tekrar” bölümüne ilk girilen şifreyi gir.

Input: 12345

Adım 7: “Kayıt ol” butonuna tıkla.

Adım 8: Açılan pop-up’da “Açık Rıza Metni’ni okudum ve anladım.” Checkbox’ını işaretle.

Adım 9: Açılan pop-up’da “Üyelik Sözleşmesi ve Kullanım Koşulları’nı okudum ve anladım.” Checkbox’ını işaretle.

Adım 10: Açılan pop-up’da “E-posta gönderim izni.”  Checkbox’ını işaretle.

Adım 11: Açılan pop-up’da “Arama izni.”  Checkbox’ını işaretle.

Adım 12: Arama iznine tıklandıktan sonra açılan telefon numarası alanını doldur.

Adım 13: Açılan pop-up’da “Ben robot değilim” Checkbox’ını işaretle.

Adım 14: “Devam Et” butonuna tıkla.

Beklenen Sonuç :   "Şifreniz en az 6 karakterden oluşmalıdır." uyarısı almalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/cf6d080f-e693-4bb0-909c-f2cf4f2cca9c)


Case 6: Şifre Tekrarı Kontrolü

Adım 1: Sitenin kayıt sayfasına gir.

Input: https://tobeto.com/kayit-ol

Adım 2: “Ad” bölümüne adını gir.

Input: Doğukan

Adım 3: “Soyad” bölümüne soyadını gir.

Input: Arslan

Adım 4: “E-posta” bölümüne geçerli bir mail adresi gir.

Input: aaa@gmail.com

Adım 5: “Şifre” bölümüne en az 6 karakterli bir şifre gir.

Input: 123456

Adım 6: “Şifre Tekrar” bölümüne ilk girilen şifreden farklı bir şifre gir.

Input: asdasd

Adım 7: “Kayıt ol” butonuna tıkla.

Adım 8: Açılan pop-up’da “Açık Rıza Metni’ni okudum ve anladım.” Checkbox’ını işaretle.

Adım 9: Açılan pop-up’da “Üyelik Sözleşmesi ve Kullanım Koşulları’nı okudum ve anladım.” Checkbox’ını işaretle.

Adım 10: Açılan pop-up’da “E-posta gönderim izni.”  Checkbox’ını işaretle.

Adım 11: Açılan pop-up’da “Arama izni.”  Checkbox’ını işaretle.

Adım 12: Arama iznine tıklandıktan sonra açılan telefon numarası alanını doldur.

Adım 13: Açılan pop-up’da “Ben robot değilim” Checkbox’ını işaretle.

Adım 14: “Devam Et” butonuna tıkla.

Beklenen Sonuç : "Şifreler eşleşmedi" uyarısı almalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/ca5fd691-7fb1-4605-838a-f87d818ff950)


Case 7: Girilen Bilgilerde 2 Farklı Hatalı Kısım Olduğunda

Adım 1: Sitenin kayıt sayfasına gir.

Input: https://tobeto.com/kayit-ol

Adım 2: “Ad” bölümüne adını gir.

Input: Doğukan

Adım 3: “Soyad” bölümüne soyadını gir.

Input: Arslan

Adım 4: “E-posta” bölümüne geçersiz bir mail adresi gir.

Input: geçersiz@gmail.com

Adım 5: “Şifre” bölümüne geçersiz bir şifre gir.

Input: asdas

Adım 6: “Şifre Tekrar” bölümüne ilk girilen şifreyi gir.

Input: asdas

Adım 7: “Kayıt ol” butonuna tıkla.

Adım 8: Açılan pop-up’da “Açık Rıza Metni’ni okudum ve anladım.” Checkbox’ını işaretle.

Adım 9: Açılan pop-up’da “Üyelik Sözleşmesi ve Kullanım Koşulları’nı okudum ve anladım.” Checkbox’ını işaretle.

Adım 10: Açılan pop-up’da “E-posta gönderim izni.”  Checkbox’ını işaretle.

Adım 11: Açılan pop-up’da “Arama izni.”  Checkbox’ını işaretle.

Adım 12: Arama iznine tıklandıktan sonra açılan telefon numarası alanını doldur.

Adım 13: Açılan pop-up’da “Ben robot değilim” Checkbox’ını işaretle.

Adım 14: “Devam Et” butonuna tıkla.

Beklenen Sonuç : "2 errors occurred" uyarısı almalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/451e2789-973f-4e8c-81c7-b7aa438665ba)


Test Senaryosu 3

Adı: Şifremi Unuttum Paneli Kontrolü

Açıklama: Şifresini unutan kullanıcı bu sayfayı kullanarak şifresini yenileyebilmelidir.

Ön Koşul: Test ortamı çalışır ve hazır durumda olmalıdır. Tobeto sifremi-unuttum sayfasına girilmiş olmalıdır.

Input: https://tobeto.com/sifremi-unuttum

Case 1: Şifre Sıfırlama E-Postası Gönderme

Adım1: Tobeto şifremi unuttum sayfasına gir.

Adım2: E-posta kısmına kayıtlı bir e-posta adresi gir.

Input: aaa@gmail.com

Adım3: Gönder butonuna tıkla.

Beklenen Sonuç : Gönder butonuna tıkladıktan sonra “Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin.” pop-up bildirim olarak çıkmalıdır. Bu işlemden sonra sistem kullanıcıyı giriş sayfasına yönlendirmelidir.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/257c5737-e568-4415-bdc8-d6e0efef9e48)

Adım 4: Şifre sıfırlama isteği gönderilen mail adresinin gelen kutusunu kontrol et.

Adım 5: Tobeto tarafından gönderilen mail içeriğinde ki linke tıkla.

Adım 6: Yönlendirilen şifre sıfırlama sayfasında yeni şifreni gir.

Input: 123456

Adım 7: Yeni şifrenin tekrarını gir.

Input: 123456

Adım 8: Gönder butonuna tıkla.

Beklenen Sonuç : Şifre sıfırlama işlemi başarılı bildirimi alınmalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/17d45100-17dc-4a25-8ff6-5ad8c3e0d165)

Case 2: Şifre Sıfırlama Durumunda Hatalı E-Posta Girilmesi

Adım1: Tobeto şifremi unuttum sayfasına gir.

Adım2: E-posta kısmına geçersiz bir e-posta adresi gir.

Input: geçersiz@gmail

Adım3: Gönder butonuna tıkla.

Beklenen Sonuç : Kullanıcı gönder tuşuna bastığında girilen e-posta adresi geçersiz bir e-posta adresi ise pop up şeklinde ekteki mesajla karşılaşmalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/106e2442-c2d8-49a0-b95a-966a6096ac8b)4


Test Senaryosu 4

Adı: Chatbot simgesinin kontrolü

Açıklama: Kullanıcının chatbot sohbet penceresini açtığı ve sorularını sorabildiği bir alan olmalıdır.

Ön Koşul: Test ortamı çalışır ve hazır durumda olmalıdır. Her sayfada Chatbot simgesi olmalı ve inputlara göre test edilebilmelidir.

Case 1: Chatbot Simgesi ve Simgenin Açık veya Kapalı Kontrolü

Adım1: Tobeto anasayfaya gir.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/625101b4-7c31-466d-8f91-4876b9bd45c6)


Input: https://tobeto.com/giris

Adım2: "Sorularınız için buradayım" yazısı yanında bulunan ikonu tıkla.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/78b86301-bd37-4c16-b420-70a3a5f52ff0)

Beklenen Sonuç : Sayfanın sağ alt kısmında chatbot mesaj bölümü açılmalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/92102671-1b62-452e-9a30-9bb4d34d693e)

Adım3: Açılan mesaj penceresinde sağ üst kısımda simge durumuna getir ikonuna tıkla.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/7ae9b731-162c-47ae-96d2-df736baa42f3)

Beklenen Sonuç: Chatbot tekrar simge durumuna gelmelidir.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/fa6ee61a-f5ab-4beb-b262-e821bbb5c951)

Case 2: Chatbot Mesaj Bölümü Kontrolü

Adım1: Tobeto anasayfaya gir.

Input: https://tobeto.com/giris

Adım2: "Sorularınız için buradayım" yazısı yanında bulunan ikonu tıkla.

Adım3: Açılan pencerede ad soyad gir.

Input: Ad Soyad :Mehmet Aslantaş

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/ffde5cee-2784-46be-b303-7cd5e14c8f3e)

Beklenen Sonuç: Girilen bilgiler sonucunda chatbot kullanıcıya “Sana hangi konuda yardımcı olmamı istersin?” şeklinde soru veya “Tobeto Hakkında mı? İstanbul Kodluyor Hakkında mı?” şeklinde iki şık sunmalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/d4e7c46c-b4f9-46af-b6ea-cd27526ccfa0)

Adım 4: Tobeto Hakkında ya da İstanbul Kodluyor Hakkında seçeneklerinden birini seç.

Beklenen Sonuç: Seçim yaptığın “Hakkında” bölümleri hakkında ayrıntılı açıklama gelmelidir.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/67504637-e960-4361-9d38-24e095a20873)


Case 3: Chatbot Mesaj Bölümünü Sonlandırma

Adım1: Tobeto anasayfaya gir.

Input: https://tobeto.com/giris

Adım2: "Sorularınız için buradayım" yazısı yanında bulunan ikonu tıkla.

Adım3: Açılan sohbet penceresinde görüşmeyi sonlandır ikonuna tıkla.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/5b2e0cbe-2103-4878-bad5-4e348741c71f)

Adım4: "Görüşmeyi bitirmek istediğinize emin misiniz" uyarısında “Evet” e tıkla.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/5b2e0cbe-2103-4878-bad5-4e348741c71f)

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/063c74ba-e00f-45a4-97c1-2977bc537cf2)

Adım5: Chatbot penceresi içerisinde açılan puanlama pop-up ı üzerinden chatbot ‘ı puanla.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/37ff6904-862d-4be6-aaed-87f786c31499)

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/063c74ba-e00f-45a4-97c1-2977bc537cf2)

Adım6: Gönder butonuna tıkla.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/7eeff978-5e83-4218-a0b9-a9425994bbc1)

Beklenen Sonuç:  Chatbot penceresi kapanmalı ve ilk simge görünümüne dönmelidir.

Case 4: Emoji Kontrolü

Adım1: Tobeto anasayfaya gir.

Input: https://tobeto.com/giris

Adım2: "Sorularınız için buradayım" yazısı yanında bulunan chatbot simgesine tıkla.

Adım3: Metin kutsunun hemen yanında bulunan emoji simgesine tıkla.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/d162bf83-ae1e-41bf-a6e4-74fb78507384)

Beklenen Sonuç: Tüm emojiler görüntülenmelidir.

Adım4: Metin kutusunun hemen yanında bulunan dosya ekleme ikonuna tıkla.

Beklenen Sonuç: Dosyayı sürükle ve bırak yazısı altında dosya seçiniz yazan bir pop-up açılmalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/a4150654-4162-4cd3-8bd0-f4459df7ff47)

Adım5: Emoji ara butonun yanında bulunan el butonuna tıkla.

Beklenen Sonuç: Açılan el emojilerinin alta doğru açıktan koyuya doğru ten rengi seçimi yapılabilmelidir.

Adım6: Dosya seçiniz butonuna tıkla.

Beklenen Sonuç: Bilgisayardan dosya seçeceğimiz dosya penceresi açılmalıdır.

![image](https://github.com/nserpilkaraman/tobeto_test_proje/assets/149595452/a4150654-4162-4cd3-8bd0-f4459df7ff47)
