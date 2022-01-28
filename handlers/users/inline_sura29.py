from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile

from keyboards.default.yonalishlar import yonalishlar_button
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp, bot


@dp.callback_query_handler(text='sura29')
async def suralar(message:CallbackQuery):

     await message.message.answer(text="Ankabut Surasi🌹")
     dokument_manzil = InputFile(path_or_bytesio='for_send/Ankabut.docx')

     user_id = message.from_user.id
     await bot.send_document(chat_id=user_id, document=dokument_manzil)
    # await message.message.answer(text="Oltmish to‘qqiz oyatdan iborat bo‘lgan bu sura ham Makkada nozil qilingandir. Sura iymon egalari sidqidildan mo‘min bo‘lganmilar yoki til uchida iymon keltirganmilar, sinash uchun turli imtihonlarga ro‘baro‘ qilinishlari aniq ekanligi haqida xabar berish bilan boshlanib, yaralganlarning fitnalariga aldanib iymon-e’tiqodidan kechgan kimsalar albatta Yaratganning azobiga giriftor bo‘lishlarini uqtiradi. Shuningdek, bu surada dinu iymonga da’vat qilguvchi kishilar zimmasida juda sharafli va ayni paytda o‘ta mushkul vazifa borligi aytilib, bir necha payg‘ambarlar faoliyati misolida Haq yo‘lidagi da’vatning mo‘‘jizasi tasvirlab beriladi. Yana bu surada Alloh taolo O’zining mo‘‘jizasi bo‘lmish Qur’oni Karimni bandalariga yetkazish uchun o‘qishni ham, yozishni ham bilmaydigan Muhammad alayhis-salomni payg‘ambarlikka tanlagani to‘g‘risida xabar berib, aks holda buzg‘unchi kimsalar: «Qur’onni Muhammadning o‘zi yozgan», deb odamlarni shubhaga solishlari aniq ekanligini uqtiradi. Sura sabr-toqat bilan Haq yo‘lida kurashgan zotlarga Allohning o‘zi yor bo‘lishi haqida oyat bilan tugallanadi. Bu suradan o‘zlari qo‘llari bilan yasab olgan butlariga sig‘inib, ulardan najot kutadigan mushriklar xuddi o‘zi to‘qigan to‘ridan panoh istaydigan o‘rgimchakka o‘xshashligi to‘g‘risidagi oyat ham o‘rin olgani uchun «Ankabut — O’rgimchak» surasi deb nomlangandir. Mehribon va rahmli Alloh nomi bilan (boshlayman). 1. Alif, Lom, Mim. 2. Odamlar: «Iymon keltirdik», deyishlari bilangina, imtihon qilinmagan hollarida, qo‘yib qo‘yilishlarini o‘yladilarmi?! 3. Holbuki Biz ulardan avvalgi (iymon keltirgan barcha) kishilarni imtihon qilgan edik-ku!! Bas (shu imtihon vositasida) albatta Alloh («Iymon keltirdik» deb) rost so‘zlagan kishilarni ham, yolg‘onchi kimsalarni ham aniq bilur. 4. Yoki yomon amallar qiladigan kimsalar Bizdan (jazoyimizdan) qochib qutulishni o‘yladilarmi?! Naqadar yomon hukm chiqaradilar-a?! 5. Kim Allohga ro‘baro‘ bo‘lishdan umidvor bo‘lsa, bas, albatta, Alloh (belgilagan mukofot va jazo) fursati shak-shubhasiz kelguvchidir. U eshitguvchi, bilguvchidir. 6. Kim jihod qilsa, faqat o‘z (foydasi) uchun jihod qilur (ya’ni kim Alloh yo‘lida sa’y harakat qilsa, bundan Alloh emas, balki o‘sha kishining o‘zi uchun manfaat bo‘lur). Zero Alloh barcha odamlardan behojatdir. 7. Iymon keltirgan va yaxshi amallar qilgan zotlarning yomonliklarini (ya’ni avval qilgan gunohlarini) shak-shubhasiz o‘chirurmiz va albatta ularni qilib o‘tgan eng chiroyli amallari bilan mukofotlarmiz. 8. Biz insonni ota-onasiga yaxshilik qilishga buyurdik (ya’ni ota-ona hoh yaxshi, hoh yomon bo‘lsin, xoh musulmon, xoh kofir bo‘lsin, ularga yaxshilik qilish farzandning burchidir, ammo) agar ular sen o‘zing bilmagan narsalarni (ya’ni soxta «xudo»larni) Menga sherik qilishing uchun zo‘rlasalar, u holda ularga itoat etmagin! (Barchangiz) Menga qaytursiz, bas (ana o‘sha kunda) Men sizlarga qilib o‘tgan amallaringizning xabarini berurman. 9. Iymon keltirgan va yaxshi amallar qilgan zotlarni shak-shubhasiz solih bandalar qatoriga (ya’ni jannatga) doxil qilurmiz (kiriturmiz). 10. Odamlar orasida shunday kimsalar ham borki, o‘zlari: «Allohga iymon keltirdik», deydi-da, so‘ng Alloh yo‘lida (kofirlar tomonidan biron aziyat bilan) ozorlansa, odamlarning (bu) fitna-ozorlarini Allohning azobi kabi qilib olur (ya’ni o‘tkinchi hokimlarning fitna-fasodlaridan Allohning azobidan qo‘rqqandek qo‘rqib o‘z iymon-e’tiqodidan kechur). Qasamki, agar Parvardigoringiz tomonidan (siz - mo‘minlarga) g‘alaba kelsa shak-shubhasiz ular: «Albatta bizlar sizlar bilan birga edik», derlar. Axir Alloh barcha odamlarning dillaridagi narsalarni juda yaxshi bilguvchi emasmi?! 11. Albatta Alloh iymon keltirgan zotlarni ham, munofiq kimsalarni ham aniq bilur. 12. Kofir bo‘lgan kimsalar iymon keltirgan zotlarga: «Sizlar bizlarning yo‘limizga ergashinglar, gunohlaringizni bizlar ko‘tarurmiz», dedilar. Holbuki ular (mo‘minlarning) gunohlaridan biron narsani ko‘tara olguvchi emasdirlar. Albatta ular yolg‘onchidirlar, I z o h. Ushbu oyat Quraysh kattalari iymon keltirgan kishilarga: «Qayta tirilish, qiyomatdagi hisob-kitob degan narsalar yo‘q narsalardir. Kishi dunyoga bir marta keladi, bundan boshqa dunyo yo‘qdir. Sizlar bizning yo‘limizga yuraveringlar, agar u dunyo haqidagi gaplar rost chiqib, qiyomat qoyim bo‘lsa barcha gunohlaringizni biz bo‘ynimizga olurmiz va sizlar azobga duchor bo‘lmassizlar», deyishganida nozil qilingan bo‘lib, ular mo‘minlarning biron gunohini bo‘yinlariga olishga qodir emasliklari haqida ogohlantiradi. Quyidagi oyatda odamlarni Haq yo‘lidan ozdirgan bunday kimsalar o‘zlarining gunohlariga qo‘shib tobe’larining gunohlariga ham javobgar bo‘lishlari haqida xabar beriladi. Sahihul-Buxoriyda rivoyat qilingan bir hadisi sharif xam bu oyati karimaga hammazmundir: «Kim odamlarni zalolatga da’vat qilsa, uning zimmasida o‘ziga ergashgan kimsalarning gunohlari ham bo‘lur, ammo ularning o‘z ustlaridagi gunohlari ham zarracha kamaymas». 13. Albatta ular o‘zlarining yuk-gunohlarini ham, u yuklari bilan birga (boshqa) yuklarni ham ko‘tarurlar va albatta qiyomat kunida o‘zlari to‘qib olgan (yolg‘onlari) to‘g‘risida so‘ralurlar. 14. Aniqki, Biz Nuhni o‘z qavmiga (payg‘ambar qilib) yubordik. Bas, u ularning orasida ellik yili kam ming yil turdi (ammo ular iymon keltirmadilar), bas ularni zolim-kofir bo‘lgan hollarida to‘fon (balosi) tutdi. 15. So‘ng Biz (Nuh)ga va kema(dagi) hamrohlariga najot berdik va (u to‘fon balosini) barcha olamlarga oyat-ibrat qilib qo‘ydik. 16. Ibrohimni (eslang) - u o‘z qavmiga degan edi: «Allohga ibodat qilinglar va Undan qo‘rqinglar! Agar bilguvchi bo‘lsangizlar mana shu sizlar uchun yaxshiroqdir. 17. Sizlar Allohni qo‘yib faqat butlarga ibodat qilmoqdasizlar va (ularni «xudolar» deb) yolg‘on to‘qimoqdasizlar. Aniqki sizlar Allohni qo‘yib ibodat qilayotgan narsalar sizlarga rizqu-ro‘z berishga qodir emaslar. Bas (shunday ekan) sizlar rizqni (yolg‘iz) Alloh dargohidan istanglar va Ungagina ibodat qilinglar, Ungagina shukr qilinglar, (zotan) sizlar Ungagina qaytarilursizlar. 18. Agar sizlar (meni) yolg‘onchi qilsangizlar, bas, sizlardan avvalgi ummatlar ham (o‘z payg‘ambarlarini) yolg‘onchi qilgandirlar. Payg‘ambar zimmasida esa faqat (Alloh farmonini bandalarga) ochiq-ravshan yetkazishgina bordir». 19. Axir ular dastavval Alloh qanday qilib (yo‘qdan) yaratishini ko‘rmadilarmi?! So‘ngra (qiyomat kunida esa) U o‘sha (avval yo‘qdan bor qilgan narsasi)ni qaytarur. Albatta bu Allohga osondir. 20. (Ey Muhammad), ayting: «Yerda aylanib (Alloh) dastavval qanday qilib yaratganini (va so‘ng O’zi yo‘qdan bor qilgan narsalarni yo‘q qilganini) ko‘ringlar. So‘ngra Alloh (ularni) ikkinchi (marta) paydo qilur. Albatta Alloh barcha narsaga qodirdir. 21. U O’zi xohlagan kimsalarni azoblar va O’zi xohlagan kishilarga rahm qilur. (Yolg‘iz) Ungagina qaytarilursizlar. 22. Sizlar (Allohning jazosidan) na yerga va na osmonga qochib qutulguvchi emasdirsizlar. Va sizlar uchun Allohdan o‘zga biron yordamchi yo‘qdir. 23. Allohning oyatlarini va Unga ro‘baro‘ bo‘lishni inkor qilgan kimsalar ular Mening marhamatimdan noumid (mahrum) bo‘lgan kimsalardir va ular uchun alamli azob bordir. 24. Bas (Ibrohimning da’vatiga) qavmining javobi faqat: «Uni o‘ldiringlar yoki yoqib yuboringlar», deyishlari bo‘ldi. So‘ng Alloh unga olovdan najot berdi. Albatta bunda iymon keltiradigan qavm uchun oyat-ibratlar bordir. 25. Ibrohim aytdi: «Sizlar faqat hayoti dunyodagi o‘zaro oshna og‘aynigarchiligingizni ko‘zlab, Allohni qo‘yib, butlarni ushladinglar. Hali qiyomat kunida ayrimlaringiz (ya’ni peshvolaringiz) ayrimlaringizdan (ergashuvchilardan) tonur, ayrimlaringiz ayrimlaringizni la’natlar. Sizlarning borar joyingiz do‘zaxdir. (U joyda) sizlar uchun yordamchilar yo‘qdir». 26. Bas Lut unga iymon keltirdi. I z o h . Lut o‘zi Ibrohimning og‘asining o‘g‘li bo‘lib, Ibrohim kofirlar tomonidan olovga tashlanganida yonmaganini ko‘rgach, uning haq payg‘ambar ekanini bilib, birinchi bo‘lib iymon keltiradi... (Ibrohim) aytdi: «Albatta men Parvardigorim (buyurgan tomon)ga hijrat qilguvchidirman. Albatta Uning O’zigina qudrat va hikmat egasidir». 27. Biz (Ibrohimga o‘g‘li) Ishoq va (nabirasi) Ya’qubni hadya etdik hamda payg‘ambarlikni ham (barcha samoviy kitoblar)ni ham uning zurriyotiga (xos) qildik va unga shu dunyoda ham ajri-mukofotini berdik, albatta u oxiratda ham solih zotlardandir. 28-29. Lut o‘z qavmiga: «Albatta sizlar shunday buzuqlik qilmoqdasizlarki, sizlardan ilgari butun olamlardan biron kimsa bunday qilmagan edi. Haqiqatan sizlar (xotinlaringizni qo‘yib) erkaklarga borurmisizlar; yo‘lto‘sar-qaroqchilik qilurmisizlar: majlislaringizda yomon ishlar qilurmisizlar?» deganini eslang. Bas (Lut) qavmining javobi faqat «Agar sen rostgo‘y kishilardan bo‘lsang, bizlarga Allohning azobini keltir-chi», deyishlari bo‘ldi. 30. (Shunda) u aytdi: «Parvardigorim, bu buzg‘unchi qavm ustiga O’zing meni g‘olib qil». 31. Qachonki Bizning elchilarimiz (ya’ni farishtalar) Ibrohimga (farzand ko‘rishi haqidagi) xushxabarni keltirishgach, aytdilar: «Albatta bizlar mana shu qishloq ahlini halok qilguvchidirmiz. Chunki uning ahli zolim — kofir bo‘ldilar». 32. (Ibrohim); «Axir u joyda Lut bor-ku?» — dedi. Ular aytdilar: «Bizlar U joyda kim borligini yaxshiroh bilguvchidirmiz. Albatta bizlar (Lutni) va uning axli-oilasini qutqarurmiz. Magar uning xotini (najot topmas, chunki u) qolib halok bo‘lguvchilardan edi. 33. Qachonki elchilarimiz Lutning oldiga kelganlarida, u bundan yomon holga tushdi va ularning kelishlaridan yuragi siqildi. Ular dedilar: «Qo‘rqma va g‘amgin bo‘lma. Albatta bizlar senga va ahli oilangga najot berguvchilardirmiz. Magar xotining (najot topmas chunki u) qolib halok bo‘lguvchilardan edi». 34. Shak-shubhasiz Biz fosiq-itoatsiz bo‘lganlari uchun bu qishloq axli ustiga osmondan azob-tosh yog‘diruvchidirmiz. 35. Aniqki Biz aql yurgizadigan qavm uchun (ibrat bo‘lsin, deb) u (qishloq)dan oyat-nishona qoldirgandirmiz. 36. Madyan (qavmi)ga o‘z birodarlari Shu’aybni (payg‘ambar qildik). Bas u aytdi: «Ey qavmim, Allohga ibodat qilingiz va oxirat kunidan umidvor bo‘lingiz hamda Yer (yuzi)da buzg‘unchilik qilib sanqib yurmangiz!» 37. Ular (Shu’aybni) yolg‘onchi qilishgach, ularni dahshatli zilzila tutib, turgan joylarida (tutdek) to‘kildilar. 38. Od va Samud (qabilalarini ham xalok qildik). (Bu) sizlarga ularning maskanlaridan (ya’ni u maskanlardan qolgan xarobalardan) ko‘rinib turibdi. Shayton ularga (qilayotgan) amallarini chiroyli ko‘rsatib, ularni (haq) yo‘ldan to‘sdi. Holbuki ular aqlu-hushli kishilar edi. 39. Qorun, Fir’avn va Homonni ham (xalok qildik). Darhaqiqat Muso ularga (payg‘ambar ekanligini dalolat qiladigan) aniq hujjatlar keltirganida ular yer (yuzi)da kibr-havo qildilar va (Bizning azobimizdan) qochib qutulguvchi bo‘lmadilar. 40. Biz (ulardan) har birini o‘z gunohi bilan ushladik. Bas ularning orasida Biz ustiga tosh yog‘dirgan kimsalar ham bordir, ular orasida qichqiriq tutib (halok bo‘lgan) kimsalar ham bordir, ular orasida Biz yerga yutdirgan kimsalar ham bordir va ular orasida Biz (suvga) g‘arq qilgan kimsalar ham bordir. Alloh ularga zulm qilguvchi bo‘lmadi, lekin ular o‘z jonlariga jabr qilguvchi bo‘ldilar. 41. Allohdan o‘zga «do‘stlar»ni ushlagan kimsalarning misoli xuddi (o‘zi uchun) uy qurib olib, (o‘sha uyidan panoh istagan) o‘rgimchakka o‘xshaydi. Albatta uylarning eng nimjoni o‘rgimchak uyasidir. Agar ular bilsalar edi, (o‘rgimchak uyasi kabi ojiz butlardan panoh istamagan bo‘lur edilar). 42. Shak-shubhasiz, Alloh ular O’zini qo‘yib, iltijo qilishayotgan butlarini bilur. U qudrat va hikmat egasidir. 43. Ushbu masallarni Biz odamlar (ibrat olsinlar) uchun ayturmiz. (Lekin) ularni faqat ilm egalarigina anglay olurlar. 44. Alloh osmonlar va yerni haq (qonun) bilan yaratgandir. Albatta bunda iymon keltirgan kishilar uchun oyat-ibrat bordir. 45. (Ey Muhammad), siz o‘zingizga vahiy qilingan Kitob – Qur’ondan bo‘lgan (oyatlar)ni tilovat qiling va namozni to‘kis ado qiling! Albatta namoz buzuqlik va yomonlikdan to‘sur. Aniqki Allohni zikr qilmoq (barcha narsadan) ulug‘roqdir. Alloh qilayotan ishlaringizni bilib turur. 46. (Ey mo‘minlar), sizlar axli kitob bilan faqat eng chiroyli yo‘sinda mujodala munozara qilinglar, magar ularning orasidagi zulmu-zo‘ravonlik qilgan kimsalar bilangina (keskin muomala qilishingiz mumkindir). Va aytinglar: «Bizlar o‘zimizga nozil qilingan (Qur’on)ga ham sizlarga nozil qilingan (Tavrot va Injil)ga ham iymon keltirganmiz. Bizlarning ilohimiz ham, sizlarning ilohingiz ham Bir (iloh)dir va bizlar Ungagina bo‘yinsunguvchimiz». 47. (Ey Muhammad, Biz sizdan avvalgi payg‘ambarlarga kitoblar nozil qilganmiz). Shuningdek, sizga ham Kitob-Qur’on nozil kildik. Bas Biz Kitob (ya’ni Tavrot va Injil) ato etgan zotlar unga (ya’ni Qur’onga) iymon keltirurlar. Ana u (Makka ahli orasida ham) unga iymon keltiradigan kishilar bordir. Bizning oyatlarimizni faqat kofirlargina inkor qilur. 48. Siz (o‘zingizga Qur’on nozil qilinishidan) ilgari biron kitobni tilovat qilguvchi bo‘lgan emas edingiz va o‘z qo‘lingiz bilan xat ham yozgan emas edingiz. Aks holda buzg‘unchi kimsalar albatta shubhaga tushgan bo‘lur edilar. 49. Yo‘q u (ya’ni Qur’on) ilm ato etilgan zotlarning ko‘ngillaridagi aniq-ravshan oyatlardir. Bizning oyatlarimizni faqat zolimlargina inkor qilur. 50. Ular (kofirlar): «Unga (ya’ni Muhammadga) ham Parvardigori tomonidan oyat-mo‘‘jizalar tushganida edi», dedilar. Ayting: «Oyat-mo‘‘jizalar yolg‘iz Allohning huzuridadir. Men esa faqat (osiylarni Allohning azobidan) ochiq ogoxlantirguvchiman xolos». 51. Axir ularga tilovat qilinayotgan shu Kitobni Biz sizga nozil qilganimiz ular uchun yetarli emasmi?! Albatta bu (Kitob)da iymon keltiradigan qavm uchun rahmat va eslatma bordir. 52. Ayting: «Alloh men bilan sizlarning o‘rtangizda yetarli guvohdir. U zot osmonlar va yerdagi bor narsani bilur. Botil narsaga (ya’ni butlarga) iymon keltirib, Allohga kofir bo‘lgan kimsalar - ana o‘shalar ziyon ko‘rguvchilarning o‘zidirlar». 53. Ular sizdan azobni tezlatishni talab qilurlar. Agar belgilangan muddat (ya’ni qiyomat kuni) bo‘lmasa edi, albatta ularga (darhol) azob kelgan bo‘lur edi. Shak-shubhasiz (azob) ularga o‘zlari sezmagan hollarida to‘satdan kelur. 54. Ular sizdan azobni tezlatishni talab qilurlar. Albatta jahannam kofirlarni o‘rab olguvchidir. 55. U kunda azob ularning ustilaridan ham, oyoqlarining ostidan ham o‘rab olur va (Alloh) aytur: «Qilib o‘tgan amallaringizning jazosini totinglar!» 56. Ey iymon keltirgan bandalarim, shak-shubha yo‘qki, Mening yerim keng, kattadir. Bas sizlar Mengagina ibodat qilingiz! 360 I z o h . Ushbu oyati karima Makkadagi mushriklarning zulmu-fitnalari sababli toat ibodatlarini bemalol qila olmay qolgan musulmonlar haqida nozil qilingandir. Tangri taolo oyat orqali ularga O’zining zamini keng ekanligi, binobarin agar bu yerda ularning iymon-e’tiqodlariga daxl qilinsa, o‘zga yerlarga hijrat qilib, o‘sha joylarda yolg‘iz O’ziga ibodat qilishlari lozimligini uqtiradi. Xuddi shu xususdagi payg‘ambar alayhis-salomning bir hadisi muboraklari ham barcha mo‘min-musulmonlar uchun ibratli eslatmadir: 'Kim o‘z dini(ni saqlab qolish) uchun bir yerdan boshqa yerga ketar ekan, albatta u jannatga haqdor bo‘libdir'. 57. Har bir jon o‘lim (sharbati)ni totguvchidir. So‘ngra O’zimizga qaytarilursizlar. 58. Iymon keltirgan va yaxshi amallar qilgan zotlarni albatta jannatda ostidan daryolar oqib turadigan joylarga joylashtirurmiz. Ular o‘sha joylarda mangu qolurlar. (Yaxshi) amallarni qilguvchi zotlarning ajri-mukofoti naqadar yaxshidir! 59. Ular (kofirlar tomonidan bo‘ladigan zulmu kulfatlarga) sabr-toqat qilgan va yolg‘iz Parvardigorlarigagina tavakkul qiladigan — suyanadigan zotlardir. 60. O’z rizqu ro‘zini ko‘tara (ya’ni topa) olmaydigan qanchadan-qancha jonzotlar bordir. Alloh ularga ham, sizlarga ham rizqu ro‘z berur. U eshitguvchi, bilguvchidir. 61. Qasamki, agar siz ulardan: «Osmonlar va yerni yaratgan, quyosh va oyni (O’z izmiga) qaratgan zot kim?» — deb so‘rasangiz, albatta ular: «Alloh», deb (javob qilurlar). Bas (shundoq ekan, o‘sha Allohga ibodat qilishning o‘rniga) qayoqqa burilib ketmoqdalar-a?! 62. Alloh bandalaridan O’zi xohlagan kishilarning rizqini keng qilur va (O’zi xoxlagan kishilarning rizqini) tang qilur. Albatta Alloh barcha narsani bilguvchidir. 63. Qasamki, agar siz ulardan: «Osmondan suv yomg‘ir yog‘dirib yerni «o‘lganidan» so‘ng «tiriltirgan» zot kim?» — deb so‘rasangiz, albatta ular: «Alloh», deb (javob qilurlar). Siz (ularga): «E’tirof etganlaringiz uchun Allohga hamdu sano bo‘lsin», deb ayting. Yo‘q, ularning ko‘plari aql yurgizmaydilar. 64. Bu hayoti dunyo faqat (bir nafaslik) o‘yin-kulgidir. Agar ular bilsalar oxirat diyorigina (mangu) hayot (diyoridir). 65. Qachon ular kemaga minsalar (g‘arq bo‘lishdan ko‘rqib) Allohga chin ixlos bilan duo-iltijo qilurlar. Endi qachonki (Alloh) ularga najot berib quruqlikka (chiqargach), banogoh ular (Allohga) shirk keltirurlar! 66. Biz ularga ato etgan ne’matlarga kofir bo‘laversinlar va (shu bir nafaslik hayotlarida) «foydalanib» qolsinlar. Hali yaqinda (bu qilmishlarining oqibatini) bilib qolajaklar! 67. Ular o‘zlarining atroflaridan odamlar talon-torojga duchor bo‘layotgani holda Biz Haramni (ya’ni Makkani) tinch-osoyishta qilib qo‘yganimizni ko‘rmadilarmi?! Nahotki ular botil-butlarga iymon keltirib, Allohning ne’mati (Islomga)ga kofir bo‘lsalar?! 68. Alloh sha’niga yolg‘on to‘qigan yoki Haq – Qur’on kelgan chog‘ida uni yolg‘on degan kimsadan ham zolimroq kim bor?! Jahannamda kofir kimsalar uchun joy topilmasmi?! 69. Bizning (yo‘limiz)da jihod qilgan — kurashgan zotlarni albatta O’z yo‘llarimizga hidoyat qilurmiz. Aniqki, Alloh chiroyli amal qilguvchi zotlar bilan birgadir.")