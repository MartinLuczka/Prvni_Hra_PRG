# Import knihoven.

import random

# Představení hlavní postavy, světa, děje.

print("Vítejte ve hře Zaklínač: První stezka")
print(" ")
jmeno = str(input("Jak se bude jmenovat Vaše postava?\n"))
print("...")
print("Po konjukci sfér, která se udála asi 1500 let před tím, než začíná tvůj příběh, se ve světě začali objevovat různé nestvůry a nelidé.")
print(" ")
print("Častou kořistí těchto nestvůr se začali stávat lidé, kteří o těchto stvoření většinou věděli jen velmi málo, často jen z různých drbů a báchorek starých lidí.")
print(" ")
print("Právě z tohoto důvodu vznikli tzv. zaklínači, kteří měli lidi těchto nestvůr zbavovat za mrzký peníz.")
print(" ")
print("Služby zaklínače nikdy nebyly levné, na zaplacení zaklínače se většinou skládaly celé rodiny, dokonce i celé vesnice.")
print(" ")
print("Zaklínači se na zimu vydávali do své pevnosti v Kear Morhen, kde přečkávali zimu. Tento čas využívali k vytváření nových letvarů, doplňování zásob, opravování svého vybavení, regeneraci.")
print(" ")
print("Tvůj příběh začíná právě po konci takovéto zimy, odpočinku bylo dost, je zase na čase vyrazit na stezku.")
print(" ")
print(f"Tvé jméno je {jmeno}, jsi poměrně mladý zaklínač. Pár zim jsi na Kear Morhen už strávil, ale poté jsi na stezku vyrazil se svým mentorem Vesemirem.")
print(" ")
print("Tohle je tvá první stezka, na které jsi odvázán pouze sám na sebe, na své reflexy, dovednosti, znalosti.")
print(" ")
print("Po řece Toulava jsi se dostal k vesnici, o které ti říkal tvůj pochybný převozník. V takovéto vesnici by se pro tebe mohla najít nějaká práce, rozhodneš se ji tedy navštit.")
print(" ")
print("Zde někde začíná tvůj příběh...")
print(" ")

# Základní definování předmětů

oreny = 10
stribrny_mec = False
vlastovka = False

# interakce s převozníkem.

print("Převozník tě vysadil u místího břehu. Břeh nebyl moc udržovaný, pravděpodobně zde často z vody vylézají různí utopenci, kteří zde mají na svědomí nejeden život.")
print(" ")

prevoznik = int(input("Máš poslední šanci se převozníka na něco zeptat, co uděláš? \n 1) Převozník je pravděpodobně jen další ožrala, který nic neví, nebudeš s ním ztácet čas.\n 2) Takový převozník potkává hodně lidí, možná něco bude vědět.\n"))
print(" ")

if prevoznik == 1:
    print("Převozníka si nechal převozníkem a od břehu se dostáváš k rozcestí s rozcestníkem, který by ti mohl pomoct s orientací.")
    print(" ")

elif prevoznik == 2:
    print("K převozníkovi uděláš pár kroků a zeptáš se ho, jestli neví o nějaké práci pro zaklínače. Ten si tě změří pohledem a povídá: „Něco bych možná věděl, ale zrovna mi vyschlo v krku, možná by to spravilo pár orénů.“")
    print(" ")
    print("Peněz moc nemáš, po prohrabání kapes dáš dohromady 10 orénů, tento vydřiduch jich bude chtít aspoň 5.")
    print(" ")
    penize_prevoznikovi = int(input("Co uděláš? \n 1) Co by ti tak tento pobuda řekl? Peníze si raději necháš pro nějaké důležitější záležitosti.\n 2) Peněz moc nemáš, ale informace se ti budou hodit, nevrle převozníkovi předáš peníze a nastražíš ucho.\n"))
    print(" ")

    if penize_prevoznikovi == 1:
        print("Na převozníka si se vykašlal, beztak nic nevěděl a jen se z tebe snažil dostat peníze. Po této zajímavé zkušenosti o lidské chamtivosti si to šineš k rozcestníku, který ti může pomoct najít další cestu.")
        print(" ")

     # Linie, ve které hráč převozníkovi věří, nebo ne.
    
    elif penize_prevoznikovi == 2:
        oreny -= 5
        print("Převozník se usměje a povídá: „Něco bych věděl. Po pár minutách chůze tímto směrem se dostaneš k místní zřícenině.“")
        print(" ")
        print("„V této zřícenině se prý nachází poklad, ale nikdo se tam neodváží. Podle místních báchorek tam prý řádí striga.“")
        print(" ")
        print("„To je Vám opravdu děsivá nestvůra pane zaklínači, velká jako medvěd, ale pařáty a čelist ještě apspoň dvakrát horší.“")
        print(" ")
        print("„Prej tam došlo k nějakýmu prokletí dcerušky původního majitele, ale do toho se já nechci pouštět, bolí mě z toho huba o tom mluvit.“")
        print(" ")
        print("„Ale takovej nebojácnej vědmák jako vy by si s tím mohl poradit, co vy na to?“")
        print(" ")

        poklad = int(input("Co uděláš? \n 1) Poklad by se ti mohl hodit, stačí si jen poradit s nestvůrou a může být o zlato postaráno na celou další zimu.\n 2) Převozníkovi nevěříš ani slovo, bez tak je to nějaká léčka. Život máš přeci jen jeden.\n"))
        print(" ")

        if poklad == 1:
            print("Došel si k místní zřícenině, ale žádný křik neslyšíš. Ani tvůj medailon se netřese. To by byla známka přítomnosti magické bytosti.")
            print(" ")
            print("Vidíš krásně velkou truhlici za vchodem do zříceniny.")
            print(" ")
            print("Pomalými kroky k ní přistupuješ, ale nic se neděje. Až když si konečně u ní, tak se zklidníš a truhlu pomalu otevíráš.")
            print(" ")
            print("Najednou uslyšíš hlasitě někoho zvolat: „TEĎ!“")
            print(" ")
            print("Z vrchu najednou začne padat balvan velký jako hrom. I přes své rychlé reflexy se nedokážeš včas skutálet na místo, kde by balvan nedopadl. Je ihned po tobě.")
            print(" ")
            print("Lidé, kteří tento balvan pustili, byli převozníkovi kumpáni, kteří si s ním teď rozdělí tvé peníze. Tvoji zbroj a meč, který si také samozřejmě vezmou a rozprodají.")
            print("...")
            print("KONEC HRY")
            print(" ")
            print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
            quit()

        elif poklad == 2:
            print("Tak tohle ti za to úsilí fakt nestojí. Bůhví o čem ten převozník povídá. Nemáš čas se zaobírat místními pověrami. Radši si jdeš obstarat pořádnou zaklínačskou zakázku.")
            print(" ")
            print("Poté si chvíli šel jiným směrem, než ti nabízel převozník a dostal si se k rozcestníku.")
            print(" ")

        else:
            print("Taková možnost nebyla, zkus to ještě jednou.")
            print(" ")
            quit()

    else:
        print("Taková možnost nebyla, zkus to ještě jednou.")
        print(" ")
        quit()

else:
    print("Taková možnost nebyla, zkus to ještě jednou.")
    print(" ")
    quit()


print("Rozcestník je starý a už poměrně dost ztrouchnivělý. Z vybledlé barvy se ti ale podaří přečíst jednotlivé lokality.")
print(" ")
print("Do leva by si se dostal do lesa, to bylo dobře čitelné.")
print(" ")
print("Pro cestu rovně přečteš nápis: VE NICE, to bude asi vesnice.")
print(" ")
print("Nápis pro cestu do prava je hodně špatně čitelný, přešteš: AMENOOM, to jsi nejsi jistý, co by mohlo být.")
print(" ")

# Linie, kde hráč neví, co ho kde čeká a po rozhodnutí se rozdělí na 3 další linie.

rozcesti = int(input("Co uděláš? \n 1) Půjdeš do leva do lesa, tam by se mohlo skrývat něco zajímavého. \n 2) Půjdeš rovně do vesnice, možná se něco zajímavého dozvíš od místních lidí. \n 3) Půjdeš do neznámé lokality, máš pro strach uděláno.\n"))
print(" ")

if rozcesti == 1:
    print("Po nějaké době se dostaneš na kraj lesa. Les je pořádně zarostlý, nikde žádná mýtina.")
    print(" ")
    print("Slunce již není tak vysoko, takže se začíná pomalu stmívat, to ti na odvaze moc nepřidává.")
    print(" ")
    print("Vstoupíš do lesa a slyšíš v dálce první vytí vlků, s těmi by sis poradit měl, máš přece svůj ocelový meč. Spíš ti dělá obavy možná přítomnost lešije nebo nějaké podobné lesní bytosti.")
    print(" ")
    print("Po nějaké době zahlédneš v dáli nějaké světlo")
    print(" ")

    # Možná interakce s hádankářem.

    hadankar = int(input("Co uděláš? \n 1) Světlo je pro tebe dobré znamení, určitě se půjdeš podívat, co ho způsobuje. \n 2) Z toho koukají nějaké nepříjemnosti, budeš pokračovat dál v prozkoumávání.\n"))
    print(" ")

    if hadankar == 1:
        print("Zdrojem světla je lampa, kterou drží jistý muž.")
        print(" ")
        print("Než stačíš promyslet další krok, tak na tebe neznámý muž promluví: „Zdravím cizinče, jsem hádankář. Chodím po tomto širém světě už dost dlouho a lidem pokládám své záludné otázky.“")
        print(" ")
        print("„Pokud budeš schopný na mou otázku odpovědět, tak tě odměna nemine. Pokud neuhádneš, budu muset putovat dále s nadějí, že se jednou někdo hoden mé odměny najde.“")
        print(" ")
        print("„Dobře poslochej, nebudu se opakovat, hádanka zní takto: Rádi mne máte, života by beze mne nebylo. Ale kdo se na mne dívá, vždycky se mračí. Kdo jsem?“")
        print(" ")

        odpoved = str(input("Tvá odpověď:\n").lower())
        print(" ")

        # Zohlednění více možných odpovědí.

        if odpoved == "slunce" or odpoved == "slunko" or odpoved == "sluníčko" or odpoved == "slunicko":
            print("„Správně, velmi dobře. Přece se jen někdo našel. Tady máš za odměnu tento stříbrný meč, je prvotřídní kvality. Nejlepší trpasličí kováři se podíleli na jeho výrobě.“")
            stribrny_mec = True
            print(" ")
            print("Hádankářovi slušně poděkuješ a pokračuješ ve své cestě lesem.")
            print(" ")

        else:
            print("„Bohužel, to není správná odpověď. Nevadí no, snaha byla. Odměna bude se mnou putovat dále.“")
            print(" ")
            print("S hádankářem se rozloušíš a pokračuješ ve svojí cestě lesem.")
            stribrny_mec = False
            print(" ")

    elif hadankar == 2:
        print("Světla si raději nevšímáš a pokračuješ dále svojí cestou lesem.")
        print(" ")

    else:
        print("Taková možnost nebyla, zkus to ještě jednou.")
        print(" ")
        quit()  

    # Interakce s čarodějnicí.

    print("Ani ne za chvíli narazíš na jakousi zvláštní chaloupku. Zvnáší se okolo ní nějaký divný opar.")
    print(" ")
    print("Najednou někdo promluví: „Co tady děláš? Vesničané si tě najali, nemám pravdu?“")
    print(" ")
    print("„Já znám ty jejich příběhy. Ztratí se jim dítě, zemře jim příbůzný, kráva už nedojí tolik jako dříve. Za všechno vždycky může ta zpropadená čarodějnice.“")
    print(" ")
    print("„Nikdo si mě nenajal. Hledám jen nějakou práci pro zaklínače, nevěděla by jsi o něčem?“, odpovíš.")
    print(" ")
    print("Čarodějnice odpoví: „O žádné práci nic nevím, radši se odsud rychle kliď vědmáku, dokud je čas a mám v sobě ještě špetku trpělivosti.“")
    print(" ")

    carodejnice = int(input("Co uděláš? \n 1) Takhle s tebou ta čarodějnice nemůže mluvit, vesničané mají stejně asi pravdu, bude lepší, když to s ní skoncuješ jednou provždy.\n 2) S čarodějnicí si raději nebudeš zahrávat, je to prastará bytost ještě z dob konjukce sfér, bůhví jakou má moc.\n"))
    print(" ")

    if carodejnice == 1:
        if stribrny_mec == True:
            print("Čarodějnice přece s tebou takto nemůže mluvit, dáš jí to dost jasně najevo tím, že začneš tasit svůj stříbrný meč. Čarodejnice je magická bytost, tady se ti kvalitní stříbro bude hodit.")
            print(" ")
            print("Čarodějnice neztrácí čas a ihned se proměnujě do své pravé formy prastarého démona.")
            print(" ")
            print("Teď se ti hodí tvá mladistvá hbitost a také samozřejmě nelehký trénink, kterým sis jako zaklínač musel projít.")
            print(" ")
            print("Vypadá to, že pár rychlých úderů stříbrným mečem ji dává dost zabrat, skvěle použité zaklínačské znamení Yrden ji taky souboj vůbec nezlehčuje.")
            print(" ")
            print("Hbitý výpad na pravou stranu její šíje stačil, aby tento souboj již čarodějnice nerozdýchala. Toto stvoření bojovalo dobře, ale na tebe v tomto souboji nemělo.")
            print(" ")
            print("Při prohledávání její chatrče si narazil na magickou truhlu, která byla uzamčena starodávnou magickou pečetí. Tato pečeť se při poražení čarodějnice prolomila a truhlu otevřela.")
            print(" ")
            print("V truhle si našel mnoho zlata, spoustu starých artefaktů a zaklínačských mutagenů, za které ti různí alchymisté a univeriztní profesoři utrhnou ruce.")
            print("")
            print("Na tuhle zimu máš vystaráno, možná i na další dvě.")
            print("...")
            print("KONEC HRY")
            print(" ")
            print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
            quit()

        elif stribrny_mec == False:
            print("Čarodějnice přece s tebou takto nemůže mluvit, dáš jí to dost jasně najevo tím, že začneš tasit svůj ocelový meč.")
            print(" ")
            print("Čarodějnice neztrácí čas a ihned se proměnujě do své pravé formy prastarého démona.")
            print(" ")
            print("Vypadá to, že údery ocelovým mečem jí nic moc nedělají. Přestože už si rozdal pár slušných ran, čarodějnice bojuje stále jako na začátku souboje.")
            print(" ")
            print("Tobě ale již síly docházejí, zaklínačských znamení si už pár seslal, ale bez pořádného navázání na dobré údery mečem jsou ti k ničemu.")
            print(" ")
            print("Najednou si vzpomeneš na to, co tě učil tvůj mentor Vesemir. Ocelový meč je jen na lidi a zvířata. Na magické bytosti musíš se stříbrem.")
            print(" ")
            print("Tato vzpomínka tě vyvedla z míry a ztratil si rovnováhu při svém výpadu. Čarodějnice už tě má ve svých pařátech. Teď už neunikneš.") 
            print(" ")
            print("Stal jsi se další lebkou zapíchnutou na kůlu u vstupu do chýše čarodějnice.")
            print("...")
            print("KONEC HRY")
            print(" ")
            print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průběhy hrou a konce.")
            quit()

    # Odmítneme interakci s čarodějnicí              

    elif carodejnice == 2:
        po_carodejnici = int(input("Co dál?: \n 1) Vrátíš se k rozcestníku a půjdeš do vesnice. \n 2) Vrátíš se k rozcestníku a půjdeš směrem k neznámé lokaci.\n"))
        print(" ")

        if po_carodejnici == 1:
            print("Dostáváš se do malé vesnice. Tady na této ceduli již tak moc vybledlá barva není, takže bez sebemenších potíží přečteš nápis vesnice: Kamenná Lhota.")
            print(" ")
            print("Při vstupu do vesnice už vidíš, jak se na tebe někteří lidé křivě dívají. Muži si při pohledu na tebe odplivávají. Ženy a děti se tě bojí.")
            print(" ")
            print("Lidé nikdy neměli rádi zaklínače. Proč? Je to jednoduché, protože jsou jiní.")
            print(" ")
            print("Zaklínači musí po absolvování tréninku projít tzv. zkouškou trav. Je to velice nebezpečná procedůra, jen pár mladých chlapců ji přežije.")
            print(" ")
            print("Po ní se zaklínačovi zlepší regenerace, zrak, sluch, vnímání okolí. Je také odolnější vůči jedům a nemocím. Pro lidi po této procedůře už zaklínači nejsou lidé, jsou to pro ně nelidé.")
            print("")
            print("Před hospodou je sice vývěska, ale je prázná a polorozpadlá. To pro zaklínače není nikdy dobré znamení.")
            print("")
            print("Rozhodneš se teda jít do lokální hospody, nad jejími dveřmi je napsáno: U Červené lišky.")
            print(" ")
            print("Při tvém vstupu do hospody se najednou ozve silný šepot, větříš zde problémy.")
            print(" ")
            print("Ještě než se dostaneš k hospodskému, tak si tě odchytí nasvalený rváč, který ti povídá: „Takové jako ty tu nemáme rádi. Vůbec se mi nelíbíš. Jestli tu chceš být ještě o minutu navíc, tak mě musíš porazit.“")
            print(" ")
            print("„Ale jelikož jsem dobrák a štěstěna je moje dobrá kamarádka, tak si o naši rvačku hodíme mincí. Pokud padne orel, tak tě nechám být. Pokud ovšem padne panna, tak si to spolu vyříkáme jako chlap s chlapem.“")
            print(" ")

            # náhodné vylosování hodu mincí.

            strany = ["Orel", "Panna"]

            vysledek = random.choices(strany, weights = [1, 2]) # Panna má větší váhu, protože rváč říká, že štěstěna je jeho dobrá kamarádka :)

            print(f"{vysledek}")
            print(" ")

            if vysledek == ['Orel']:
                print("Usmálo se na tebe štěstí.")
                print(" ")
                print("Rváč povídá: „Kurňa chlape, ty máš ale štěstí. No nic, štěstěna byla dnes na tvé straně, holka jedna paličatá.“")
                print(" ")

            elif vysledek == ['Panna']:
                print("Teď si neměl moc velké štěstí")
                print(" ")
                print("Rváč povídá: „Říkal jsem ti, že je štěstěna moje kamarádka. Teď si to budeme muset rozdat pěkně po staru, nebo máš snad lepší nápad?“")
                print(" ")

                rvac = int(input("Co uděláš? \n 1) Takového tlučhubu si namažeš na chleba, dyť jsi přece zaklínač.\n 2) Takové problémy ti nestojí za to, nabídneš mu své peníze a budeš doufat, že je přijme.\n"))
                print(" ")

                if rvac == 1:
                    print("„Když se chceš prát, tak se jdeme prát. Neboj se, nebudu tě šetřit.“, říká chraplavým hlasem rváč.")
                    print(" ")
                    print("Zjišťuješ, že to nebude tak jednoduché, rváč zatím každou tvoji ránu vykryl, ale ty si jich už pár schytal.")
                    print(" ")
                    print("Pěstní souboje nejsou tvá silná stránka, nejsi žádný Geralt z Rivie. Rváč má jasnou převahu.")
                    print(" ")
                    print("Po slušném začátku si v průběhu boje dost upadl a rváč tě zmlátil jako psa.")
                    print(" ")
                    print("Po neúspěšném boji zůstáváš ležet na zemi, tohle už asi nerozdejcháš kamaráde. Na následky zranění pomalu umíráš...")
                    print(" ")
                    print("Říká se, že žádný zaklínač neumírá v posteli, ale tohle je poměrně ubohý konec, nemyslíš?.")
                    print("...")
                    print("KONEC HRY")
                    print(" ")
                    print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                    quit()

                # Teď záleží na tom, jestli hráč dal převozníkovi peníze.

                elif rvac == 2:
                    print("Předáváš rváčovi své peníze a doufáš, že částka bude stačit.")
                    print(" ")

                    if oreny == 10:
                        print("Rváč se na tebe pousměje a povídá: „Když si neměl štěstí v hodu mincí, tak máš štěstí aspoň v tom, že s sebou nosíš dostatečný obnos peněz, 10 orénů mi protentokrát bude stačit.“")
                        print(" ")
                        oreny -= 10

                    elif oreny == 5:
                        print("Rváč se na tebe zamračí a povídá: „To si snad děláš srandu, 5 orénů?, na takovou vindru mě chceš ukecat? Já z tebe tu kuráž vymlátím!“")
                        print(" ")
                        print("„Když nemáš peníze, tak doufej, že aspoň dobře bojuješ.“, říká chraplavým hlasem rváč.")
                        print(" ")
                        print("Rváč zatím každou tvoji ránu vykryl, ale ty si jich už pár schytal.")
                        print(" ")
                        print("Pěstní souboje nejsou tvá silná stránka, nejsi žádný Geralt z Rivie. Rváč má jasnou převahu.")
                        print(" ")
                        print("Po slušném začátku si v průběhu boje dost upadl a rváč tě zmlátil jako psa.")
                        print(" ")
                        print("Po neúspěšném boji zůstáváš ležet na zemi, tohle už asi nerozdejcháš kamaráde. Na následky zranění pomalu umíráš...")
                        print(" ")
                        print("Říká se, že žádný zaklínač neumírá v posteli, ale tohle je poměrně ubohý konec, nemyslíš?")
                        print("...")
                        print("KONEC HRY")
                        print(" ")
                        print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                        quit()

                else:
                    print("Taková možnost nebyla, zkus to ještě jednou.")
                    print(" ")
                    quit()   

            # Budeme pokračovat dále v příběhu okolo hospodského.

            print("Krizi s rváčem si nějak zažehnal a konečně si můžeš promluvit s hospodským, který snad bude o něčem vědět.")
            print(" ")
            print("Přijdeš k hospodskému a povídáš: „Nenašla by se tu nějaká práce pro zaklínače?“")
            print(" ")
            print("Hospodský se na tebe podívá ostrým pohledem a rázným hlasem zakřičí: „Nenašla, ještě jeden takový provokativní kec a pošlu na tebe místní chlapy.“")
            print(" ")
            print("Po pár sekundové odmlce se k tobě hospodský nakloní a nenápadným šepotom ti říká: „Tohle je poměrně klidná věsnice pane zaklínači, ale poslední dobou tu máme takový problém.“")
            print(" ")
            print("Hospodský pokračuje: „Víte, poslední dobou nás tu drží zkrátka místní gang. Problémy s nimi byli již předtím, ale poslední dobou si začali vyskakovat.“")
            print(" ")
            print("„Dnes se člověk musí mít pořád na pozoru. Mlynář Pešek si pod vlivem minulý týden pustil hubu na špacír a dnes nemá kde bydlet. Barák mu do základů vypálali a zvířata do jednoho potratili.“")
            print(" ")
            print("„My bychom se jich potřebovali zbavit. Berou si, co si zachtějí. Občas chodí po domech a vybírají peníze, kdo nedá, tězce zaplatí. Dokonce i znásilňují naše děvčata, hotové neštěstí.“")
            print(" ")
            print("„My bychom s tím už dávno něco udělali, ale místní chlapy se bojí o své rodiny. To není jen tak. Každý si radši hledí svého.“")
            print(" ")
            print("„Lidi z vesnice dali dohromady slušnou sumu pro někoho, jako jste vy. Celých 300 orenů! Co vy na to, pomůžete nám?“")
            print(" ")

            # Hráč se buď rozhodne pomoct místním vesničanům, nebo zhodnotí situaci jako příliš riskantní a odejde jinam.

            gang = int(input("Co uděláš? \n 1) Tolik peněz si rozhodně nenecháš ujít. Pomůžeš tím i sužovaným vesničanům. \n 2) S gangem nájemných vrahů si nebudeš nic začínat, peníze si zkusíš obstarat jinde.\n"))
            print(" ")

            if gang == 1:
                print("Souhlasně kývneš hlavou, aby si dal hospodskému vědět, že jeho zakázku přijímáš. Ten ti zatím dal jen symbolických 5 orénů, které uzavírají smlouvu.")
                oreny += 5
                print(" ")
                print("Ještě než odejdeš dveřmi krčmářskými, tak tě zastaví jakási stařena, představí se ti jako zdejší léčitelka a mastičkářka.")
                print(" ")
                print("„Dobrý pane, nechtěl byste si ode mne lektvar koupiti. Přesněji elixír, abych byla přesná, je znám pod jménem vlaštovka.“, povídá.")
                print(" ")
                print("„Při boji urychlí regeneraci vašeho systému, budete rychlejší a vytrvalejší. Co vy na to? Chci za něj jen hubičku, 10 orénů přesně.“")
                print(" ")
                elixir = int(input("Chceš si od léčitelky koupit elixír vlaštovka? \n 1) Chceš, takovýto elixír se ti před bojem může hodit. \n 2) Necheš, jsou to pro tebe zbytečné vyhozené peníze, s takovými bandity si poradíš raz dva.\n"))
                print(" ")
                
                # Hráč si elixír buď koupí a proti násilníkům vyhraje, nebo si ho nekoupí a setkání s badnou hrdlořezů nepřežije.

                if oreny >= 10 and elixir == 1:
                    print("Elixír sis koupil, souboj by pro tebe teď neměl být problém.")
                    print(" ")
                    vlastovka = True
                    oreny -= 10

                elif oreny < 10 and elixir == 1:
                    print("Elixír chtít můžeš, ale pokut nemáš 10 orénů, tak ti ho léčitelka neprodá. Smůla!")
                    print(" ")

                elif elixir == 2:
                    print("Elixír nepotřebuješ, na bandu podvraťáků se cítíš být dostatečně silný.")
                    print(" ")

                if vlastovka == True:
                    print("Od místních před hospodou ses dozvěděl, že gang má tábor ve staré stodole na kraji vesnice, takže se tam jdeš podívat.")
                    print(" ")
                    print("Stojíš před branami staré stodoly, ze vnitř slyšíš smích a hodování.")
                    print(" ")
                    print("Než začne tvůj smrtelný tanec, tak ještě požiješ vlaštovku od místní léčitelky, účinný to elixír.")
                    print(" ")
                    print("Elixír okamžitě působí na tvůj metabolizmus, všude po těle se ti rozšířili žíly a srdce ti začalo tloust jako o život.")
                    print(" ")
                    print("Když otevřeš dveře od stodoly, tak banda zrovna zneužívá jedno z místních děvčat.")
                    print(" ")
                    print("Takhle to rozhodně nenecháš být a rychle tasíš svůj ocelový meč.")
                    print(" ")
                    print("Ze všech stran na tebe naběhnou hrdlořezové, ale ty zůstáváš v klidu.")
                    print(" ")
                    print("S klidem odrazíš prvního útočníka, kterému v mžiku sekundy rozřízneš hrdlo, dalšího útočníka následuje podobný osud.")
                    print(" ")
                    print("Od této chvíle předvádíš jednu parádu za druhou, skupinový styl boje ti jde.")
                    print(" ")
                    print("V bojové vřavě si ale nevšimneš seknutí nepřátelského meče směrem k tobě, máš řeznou ránu přes celá záda, ale přes vliv vlaštovky skoro nic necítíš.")
                    print(" ")
                    print("Rána se ti hned uzavírá a spomalení krvácení následuje.")
                    print(" ")
                    print("Poslední násilníky pošleš na věčnost dvoumi rychlými výpady. Tímto je tvoje zakázka splněna.")
                    print(" ")
                    print("Vystrašené děvče pošleš domů, pohled na mrtvá těla ji ovšem v paměti zůstanou snad nadosmrti.")
                    print(" ")
                    print("Mrtvá těla ještě před stodolou vyskládáš na hromadu a zapálíš pomocí znamení Igni.")
                    print(" ")
                    print("Do hospody si skočíš pro odměnu, které se ti dostane. Měl by si co nejdřív z vesnice odejít, nemá cenu zůstávat zde o minutu navíc. Na nějakou dobu ti tyto peníze určitě vystačí.")
                    print("...")
                    print("KONEC HRY")
                    print(" ")
                    print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                    quit()

                elif vlastovka == False:
                    print("Od místních před hospodou ses dozvěděl, že gang má tábor ve staré stodole na kraji vesnice, takže se tam jdeš podívat.")
                    print(" ")
                    print("Stojíš před branami staré stodoly, ze vnitř slyšíš smích a hodování.")
                    print(" ")
                    print("Není už na co čekat, rázně vyrážíš dveře stodoly znamením Aard.")
                    print(" ")
                    print("Po vyražení dveří se ti naskýtá pohled, jak banda zrovna zneužívá jedno z místních děvčat.")
                    print(" ")
                    print("Takhle to rozhodně nenecháš být a rychle tasíš svůj ocelový meč.")
                    print(" ")
                    print("Ze všech stran na tebe naběhnou hrdlořezové, ale ty zůstáváš v klidu.")
                    print(" ")
                    print("S klidem odrazíš prvního útočníka, kterému v mžiku sekundy rozřízneš hrdlo, dalšího útočníka následuje podobný osud.")
                    print(" ")
                    print("Od této chvíle předvádíš jednu parádu za druhou, skupinový styl boje ti jde.")
                    print(" ")
                    print("V bojové vřavě si ale nevšimneš seknutí nepřátelského meče směrem k tobě, máš řeznou ránu přes celá záda.")
                    print(" ")
                    print("Stodolou se najednou ozve tvůj mrazivý výkřik. Záda ti strašně krvácí a pomalu ztrácíš sílu k boji.")
                    print(" ")
                    print("Jeden z násilníků využije tvého zaváhání a do levého stehna ti zarazí dvoucečnou sekeru.")
                    print(" ")
                    print("To tě už úplně srazí k zemi. Při tom upustíš svůj meč, který se ještě znažíš vzít do rukou, ale jeden z hrdlořezů ho odkopne.")
                    print(" ")
                    print("Už nemůžeš udělat nic, na seslání zaklínačského znamení jsi moc vyčerpaný.")
                    print(" ")
                    print("V téhle pozici už to máš rychle za sebou. Mohl jsi dopadnout hůře, mohl jsi trpět.")
                    print(" ")
                    print("Vesničanům si situaci ještě zhoršil, po tomto incidentu bylo výhružně povražděno několik rodin a podpáleno několik domů.")
                    print("...")
                    print("KONEC HRY")
                    print(" ")
                    print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                    quit()

            elif gang == 2:
                print("To si teda vesničany moc nepotěšil. Byl jsi jejich jediná naděje.")
                print(" ")
                print("Nedá se nic dělat, zaklínač má samozřejmě plné právo zakázku odmítnout.")
                print(" ")
                print("Zprávy o tvém odmítnutí se rychle rozkřiknou. Měl by ses raději na nějakou dobu uklidit někam jinam.")
                print(" ")
                print("Tady už tě nic dobrého nečeká. Budeš muset dále pokračovat na své stezce.")
                print(" ")
                print("Jestli jsi udělal dobře, nebo ne, tak to už se teď nedozvíme...")
                print("...")
                print("KONEC HRY")
                print(" ")
                print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                quit()

            else:
                print("Taková možnost nebyla, zkus to ještě jednou.")
                print(" ")
                quit()

        elif po_carodejnici == 2:
            print("Ocitneš se u místního kamenolomu.")
            print(" ")
            print("Vypadá to, že kamenolom je už hodně dlouho opuštěnný, všude jen samé polorozpadlé chatičky a mnoho použitého nářadí. Toto nářadí už zub času hodně ohlodal.")
            print(" ")
            print("Najednou uslyšíš nějaké hluboké mrčení z jeskynně hned vedle kamenolomu.")
            print(" ")

            #  Hráč se s trollem může či nemusí setkat, je to na něj.

            troll = int(input("Co uděláš? \n 1) Jeskynni půjdeš prozkoumat, nemyslíš si, že v ní bude něco nebezpečného. \n 2) Skřeky z opuštěných míst nikdy nevěstí nic dobrého, raději to tady zabalíš.\n"))
            print(" ")

            if troll == 1:
                print("Čím hlouběji si v jeskynni, tím je skřik hlasitější. V jeskynni to taky pěkně smrdí.")
                print(" ")
                print("Po chvíli si myslíš, že tě snad šálí zrak. Narazil jsi na skalního trolla, ten je v této lokalitě obzvlášť neobvyklý.")
                print(" ")
                print("Právě asi kvůli němu je tu zde tak pusto. Vypadá to, že se místní obyvatelstvo s přítomností trolla smířilo.")
                print(" ")
                print("K trollovi se opatrně přibližuješ, když v tom najednou si tě všimne a povídá:„Ah, člověk. Já rád vidět. Já muset mluvit k ty.“")
                print(" ")
                print("Vypadá to, že troll není nepřátelský, chce ti něco sdělit.")
                print(" ")
                print("„Ty muset přinést stříbrný meč. Můj jedinný naděje. Já dát zlato.“")
                print(" ")
                print("Vypadá to, že troll chce přinést stříbrný meč. Splnění jeho přání odměňuje zlatem.")
                print(" ")

                # Meč může hráč získat jedině od hádankáře, poté musí odmítnout souboj s čarodějnicí, pokud chce získat tento konec.

                if stribrny_mec == True:
                    print("Stříbrný meč náhodou po ruce máš.")
                    print(" ")
                    print("Meč trollovi opatrně podáš.")
                    print(" ")
                    print("Troll meč uchopí a povídá :„Ano, ty zbavit troll trápení. Já děkovat.“")
                    print(" ")
                    print("Troll meč pevně uchytí do nešikovných rukou. Najednou si jím propíchne hruď.")
                    print(" ")
                    print("Než se stačíš vzpamatovat z toho, co si právě viděl, tak se troll postupně promění v normálního chlapce.")
                    print(" ")
                    print("Chlapec po chvíli přichází k sobě a povídá: „Děkuji moc za záchranu člověče. Několik desítek let jsem byl zakletý do podoby tohoto trolla.“")
                    print(" ")
                    print("„Jediné, co mě mohlo zachránit byla magie z dobře ukovaného stříbrného meče.“")
                    print(" ")
                    print("„Pokud by meč nebyl kvalitní mechanicky ani magicky, tak bych zůstal trollem.“")
                    print(" ")
                    print("„Zaklela mě takhle jedna mocná čarodějka, když jsem byl ještě dítě. Teď jsem v podstatě také ještě dítě, vůbec jsem nezestárl...“")
                    print(" ")
                    print("Vzadu v jeskynni se nachází truhlice s pokladem, který jsem našel již dávno. Poklad je nyní tvůj. Pokud by tvůj meč neprolomil kletbu, k pokladu bych tě nepustil.")
                    print(" ")
                    print("Rozsah pokladu tě překvapuje. Tolik zlata jsi ještě pohromadě nikdy neviděl. Takové množství tě zabezpečí aspoň na jednu dekádu. O tomhle až budeš vyprávět v Kear Morhen...")
                    print("...")
                    print("KONEC HRY")
                    print(" ")
                    print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                    quit()

                elif stribrny_mec == False:
                    print("Žádný stříbrný meč u sebe nemáš, to se trollovi nebude líbit.")
                    print(" ")
                    print("Trollovi citlivě naznačíš, že žádný stříbrný meč nemáš.")
                    print(" ")
                    print("Troll se zamračí a povídá: „Ty dělat z trolla sranda. K troll už ty nevracet, jinak troll zabít.“")
                    print(" ")
                    print("Měl bys jít někam jinam. Troll už tě tu nechce vidět. Pokud se tu ukážeš, tak tě zabije.")
                    print(" ")
                    print("Při odchodu z kamenolomu tě ovšem zehlédne místní dívenka, která si za vesnicí hrála s kamarády na schovávanou.")
                    print(" ")
                    print("Řekne o tom doma a vesničané začnou být nedůvěřivý.")
                    print(" ")
                    print("Ve vesnici se o tobě začně říkat, že pro trolla pracuješ, plníš jeho zlá přání. Někdo o tobě také říká, že jsi špinavý měňavec.")
                    print(" ")
                    print("Drby se šíří rychle a lidé si vždy něco vymyslí.")
                    print(" ")
                    print("Lidé se k tobě začnou chovat odtažitě, nebudou s tebou chtít mít nic společného.")
                    print(" ")
                    print("Pověst u lidí je pro zaklínače velmi důležitá. Přece nebudou dávat peníze někomu, komu nevěří.")
                    print(" ")
                    print("Někde mají zaklínače rádi více, někde méně. Zálezí na povaze lidu. Tady jsi svou pověst ztratil.")
                    print("")
                    print("Tady už tě nic dobrého nečeká. Budeš muset dále pokračovat na své stezce. Snad budeš mít jinde více štěstí...")
                    print("...")
                    print("KONEC HRY")
                    print(" ")
                    print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                    quit()

            elif troll == 2:
                print("Z takových neznámých zvuků ti není vůbec dobře, radši jdeš pryč.")
                print(" ")
                print("Při odchodu z kamenolomu tě ovšem zehlédne místní dívenka, která si za vesnicí hrála s kamarády na schovávanou.")
                print(" ")
                print("Řekne o tom doma a vesničané začnou být nedůvěřivý.")
                print(" ")
                print("Ve vesnici se o tobě začně říkat, že pro trolla pracuješ, plníš jeho zlá přání. Někdo o tobě také říká, že jsi špinavý měňavec.")
                print(" ")
                print("Drby se šíří rychle a lidé si vždy něco vymyslí.")
                print(" ")
                print("Lidé se k tobě začnou chovat odtažitě, nebudou s tebou chtít mít nic společného.")
                print(" ")
                print("Zaklínačova pověst u lidí je pro zaklínače velmi důležitá. Přece nebudou dávat peníze někomu, komu nevěří.")
                print(" ")
                print("Někde mají zaklínače rádi více, někde méně. Zálezí na povaze lidu. Tady jsi svou pověst ztratil.")
                print("")
                print("Tady už tě nic dobrého nečeká. Budeš muset dále pokračovat na své stezce. Snad budeš mít jinde více štěstí...")
                print("...")
                print("KONEC HRY")
                print(" ")
                print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                quit()

            else:
                print("Taková možnost nebyla, zkus to ještě jednou.")
                print(" ")
                quit()

        else:
            print("Taková možnost nebyla, zkus to ještě jednou.")
            print(" ")
            quit()

    else:
        print("Taková možnost nebyla, zkus to ještě jednou.")
        print(" ")
        quit()     

# Jdeme do vesnice.

elif rozcesti == 2:
    print("Dostáváš se do malé vesnice. Tady na této ceduli již tak moc vybledlá barva není, takže bez sebemenších potíží přečteš nápis vesnice: Kamenná Lhota.")
    print(" ")
    print("Při vstupu do vesnice už vidíš, jak se na tebe někteří lidé křivě dívají. Muži si při pohledu na tebe odplivávají. Ženy a děti se tě bojí.")
    print(" ")
    print("Lidé nikdy neměli rádi zaklínače. Proč? Je to jednoduché, protože jsou jiní.")
    print(" ")
    print("Zaklínači musí po absolvování tréninku projít tzv. zkouškou trav. Je to velice nebezpečná procedůra, jen pár mladých chlapců ji přežije.")
    print(" ")
    print("Po ní se zaklínačovi zlepší regenerace, zrak, sluch, vnímání okolí. Je také odolnější vůči jedům a nemocím. Pro lidi po této procedůře už zaklínači nejsou lidé, jsou to pro ně nelidé.")
    print("")
    print("Před hospodou je sice vývěska, ale je prázná a polorozpadlá. To pro zaklínače není nikdy dobré znamení.")
    print("")
    print("Rozhodneš se teda jít do lokální hospody, nad jejími dveřmi je napsáno: U Červené lišky.")
    print(" ")
    print("Při tvém vstupu do hospody se najednou ozve silný šepot, větříš zde problémy.")
    print(" ")
    print("Ještě než se dostaneš k hospodskému, tak si tě odchytí nasvalený rváč, který ti povídá: „Takové jako ty tu nemáme rádi. Vůbec se mi nelíbíš. Jestli tu chceš být ještě o minutu navíc, tak mě musíš porazit.“")
    print(" ")
    print("„Ale jelikož jsem dobrák a štěstěna je moje dobrá kamarádka, tak si o naši rvačku hodíme mincí. Pokud padne orel, tak tě nechám být. Pokud ovšem padne panna, tak si to spolu vyříkáme jako chlap s chlapem.“")
    print(" ")

    # náhodné vylosování hodu mincí.

    strany = ["Orel", "Panna"]

    vysledek = random.choices(strany, weights = [1, 2]) # Panna má větší váhu, protože rváč říká, že štěstěna je jeho dobrá kamarádka :)

    print(f"{vysledek}")
    print(" ")

    if vysledek == ['Orel']:
        print("Usmálo se na tebe štěstí.")
        print(" ")
        print("Rváč povídá: „Kurňa chlape, ty máš ale štěstí. No nic, štěstěna byla dnes na tvé straně, holka jedna paličatá.“")
        print(" ")

    elif vysledek == ['Panna']:
        print("Teď si neměl moc velké štěstí")
        print(" ")
        print("Rváč povídá: „Říkal jsem ti, že je štěstěna moje kamarádka. Teď si to budeme muset rozdat pěkně po staru, nebo máš snad lepší nápad?“")
        print(" ")

        rvac = int(input("Co uděláš? \n 1) Takového tlučhubu si namažeš na chleba, dyť jsi přece zaklínač.\n 2) Takové problémy ti nestojí za to, nabídneš mu své peníze a budeš doufat, že je přijme.\n"))
        print(" ")

        if rvac == 1:
            print("„Když se chceš prát, tak se jdeme prát. Neboj se, nebudu tě šetřit.“, říká chraplavým hlasem rváč.")
            print(" ")
            print("Zjišťuješ, že to nebude tak jednoduché, rváč zatím každou tvoji ránu vykryl, ale ty si jich už pár schytal.")
            print(" ")
            print("Pěstní souboje nejsou tvá silná stránka, nejsi žádný Geralt z Rivie. Rváč má jasnou převahu.")
            print(" ")
            print("Po slušném začátku si v průběhu boje dost upadl a rváč tě zmlátil jako psa.")
            print(" ")
            print("Po neúspěšném boji zůstáváš ležet na zemi, tohle už asi nerozdejcháš kamaráde. Na následky zranění pomalu umíráš...")
            print(" ")
            print("Říká se, že žádný zaklínač neumírá v posteli, ale tohle je poměrně ubohý konec, nemyslíš?.")
            print("...")
            print("KONEC HRY")
            print(" ")
            print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
            quit()

        # Teď záleží na tom, jestli hráč dal převozníkovi peníze.

        elif rvac == 2:
            print("Předáváš rváčovi své peníze a doufáš, že částka bude stačit.")
            print(" ")

            if oreny == 10:
                print("Rváč se na tebe pousměje a povídá: „Když si neměl štěstí v hodu mincí, tak máš štěstí aspoň v tom, že s sebou nosíš dostatečný obnos peněz, 10 orénů mi protentokrát bude stačit.“")
                print(" ")
                oreny -= 10

            elif oreny == 5:
                print("Rváč se na tebe zamračí a povídá: „To si snad děláš srandu, 5 orénů?, na takovou vindru mě chceš ukecat? Já z tebe tu kuráž vymlátím!“")
                print(" ")
                print("„Když nemáš peníze, tak doufej, že aspoň dobře bojuješ.“, říká chraplavým hlasem rváč.")
                print(" ")
                print("Rváč zatím každou tvoji ránu vykryl, ale ty si jich už pár schytal.")
                print(" ")
                print("Pěstní souboje nejsou tvá silná stránka, nejsi žádný Geralt z Rivie. Rváč má jasnou převahu.")
                print(" ")
                print("Po slušném začátku si v průběhu boje dost upadl a rváč tě zmlátil jako psa.")
                print(" ")
                print("Po neúspěšném boji zůstáváš ležet na zemi, tohle už asi nerozdejcháš kamaráde. Na následky zranění pomalu umíráš...")
                print(" ")
                print("Říká se, že žádný zaklínač neumírá v posteli, ale tohle je poměrně ubohý konec, nemyslíš?")
                print("...")
                print("KONEC HRY")
                print(" ")
                print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
                quit()

        else:
            print("Taková možnost nebyla, zkus to ještě jednou.")
            print(" ")
            quit()   

    # Budeme pokračovat dále v příběhu okolo hospodského.

    print("Krizi s rváčem si nějak zažehnal a konečně si můžeš promluvit s hospodským, který snad bude o něčem vědět.")
    print(" ")
    print("Přijdeš k hospodskému a povídáš: „Nenašla by se tu nějaká práce pro zaklínače?“")
    print(" ")
    print("Hospodský se na tebe podívá ostrým pohledem a rázným hlasem zakřičí: „Nenašla, ještě jeden takový provokativní kec a pošlu na tebe místní chlapy.“")
    print(" ")
    print("Po pár sekundové odmlce se k tobě hospodský nakloní a nenápadným šepotom ti říká: „Tohle je poměrně klidná věsnice pane zaklínači, ale poslední dobou tu máme takový problém.“")
    print(" ")
    print("Hospodský pokračuje: „Víte, poslední dobou nás tu drží zkrátka místní gang. Problémy s nimi byli již předtím, ale poslední dobou si začali vyskakovat.“")
    print(" ")
    print("„Dnes se člověk musí mít pořád na pozoru. Mlynář Pešek si pod vlivem minulý týden pustil hubu na špacír a dnes nemá kde bydlet. Barák mu do základů vypálali a zvířata do jednoho potratili.“")
    print(" ")
    print("„My bychom se jich potřebovali zbavit. Berou si, co si zachtějí. Občas chodí po domech a vybírají peníze, kdo nedá, tězce zaplatí. Dokonce i znásilňují naše děvčata, hotové neštěstí.“")
    print(" ")
    print("„My bychom s tím už dávno něco udělali, ale místní chlapy se bojí o své rodiny. To není jen tak. Každý si radši hledí svého.“")
    print(" ")
    print("„Lidi z vesnice dali dohromady slušnou sumu pro někoho, jako jste vy. Celých 300 orenů! Co vy na to, pomůžete nám?“")
    print(" ")

    # Hráč se buď rozhodne pomoct místním vesničanům, nebo zhodnotí situaci jako příliš riskantní a odejde jinam.

    gang = int(input("Co uděláš? \n 1) Tolik peněz si rozhodně nenecháš ujít. Pomůžeš tím i sužovaným vesničanům. \n 2) S gangem nájemných vrahů si nebudeš nic začínat, peníze si zkusíš obstarat jinde.\n"))
    print(" ")

    if gang == 1:
        print("Souhlasně kývneš hlavou, aby si dal hospodskému vědět, že jeho zakázku přijímáš. Ten ti zatím dal jen symbolických 5 orénů, které uzavírají smlouvu.")
        oreny += 5
        print(" ")
        print("Ještě než odejdeš dveřmi krčmářskými, tak tě zastaví jakási stařena, představí se ti jako zdejší léčitelka a mastičkářka.")
        print(" ")
        print("„Dobrý pane, nechtěl byste si ode mne lektvar koupiti. Přesněji elixír, abych byla přesná, je znám pod jménem vlaštovka.“, povídá.")
        print(" ")
        print("„Při boji urychlí regeneraci vašeho systému, budete rychlejší a vytrvalejší. Co vy na to? Chci za něj jen hubičku, 10 orénů přesně.“")
        print(" ")
        elixir = int(input("Chceš si od léčitelky koupit elixír vlaštovka? \n 1) Chceš, takovýto elixír se ti před bojem může hodit. \n 2) Necheš, jsou to pro tebe zbytečné vyhozené peníze, s takovými bandity si poradíš raz dva.\n"))
        print(" ")
        
        # Hráč si elixír buď koupí a proti násilníkům vyhraje, nebo si ho nekoupí a setkání s badnou hrdlořezů nepřežije.

        if oreny >= 10 and elixir == 1:
            print("Elixír sis koupil, souboj by pro tebe teď neměl být problém.")
            print(" ")
            vlastovka = True
            oreny -= 10

        elif oreny < 10 and elixir == 1:
            print("Elixír chtít můžeš, ale pokut nemáš 10 orénů, tak ti ho léčitelka neprodá. Smůla!")
            print(" ")

        elif elixir == 2:
            print("Elixír nepotřebuješ, na bandu podvraťáků se cítíš být dostatečně silný.")
            print(" ")

        if vlastovka == True:
            print("Od místních před hospodou ses dozvěděl, že gang má tábor ve staré stodole na kraji vesnice, takže se tam jdeš podívat.")
            print(" ")
            print("Stojíš před branami staré stodoly, ze vnitř slyšíš smích a hodování.")
            print(" ")
            print("Než začne tvůj smrtelný tanec, tak ještě požiješ vlaštovku od místní léčitelky, účinný to elixír.")
            print(" ")
            print("Elixír okamžitě působí na tvůj metabolizmus, všude po těle se ti rozšířili žíly a srdce ti začalo tloust jako o život.")
            print(" ")
            print("Když otevřeš dveře od stodoly, tak banda zrovna zneužívá jedno z místních děvčat.")
            print(" ")
            print("Takhle to rozhodně nenecháš být a rychle tasíš svůj ocelový meč.")
            print(" ")
            print("Ze všech stran na tebe naběhnou hrdlořezové, ale ty zůstáváš v klidu.")
            print(" ")
            print("S klidem odrazíš prvního útočníka, kterému v mžiku sekundy rozřízneš hrdlo, dalšího útočníka následuje podobný osud.")
            print(" ")
            print("Od této chvíle předvádíš jednu parádu za druhou, skupinový styl boje ti jde.")
            print(" ")
            print("V bojové vřavě si ale nevšimneš seknutí nepřátelského meče směrem k tobě, máš řeznou ránu přes celá záda, ale přes vliv vlaštovky skoro nic necítíš.")
            print(" ")
            print("Rána se ti hned uzavírá a spomalení krvácení následuje.")
            print(" ")
            print("Poslední násilníky pošleš na věčnost dvoumi rychlými výpady. Tímto je tvoje zakázka splněna.")
            print(" ")
            print("Vystrašené děvče pošleš domů, pohled na mrtvá těla ji ovšem v paměti zůstanou snad nadosmrti.")
            print(" ")
            print("Mrtvá těla ještě před stodolou vyskládáš na hromadu a zapálíš pomocí znamení Igni.")
            print(" ")
            print("Do hospody si skočíš pro odměnu, které se ti dostane. Měl by si co nejdřív z vesnice odejít, nemá cenu zůstávat zde o minutu navíc. Na nějakou dobu ti tyto peníze určitě vystačí.")
            print("...")
            print("KONEC HRY")
            print(" ")
            print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
            quit()

        elif vlastovka == False:
            print("Od místních před hospodou ses dozvěděl, že gang má tábor ve staré stodole na kraji vesnice, takže se tam jdeš podívat.")
            print(" ")
            print("Stojíš před branami staré stodoly, ze vnitř slyšíš smích a hodování.")
            print(" ")
            print("Není už na co čekat, rázně vyrážíš dveře stodoly znamením Aard.")
            print(" ")
            print("Po vyražení dveří se ti naskýtá pohled, jak banda zrovna zneužívá jedno z místních děvčat.")
            print(" ")
            print("Takhle to rozhodně nenecháš být a rychle tasíš svůj ocelový meč.")
            print(" ")
            print("Ze všech stran na tebe naběhnou hrdlořezové, ale ty zůstáváš v klidu.")
            print(" ")
            print("S klidem odrazíš prvního útočníka, kterému v mžiku sekundy rozřízneš hrdlo, dalšího útočníka následuje podobný osud.")
            print(" ")
            print("Od této chvíle předvádíš jednu parádu za druhou, skupinový styl boje ti jde.")
            print(" ")
            print("V bojové vřavě si ale nevšimneš seknutí nepřátelského meče směrem k tobě, máš řeznou ránu přes celá záda.")
            print(" ")
            print("Stodolou se najednou ozve tvůj mrazivý výkřik. Záda ti strašně krvácí a pomalu ztrácíš sílu k boji.")
            print(" ")
            print("Jeden z násilníků využije tvého zaváhání a do levého stehna ti zarazí dvoucečnou sekeru.")
            print(" ")
            print("To tě už úplně srazí k zemi. Při tom upustíš svůj meč, který se ještě znažíš vzít do rukou, ale jeden z hrdlořezů ho odkopne.")
            print(" ")
            print("Už nemůžeš udělat nic, na seslání zaklínačského znamení jsi moc vyčerpaný.")
            print(" ")
            print("V téhle pozici už to máš rychle za sebou. Mohl jsi dopadnout hůře, mohl jsi trpět.")
            print(" ")
            print("Vesničanům si situaci ještě zhoršil, po tomto incidentu bylo výhružně povražděno několik rodin a podpáleno několik domů.")
            print("...")
            print("KONEC HRY")
            print(" ")
            print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
            quit()

    elif gang == 2:
        print("To si teda vesničany moc nepotěšil. Byl jsi jejich jediná naděje.")
        print(" ")
        print("Nedá se nic dělat, zaklínač má samozřejmě plné právo zakázku odmítnout.")
        print(" ")
        print("Zprávy o tvém odmítnutí se rychle rozkřiknou. Měl by ses raději na nějakou dobu uklidit někam jinam.")
        print(" ")
        print("Tady už tě nic dobrého nečeká. Budeš muset dále pokračovat na své stezce.")
        print(" ")
        print("Jestli jsi udělal dobře, nebo ne, tak to už se teď nedozvíme...")
        print("...")
        print("KONEC HRY")
        print(" ")
        print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
        quit()

    else:
        print("Taková možnost nebyla, zkus to ještě jednou.")
        print(" ")
        quit()

# Hráč se zde dostane do opuštěného kamenolomu

elif rozcesti == 3:
    print("Ocitneš se u místního kamenolomu.")
    print(" ")
    print("Vypadá to, že kamenolom je už hodně dlouho opuštěnný, všude jen samé polorozpadlé chatičky a mnoho použitého nářadí. Toto nářadí už zub času hodně ohlodal.")
    print(" ")
    print("Najednou uslyšíš nějaké hluboké mrčení z jeskynně hned vedle kamenolomu.")
    print(" ")

    #  Hráč se s trollem může či nemusí setkat, je to na něj.

    troll = int(input("Co uděláš? \n 1) Jeskynni půjdeš prozkoumat, nemyslíš si, že v ní bude něco nebezpečného. \n 2) Skřeky z opuštěných míst nikdy nevěstí nic dobrého, raději to tady zabalíš.\n"))
    print(" ")

    if troll == 1:
        print("Čím hlouběji si v jeskynni, tím je skřik hlasitější. V jeskynni to taky pěkně smrdí.")
        print(" ")
        print("Po chvíli si myslíš, že tě snad šálí zrak. Narazil jsi na skalního trolla, ten je v této lokalitě obzvlášť neobvyklý.")
        print(" ")
        print("Právě asi kvůli němu je tu zde tak pusto. Vypadá to, že se místní obyvatelstvo s přítomností trolla smířilo.")
        print(" ")
        print("K trollovi se opatrně přibližuješ, když v tom najednou si tě všimne a povídá:„Ah, člověk. Já rád vidět. Já muset mluvit k ty.“")
        print(" ")
        print("Vypadá to, že troll není nepřátelský, chce ti něco sdělit.")
        print(" ")
        print("„Ty muset přinést stříbrný meč. Můj jedinný naděje. Já dát zlato.“")
        print(" ")
        print("Vypadá to, že troll chce přinést stříbrný meč. Splnění jeho přání odměňuje zlatem.")
        print(" ")

        # Meč může hráč získat jedině od hádankáře, poté musí odmítnout souboj s čarodějnicí, pokud chce získat tento konec.

        if stribrny_mec == True:
            print("Stříbrný meč náhodou po ruce máš.")
            print(" ")
            print("Meč trollovi opatrně podáš.")
            print(" ")
            print("Troll meč uchopí a povídá :„Ano, ty zbavit troll trápení. Já děkovat.“")
            print(" ")
            print("Troll meč pevně uchytí do nešikovných rukou. Najednou si jím propíchne hruď.")
            print(" ")
            print("Než se stačíš vzpamatovat z toho, co si právě viděl, tak se troll postupně promění v normálního chlapce.")
            print(" ")
            print("Chlapec po chvíli přichází k sobě a povídá: „Děkuji moc za záchranu člověče. Několik desítek let jsem byl zakletý do podoby tohoto trolla.“")
            print(" ")
            print("„Jediné, co mě mohlo zachránit byla magie z dobře ukovaného stříbrného meče.“")
            print(" ")
            print("„Pokud by meč nebyl kvalitní mechanicky ani magicky, tak bych zůstal trollem.“")
            print(" ")
            print("„Zaklela mě takhle jedna mocná čarodějka, když jsem byl ještě dítě. Teď jsem v podstatě také ještě dítě, vůbec jsem nezestárl...“")
            print(" ")
            print("Vzadu v jeskynni se nachází truhlice s pokladem, který jsem našel již dávno. Poklad je nyní tvůj. Pokud by tvůj meč neprolomil kletbu, k pokladu bych tě nepustil.")
            print(" ")
            print("Rozsah pokladu tě překvapuje. Tolik zlata jsi ještě pohromadě nikdy neviděl. Takové množství tě zabezpečí aspoň na jednu dekádu. O tomhle až budeš vyprávět v Kear Morhen...")
            print("...")
            print("KONEC HRY")
            print(" ")
            print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
            quit()

        elif stribrny_mec == False:
            print("Žádný stříbrný meč u sebe nemáš, to se trollovi nebude líbit.")
            print(" ")
            print("Trollovi citlivě naznačíš, že žádný stříbrný meč nemáš.")
            print(" ")
            print("Troll se zamračí a povídá: „Ty dělat z trolla sranda. K troll už ty nevracet, jinak troll zabít.“")
            print(" ")
            print("Měl bys jít někam jinam. Troll už tě tu nechce vidět. Pokud se tu ukážeš, tak tě zabije.")
            print(" ")
            print("Při odchodu z kamenolomu tě ovšem zehlédne místní dívenka, která si za vesnicí hrála s kamarády na schovávanou.")
            print(" ")
            print("Řekne o tom doma a vesničané začnou být nedůvěřivý.")
            print(" ")
            print("Ve vesnici se o tobě začně říkat, že pro trolla pracuješ, plníš jeho zlá přání. Někdo o tobě také říká, že jsi špinavý měňavec.")
            print(" ")
            print("Drby se šíří rychle a lidé si vždy něco vymyslí.")
            print(" ")
            print("Lidé se k tobě začnou chovat odtažitě, nebudou s tebou chtít mít nic společného.")
            print(" ")
            print("Pověst u lidí je pro zaklínače velmi důležitá. Přece nebudou dávat peníze někomu, komu nevěří.")
            print(" ")
            print("Někde mají zaklínače rádi více, někde méně. Zálezí na povaze lidu. Tady jsi svou pověst ztratil.")
            print("")
            print("Tady už tě nic dobrého nečeká. Budeš muset dále pokračovat na své stezce. Snad budeš mít jinde více štěstí...")
            print("...")
            print("KONEC HRY")
            print(" ")
            print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
            quit()

    elif troll == 2:
        print("Z takových neznámých zvuků ti není vůbec dobře, radši jdeš pryč.")
        print(" ")
        print("Při odchodu z kamenolomu tě ovšem zehlédne místní dívenka, která si za vesnicí hrála s kamarády na schovávanou.")
        print(" ")
        print("Řekne o tom doma a vesničané začnou být nedůvěřivý.")
        print(" ")
        print("Ve vesnici se o tobě začně říkat, že pro trolla pracuješ, plníš jeho zlá přání. Někdo o tobě také říká, že jsi špinavý měňavec.")
        print(" ")
        print("Drby se šíří rychle a lidé si vždy něco vymyslí.")
        print(" ")
        print("Lidé se k tobě začnou chovat odtažitě, nebudou s tebou chtít mít nic společného.")
        print(" ")
        print("Zaklínačova pověst u lidí je pro zaklínače velmi důležitá. Přece nebudou dávat peníze někomu, komu nevěří.")
        print(" ")
        print("Někde mají zaklínače rádi více, někde méně. Zálezí na povaze lidu. Tady jsi svou pověst ztratil.")
        print("")
        print("Tady už tě nic dobrého nečeká. Budeš muset dále pokračovat na své stezce. Snad budeš mít jinde více štěstí...")
        print("...")
        print("KONEC HRY")
        print(" ")
        print(f"Děkuji moc za dohrání hry {jmeno}, klidně si hru zahraj vícekrát a objev všechny možné průchody hrou a konce.")
        quit()

    else:
        print("Taková možnost nebyla, zkus to ještě jednou.")
        print(" ")
        quit()

else:
    print("Taková možnost nebyla, zkus to ještě jednou.")
    print(" ")
    quit()


