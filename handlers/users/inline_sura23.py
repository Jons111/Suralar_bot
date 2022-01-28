from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile

from keyboards.default.yonalishlar import yonalishlar_button
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp, bot


@dp.callback_query_handler(text='sura23')
async def suralar(message:CallbackQuery):

     await message.message.answer(text="Mu'minun Surasi🌹")
     dokument_manzil = InputFile(path_or_bytesio="for_send/Mu'minun.docx")

     user_id = message.from_user.id
     await bot.send_document(chat_id=user_id, document=dokument_manzil)
    # await message.message.answer(text="Bir yuz o‘n sakkiz oyatdan iborat bu sura Makkada nozil qilingandir. Sura Alloh Taoloning borligi va birligiga hamda Muhammad alayhis-salom U zotning so‘nggi payg‘ambari ekanligiga iymon keltirgan mo‘minlar Firdavs bog‘lariga merosxo‘r bo‘lish uchun qaysi amallarni qilib, qaysi amallardan tiyilishlari lozim ekanligini bayon qilish bilan boshlanadi. Shu boisdan u «Mo‘minlar» deb atalgandir. Bu surada ham o‘tmishdagi ayrim payg‘ambarlar va ularga mushriklar tomonidan yetgan ozorlar zikr qilinishi bilan payg‘ambar alayhis-salomga Makka kofirlarining yetkazayotgan aziyatlarida tasalli beriladi, Suraning mehvari (o‘qi) asosan bu dunyodagi hayot uchun qayta tirilish haq ekani atrofida aylanadi. Yana bu surada hayotlarini kufr bilan o‘tkazgan kimsalarning «sakarotul-mavt — o‘lim mastligi» chog‘ida tortadigan azoblari, ajallari yetib — orzu-xayollari puchga chiqqan paytida chekadigan afsus nadomatlari ham bayon qilinadi. Sura odamlar ikki toifaga: baxtli va badbaxtlarga bo‘linadigan, har qanday nasl-nasab, qarindosh-urug‘chilikdan toniladigan, faqat iymon va qilingan yaxshi amalgina foyda beradigan Qiyomat kuni haqida xabar berish bilan nihoya topadi. Mehribon va rahmli Alloh nomi bilan (boshlayman). 1. Darhaqiqat mo‘minlar najot topdilar. 2. Ular namozlarida (qo‘rquv va umid bilan) bo‘yin eguvchi kishilardir. 3. Ular behuda – foydasiz (so‘z va amallardan) yuz o‘girguvchi kishilardir. 4. Ular zakotni (ado) qilguvchi kishilardir. 5. Ular avratlarini (haromdan-zinodan) saqlaguvchi kishilardir. 6. Magar o‘z juftu-halollaridan va qo‘llaridagi cho‘rilaridangina (saqlanmaydilar). Bas ular malomat qilinmaslar. 7. Endi kim shundan o‘zgani (zino va shu kabi shariati Islomiyyada harom qilingan narsalarni) istasa, bas ana o‘shalar haddan oshguvchilardir. 8. Ular (ya’ni mo‘minlar) o‘zlariga ishonilgan omonatlarga va (o‘zgalarga) bergan ahdu paymonlariga rioya qilguvchi kishilardir. 9. Ular (barcha) namozlarini (vaqtida ado etib qazo bo‘lishdan) saqlaguvchi kishilardir. 10—11. Ana o‘shalar Firdavs (jannatiga) merosxo‘r bo‘lguvchi vorislardir. Ular o‘sha joyda mangu qolurlar. I z o h . Yuqoridagi oyatlardan ma’lum bo‘lishicha, mo‘minlar najot topib, baxt-saodatga erishishlari uchun, Firdavs jannatiga merosxo‘r bo‘lishlari uchun mazkur fazilatlarga ega bo‘lishlari lozim ekan. 12. (Qasamki), Biz insonni (ya’ni Odam alayhis-salomni) loyning mag‘zidan yaratdik. I z o h . «Loyning mag‘zi»dan murod — loy-er jinsidagi barcha moddalardir. Darvoqe’, zamonaviy tibbiyot ham inson vujudida yer jinsining barcha moddalari mavjud ekanini isbotlaydi. 13. So‘ngra uni (ya’ni barcha insonlarni) avvalo mustahkam qarorgohdagi (ya’ni bachadondagi) nutfa-maniy qildik. 14. So‘ngra bu nutfadan laxta qonni yaratib, laxta qondan parcha go‘shtni yaratib, parcha go‘shtdan suyaklarni yaratib, bu suyaklarga go‘sht qopladik, so‘ngra (unga jon kirgizib, avval boshdagi bir tomchi suv — nutfadan butunlay) boshqa bir jonzot holida paydo qildik. Bas eng go‘zal yaratguvchi (ya’ni yo‘qdan bor qilguvchi bo‘lmish) Alloh barakotli — buyukdir. I z o h. Ushbu oyatda insonning ona qornidagi bir tomchi suvdan to tirik, komil insonga aylangunigacha kechgan jarayon Yaratganning O’z ilohiy qalami bilan aniq-ravshan qilib chizib berildi. 15. So‘ngra shak-shubhasiz sizlar (ey insonlar), mana shundan (ya’ni yaralib, hayotga kelganingizdan) keyin (ajallaringiz bitgach) albatta vafot topguvchidirsizlar. 16. So‘ngra shak-shubhasiz sizlar qiyomat kunida qayta tirilursizlar. 17. (Qasamki) Biz sizlarning ustingizda yetti yo‘lni (ya’ni yetti qavat osmonni) yaratdik. Biz O’z xalqimizdan g‘ofil bo‘lmadik. I z o h. Mufassirlar aytishicha, bu oyatda yetti qavat osmonning “etti yo‘l” deb atalishini shunday tushunmoq mumkin: Alloh taolo insonni va barcha maxluqotni yaratganidan so‘ng Ularning holidan g‘ofil bo‘lib qolgani yo‘q, balki ularga rizqu ro‘z yog‘ilib turishi uchun ustlarida yetti yo‘l-etti osmonni paydo qildi. 18. Va Biz osmondan (aniq) o‘lchov bilan suv (yomg‘ir-qor) yog‘dirib, uni yerga joylab qo‘ydik. Shak-shubhasiz, Biz uni ketkazishga ham qodirdirmiz. 19. So‘ng Biz sizlar uchun u (suv) yordamida xurmo va uzum bog‘larini paydo qildik. Sizlar uchun u (bog‘larda) ko‘p mevalar bo‘lur, sizlar ulardan yeysizlar. 20. Yana (Biz sizlar uchun) Turi Sayno (tog‘i)dan chiqadigan yog‘li va yeguvchilar uchun (non) hurush bo‘lgan holda o‘sadigan bir daraxtni (ya’ni zaytunni yaratdik). 21. Albatga sizlar uchun chorva mollarida xam ibrat bordir – Biz sizlarni ularning qornidagi sut bilan sug‘orurmiz, yana sizlar uchun ularda (yunglaridan kiyimlar to‘qish, minish kabi) ko‘p foydalar bordir, shuningdek ular(ning go‘sht-yog‘lari) dan yeysizlar. 22. Yana ularning ustida va (daryo-dengizlarda esa) kemalarda yuk tashiysizlar. 23. (Qasamki), Biz Nuhni o‘z qavmiga payg‘ambar qildik. Bas u: «Ey qavmim, Allohga ibodat qilinglar! Sizlar uchun Undan o‘zga iloh yo‘qdir. Axir qo‘rqmaysizlarmi», dedi. 24. (Shunda) uning qavmidan kofir bo‘lgan kimsalar: «Bu ham xuddi sizlarga o‘xshagan odam. (Faqat) sizlardan ustun bo‘lib olmoqchi. Agar Alloh (payg‘ambar yuborishni) xohlasa edi, farishtalarni tushirgan bo‘lur edi. Bizlar bu (Nuh aytayotgan «Alloh yakka-yagonadir», degan so‘z)ni avvalgi ota bobolarimizdan eshitgan emasmiz. 25. U (ya’ni Nuh) faqat bir jinni bo‘lgan odamdir. Bas unga bir (oz) vaqtgacha ko‘z tutinglar, (agar shu so‘zidan qaytmas ekan o‘ldirib yuborursizlar)», dedilar. 26. (Nuh) aytdi: «Parvardigorim, ular meni yolg‘onchi qilganlari sababli O’zing menga yordam qilgin (va ularni halok qilgin)». 27. Bas Biz unga vahiy qildik: Bizning hifzu-himoyamizda va Bizning vahiy ta’limimiz bilan bir kema yasagin. Bas qachon Bizning farmonimiz kelib, tannurdan (olov o‘rniga) favvoralar otilgan vaqtida u kemaga har (jonivordan) bir juftdan va ahli-oilangni solgin. Lekin (kofirlardan) qaysi kimsalar ustida Bizning so‘zimiz (ya’ni suvga g‘arq bo‘lishi haqidagi hukmimiz) o‘tgan bo‘lsa (ularni tark qilgin) hamda u zolim kimsalar haqida (ya’ni ularga najot berishimni so‘rab) Menga xitob-iltijo qilmagin. Ular shak-shubhasiz g‘arq qilinguvchidirlar. I z o h. Ayrim sahobalar «tannur»dan murod barcha yer yuzi, degan farazni ham aytganlar. Shuning uchun biz Hud surasining 40-oyatida tannurni “er” deb ham tarjima qilganmiz. 28. Endi qachon o‘zing va sen bilan birga bo‘lgan kishilar kema ustida joylashib olgach, aytgin: «Bizlarni zolim qavmdan qutqargan Allohga hamdu-sano bo‘lsin». 29. Yana ayt: «Parvardigorim, meni bir muborak manzilga tushirgin. Sen o‘zing eng yaxshi(manzillarga) tushirguvchisan». 30. Albatta bunda (ya’ni Nuh va uni qavmi mojarosida) oyat-ibratlar bordir. Biz imtihon qilguvchidirmiz. 31. So‘ngra Biz ulardan keyin boshqa asrlarni (ya’ni avlodlarni Od qabilasini) paydo qildik. 32. Bas ularga o‘zlaridan bo‘lgan bir payg‘ambarni (ya’ni Hudni) yubordik. (U aytdi): «Allohga ibodat qilinglar! Sizlar uchun Undan o‘zga iloh yo‘qdir. Axir qo‘rqmaysizlarmi?!» 33. Uning qavmidan kofir bo‘lgan, oxiratdagi muloqotni yolg‘on degan va Biz hayoti dunyoda boy-badavlat qilib qo‘ygan kimsalar dedilar: «Bu ham xuddi sizlarga o‘xshagan odam. U ham sizlar yeydigan narsadan yeydi, sizlar ichadigan narsadan ichadi. 34. Qasamki, agar sizlar o‘zingizga o‘xshagan odamga itoat kilib (o‘z butlaringizdan kechsangizlar), u holda albatta ziyon ko‘rguvchidirsizlar. 35. U sizlarga o‘lib tuproq va suyaklarga aylanganingizdan keyin albatta (qabrlaringizdan) chiqarilguvchidirsizlar, deb va’da bermoqdami? 36. Sizlarga va’da qilinayotgan narsa juda-juda uzoqdir. 37. Hayot faqat (shu) dunyodagi hayotimizdir. (Ayrimlarimiz) o‘lsak (boshqalarimiz) hayotga kelaveramiz. Biz hech qayta tirilguvchi emasmiz. 38. U (ya’ni Hud) faqat Alloh sha’niga yolg‘on to‘qigan kimsadir. Bizlar unga hech iymon keltirguvchi emasmiz. 39. (Shunda Hud) aytdi: «Parvardigorim, meni yolg‘onchi qilganlari sababli O’zing menga yordam qilgin (va ularni halok qilgin)». 40. (Alloh) dedi: «Ozginadan keyin ular albatta nadomat qilguvchilarga aylanib qolurlar». 41. Bas haqli ravishda ularni (dahshatli) qichqiriq tutib, Biz ularni xas xashakka aylantirdik. U zolim qavmga halokat bo‘lgay. 42. So‘ngra, ulardan keyin boshqa asrlarni (avlodlarni) paydo qildik. 43. Biron millat-avlod o‘z ajalidan o‘zib ham keta olmas, (uni) ketga ham sura bilmas. 44. So‘ngra paydar-pay payg‘ambarlar yubordik. Har qachon biron millatga o‘z payg‘ambarlari kelsa, uni yolg‘onchi qildilar. Bas, Biz ularni (ya’ni u iymonsiz millatlarni) birin-ketin (halok qildik) va ularni (kishilar o‘rtasida ko‘chib yuradigan) gapga aylantirib qo‘ydik. Bas iymon keltirmaydigan qavmga halokat bo‘lgay. 45-46. So‘ngra Biz Muso va uning birodari Horunni O’z oyat-mo‘‘jizalarimiz va ochiq hujjat bilan Fir’avn va uning odamlariga payg‘ambar qilib yuborganimizda, ular kibr-havo qildilar. Ular mutakabbir qavm edilar. 47. Ular aytdilar: «Xuddi o‘zimizga o‘xshagan ikki kishiga iymon qeltirurmizmi?! Holbuki ularning qavmi (ya’ni Bani Isroil) bizlarga qullik qilguvchidirlar». 48. Bas ikkisini yolg‘onchi qilishib, halok qilinguvchilardan bo‘ldilar. 49. Darhaqiqat, Biz Musoga (Bani Isroil qavmi) hidoyat topishi uchun Kitob – Tavrotni ato etdik. 50. (Keyin) Maryamning o‘g‘li (Iysoni) va uning onasi Maryamni (Bizning qudratimizga dalolat qiladigan) oyat-alomat qildik va ikkisini bir oqar suvli baland-ko‘rkam qarorgohga joyladik. 51. (Yuborgan barcha payg‘ambarlarimizga shunday dedik); «Ey payg‘ambarlar, halol-pok taomlardan yenglar va yaxshi amallar qilinglar! Albatta Men qilayotgan amallaringizni bilguvchidirman. 52. Shak-shubhasiz (barchangizni) millatingiz ya’ni diningiz) bir millat (ya’ni Islomdir). Men esa sizlarning Parvardigoringizdirman, bas, Mendangina qo‘rqingiz!» 53. So‘ng (odamlar) ishlarini (ya’ni dinlarini) bo‘laklarga bo‘lib yubordilar. Har bir guruh o‘z oldilaridagi narsa (din) bilan xursanddirlar. 54. Bas (ey Muhammad), siz (ma’lum) vaqtgacha ularni (ya’ni Makka mushriklarini) o‘z g‘aflatlarida qoldiring! 55-56. Ular Biz ularga berayotgan mol-davlat va bolalari uchun yaxshiliklarni tezlatishimiz deb o‘ylaydilarmi? Yo‘q, ular (buni g‘aflatlari yanada ziyoda bo‘lishi uchun qilinayotganini) sezmaydilar. 57. Albatta, Parvardigorlaridan qo‘rqib xavfda turguvchi kishilar, 58. Parvardigorlarining oyatlariga iymon keltiradigan kishilar, 59. Parvardigorlariga shirk keltirmaydigan kishilar, 60. (Kambag‘al-bechoralarga) bergan sadaqalarini (qiyomat kunida hisob-kitob uchun) Parvardigorga qaytguvchi ekanliklaridan dillari qo‘rqib turgan xolda beradigan kishilar – 61. Ana o‘shalargina (barchadan) o‘zguvchi bo‘lgan hollarida yaxshiliklar qilishga shoshurlar. 62. Biz hech bir jonni toqatidan tashqari narsaga taklif qilmasmiz. Bizning dargohimizda faqat haqni so‘zlaydigan kitob (ya’ni har bir bandaning nomayi a’moli) bordir. Ularga (qiyomat kunida yaxshiliklarini yashirish yo yomonliklarini oshirish bilan) zulm kilinmas. 63. Yo‘q, (kofirlarning) dillari bundan (ya’ni yuqorida mazkur bo‘lgan mo‘minlarning fazilatlaridan) g‘aflatdadir. Ular uchun o‘zlari qiluvchi bo‘lgan bundan boshqa (dinsizlik, riyokorlik, shirk va dilozorlik kabi) amallar bordir. 64. To qachon Biz ularning boyonlarini azobga giriftor qilganimizda (ya’ni mol davlatlarini ketkazib, och-yalang‘och qilib qo‘yganimizda) banogoh ular faryod qilurlar. 65. (Shunda Biz dermiz): «Bugun endi faryod qilmangiz! Aniqki sizlarga Biz tomonimizdan (hech qanday) yordam bo‘lmas. 66. (Chunki) sizlarga Mening oyatlarim tilovat qilinganida, sizlar ketingizga tislangan edingiz. 67. («Baytulloh bizlarniki», deb), u bilan mutakabbirlik qilgan hollaringizda tungi suhbatlaringizda (Qur’on xususida) behuda so‘zlar aytar edingizlar». 68. Axir ular bu So‘zni — Qur’onni tadabbur-tafakkur qilib ko‘rmadilarmi yoki ularga avval o‘tgan ota-bobolariga kelmagan narsa keldimi (ya’ni ularga ham Alloh tarafidan payg‘ambarlar kitoblar bilan kelgan edi-ku)?! 69. Yoki o‘z payg‘ambarlarining (ya’ni Muhammad alayhis-salomning ishonchli, rostgo‘y va xushxulq inson ekanini) tanimay, uni inkor qilguvchi bo‘ldilarmi?! 70. Yoxud: «Unda (Muhammadda) jinnilik bor», dedilarmi?! Yo‘q! (Muhammad) ularga Haqiqatni keltirdi. Ularning ko‘plari esa Haqiqatni yomon ko‘rguvchilardir. 71. Agar Haqiqat — Qur’on ularning havoi nafslariga ergashsa edi (ya’ni unda: «Allohning sheriklari bor», degan gap kelsa edi, albatta osmonlar, yer va ulardagi bor jonzot buzilib-halok bo‘lgan bo‘lur edi. Yo‘q, Biz ular uchun eslatma keltirdik, Ular esa o‘zlariga (kelgan) eslatmadan yuz o‘girguvchidirlar. 72. (Ey Muhammad,) yoki siz ulardan xarj (ya’ni Qur’on oyatlarini keltirganingiz evaziga haq) so‘ramoqdamisiz? (Yo‘q, siz hargiz ulardan xarj so‘ramassiz, chunki) Parvardigoringizning xarji – beradigan ajri yaxshiroqdir. U eng yaxshi rizq berguvchidir. 73-74. Shak-shubhasiz siz ularni faqat to‘g‘ri yo‘lga da’vat qilursiz. Albatta oxiratga iymon keltirmaydigan kimsalar bu yo‘ldan ozguvchidirlar. 75. Agar Biz ularga rahm-shafqat qilsak va ular bilan bo‘lgan narsani (qahatchilikni) aritsak, shak-shubhasiz ular yana o‘z tug‘yonlarida adashib uloqib yurishga kayturlar. 76. Mana Biz ularni azob-ocharchilik bilan ushladik. Ular esa na Parvardigorga bo‘yin egdilar va na tavba-tazarru’ qildilar. 77. To qachon Biz ularga qattiq azob-qahatchilik darvozasini ochib qo‘yganimizda, esa banogoh ular noumid bo‘lguvchidirlar. I z o h . Rivoyat qilinishicha, Makka mushriklari payg‘ambar alayhis-salomning qarg‘ishlariga uchrab, ocharchilikka giriftor bo‘lishib ham iymon keltirmaganlaridan keyin ularga «azob darvozasi ochilib», bu qahatchilik yetti yilga cho‘zilgan ekan. Shunda Quraysh kattalari butunlay umidsizlikka tushib, payg‘ambar alayhis-salomning huzurlariga kelishganida, Alloh taolo u zotga agar bu kofirlarga yana mo‘l-ko‘lchilik berilsa, ular o‘zlarining kibru tug‘yonlariga qaytishlari haqida xabar beradi. Yuqorida mazkur bo‘lgan uch oyati karima shu haqdadir. 78. (Alloh) sizlar uchun quloq(lar)ni, ko‘zlarni va dillarni paydo qilgan zotdir. Sizlar esa kamdan-kam shukr qilursizlar. 79. U sizlarni yer yuzida yaratib - (taratgan) zotdir. Va sizlar (qiyomat kunida) Uning huzuriga to‘planursizlar. 80. U hayot va o‘lim beradigan zotdir. Kecha va kunduzning o‘zgarib turishi ham Uning (izmidadir). Axir aql yurgizmaysizlarmi?! 81. Yo‘q, ular ham xuddi avvalgilar aytgan so‘zlarni aytdilar. 82. Ular dedilar: «Bizlar o‘lib tuproq va suyaklarga aylangan vaqtimizda yana qayta tirilguvchimizmi?! 83. Darvoqe’ bizlarga ham, ilgari ota-bobolarimizga ham mana shu va’da qilingan. Bu faqat avvalgilarning afsonalaridir». 84. (Ey Muhammad, ularga) ayting: «Agar bilguvchi bo‘lsanglar (aytinglar-chi), bu yer va undagi bor jonzot kimniki?» 85. Ular: «Allohnikidir», derlar. Ayting: «Bas (shundan) ibrat-eslatma olmaysizlarmi?! » 86. Ayting: «Yetti osmonning hojasi va ulug‘ arshning sohibi kimdir?» 87. Ular: «(Bularning barchasi) Allohnikidir», derlar. Ayting: «Axir qo‘rqmaysizlarmi?!» 88. Ayting: «Agar bilsanglar (aytinglar-chi), Barcha narsaning podshohligi qo‘lida bo‘lgan, O’zi (barchaga) Homiylik qiladigan, Unga qarshi birov homiylik qila olmaydigan zot kimdir?» 89. Ular: «Bunday podshohlik va homiylik yolg‘iz Allohnikidir», derlar. Ayting: «Bas qanday aldanmoqdadirsizlar?!» 90. Yo‘q! Biz ularga (qayta tirilishlari haqidagi) Haqiqatni keltirdik. Ular esa shak-shubhasiz yolg‘onchidirlar. 91. Allohning bolasi yo‘qdir va U zot bilan birga biron iloh bo‘lgan emasdir. Aks holda albatta har bir iloh o‘zi yaratgan narsa bilan ketib, bir-birlaridan ustun bo‘lib olur edilar, (ya’ni har bir «iloh» o‘z hukmini o‘tkazmoqni istab, natijada yeru osmon buzilib ketgan bo‘lur edi). Alloh ular aytayotgan sheriklardan pokdir. 92. U g‘aybu-shahodatni (ya’ni yo‘qu-borni) bilguvchidir. Bas u (mushriklarning) shirklaridan yuksakdir. 93. Ayting: «Parvardigorim, agar Sen menga (kofirlarga) va’da qilinayotgan (azob)ni (ularning ustiga tushganini) ko‘rguzadigan bo‘lsang, 94. Parvardigorim, (o‘sha soatda) meni u zolim qavm bilan birga qilmagin». 95. Albatta, Biz sizga ularga va’da qilayotgan (azobimizni) ko‘rgizishga qodirdirmiz. 96. Siz (ular qilayotgan) yomonlikni eng go‘zal so‘zlar bilan daf’ qiling! Biz ular (sizni masxaralab) aytayotgan gaplarni juda yaxshi bilguvchidirmiz. 97. Va ayting: «Parvardigorim, men Sendan shaytonlarning vasvasalaridan panoh berishingni so‘rayman.98. Yana men Sendan (yo) Parvardigorim, ular mening huzurimga kelishlaridan panoh berishingni so‘rayman». 99. Toki qachon ulardan (ya’ni mushriklardan) biriga o‘lim kelganida: «Parvardigor, meni (yana hayotga) qaytaringlar. 100. Shoyad, men qolgan umrimda yaxshi amal qilsam», deb qolur. Yo‘q! (U aslo hayotga qaytarilmas). Darhaqiqat bu (har bir jon berayotgan kofir) aytadigan so‘zdir. Ularning ortida to qayta tiriladigan kunlarigacha (dunyoga qaytishlaridan to‘sib turadigan) bir to‘siq bo‘lur. I z o h. Naql qilishlaricha, umrini kufru-tug‘yon bilan sovurgan kimsaga o‘lim soati kelganida, shu qadar nadomat va azobga duchor qilinadiki, bu azob oldida dunyodagi barcha uqubatlar rohat bo‘lib qoladi. Endi u jahannamda shunday azoblarga giriftor bo‘ladiki, buning oldida o‘layotgan soatida ko‘rgan azobi rohatga aylanib qoladi. 101. Bas qachon sur chalinganida (ya’ni qiyomat qoyim bo‘lganida) ana u kunda ularning o‘rtalarida hech qanday nasl nasab qolmas va ular bir-birlari bilan savol-javob ham qila olmaslar. 102. Endi kimning (yaxshilik) mezonlari (yomonlik-gunohlaridan) og‘ir kelsa bas, ana o‘shalar najot topguvchidirlar. 103. Kimning mezonlari yengil bo‘lsa (ya’ni yomonliklari yaxshi amallarini bosib ketsa), bas ana o‘shalar o‘zlariga ziyon qilibdilar. Ular jahannamda mangu qolguvchidirlar. 104. Ularning yuzlarini o‘t kuydirib badbashara bo‘lib qolguvchidirlar. 105. (Ularga): «Sizlarga mening oyatlarim tilovat qilingan emasmidi, sizlar ularni yolg‘on degan emasmidingizlar?!» (deyilganida), 106. Ular dedilar: «Parvardigoro, badbaxtligimiz bizlardan g‘olib kelib, adashgan qavm bo‘lib qolgan ekanmiz. 107. Parvardigoro, bizlarni (jahannamdan hayoti dunyoga) chiqargin. Bas agar yana (tug‘yonga) qaytsak, u holda shak-shubhasiz (o‘z jonimizga) jabr qilguvchidirmiz». 108. (Alloh) aytdi: «(Jahannamda) xor bo‘lingiz va Menga so‘z qotmangiz! 109. Aniqki, Mening bandalarimdan bir guruh bor edi. Ular: «Parvardigoro, (O’zingga) iymon keltirdik. Bas sen Bizlarni mag‘firat qilgin va bizlarga rahm ayla: Sen O’zing rahm qilguvchilarning yaxshirog‘idirsan», der edilar. 110. Bas sizlar ularni masxara qildingiz, hatto ular(ning ustidan kulish) sizlarga Meni eslashni unutdirdi. Sizlar ulardan kulgan edingiz. 111. Men bugun ularni (sizlarning ozor-aziyatlaringizga) sabr-toqat qilganlari sababli mukofotladim — ular haqiqiy (baxt-saodatga) erishguvchidirlar». 112. «Yerda qancha yil turdinglar?» dedi (Alloh). 113. Ular aytdilar: «Bir kun yo yarim kun. Sanab turguvchi (farishtalardan) so‘ragin». 114. (Alloh) dedi: «Agar sizlar biladigan bo‘lsangizlar (dunyoda) juda oz turdingizlar (ya’ni-sizlar abadiy deb o‘ylagan dunyo aslida juda oz muddatdir). 115. Yoki sizlarning gumoningizcha, Biz sizlarni behuda (ya’ni dunyoda sizlarga biron vazifa bermaydigan, oxiratda hisob-kitob qilmaydigan holda) yaratdigu, sizlar Bizning huzurimizga qaytarilmaysizlarmi?!» (Undoq emas)! 116. Zotan Haq Podshoh - Alloh (biron ishni behuda qilishdan) yuksakdir. Hech qanday iloh yo‘q, magar U - ulug‘ arsh sohibi bordir. 117. Kim o‘zi uchun hech qanday hujjat bo‘lmagan holda Alloh bilan birga boshqa biron ilohga iltijo qilsa, bas uning hisob-kitobi Parvardigorining huzurida bo‘lur. Albatta kofir bo‘lgan kimsalar najot topmaslar. 118. (Ey Muhammad), ayting: «Parvardigorim, O’zing (gunohlarimizni) mag‘firat hqilgin va (holimizga) rahm ayla. Sen O’zing rahm qilguvchilarning yaxshirog‘idirsan».")