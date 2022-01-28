from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile

from keyboards.default.yonalishlar import yonalishlar_button
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp, bot


@dp.callback_query_handler(text='sura21')
async def suralar(message:CallbackQuery):

     await message.message.answer(text="Anbiyo Surasi🌹")
     dokument_manzil = InputFile(path_or_bytesio='for_send/Anbiyo.docx')

     user_id = message.from_user.id
     await bot.send_document(chat_id=user_id, document=dokument_manzil)
    # await message.message.answer(text="Bu sura Makkada nozil bo‘lgan. U bir yuz o‘n ikki oyatdir. Sura qiyomat soati yaqinlashib qolgani, odamlar esa u Kundagi hisob-kitobga hozirlanib, yaxshi amallar qilish o‘rniga g‘aflat uyqusiga g‘arq ekanliklari haqida xabar berish bilan boshlanadi. So‘ng o‘quvchi e’tibori koinotdagi har bir mavjudotning o‘ta nozik va aniq o‘lchov bilan yaratilib, yakkayu yolg‘iz Yaratgan tomonidan boshqarib turilishiga qaratiladi va yeru osmonda Allohdan o‘zga yana biron iloh bo‘lsa, u o‘lchov va tartibga futur yetib, borliq buzilib ketishi aniq ekanligi ta’kidlanadi. Bu surada Ibrohim payg‘ambar va u zot bilan butparastlar o‘rtasida bo‘lib o‘tgan mojarolar xususida batafsil hikoya qilinib, o‘zini o‘zi himoya qilishga ojiz bo‘lgan jonsiz but-sanamlar birovga yordam qilishi yoki ziyon yetkazishi amrimahol ekanligi uqtiriladi. Yana bu surada Alloh taoloning payg‘ambarlaridan Ishoq, Ya’qub, Lut, Nuh, Dovud, Sulaymon, Ayyub, Ismoil, Idris, Zul-kifl, Zunnun, Zakariyo va Iyso alayhis-salomlar to‘g‘risida ham xabarlar vorid bo‘lganki, suraning «Anbiyo — Payg‘ambarlar» deb nomlanishiga ham bois shudir. Suraning nihoyasida Alloh taoloning so‘nggi payg‘ambari hazrati Muhammad sollallohu alayhi vasallamning barcha olamga Allohning rahmat-marhamati bo‘lib kelganlari zikr qilinadi. Mehribon va rahmli Alloh nomi bilan (boshlayman). 1. Odamlarga hisob-kitoblari (ya’ni qiyomat qoyim bo‘lishi) yaqinlashib qoldi. Ular esa g‘aflatda, (iymon keltirib, yaxshi amallar qilishdan) yuz o‘girguvchidirlar. 2—3. Ularga Parvardigorlari tomonidan biron yangi eslatma — oyat kelar ekan, albatta uni masxara qilib, dillari g‘ofil bo‘lgan hollarida tingladilar va zolim kofir kimsalar: «Bu (ya’ni Muhammad) o‘zlaringizga o‘xshagan bir odam xolos ku! Ko‘rib turgan holingizda sehr-joduga (aldanish uchun) kelaverasizlarmi?!» (deb) o‘zaro shivirlashdilar. 4. (Shunda Muhammad) aytdi: «Parvardigorim osmonu-zamindagi har bir so‘zni bilur. U eshitguvchi, bilguvchidir». 5. «Balki, —dedilar ular — (Muhammad vahiy deb da’vo qilayotgan so‘zlar) – aloq-chaloq tushlardir, balki (bu so‘zlarni) u o‘zi to‘qib olgandir, balki u bir shoirdir. Bas, u ham ilgari yuborilgan payg‘ambarlar (keltirganlari) kabi biron oyat-mo‘‘jiza keltirsin!» 6. Ulardan oldin, Biz halok qilgan biron qishloq-shahar (aholisi) iymon keltirgan emas, bas, ular iymon keltirarmidilar?! 7. (Ey Muhammad), Biz sizdan ilgari ham faqat kishilarni (ya’ni insonlarni) O’zimiz vahiy yuborgan holda payg‘ambar qilgandirmiz. Bas (ey Makka ahli), agar o‘zlaringiz bilmaydigan bo‘lsangizlar (Tavrot, Injilni biladigan) ahli ilmlardan so‘ranglar! 8. Biz u (payg‘ambar)larni taom yemaydigan bir jasad qilgan emasmiz va ular mangu hayot kechirguvchi ham emas edilar. 9. So‘ngra Biz (bergan) va’damizga vafo qilib, u (payg‘ambar)larga O’zimiz xohlagan (iymonli) kishilar bilan birga najot berganmiz, haddan oshuvchi kimsalarni — kofirlarni esa halok qilganmiz. 10. Darhaqiqat Biz sizlarga bir Kitob — Qur’on nozil qildikki, unda sizlar uchun zikr (ya’ni sha’nu sharaf) bordir. (Chunki u sizlarning tilingizda nozil qilindi). Aql yurgizmaysizlarmi?! 11. Qancha zolim-kofir bo‘lgan qishloq-shaharlarning (ahlini) halok qildik va ularning ortidan (butunlay) boshqa qavm-avlodni vujudga keltirdik. 12. Bas, qachonki ular (ya’ni halok qilingan kimsalar halokatlari oldida) Bizning azobimiz (tushishini) sezib qolishgach, banogoh u joydan qochib qolurlar. 13. (Shu payt farishtalar): «Qochmanglar, maishatga botgan joylaringizga, o‘z maskanlaringizga qaytinglar, ehtimol javob berarsizlar», (deganlarida), 14. (Ular bir-birlariga): «Ey holimizga voy! Darhaqiqat, bizlar (o‘zimizga) zolim bo‘ldik», dedilar. 15. Bas, to Biz ularni (o‘t-o‘lan kabi) o‘rilgan, (o‘tin kabi) o‘chgan holga solgunimizcha ularning ana o‘sha dod-voylari davom etdi. 16. Biz osmon va yerni hamda ularning orasidagi narsalarni o‘ynab-behuda yaratganimiz yo‘q. (Balki O’z qudratimizni namoyish qilish uchun va bandalarimiz foydalanishlari uchun yaratdik.) 17. Agar Biz vaqtichog‘lik qilishni (ya’ni xotin, bola-chaqa orttirishni) istasak, agar (shunday) qilguvchi bo‘lgan chog‘imizda ham uni (ya’ni xotin, bola chaqani) O’z dargohimizdan (ya’ni maloikalardan yoki jannat hurlaridan) qilgan bo‘lur edik. 18. Yo‘q, (Biz unday aybu nuqsondan pokdirmiz), Biz Haq Qur’onni botil jaholatning ustiga oturmiz, bas (haqiqat botilni) ezib-yanchib, banogoh (botil) yo‘q bo‘lur. Sizlar uchun esa (mushriklar, Allohni «xotin, bolasi bor», deb noloyiq sifatlar bilan) sifatlaganlaringiz sababli halokat bo‘lur. 19. Osmonlar va yerdagi bor jonzot Unikidir. Uning huzuridagi zotlar (ya’ni farishtalar) Unga ibodat qilishdan orlanib-zorlanmaydilar. 20. Ular tunu kun sustkashlik qilmasdan (Allohni) poklaydilar. 21. Yoki ular (ya’ni mushriklar) yerning o‘zidan (ya’ni, tosh, yog‘ochlardan), (o‘liklarni) tiriltira oladigan «xudolarni» topib oldilarmi?! 22. Agar (osmonu zaminda) Allohdan o‘zga xudolar bulganida, har ikkisi buzilib ketar edi, Bas, arsh egasi bo‘lmish Alloh ular sifatlayotgan (sheriklardan) pokdir. 23, U O’zi qiladigan biron narsa haqida mas’ul bo‘lmas, ular (ya’ni bandalar esa qiladigan har bir ish-amallari xususida) mas’ul bo‘lurlar. 24. Yoki Uni qo‘yib (boshqa) «xudolarni» topib oldilarmi?! (Ey Muhammad), ayting: («Ey mushriklar, mana shu shirklaringiz haq ekanligiga) hujjat dalillaringizni ko‘rsatingiz! Mana men bilan birga bo‘lgan (mo‘minlarning) eslatmasi (ya’ni Qur’on) va mendan avvalgilarning eslatmalari (ya’ni Tavrot, Injil, Mana shu kitoblarning qaysi birida Allohdan o‘zga ham xudolar mavjud ekanligiga hujjat-dalil bor?!)» Yo‘q, ularning aksariyati Haqikatni bilmay turib, (Undan) yuz o‘giruvchilardir. 25. (Ey Muhammad), Biz sizdan ilgari yuborgan har bir payg‘ambarga ham: «Hech qanday iloh yo‘q, magar Mengina bordirman, bas Mengagina ibodat qilinglar», deb vahiy yuborgandirmiz. 26. Ular (ya’ni mushriklar): «Rahmonning (farishtalardan) bolasi bor», dedilar. U zot (mushriklarning badgumonlaridan) mutlaqo pokdir. Yo‘q, (farishtalar aslo Allohning bolalari emas, balki) ulug‘ bandalardir. 27. (Farishtalar) U zotdan ilgari biron so‘z aytmaydilar (ya’ni Alloh buyurmagan biron ishni qilmaydilar), Ular (Allohning) amri farmoni bilangina amal qilurlar. 28. U zot ularning oldilaridagi (qiladigan) va orqalaridagi (qilib o‘tgan) barcha ish-amallarini bilur. Ular (qiyomat qoyim bo‘lgan kunda) faqat (Alloh) rozi bo‘lgan kishilarnigina shafoat qilurlar – oqlay olurlar. Ularning (o‘zlari Allohdan) qo‘rqib xavfu xatarda tururlar. 29. Ulardan biron kimsa: «Men ham (Allohdan) o‘zga bur ilohman», desa, bas, Biz o‘shani jahannam bilan jazolarmiz. Biz barcha zolim-mushriklarni ham ana shunday jazolaymiz. 30. Kofir bo‘lgan kimsalar osmonlar ham, yer ham (avvalda) to‘siq (ya’ni osmonlardan yog‘in yog‘mas, yerdan esa biron giyoh unmas) bo‘lganini, bas, Biz ularni ochib yuborganimizni (ya’ni osmondan yog‘in yog‘dirib, yerdan giyoh undirganimizni) va barcha jonli mavjudotni suvdan (paydo) qilganimizni ko‘rmadilarmi?! Endi ham iymon keltirmaydilarmi?! 31. Biz yer (odamlarni) tebratmasin uchun unda tog‘larni (paydo) qildik va adashmasliklari uchun unda keng dara-yo‘llar qildik. 32. Biz osmonni qulab tushmaydigan tom qilib qo‘ydik. Ular (mushriklar) esa (osmondagi oy, quyosh, yulduz kabi Allohning qudratini ko‘rsatib turgan) alomatlardan yuz o‘giruvchidirlar. 33. (Alloh) kecha va kunduzni, quyosh va oyni yaratgan zotdir. (Bularning) barchasi o‘z falak-fazosida suzurlar! 34. (Ey Muhammad), Biz sizdan avval ham biron odamzodga abadiy hayot bergan emasmiz. Bas, agar siz o‘lsangiz, ular abadiy qolurlarmi?! (Yo‘q, ular ham mangu qolmaslar). 35. Har jon o‘limni totib ko‘rguvchidir. Biz sizlarni (sabr-toqatlaringizni sinash uchun) yomonlik bilan ham, (shukr qilishingizni bilish uchun) yaxshilik bilan ham «aldab» imtihon qilurmiz. (Keyin) faqat Bizgagina qaytarilursizlar. 36. (Ey Muhammad), qachon kofir bo‘lgan kimsalar sizni ko‘rsalar, faqat (bir birlariga sizni ko‘rsatishib): «Sizlarning ilohlaringizni ayblaydigan kimsa mana shumi?» (deyishib) masxara qiladilar xolos. Holbuki ularning o‘zlari Parvardigorning eslatmasi Qur’ondan yuz o‘giruvchilardir. 37. (Haqiqatan) inson shoshqaloq holda yaralgandir. Yaqinda Men sizlarga O’z oyat-alomatlarimni ko‘rgazurman (ya’ni Menga osiy bo‘lgan kimsalarni qanday azoblashimni ko‘rursizlar) . Bas, Meni shoshtirmangiz. 38. Ular (ya’ni dinsiz kimsalar): «Agar rostgo‘y bo‘lsangiz (aytinglar-chi) mana shu va’da qachon bo‘ladi?» derlar. 39. Agar kofir bo‘lgan kimsalar na oldilaridan va na ortlaridan (do‘zax) o‘tini to‘sa olmay qoladigan, ularga yordam berilmaydigan vaqtni (qiyomat kunidagi dahshatlarni) bilsalar edi, (bu so‘zlarni aytmagan bo‘lur edilar). 40. Yo‘q, (qiyomat) to‘satdan kelib, ularni hayronu xasta qilib qo‘yur, bas uni qaytarishga ham kuchlari yetmas, ularga (tavba-tazarru’ uchun) muhlat ham berilmas. 41. (Ey Muhammad), aniqki, sizdan avvalgi payg‘ambarlar ham masxara qilingan. Bas ularning ustidan kulgan kimsalarga o‘zlari (ishonmay) masxara qilgan narsalari (Allohning azobi) tushgandir. 42. Ayting: «Kechasiyu kunduzi sizlarni Rahmon (azobidan) kim saqlay olur?!» Yo‘q, ular Parvardigorni eslashdan yuz o‘girguvchilardir. 43. Yoki ularning Bizdan o‘zga himoya qiladigan «xudolari» bormikan?! U («xudolar») o‘zlariga yordam qilishga ham qodir emaslar va ular Bizning tomonimizdan himoya ham qilinmaslar. 44. Yo‘q, Biz ularni (kofirlarni) va ota-bobolarini (dunyo matolaridan shunday) foydalantirdikki, hatto ularga umr-hayot uzun-abadiy (ko‘rinib, bir kun kelib bu hayot tugashiga ishonmay qo‘ydilar va Allohning azobini ham inkor qildilar). Axir ular Biz yerni atrofidan kamaytirib kelayotganimizni (tobora ko‘proq kishilar Islom kirib, kufr dunyosi qisqarib borayotganini) ko‘rmaydilarmi?! O’shalar g‘olib bo‘lurlarmi?! (Yo‘q, ular mag‘lubdirlar, Allohning diniga iymon keltirgan zotlar g‘olibdirlar). 45. Ayting: Men sizlarni faqat vahiy bilan qo‘rqitib-ogohlantirurman. (Leki gunglar (ya’ni dinsizlar o‘zlari uchun oxiratda azob haqidagi vahiy bilan) qo‘rqitilayotgan vaqtlarida da’vatni eshitmaydilar. 46. Qasamki, agar ularga Parvardigoringizning azobidan andak yetsa, albatta ular: «Holimizga voy! Darhaqiqat bizlar (o‘z jonimizga) jabr qilguvchilar bo‘ldik», deb qolurlar. 47. Biz qiyomat kuni uchun adolatli mezon-tarozilar qo‘yurmiz, bas, biron jonga zarracha zulm qilinmas. Agar xardal (o‘simligining) urug‘idek (yaxshi yoki yomon amal qilingan) bo‘lsa, o‘shani-da keltirurmiz! Biz O’zimiz yetarli hisob kitob qilguvchidirmiz. 48. Darhaqiqat, Biz Muso va Horunga (haq bilan botilni) ajratguvchi, ziyo va taqvodor kishilar uchun eslatma bo‘lgan (Tavrotni) ato etdik. 49. Ular Parvardigorlaridan ko‘rmay turib, qo‘rqurlar. Ular (qiyomat qoyim bo‘ladigan) soatdan xavfda turguvchilardir. 50. Bu (Qur’on) Biz nozil qilgan muborak eslatmadir. Hali sizlar uni inkor qilguvchimisizlar?! I z o h. Ushbu oyatdagi xitob Makka arablariga qaratilgan bo‘lib, uni shunday tushunmoq lozim: Boshqa til, boshqa millat egalari Qur’on tilini bilmaganlari bois, Uning qadri qimmatini to‘la anglay olmasliklari mumkin. Ammo sizlar o‘z tilingizda nozil qilingan, teran ma’no-mohiyatidan tashqari balog‘at va fasohatga to‘liq bo‘lgan nazmining o‘zidan ilohiy mo‘jiza ekani ko‘rinib turgan Kitobni qanday inkor qila olasizlar?! 51. Darhaqiqat Biz (Musodan) ilgari Ibrohimga Haq yo‘lini ato etdik. Biz uning (Haq yo‘lga loyiq ekanini) bilgan edik. 52. O’shanda (Ibrohim) otasi va qavmiga: «Sizlar doimo cho‘qinadigan bu haykallar nimadir (ya’ni nega jonsiz haykallarga sig‘inyapsizlar?!)» deganida: 53. Ular aytdilar: «Bizlar ota-bobolarimizni ham ularga sig‘ingan holda topganmiz». 54. U dedi: «Darhaqiqat sizlar ham, ota-bobolaringiz ham ochiq zalolatda ekansizlar». 55. Ular aytdilar: «Keltirgan aytgan (bu so‘zlaring) rostmi yoki sen hazil qilguvchilardanmisan?» 56. U dedi: «Yo‘q! Sizlarning Parvardigoringiz (mana bu hech kimga foyda ham, ziyon ham yetkaza olmaydigan butlar emas, balki) osmonlar va yerning Parvardigoridirki, U zot ularni O’zi yaratgandir. Men bunga guvohlik berguvchilardandirman. 57. Alloh nomiga qasamki, sizlar (hayitgohlaringizga) ketganlaringizdan keyin butlaringizni bir balo qilurman». I z o h. Tangri taoloning hidoyati bilan go‘daklik chog‘idayoq xonsiz haykal-butlarga sig‘inishdan bosh tortgan Ibrohim alayhis-salomni otasi: «Zora xudolarimiz haqidagi xato fikrlari o‘zgarsa», deb o‘zlarining yilda bir bo‘ladigan diniy bayramlariga olib bormoqchi bo‘ladi. Lekin u oyog‘i og‘riyotganini bahona qilib, bayramga bormaydi va ichida ular ketgach butxonadagi haykallarni sindirishga qasam ichadi. 58. Bas, u (butlarni) parcha-parcha qildi. Faqat, «shoyad (mushriklar u butlarning) kattasiga qaytsalar» deb, o‘shanigina (qoldirdi va uning bo‘yniga bir boltani ilib qo‘ydi). 59. Ular (qaytib kelganlaridan so‘ng): «Bizning xudolarimizni kim bunday qildi? Shubhasiz u zolim kimsalardandir», dedilar. 60. Ular(ning ayrimlari) aytishdi: «(Xudolarimizni) ayblab yuradigan Ibrohim degan bir yigitni eshitgandik» 61. (Shunda ularning kattalari): «Uni odamlar qoshiga keltiringiz! Ular guvoh bo‘lsinlar», deyishdi. 62. (Uni keltirishgach): «Xudolarimizni sen shu (holga) soldingmi, ey Ibrohim?» deb (so‘rashdi). 63. (Ibrohim) aytdi: «Yo‘q, bu ishni ularning kattasi mana bu «haykal» qildi. Bas, (butlaringizdan) so‘ranglar, agar gapira oladigan bo‘lsalar (aytib bersinlar)». 64. Bas, (mushriklar) o‘zlariga kelib, (bir-birlariga): «Sizlar o‘zingiz zolimlarsiz» dedilar. 65. So‘ngra esa yana boshlari aylanib: «Sen ularning gapirmasliklarini yaxshi bilarding-ku?!» deyishdi. 66. (Ibrohim) aytdi: «Axir Allohni qo‘yib, sizlarga biron foyda xam, ziyon ham yetkaza olmaydigan narsalarga sig‘inasizlarmi?! 67. Sizlarga ham, Allohni qo‘yib sig‘inayotgan butlaringizga ham suf-e! Axir aql yurgizmaysizlarmi?!» 68. (Ibrohimning haq ta’na va dashnomlariga biron javob topa olmay qolgan Namrud boshchiligidagi mushriklar dedilar: «Uni yoqib yuboringlar! Agar uddalay olsanglar (mana shu ish bilan) o‘z xudolaringizga yordam qilinglar». I z o h. Shundan keyin mushriklar ulkan o‘tin g‘arami hozirlashib, uning hamma tomoniga o‘t qo‘ydilar va Ibrohimni qo‘l-oyog‘ini bog‘lab bir manjaniqqa (qadimiy tosh otish quroli) solishib olovga otdilar. Shunda... 69. Biz aytdik: «Ey olov, sen Ibrohim uchun salqin va omonlik bo‘l!» I z o h . Mufassirlar aytishlaricha, Ibrohim alayhis-salom manjaniqdan otilgan lahzada uning yoniga farishta Jabroil kelib: «Menga biron hojat-tilaging bormi?» — deb so‘ragan ekanlar, Ibrohim: «Senga (ya’ni yolg‘iz Allohdan o‘zga biron kimsaga) ehtiyojim yo‘q», deb javob beribdilar. «Parvardigorga-chi?» - so‘rabdi Jabroil, «Parvardigorim o‘zi ahvolimdan ogohdir», debdilar Ibrohim. Shunda Tangri taolo olovga yuqorida zikr qilingan farmonini yuborib, uning yorug‘i qolib, issig‘i yo‘qolibdi. Ibrohim alayhis salomning esa bog‘langan arqoni yonib bitibdi-yu, u kishining o‘ziga ozor yetmabdi. Qissadan hissa shuki, kimda kim Ibrohim payg‘ambar kabi yolg‘iz Alloh taologa bandalik qilib, U zotdan o‘zga biron kimsadan madad-yordam tilamasa Alloh uni o‘tda kuydirmas, suvda cho‘ktirmas. 70. Ular (Ibrohimga) makr qilmoqchi bo‘ldilar (ya’ni uni yondirib yubormoqchi bo‘ldilar). Biz esa ularning o‘zlarini ko‘proq ziyon ko‘rguvchi qilib qo‘ydik. 71. Va unga hamda Lutga najot berib, (ularni) Biz barcha olamlar uchun muborak qilgan (Shom) zaminiga (yubordik). 72. Biz (Ibrohimga Bizdan bir farzand so‘raganida) Ishoqni hadya etdik va Ya’qubni ham ziyoda qildik hamda (ularning) barchalarini solih kishilar qildik. 73. Yana ularni Bizning amrimiz bilan (kishilarni Haq yo‘lga) hidoyat etadigan peshvolar kildik va ularga yaxshi amallar qilishni, namozni to‘kis ado etishni va zakotni (mustahiq kishilarga) ato etishni vahiy qildik. Ular yolg‘iz Bizgagina ibodat qilguvchi bo‘ldilar. 74. Lutga esa hikmat va ilm ato etdik va uni nopokliklar qiluvchi bo‘lgan qishloq (ahli)dan kutqardik. Darhaqiqat ular yomon buzuq qavm edilar. 75. Va uni O’z rahmat-jannatimizga dohil qildik. Shak-shubhasiz u solihlardandir. 76. Nuhni (eslang): O’shanda - (mazkur payg‘ambarlarning davridan) ilgari nido qilganida Biz uning (nidosini) mustajob qilib, o‘zini va axli-tobe’larini ulug‘ g‘amdan qutqardik. 77. Va unga Bizning oyatlarimizni yolg‘on degan qavmdan madad-najot berdik. Darhaqiqat ular yomon qavm edilar. Bas, Biz ularning barchasini g‘arq qilib yubordik. 78. Dovud va Sulaymonning ekinzor xususida hukm qilayotgan paytlarini (eslang). O’shanda unga qavmning qo‘ylari bo‘shalib kirib (uni payhon qilib yuborgan) edi. Biz ular (chiqargan) hukmga shohid edik. 79. Bas, Biz uni Sulaymonga anglatdik. I z o h . Rivoyat qilishlaricha, Dovud va Sulaymon payg‘ambarlarning oldilariga ikki kishi bir mojaro xususida hukm so‘rab keladi. Ulardan birining qo‘ylari ikkinchisining ekinzoriga kirib ketib biron narsani sog‘ qoldirmay payhon qilib chiqib ketgan edi, Dovud alayhis-salom qo‘ylar ekinzor egasiga berilsin, deb hukm chiqaradilar. Buni eshitgan o‘g‘illari Sulaymon alayhis-salom esa «erni qo‘ylarning egasiga, qo‘ylarni esa ekinzor sohibiga berilsa-yu, qo‘ylarning egasi yerni o‘nglab, ekin ekib avvalgi holiga qaytargach, qo‘ylarini qaytib olsa. Shu muddat ichida ekinzor sohibi u qo‘ylarning yungi, sutidan foydalanib, shu davrda tug‘ilgan qo‘zilarini ham o‘ziga olib qolsa», deydilar. Shunda Dovud Sulaymonga qarab: «O’g‘ilcham, sening hukming to‘g‘riroqdir», deb o‘z chiqargan hukmlarini bekor qiladi... Biz har ikkisiga hikmat-payg‘ambarlik va ilm ato etdik. Tog‘lar va qushlarni Dovud bilan birga tasbeh aytadigan qilib bo‘ysundirib qo‘ydik. Biz shunday qila olguvchidirmiz. I z o h. Aytishlaricha, Dovud alayhis-salom benazir xush ovoz sohibi bo‘lib, Zaburni tilovat qilganlarida samoda uchib ketayotgan qush muallaq qotib, atrofdagi tog‘lar ham birga qiroat qilar ekan. 80. Yana (Dovudga) sizlarga ziyon yetishidan saqlaydigan sovut ilmini ta’lim berdik. Bas sizlar shukr qilurmisiz?! 81. Sulaymonga esa bo‘ronli shamolni (bo‘ysundirib), uning amri bilan Biz muborak qilgan zaminga (Shomga) esadigan qilib qo‘ydik. Biz barcha narsani bilguvchidirmiz. 82. Yana shayton-jinlardan (Sulaymon uchun) g‘avvoslik qiladigan va bundan boshqa ishlarni ham ado etadigan kimsalarni (yaratdik). Va biz ularni (Sulaymonning amridan chiqib ketmasliklari uchun) qo‘riqlab turguvchi bo‘ldik. 83. Ayyubning Parvardigoriga nido qilib: «(Parvardigorim), meni balo ushladi. O’zing rahm-shafqat qilguvchilarning rahmlirog‘idirsan», deb iltijo qilgan paytini (eslang). 84. Bas Biz uning (duosini) mustajob qilib, undagi ziyon-zahmatni ketkazdik hamda O’z huzurimizdan mehribonlik ko‘rsatib, barcha ibodat qilguvchilarga eslatma-ibrat bo‘lsin, deb (Ayyubga) ahli-oilasini va ular bilan qo‘shib yana o‘shalarning mislicha bola-chaqa ato etdik. I z o h. Ayyub payg‘ambar asli Rum mamlakatidan bo‘lib, ser-farzand va boy-badavlat kishi edilar. So‘ngra boshlariga og‘ir kunlar tushib mol-dunyolaridan ajradilar, lekin qanoat qildilar; bolalari birin-ketin halok bo‘lishib, ulardan ham judo bo‘ldilar, sabr qildilar; salomatliklaridan ajrab, eng og‘ir xastaliklarga duchor bo‘ldilar, shikoyat qilmadilar. Qachonki ayrim kimsalar: «Bu eng yomon gunoh-jinoyatlarni qilganki, Xudo unga shunday balolarni yuborgan», deganlarini eshitgandan keyingina sabr kosasi to‘lib, Alloh taologa iltijo qilib, o‘z holidan shikoyat qilgan va Tangri taolo u zotning duolarini ijobat qilib, salomatliklarini ham, mol-davlatlarini ham qaytarib bergan. Halok bo‘lgan yetti o‘g‘il, yetti qizlariga hayot ato etib, yana yetti o‘g‘il va yetti qiz ko‘rganlar, Mazkur oyatdagi «barcha ibodat qilguvchilarga eslatma-ibrat bo‘lsin, deb» degan so‘zlarning ma’nosi shuki, boshlariga biron balo tushgan kishilar Ayyub alayhis-salom kabi sabr-qanoat qilsalar, albatta Alloh taolo ularning balolarini ketkazib, avvalgidan ham ziyoda ne’matlar ato etur. 85. Ismoilni, Idrisni va Zul-kiflni (eslang). Barchalari sabr qilguvchi zotlardandirlar. 86. Biz ularni O’z rahmat-jannatimizga doxil qildik. Darhaqiqat ular solih zotlardandirlar. 87. Zunnun — Yunusning (qavmidan) g‘azablangan holda (o‘z qishlog‘idan chiqib) ketib, Bizni uning ziyoniga hukm qilmaydi, deb o‘ylagan paytini, so‘ng (Biz uni baliq qorniga tashlaganimizdan keyin) qorong‘u zulmatlarda turib: «Hech iloh yo‘q, magar O’zing bordirsan, ey pok Parvardigor, darhaqiqat men (o‘z jonimga) jabr qilguvchilardan bo‘lib qoldim», deb nido qilgan (paytini eslang). 88. Bas, Biz uning (duosini) mustajob qildik va uni g‘am-g‘ussadan qutqardik. Biz mo‘minlarga mana shunday najot berurmiz. 89. Zakariyoning: «Parvardigorim, meni yolg‘iz holda tashlab qo‘yma (ya’ni menga O’z dargohingdan bir merosxo‘r farzand ato et), O’zing vorislarning yaxshirog‘idirsan (ya’ni hammaning ortida qolguvchidirsan) deb nido qilgan paytini (eslang). 90. Bas Biz uning (duosini) mustajob qildik va unga Yahyoni hadya etdik hamda juftini o‘nglab (tug‘maydigan kampirni bola ko‘rishga qodir qilib) qo‘ydik. Darhaqiqat ular (ya’ni mazkur payg‘ambarlar) yaxshi ishlarni qilishga shoshar va Bizga rag‘bat va qurquv bilan duo-iltijo qilar edilar. Ular Bizga ta’zim-itoat qilguvchi edilar. 91. Yana o‘z nomusini saqlagan ayolni (ya’ni Maryamni eslang). Bas, Biz O’z tarafimizdan bo‘lgan ruhni unga pufladik (va u Isoga homilador bo‘ldi) va uni hamda o‘g‘lini barcha olamlar uchun oyat-ibrat qildik. 92. (Ey insonlar), sizlarning millatingiz-diningiz haqiqatda bir dindir (ya’ni Islomdir). Men esa (barchalaringizning) Parvardigoringizdirman. Bas, Mengagina ibodat qilinglar! (Odamlar) esa ishlarini (ya’ni dinlarini) o‘zaro parchalab-bo‘lib oldilar. Barchalari Bizga qaytguvchidirlar. 94. Bas, kim mo‘min bo‘lgan holida yaxshi amallardan qilsa uning sa’y-harakati zoe bo‘lmas – Biz uni yozib qo‘yguvchidirmiz. 95-96-97. Biz halok qilgan biron qishloq-shahar (ahli qayta dunyoga kelishi) haromdir. To Ya’juj va Ma’juj (to‘g‘oni) ochilib, ular har bir tepalikdan oqib keladigan va Haq va’da (ya’ni qiyomat) yaqin bo‘ladigan vaqtgacha ular (ya’ni Biz halok qilgan kimsalar) qaytmaydilar. Ana u vaqtda esa kofir bo‘lgan kimsalarning ko‘zlari qotib: «Ey, holimizga voy, bizlar bunday (oqibatdan) g‘aflatda edik. Yo‘q, bizlar (o‘z jonlarimizga) jabr qilguvchi bo‘ldik», (deydilar). 98. (Ey mushriklar), sizlar ham, Allohni qo‘yib sig‘inayotgan butlaringiz ham jahannam o‘tinlaridir. Sizlar u (jahannamga) tushguvchidirsizlar. 99. Agar (sizlar sig‘inadigan butlaringiz) xudolar bo‘lganida (jahannamga) tushmagan bo‘lur edilar. (Bu butlar va ularga sig‘inadiganlarning) barchalari u joyda abadiy qolguvchidirlar. 100. Ular uchun u joyda (faqat) dod-faryod qilishgina bordir. Ular u joyda (biron narsani) eshitmaslar. 101. Albatta Bizning tomonimizdan go‘zal (manzilat-martaba) berilgan zotlar - ana o‘shalar (jahannamdan) uzoq qilinurlar. 102. Ular uning sharpasini ham eshitmaslar. Ular o‘zlari istagan ne’matlarda abadiy qolguvchidirlar. 103. Ularni Buyuk dahshat (ya’ni qiyomat) mahzun qilmas. Farishtalar ularni: «Mana shu sizlarga va’da qilingan kundir», deb kutib olurlar. 104. U kunda Biz osmonni ham xuddi maktub yozilgan sahifani o‘ragan yanglig‘ o‘rab, birinchi marta qanday yaratgan bo‘lsak, (o‘sha holga) qaytarurmiz. (Bu) Bizning zimmamizdagi va’dadir. Albatta Biz (shunday) qilguvchidirmiz. 105. Darhaqiqat Biz (Lavhul-mahfuzda) zikr qilgandan so‘ng Zaburda: «Albatta (jannatning) yeriga mening solih bandalarim voris bo‘lurlar», deb yozib qo‘ygandirmiz. 106. Albatta mana shu (Qur’onda) ibodat qilguvchi qavm uchun yetarli narsa bordir. 107. (Ey Muhammad), darhaqiqat Biz sizni barcha olamlarga faqat rahmat (ya’ni Allohning rahmati-jannatiga yetaklaguvchi) qilib yubordik. 108. Ayting: «Menga faqat (Sizning) ilohingiz yakka yagona iloh ekani vahiy qilinur. Bas, sizlar (vahiyga) bo‘yinsunuvchimisizlar?» 109. Endi agar yuz o‘girsalar, u holda ayting: «Men sizlarning (barchangizga hech kimni ayirmay menga nozil bo‘lgan vahiyni) eshitdirdim. Sizlarga va’da qilingan (qiyomat kunidagi azobni) yaqin yo yiroqligini esa bilmasman». 110. Albatta U zot so‘zning oshkorasini ham bilur, sizlar berkitadigan so‘zlarni ham bilur. Qur’oni karim. Alouddin Mansur tarjimasi www.ziyouz.com kutubxonasi 288 111. Bilmayman, ehtimol bu (ya’ni azob soatining ta’xirga tashlanishi) sizlar uchun bir aldov-sinov va bir oz vaqtgacha (ajallaringiz yetib o‘lguningizgacha) foydalanishdir». 112. (Muhammad) aytdi: «Parvardigorim, O’zing Hak hukmingni qilgin. Parvardigorimiz — sizlarning («Alloh yolg‘iz emas», deb U zotni bo‘hton sifat bilan) sifatlashlaringizdan madad so‘raladigan Rahmondir».")