from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile

from keyboards.default.yonalishlar import yonalishlar_button
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp, bot


@dp.callback_query_handler(text='sura36')
async def suralar(message:CallbackQuery):

     await message.message.answer(text="Yosin Surasi🌹")
     dokument_manzil = InputFile(path_or_bytesio='for_send/Yosin.docx')

     user_id = message.from_user.id
     await bot.send_document(chat_id=user_id, document=dokument_manzil)
    # await message.message.answer(text="Sakson uch oyatdan tashkil topgan bu sura ham Makkada nozil bo‘lgandir. U Qur’oni Karimga qasam-la Muhammad alayhis-salomning haq payg‘ambar ekanliklarini tasdiqlash bilan boshlanib, so‘ngra u Zotni yolg‘onchi qilgan Quraysh kofirlari va ularning topajak oqibatlari haqida xabar beradi. Bu surada Alloh taoloning Antokiya shahriga yuborgan elchilari va shahar ahli ularni yolg‘onchi qilganlari sababli halokatga duchor bo‘lganlari to‘g‘risida hamda o‘sha yerdagi iymon keltirganligi sharofatidan Allohning marhamatiga sazovor bo‘lgan Habib an-Najjor ismli bir solih banda haqida hikoya qilinadi. Yana bu surada o‘quvchi e’tibori kecha bilan kunduzning almashib turishidagi; oy va quyoshdek buyuk sayyoralarning biron soniya tinim bilmasdan o‘z fazolarida o‘ta nozik intizom bilan aylanib turishlaridagi Yaratganning qudratiga dalolat qiladigan jihatlarga qaratiladi. Bu surada iymon va taqvo ahli uchun hozirlab qo‘yilgan jannat manzaralari nihoyatda jonli lavhalarda chizib beriladi va kofirlarning tillar soqov bo‘lib, qo‘llar tilga kiradigan, oyoqlar guvohlik beradigan qiyomat kunidagi ahvollari butun dahshati bilan bayon qilinadi. Sura o‘zining ilk oyati «Yosin» nomi bilan atalgan bo‘lib, uning Qur’oni Karimda tutgan o‘rni — martabasi haqida payg‘ambar alayhis-salomdan mana shunday hadisi sharif rivoyat qilingandir. U zot: «Albatta har bir narsaning qalbi bordir. Qur’onning qalbi «Yosin»dir. Men bu surani ummatimdan har kishining qalbida bo‘lishini istar edim» degan ekanlar. Mehribon va rahmli Alloh nomi bilan (boshlayman). 1. Yo, Sin. 2-3-4. (Ey Muhammad, ushbu) hikmatli Qur’onga qasamki, hech shak shubhasiz siz To‘g‘ri yo‘l (ya’ni haq din) ustidagi payg‘ambarlardandirsiz. 5-6. (Bu Qur’on) ota-bobolari (biron payg‘ambar orqali oxirat azobidan) ogohlantirilmasdan, g‘ofil bo‘lib qolgan bir qavmni ogohlantirishingiz uchun qudratli va mehribon zot tomonidan nozil qilingandir. 7. Aniqki ularning ko‘plariga So‘z (ya’ni azob haqidagi hukm) haq bo‘lgandir. Bas ular iymon keltirmaslar. 8. Darhaqiqat Biz ularning bo‘yinlariga to iyaklarigacha (etadigan) kishanlarni urib qo‘ydik, bas ular g‘o‘dayib qoldilar (ya’ni ular Haqqa egilmaslar). 9. Va Biz ularning oldilaridan bir to‘siq – parda qilib, ularni o‘rab qo‘ydik. Bas ular ko‘ra olmaslar. 10. (Ey Muhammad), siz ularni ogohlantirdingizmi yoki ogohlantirmadingizmi ularga barobardir — iymon keltirmaslar. 11. Siz faqat ergashgan va g‘oyibda (ya’ni, ko‘rmay) turib, Rahmondan qo‘rqqan kishilarnigina ogohlantira olursiz. Bas o‘sha (kishilarga) mag‘firat va ulug‘ ajr (jannat) xushxabarini bering! 12. Albatta Biz O’zimizgina o‘liklarni tiriltirurmiz va ularning qilgan amallarini hamda (qoldirgan) izlarini yozib qo‘yurmiz. Barcha narsani Biz ochiq Kitobda (ya’ni Lavh-ul-Mahfuzda) belgilab qo‘ygandirmiz. 13. (Ey Muhammad), siz ularga (Antokiya) qishlog‘ining ahlini — u joyga elchilar kelgan paytini misol keltiring! I z o h . Ushbu va quyidagi oyatlarda so‘z Haq yo‘liga da’vat qilish uchun Iyso alayhis salom tomonidan Rum mamlakatidagi Antokiya shahri aholisiga yuborilgan elchilar va ularni yolg‘onchi qilganlari oqibatida halokatga duchor bo‘lgan Antokiya axli haqida boradi. Bu qissa orqali Qur’on Makka mushriklarini Muhammad payg‘ambar alayhis salomga iymon keltirmaslikning mudhish oqibatlaridan ogohlantiradi. 14. O’shanda Biz ularga ikki (elchini) yuborganimizda, u ikkisini yolg‘onchi qilishgach, uchinchi (elchi) bilan quvvatlantirdik. Bas (uchchala elchi Antokiya ahliga): “Darhaqiqat biz sizlarga (yuborilgan) elchilarmiz”, degan edilar. 15 Ular: «Sizlar ham xuddi o‘zimizga o‘xshagan odamlarsiz. Raxmon (ya’ni Alloh) biron narsa – vahiy nozil qilgani yo‘q. Sizlar faqat yolg‘on so‘zlamoqdasizlar», dedilar. 16. (Elchilar) aytdilar: “Parvardigorimiz bilurki, bizlar shak-shubhasiz sizlarga (yuborilgan) elchilardirmiz. 17. Va bizlarning zimmamizda (Allohning vahiysini sizlarga) ochiq-ravshan yetkazish bordir”. 18. Ular dedilar: «Haqiqatan bizlar sizlar haqingizda badgumondamiz. Qasamki, agar (bu so‘zlaringizni) to‘xtatmasangizlar albatta sizlarni toshbo‘ron kilurmiz va sizlarga biz tomondan bir alamli azob yetar». 19. (Elchilar) aytdilar: «Badgumoningiz o‘zlaringiz bilandir (ya’ni bizlardan emas, balki o‘zlaringizning kufrlaringizdan badgumon qilinglar). Sizlarga va’z nasihat qilinsa (qabul qilish o‘rniga badgumonda bo‘lib do‘q-po‘pisa qilurmisiz)?! Yo‘q, sizlar haddan oshgan qavmdirsiz!» 20. (Shu payt) bir kishi shaharning bir chekkasidan shoshgancha kelib, dedi: «Ey qavmim, bu elchilarga ergashinglar! 21. O’zlari hidoyatda bo‘lgan va sizlardan biron ajr-mukofot so‘ramaydigan zotlarga ergashinglar!» I z o h. Rivoyat qilinishicha, bu kishi shahar chetida istiqomat qiluvchi xudojo‘y va sahovatli — bir odam bo‘lib, ismi Habib an-Najjor edi. U hamshaharlari o‘zlarini haq yo‘liga da’vat qilish uchun kelgan elchilarni yolg‘onchi qilishib, o‘ldirishmoqchi bo‘lib turganlaridan xabar topgach, shoshgancha ularning oldiga kelib, mazkur oyatlardagi so‘zlarni aytadi. Bu so‘zlarni eshitgan qavmi: «Hali sen ham shularning dinidamisan?!» deganlarida, 22. U aytdi: «Nega men o‘zimni yaratgan Zotga ibodat qilmayin? Sizlar ham (dunyodan o‘tgach) yolg‘iz Ungagina qaytarilursizlar. 23. Men U zotni qo‘yib (jonsiz butlarni) xudo qilib olaymi?! (Hargiz unday qilmasman, chunki) agar Rahmon menga biron ziyon yetkazishni istasa, u (but)larning oqlovlari meni biron narsadan behojat qila olmas va ular meni (Allohning azobidan) qutqara olmaslar. 24. U holda men shak-shubhasiz ochiq zalolatda bo‘lurman. 25. Haqiqatan men (jonsiz butlarga emas, balki barchalaringizni yaratgan) Parvardigoringizga iymon keltirganman. Bas meni tinglangiz!» 26-27. (Lekin joxil qavm Habib an-Najjorning so‘zlariga quloq solmasdan uni qatl qilishgach, unga) «Jannatga kir», deyildi. (Allohning amri bilan jannatga kiritilib, u joydagi noz-ne’mat va izzat-ikromni ko‘rgach), u aytdi: «Qani edi qavmim ham meni Parvardigorim mag‘firat qilganini va meni izzat-ikromli kishilardan qilganini bilsalar edi». 28. Biz (Habib an-Najjorni o‘ldirganlaridan) keyin uning ustiga (ularni halok qilish uchun) osmondan biron qo‘shin (ya’ni azob farishtalarini) tushirmadik, Biz (hech narsa) tushirguvchi bo‘lmadik. 29. Faqat birgina dahshatli qichqiriq bo‘ldi-yu, banogoh ular «o‘chib» qoldilar. 30. (Allohning elchilarini yolg‘onchi qilib, ularga ozor-aziyat yetkazadigan barcha) bandalarga hasrat-nadomat bo‘lgay! Ularga biron payg‘ambar kelmas, magar ular uning ustidan masxara qilib kulguvchi bo‘lurlar. 31. Axir ular o‘zlaridan ilgari ham qancha asrlarni (avlodlarni) halok qilganimizni — o‘shalar ularning oldiga (ya’ni bu dunyoga) qaytib kelmasliklarini ko‘rmadilarmi?! 32. Hech shak-shubhasiz (ularning barchalari (qiyomat kunida) to‘planguvchi, Bizning dargohimizda hozir qilinguvchidirlar. 33. O’lik-quruq yer ular uchun (qayta tirilish haq ekaniga) bir oyat-alomatdir – Biz uni (suv bilan) tiriltirdik va undan (turli) don-dunni undirib chiqardik. Bas ular o‘sha (don) dan yerlar. 34. Yana Biz u (er)da xurmozor va uzumzor bog‘larni (paydo) qildik va unda buloqlarni oqizib qo‘ydik. 35. Toki (odamlar o‘sha bog‘larning) mevasidan yesinlar uchun (shunday qildik). Holbuki u (mevalar)ni ular (qo‘llari bilan) qilmagan — yasab olmagan edilar. Axir shukr qilmaydilarmi?! 36. Yer undirib-o‘stiradigan narsalardan, (odamlarning) o‘zlaridan va yana ular bilmaydigan narsalardan iborat barcha juftlarni yaratgan (Alloh har qanday aybu-nuqsondan) pok zotdir. I z o h . Mazkur oyatda Alloh taolo koinotdagi barcha narsani juft qilib yaratgani uqtirildi. Endi quyidagi oyatlarda ana o‘sha juftlardan kecha va kunduz hamda quyosh va oy haqida so‘z yuritilib, ulardan har biri Buyuk Ilohiy qudratga dalolat qiladigan oyat alomatlardan ekani ta’kidlanadi. 37. Kecha ham ular uchun (bizning qudratimizni ko‘rsatib turadigan) bir oyatdir: Biz undan kunduzni yechib olishimiz bilan banogoh ular zulmatda qolurlar. 38. Quyosh (biron soniya to‘xtamay) o‘z qarorgohi sari joriy bo‘lur. Bu qudratli va bilguvchi zotning taqdiri — o‘lchovidir. I z o h . Yerdan ming-ming marta katta hajmga ega bo‘lgan quyosh to «kun va oy birlashib ketadigan» qiyomat kuni kelgunicha bir nafas ham tinmasdan fazoda aylanaveradi, Faqat qudratli va dono zot — Alloh taoloning O’zigina uni shunday tartib o‘lchovga bo‘ysundirib qo‘ya olur. 39. Biz oyni ham toki u eski (xurmo) butog‘i kabi bo‘lib (egilib hilol holiga kelib) qolgunicha bir necha manzilga belgilab-tayinlab qo‘gandirmiz. I z o h . Darhaqiqat oy bir oy davomida yigirma sakkiz manzil — joyda turli suratda ko‘ringani sababli ko‘zga yigirma sakkizta bo‘lib tuyuladi. So‘ngra bir yoki ikki kecha ko‘rinmasdan turadi-da, keyin yana o‘sha tartibda takrorlanadi, Agar quyosh kunduzlari olamni nur va haroratga to‘ldirsa, oy kechalarga yorug‘lik baxsh etishi bilan birga barcha kishilar uchun vaqt o‘lchovi bo‘lib ham xizmat qiladi. 40. Na quyosh uchun oyga yetish mumkin bo‘lur va na kecha kunduzdan o‘zguvchidir. (Quyosh, oy va yulduzlarning) barchalari falakda suzib yurur. I z o h . Ya’ni to qiyomat qoyim bo‘lgunicha quyosh oyga yeta olmas va kecha kunduzning o‘rnini egallab ola bilmas. Ushbu oyati karimada yana koinotdagi barcha katta-kichik sayyoralar fazoda muallaq holda suzib yurishlari bayon qilingandir. Ilm fanga yigirmanchi asrning boshlariga kelibgina ma’lum bo‘lgan bu haqiqatlar haqida Qur’oni Karim bundan o‘n to‘rt asr ilgari xabar bergan edi. Bunda aql egalari uchun ibrat bordir. 41. Biz ularning avlod-zurriyotlarini (Nuh payg‘ambar bilan birga odamlar va turli jonivorlarga) to‘la kemada ko‘targanimiz (va to‘fon balosidan najot berganimiz) ular uchun (Bizning qudratimizni ko‘rsatadigan) yana bir oyatdir. 42. Yana Biz ular uchun xuddi O’sha (kemaga) o‘xshash (boshqa) minadigan narsalarini (ya’ni katta-kichik kemalarni) ham yaratdik. 43. Agar Biz xoxlasak ularni g‘arq qilurmiz-da, so‘ng ular uchun biron yordamchi bo‘lmas va ular (halokatdan) qutqazilmaslar. 44. Magar Biz tomondan bo‘lgan marhamat sababli va (ma’lum) bir vaqtgacha (ya’ni ajallari yetguncha hayot ne’matlaridan) bahramand bo‘lishlari uchun (ularga balo-qazolardan najot berilur). 45. Qachon (mushriklar)ga: «rahmatga erishishlaringiz uchun oldilaringizdagi (dunyo fitnalaridan) va ortingizdagi (oxirat azobidan) qo‘rqinglar», (ya’ni iymonga kelinglar) deyilsa (ular quloq solmaslar). 46. Ularga Parvardigorning oyatlaridan biron oyat kelmas, magar ular (o‘sha oyatlnrdan) yuz o‘girguvchi bo‘lurlar. 47. Qachon ularga: «Alloh sizlarga rizq qilib bergan narsalardan infoq-ehson qilinglar», deyilsa, kofir bo‘lgan kimsalar iymon keltirgan zotlarga (istehzo bilan): «Agar Alloh xohlasa O’zi taomlantirib oladigan kishilarga bizlar taom berurmizmi? Sizlar hech shak-shubhasiz ochiq zalolatdadirsizlar», derlar. 48. Ular: «Agar rostgo‘y bo‘lsangizlar (aytinglar-chi), mana shu va’da (qilingan azob) qachon bo‘ladi?» — derlar. 49. Ular faqat birgina dahshatli qichqiriqni kutmoqdalar xolos. U ularni (o‘limdan mutlaqo bexabar hollarida ko‘cha-ko‘y va bozorlarda bir-birlari bilan) janjallashib turganlarida olib ketar (ya’ni halok etar). 50. Bas ular na biron vasiyat qilishga va na uylariga qaytishga qodir bo‘lurlar. 51. (Qiyomat soati kelib farishta Isrofilning) suri chalinishi bilan banogoh ular qabrlaridan Parvardigorlari huzuriga (hisob-kitob uchun) sug‘urilib chiqurlar. 52. Ular: «Ey bizlarga o‘lim bo‘lsin! Kim bizlarni yotgan joyimizdan (qabrlarimizdan) turg‘azdi?» deganlarida, (ularga aytilur): «Mana shu Rahmon va’da qilgan va payg‘ambarlar rost so‘zlagan narsa Qiyomatdir». 53. Faqatgina bir dahshatli qichqiriq bo‘lar-u, banogoh ularning barchalari Bizning dargohimizda hozir qilinguvchidirlar. 54. Mana bu Kunda hech bir jonga biron zulm qilinmas va sizlar faqat o‘zlaringiz qilib o‘tgan amallaringiz sababli jazolanursiz. 55. Shak-shubhasiz jannat egalari bu Kunda o‘zlari istagan (orzu qilgan) ish(lari) bilan shod-xurram bo‘lguvchidirlar. 56. Ular o‘z juftlari bilan birga barcha soya-salqin joylardagi so‘rilarda yastanib o‘tirurlar. 57. Ular uchun u joyda (har turli) meva-cheva mavjuddir va ular uchun chorlagan – istagan narsalari hozirdir. 58. (Ularga) Mehribon Parvardigori tomonidan salom aytilur. I z o h . Hadisi sharifda vorid bo‘lishicha «Jannat egalari o‘zlariga va’da qilingan noz ne’matlar ichida rohat-farog‘atda ekanlar, banogoh ustlarida bir nur paydo bo‘lur. Boshlarini ko‘tarib... «Assalomu alaykum, ey ahli jannat», deb turgan Parvardigori olamni ko‘rurlar». Jannat egalari yetajak saodati abadiyya zikr qilingach, endi do‘zaxilarning topajak azob uqubatlari haqida xabar beriladi. 59. Ey jinoyatchi kimsalar, mana bu Kunda (mo‘minlardan) ajralinglar! 60-61. Men sizlarga «Ey Odam bolalari, shaytonga ibodat qilmangiz, chunki u sizlarga ochiq dushmandir. Mengagina ibodat qilinglar! Mana shu To‘g‘ri yo‘ldir», deb buyurmaganmidim?! 62. Aniqki (shayton) sizlarning ichingizdan ko‘p avlodni yo‘ldan ozdirdi. Axir aql yuritguvchi bo‘lmadingizlarmi?! 63. Sizlarga va’da qilingan jahannam mana shudir! 64. Sizlar (hayoti dunyoda) kofir bo‘lib o‘tganlaringiz sababli mana bu Kunda (jahannamga) kiringiz! 65. Bu kun Biz ularning og‘izlarini muhrlab qo‘yurmiz. Va Bizga ularning qilib o‘tgan ishlari haqida — ularning qo‘llari so‘zlar va oyoqlari guvohlik berur. 66. Agar Biz xohlasak, ularning ko‘zlarini yo‘q qilgan bo‘lur edik. Ana u holda ular yo‘llariga shoshardilar-u, (lekin) qayoqdan ko‘ra olsinlar. 67. Agar Biz xohlasak, ularni turgan joylarida (maymun, to‘ng‘iz yoki tosh kabi) boshqa narsalarga aylantirib qo‘ygan bo‘lur edik. So‘ng ular (oldinga) yurishga ham qodir emaslar, (ortlariga ham) qayta olmaslar. I z o h. Ushbu ikki oyatni shunday tushunmoq lozim: Alloh taolo hayotlarini kufru isyon bilan o‘tkazgan kimsalar haqida «Agar biz istasak ularning ko‘zlarini ko‘r qilib, yo‘llarini topa olmaydigan qilib ko‘yishimiz yoki ularni insonlikdan chiqarib butunlay boshqa narsalarga aylantirib qo‘yishimiz mumkin edi. Ammo Biz ularni To‘g‘ri yo‘lga yursinlar va tavba-tazarru’ qilsinlar deb insonliklarida qoldirgan edik. Lekin ular o‘z dinsizliklaridan qaytmadilar va oqibat-natijada jahannam egalari bo‘lib qoldilar», deydi va bu bilan hali hanuz hayoti dunyoda bo‘lgan kishilarni ogohlantiradi. 68. Biz kimga (uzun) umr bersak uning xilqatini (jismu-jonini) tuban — nochor qilib qo‘yurmiz. Axir aql yurgizmaydilarmi (ya’ni bir kishining surat va siyratida yosh-yalangligi bilan qari-qartangligi o‘rtasida naqadar katta farq borligini ko‘rib ibrat olmaydilarmi)?! 69-70. (Muhammadga) she’r o‘rgatmadik va (shoirlik) uning uchun durust emasdir. I z o h. Zotan Muhammad alayhis-salom modomiki Alloh taolo tomonidan yuborilgan payg‘ambar ekanlar, demak faqat rost so‘zlamoqlari lozim. She’riyat esa o‘z ko‘tarinkiligi, mubolag‘alari bilan (ya’ni o‘z tabiati bilan to‘la ma’nodagi) rostgo‘ylikni ko‘tara olmaydi. Bil’aks shoirlarning e’tiroflaricha ham, she’rning eng shirini eng yolg‘onidir. Binobarin, o‘z ummatlariga bir umr amal qilib o‘tishadigan din arkonlarini o‘rgatadigan va g‘ayb olami, oxirat diyori haqida xabar beradigan payg‘ambar shoir bo‘lishi durust emasdir. (Muhammad tilovat qilayotgan narsa) faqat u tirik bo‘lgan kishilarni ogohlantirishi uchun va kofirlar ustiga So‘z — azob haq bo‘lishi uchun (nozil qilingan) bir eslatma va ochiq-ravshan Qur’ondir. 71. Axir ular, Biz uchun O’z (qudrat) qo‘limiz bilan qilgan narsalarni — chorva hayvonlarini yaratib qo‘yganimizni — ko‘rmadilarmi?! Mana ular o‘sha (hayvon)larga egadirlar. 72. Biz o‘sha (hayvon)larni ularga bo‘ysundirib qo‘yganmiz. Ana ularning minadigan narsalari ham o‘sha (hayvon)lardandir, yeydigan (taom)lari ham o‘shalardandir. 73. Yana ular uchun o‘sha (hayvon)larda (turli) foydalar va ichimlik (sut qaymoq)lar bordir. Axir shukr qilmaslarmi?! 74. (Yo‘q, ular shukr qilmadilar, balki) Allohni qo‘yib yordam olish umidida (o‘zga) «xudo»larni tutdilar. 75. Ular o‘sha («xudo»lari) uchun hozirlangan qo‘shinlari bo‘lgan hollarida xam u («xudo»lar) ularga yordam berishga qodir bo‘lmaslar. 76. Bas (ey Muhammad), sizni ularning so‘zlari g‘amgin qilmasin! Zotan Biz ularning yashiradigan narsalarini ham, oshkor qiladigan narsalarini ham bilurmiz. 77. Inson Biz uni nutfadan, bir tomchi suvdan yaratganimizni, endi esa banogoh u (O’zimizga) ochiq qarshilik qilguvchi bo‘lib qolganini ko‘rmadimi?! 78. U Bizga «Chirib bitgan suyaklarni kim ham tiriltira olur?» deb, misol keltirdi-yu, (ammo) o‘zining (bir tomchi suvdan) yaralganini unutib qo‘ydi. 79. (Ey Muhammad), ayting: «U (chirigan suyak)larni dastlab (bir tomchi suv)dan paydo qilgan zotning O’zi qayta tiriltirur. U (O’zi yaratgan) barcha xalqni bilguvchidir». 80. U sizlar uchun yam-yashil daraxtdan olov paydo qilgan zotdir. Bas, sizlar o‘shandan o‘t yoqursizlar. 81. Osmonlar va yerni yaratgan zot yana ularning o‘xshashini yaratishga qodir emasmi?! Yo‘q, (albatta qodirdir), Uning O’zigina yaratguvchi va bilguvchidir. 82. Biron narsani (yaratishni) iroda qilgan vaqtida Uning ishi faqatgina «Bo‘l», demoqligidir. Bas u (narsa) bo‘lur — vujudga kelur. 83. Bas barcha narsaning egaligi O’z qo‘lida bo‘lgan (Alloh har qanday aybu nuqsondan) pok zotdir. Yolg‘iz Ungagina qaytarilursizlar.")