from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile

from keyboards.default.yonalishlar import yonalishlar_button
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp, bot


@dp.callback_query_handler(text='sura35')
async def suralar(message:CallbackQuery):

     await message.message.answer(text="Fotir Surasi🌹")
     dokument_manzil = InputFile(path_or_bytesio='for_send/Fotir.docx')

     user_id = message.from_user.id
     await bot.send_document(chat_id=user_id, document=dokument_manzil)
    # await message.message.answer(text="Ushbu sura ham Makkada nozil qilingan bo‘lib, qirq besh oyatdan iborat. Sura Alloh taologa hamdu-sano aytish bilan boshlanib, Uning osmonlar va yerni yo‘qdan bor qilgan zot ekani hamda insonlarni haq yo‘lga hidoyat qilish uchun O’zi bilan ular o‘rtasida farishtalarni elchi-vositachi qilib qo‘ygani haqida xabar beriladi. Bu surada hayoti dunyodan keyin oxirat hayoti kelishi haq ekanligiga osmonu zaminda kishilar ko‘z o‘ngida kechadigan voqea-hodisalar ham aniq dalolat qilib turishi va shu bilan birga koinotdagi har bir maxluqot o‘zining nechog‘li mukammalligi va o‘ta nozik intizomi bilan nihoyat darajada qudrat va hikmat egasi bo‘lgan bir Yaratguvchi mavjud ekaniga ochiq hujjat bo‘la olishi uqtiriladi. Sura mushriklarning jonsiz butlarga sig‘inishlarini keskin qoralash bilan nihoyalanadi. Bu sura Alloh taoloning go‘zal ismlaridan biri bo‘lmish «Fotir» — «Ilk Yaratguvchi» nomi bilan atalgandir. Mehribon va rahmli Alloh nomi bilan (boshlayman). 1. Hamdu-sano osmonlar va yerni ilk yaratguvchi hamda (O’zi bilan bandalari o‘rtasida) farishtalarni ikki, uch, to‘rt qanotli elchilar (vositachilar) qilguvchi Alloh uchundir. U zot (yaratgan) mahluqotida O’zi xohlagan narsani ziyoda qilur. Albatta Alloh barcha narsaga qodirdir. 2. Alloh odamlar uchun ne bir rahmat-marhamatni ochib qo‘ysa, bas uni ushlab-to‘sib qolguvchi bo‘lmas va neni ushlab qolsa, bas U zot (ushlab qolgani)dan so‘ng u (narsani bandalarga) biron yuborguvchi bo‘lmas. U qudrat va hikmat egasidir. 3. Ey insonlar, sizlarga Alloh ato etgan son-sanoqsiz ne’matni eslangiz! Sizlarga osmonu zamindan rizqu-ro‘z beradigan Allohdan o‘zga bironta yaratguvchi bormi?! Hech bir iloh yo‘q, magar Uning O’zigina bordir. Bas, qayoqqa burilib ketmoqdasizlar?! 4. (Ey Muhammad), agar (mushriklar) sizni yolg‘onchi qilsalar, bas (bilingki), sizdan avvalgi payg‘ambarlar ham yolg‘onchi qilingandirlar. (Barcha) ishlar yolg‘iz Allohga qaytarilur. 5. Ey insonlar, albatta Allohning (qayta tiriltirish va bu dunyoda qilib o‘tilgan yaxshi-yomon amallarning mukofot jazosini berish to‘g‘risidagi) va’dasi haq (va’dadir). Bas, hargiz sizlarni hayoti dunyo aldab qo‘ymasin! Va hargiz sizlarni Alloh (barcha gunoxlarni kechib yuboraveradi, deb) aldaguvchi (shayton) aldab qo‘ymasin! 6. Aniqki, shayton sizlarga dushmandir, bas uni dushman tutinglar! Shak shubhasiz u, o‘z firqasini (ya’ni o‘ziga ergashgan kimsalarni) do‘zax egalari bo‘lishlari uchun da’vat qilur. 7. Kofir bo‘lgan kimsalar uchun qattiq azob bordir. Iymon keltirgan va yaxshi amallar qilgan zotlar uchun esa mag‘firat va ulug‘ mukofot bordir. 8. Axir (qilgan) yomon amali o‘ziga chiroyli ko‘rinib, uni go‘zal (amal) deb o‘ylagan kimsa (Alloh haq yo‘lga hidoyat qilgan zot kabi bo‘lurmi)?! Zotan Alloh O’zi xohlagan kimsalarni yo‘ldan ozdirur va O’zi xohlagan kishilarni hidoyat qilur. Bas (Ey Muhammad), joningiz ularning (iymon keltirmaganlari) ustida hasrat-nadomatlar chekib ketmasin. Albatta Alloh ularning qilayotgan hunarlarini bilguvchidir. 9. Allohning O’zi shamollarni yubordi. Bas ular bulutni qo‘zg‘atgach, Biz uni o‘lik shaharga haydab, uning yordamida o‘lgan yerni tiriltirdik. (Qiyomat qoyim bo‘lgan kuni) qayta tirilish ham shuning o‘zidir. 10. Kim kuch-qudratni istaydigan bo‘lsa, bas barcha kuch-qudrat Allohnikidir. (Har bir) xush so‘z Unga yuksalur va yaxshi amalni ham (Alloh O’z dargohiga) ko‘tarur. Yomon makr-hiylalar qiladigan kimsalar uchun esa qattiq azob bordir va ularning makrlari ham halok bo‘lur (ya’ni behuda ketur). 11. Alloh sizlarni (avval) tuproqdan, so‘ngra nutfadan yaratib, keyin sizlarni juft-juft (ya’ni erkak-ayol) qilib qo‘ydi. Har bir ayolning homilador bo‘lishi ham, ko‘zi yorishi ham shak-shubhasiz Uning bilishi – ogohligi bilan bo‘lur. Har bir umr ko‘rguvchining umri uzun qilinmas va (yo) umridan kamaytirilmas, magar (bularning barchasi) Kitobda (ya’ni Lavhul-Mahfuzda bitilgan bo‘lur). Albatta bu Allohga osondir. 12. Daryo-dengiz teng bo‘lmas — bunisi shirin-totli va ichilishi oson, bunisi esa sho‘r-taxirdir. Sizlar (ularning) har biridan yangi go‘sht (ya’ni baliq tutib) yeysizlar va taqadigan zeb-ziynat chiqarib olursizlar. Va sizlar (Allohning) fazlu-marhamatidan (ya’ni rizqu-ro‘zidan) istashlaringiz uchun (dengiz va daryolarda suvni) yorib ketayotgan kemalarni ko‘rursizlar. Shoyad shukr qilsangizlar. 13. (Alloh) kechani kunduzga kiritur va kunduzni kechaga kiritur, U quyosh va oyni ham (sizlarning manfaatingiz uchun) bo‘yinsundirib qo‘ygandir – har biri muayyan muddatgacha (ya’ni qiyomat kunigacha o‘z fazosida) joriy bo‘lur. Ana shu Alloh sizlarning Parvardigoringizdirki, (barcha olamlarga) podshohlik yolg‘iz Unikidir. (Ey mushriklar), sizlar U zotni qo‘yib iltijo qilayotgan butlaringiz esa po‘stloqcha narsaga ham ega emasdirlar. 14. Agar sizlar ularni chorlasangizlar, duolaringizni eshitmaslar. Agar eshitsalar-da, sizlarga javob qila olmaslar va qiyomat kunida ularni (Allohga) sherik qilib olganlaringizni inkor qilurlar. (Ey Muhammad, dunyo-yu, oxirat haqida hech kim) sizga xabardor zot (ya’ni Alloh) kabi xabar bera olmas. 15. Ey insonlar, sizlar Allohga muhtojdirsizlar. Allohning O’zigina (barcha odamlardan) behojat va (barcha) maqtovga loyiq zotdir. 16. Agar U xoxlasa sizlarni (er yuzidan) ketkazib, (o‘rningizga) yangi bir xalqni keltirur. 17. Va bu (ish) Allohga qiyin emasdir. 18. (Qiyomat kunida) hech bir ko‘targuvchi (ya’ni gunohkor jon) o‘zga jonning yukini (ya’ni gunohini) ko‘tarmas, Agar og‘ir gunoh egasi bo‘lgan jon (birovni) o‘z yuki-gunohiga (ya’ni gunohining bir qismini ko‘tarishga) chorlasa, (garchi chorlanguvchi) yaqin qarindoshi bo‘lsa-da, u (gunohdan) biron narsa ko‘tarilmas (ya’ni u kunda har kim o‘z amali bilan mashg‘ul bo‘lib, ota bolaga, aka ukaga qarashga imkon topmas). (Ey Muhammad), siz faqat g‘aybdagi (ya’ni ko‘zlariga ko‘rinmaydigan) Parvardigordan qo‘rqadigan va namozni to‘kis ado etgan zotlarnigina ogohlantira olursiz. Kim pokdoman bo‘lsa, u faqat o‘z (foydasi) uchun pokdoman bo‘lur. Yolg‘iz Allohgagina qaytilur. 19-20-21. Ko‘r kimsa (kofir) bilan ko‘rguvchi zot (mo‘min), zulmatlar (kufr) bilan nur (iymon), soya (jannat) bilan jazirama (do‘zax) barobar emasdir. 22. Tiriklar (mo‘minlar) bilan — o‘liklar (kofirlar) ham barobar emasdir. Albatta Alloh O’zi xohlagan kishilarga (xaq da’vatni) eshittirur. (Ey Muhammad), siz qabrlardagi kimsalarga (ya’ni o‘lik dillariga) eshittira olguvchi emasdirsiz. 23. Siz faqat ogoxlantirguvchidirsiz. 24. Albatta Biz sizni haq (din) bilan, xushxabar eltguvchi va ogohlantirguvchi qilib yubordik. (Sizning ummatingizdan avvalgi) har bir ummat ichida ham albatta bir ogoxlantirguvchi — payg‘ambar o‘tgandir. 25. Agar (mushriklar) sizni yolg‘onchi qilsalar, bas (bilingki), ulardan avvalgi kimsalar ham (o‘zlariga kelgan payg‘ambarlarni) yolg‘onchi qilgandilar. Holbuki payg‘ambarlari ularga aniq-ravshan mo‘‘jizalar, (ilohiy) sahifalar va (Tavrot, Injil kabi) nurli Kitob keltirgan edilar. 26. So‘ngra kofir bo‘lgan kimsalarni (kufrlari sababli) ushladim – jazoladim. Bas Mening inkorim – azobim qandoq bo‘ddi?! 27. Alloh osmondan suv (yomg‘ir-qor) yog‘dirib, uning yordamida rangu ro‘ylari turli-tuman bo‘lgan mevalarni chiqarganimizni ko‘rmadingizmi?! Yana tog‘lardan ham oq, qizil — rango-rang yo‘l(li tog‘lar) ham, tim qora (tog‘lar) ham bordir. 28. Shuningdek odamlar, jonivorlar va chorva hayvonlari orasida ham rang-baranglari bordir. Allohdan bandalari orasidagi olim-bilimdonlargina qo‘rqur. Shak-shubhasiz Alloh qudratli, mag‘firatlidir. I z o h . Bu ikki oyatda olamdagi barcha mavjudotning yaratguvchisi yolg‘iz Alloh taolo ekanligi ta’kidlanmoqda. Darhaqiqat ilm-ma’rifat egasi bo‘lgan har bir inson osmondan yog‘ilgan bir xil rangdagi suv sababli qora yerdan unib chiqadigan rangu ro‘yi turli tuman bo‘lgan nabotot olamiga, usti ko‘rinishi ham, ostida yashirgan xazina-dafinalari ham rango rang tog‘u-toshlarga – jamodot olamiga va zaminning ostu-ustida tarqalib, o‘zlariga yuklangan vazifalarni bosh tortmasdan bajarib yurgan hayvonot olamining rang-barangligiga va nihoyat mana shu barcha mavjudotdan foydalanib, ularni boshqarishni o‘z zimmasiga olgan insonlarning rangu ro‘ylari ham, fe’li atvor va udum an’analari ham necha turfa ekanligiga tafakkur va ibrat nazari bilan boqsa, Yaratganning qudratu-xunarmandchiligiga tasanno aytmasdan qolmas. Shuning uchun ham mazkur oyatda Allohdan faqat haqiqiy ilm-ma’rifat egalari qo‘rqishlari uqtirib o‘tildi. 29-30. Albatta Allohning Kitobini tilovat qiladigan, namozni to‘kis ado etadigan va Biz ularga rizq qilib bergan narsalardan maxfiy va oshkora infoq-ehson qiladigan zotlar hargiz kasod bo‘lmaydigan oldi-sotdidan (ya’ni ulardan yaxshi amal va infoq-ehson Allohdan ajru-mukofot bo‘lishidan) umidvordirlar, zero (Alloh) ularning ajrlarini komil qilib berur va O’z fazlu-karamidan ularga yana ziyoda (mukofotlar) ham berur. Albatta U mag‘firatli va o‘ta shukr qilguvchidir (ya’ni ozgina yaxshi amal uchun ko‘p mukofot ato qilguvchidir). 31. (Ey Muhammad), Biz sizga vahiy qilgan Kitob – Qur’on o‘zidan avvalgi ilohiy kitoblarni tasdiqlaguvchi bo‘lgan Haq (Kitobdir). Albatta Alloh O’z bandalaridan ogoh va (ularning barcha ishlarini) ko‘rib turguvchidir. 32. So‘ngra Biz bu Kitobga bandalarimizdan O’zimiz tanlagan zotlarni (ya’ni sizning ummatingizni) voris qildik. Bas ularning orasida (Qur’onni o‘qisa-da, unga amal qilmaydigan) o‘z joniga jabr qilguvchi ham bor, ularning orasida o‘rtacha amal qilguvchi ham bor va ularning orasida Allohning iznu irodasi bilan mudom yaxshiliklarga shoshilguvchi ham bordir. Ana o‘sha (ya’ni Qur’onga voris bo‘lish Allohning) katta marhamatidir. 33. Ular oltindan bo‘lgan bilakuzuklar va marvarid-marjonlar bilan bezangan hollarida mangu (turadigan) jannatlarga kirurlar. U joyda ularning liboslari harir-ipak bo‘lur. 34. Va ular (jannatga kirgan chog‘larida) dedilar: «Bizlardan g‘am-qayguni ketkazgan zot — Allohga hamdu-sano bo‘lsin. Darhaqiqat Parvardigorimiz mag‘firatli va o‘ta shukr qilguvchidir. 35. U O’z fazlu-marhamati bilan bizlarni mangu turadigan bir diyorga tushirdiki, bu joyda bizlarga na mashaqqat yetar va na charchoq yetar». 36. Kofir bo‘lgan kimsalar uchun esa jahannam o‘ti bordirki, na ularga (ikkinchi bor o‘lish) hukm qilinib, o‘la olurlar va na ulardan (jahannam) azobi yengillatilur. Biz har bir kofirni mana shunday jazolarmiz. 37. Ular u joyda: «Parvardigoro, bizlarni (bu azobdan) chiqargin, bizlar qilib o‘tgan amallarimizdan boshqa yaxshi (amallarni) qilurmiz», deb dod-voy qilurlar. Axir Biz sizlarga eslatma oladigan kishi eslatma olgudek uzun umr bermaganmidik?! Sizlarga ogohlantirgurchi (payg‘ambar) ham kelgan edi-ku! Bas endi azoblaringizni totaveringlar! Endi zolim kimsalar uchun biron yordamchi bo‘lmas! 38. Albatta Alloh osmonlar va yerning g‘aybini (sirru asrorini) bilguvchidir. Albatta U dillardagi sirlarni ham aniq bilguvchidir. 39. U sizlarni yer yuzida xalifa qilib qo‘ygan zotdir. Bas kim kofir bo‘lsa, uning kufri faqat o‘zining ziyoniga bo‘lur. Kofir bo‘lgan kimsalarga kufrlari Parvardigor huzurida faqat g‘azabnigina ziyoda qilur. Kofir bo‘lgan kimsalarga kufrlari faqat isyonkorliknigina ziyoda qilur. 40. (Ey Muhammad, mushrmilarga) ayting: «Xabar beringiz-chi, sizlar Allohni qo‘yib iltijo qilayotgan butlaringiz (nimaning sharofati bilan iltijo-ibodat qilinishga sazovor bo‘ldilar?) Sizlar menga ko‘rsatma beringiz-chi, ular yerdagi biron narsani yaratganmilar, yoki ularning osmonlarni (yaratishda Allohga) sherikliklari bormi, yoxud Biz ularga biron kitob ato etdikmi-ki, ular o‘sha (kitobdan o‘zlarining Bizga sherik ekanliklari haqida) biron hujjat ustida bo‘lsalar?! Yo‘q, u zolim kimsalar bir-birlariga («Butlarimiz bizlarni shafoat qiladilar», deb) faqat aldovni va’da qilurlar. 41. Albatta Alloh osmonlar va yerni qulab tushishdan ushlab-asrab turur. Aniqki agar ular qulasalar, U zotdan so‘ng (ya’ni Allohdan o‘zga) biron kimsa ularni tutib tura olmas. Darhaqiqat U halim va mag‘firatli bo‘lgan zotdir. 42. (Makka kofirlari) agar ularga biron ogohlantirguvchi (payg‘ambar) kelsa, albatta har qanday ummatlardan ham hidoyat topguvchiroq bo‘lishlari haqida jon-jahdlari bilan qasam ichgandilar. Bas qachonki ularga ogohlantirguvchi (Muhammad alayhis-salom) kelgach, (bu) ularni yanada (hidoyatdan) uzoqlashtirdi xolos. 43. Ular yerda mutakabbirlik qilgan va (payg‘ambarga qarshi) yomon makr hiyla qilgan hollarida (hidoyatdan uzoqlashdilar). Yomon makr-hiyla esa faqat o‘z egalarini o‘rab halok qilur. Bas ular faqat avvalgilarning sunnatlariga (ya’ni ko‘rguliklariga) ko‘z tutmoqdalar, xolos (ya’ni ularning ham boshlariga avvalgi dinsizlarning kuni tushar). Bas siz hargiz Alloh sunnati-qonunining o‘zgarganini ko‘rmassiz va hargiz Alloh sunnatining aylanganini (ya’ni azobga mustahiq bo‘lgan kimsalar qolib, o‘zgalar azoblanganini) ko‘rmassiz. 44. Axir ular yer yuzida sayr qilib o‘zlaridan avvalgi (dinsiz kimsalarning) oqibatiqanday bo‘lganini ko‘rmaydilarmi?! Holbuki (avvalgilar) bulardan ko‘ra kuchli-quvvatliroq edilar. Na osmonlardagi va na yerdagi biron narsa Allohdan qochib qutulguvchi emasdir. Zotan U bilim va qudrat egasi bo‘lgan zotdir. 45. Agar Alloh odamlarni ular qilgan gunohlari bilan jazolasa edi, (er) ustida biron jonivorni qo‘ymagan bo‘lur edi. Lekin U zot ularni (jazolashni) belgilagan muddatgacha (ya’ni qiyomat kunigacha) qoldirur. Bas qachon o‘sha muddat kelgach (ularning har biriga qilib o‘tgan barcha yaxshi-yomon amallarining mukofot-jazolarini berur). Zero Alloh bandalarini ko‘rib turguvchi bo‘lgan zotdir.")