# -*- coding: utf-8 -*-
import urllib.request, sys, time

IMG = {
 'hero':"https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Chureito_Pagoda_and_Mount_Fuji_2023-03-07.jpg/960px-Chureito_Pagoda_and_Mount_Fuji_2023-03-07.jpg",
 'strip_temples':"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Torii_path_with_lantern_at_Fushimi_Inari_Taisha_Shrine%2C_Kyoto%2C_Japan.jpg/960px-Torii_path_with_lantern_at_Fushimi_Inari_Taisha_Shrine%2C_Kyoto%2C_Japan.jpg",
 'strip_villes':"https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Shibuya_Crossing%2C_Aerial.jpg/960px-Shibuya_Crossing%2C_Aerial.jpg",
 'strip_nature':"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/View_of_Mount_Fuji_from_%C5%8Cwakudani_20211202.jpg/960px-View_of_Mount_Fuji_from_%C5%8Cwakudani_20211202.jpg",
 'def_tokyo':"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Tokyo_skyline_seen_from_Tokyo_Skytree.jpg/960px-Tokyo_skyline_seen_from_Tokyo_Skytree.jpg",
 'def_kansai':"https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Kiyomizu.jpg/960px-Kiyomizu.jpg",
 'def_hokkaido':"https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Lavender%2C_Furano_%287662399108%29.jpg/960px-Lavender%2C_Furano_%287662399108%29.jpg",
 'def_alpes':"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/View_of_Mount_Fuji_from_%C5%8Cwakudani_20211202.jpg/960px-View_of_Mount_Fuji_from_%C5%8Cwakudani_20211202.jpg",
 'def_ouest':"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Itsukushima_Shrine_Torii_Gate_%2813890465459%29.jpg/960px-Itsukushima_Shrine_Torii_Gate_%2813890465459%29.jpg",
 'def_okinawa':"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Kerama_Island_-_6080663849.jpg/960px-Kerama_Island_-_6080663849.jpg",
 'tokyo1':"https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Shibuya_Crossing%2C_Aerial.jpg/960px-Shibuya_Crossing%2C_Aerial.jpg",
 'tokyo2':"https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Sensoji_2023.jpg/960px-Sensoji_2023.jpg",
 'tokyo3':"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Skyscrapers_of_Shinjuku_2009_January.jpg/960px-Skyscrapers_of_Shinjuku_2009_January.jpg",
 'tokyo4':"https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Meiji_Jingu_2023-3.jpg/960px-Meiji_Jingu_2023-3.jpg",
 'tokyo5':"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/230128_Kamakura_Daibutsu_Japan04s3.jpg/960px-230128_Kamakura_Daibutsu_Japan04s3.jpg",
 'kansai1':"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Torii_path_with_lantern_at_Fushimi_Inari_Taisha_Shrine%2C_Kyoto%2C_Japan.jpg/960px-Torii_path_with_lantern_at_Fushimi_Inari_Taisha_Shrine%2C_Kyoto%2C_Japan.jpg",
 'kansai2':"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Golden_Pavilion_Kinkaku-ji_water_mirror_2024.jpg/960px-Golden_Pavilion_Kinkaku-ji_water_mirror_2024.jpg",
 'kansai3':"https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Arashiyama_013.jpg/960px-Arashiyama_013.jpg",
 'kansai4':"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/T%C5%8Ddai-ji_Kon-d%C5%8D.jpg/960px-T%C5%8Ddai-ji_Kon-d%C5%8D.jpg",
 'kansai5':"https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Osaka_Castle_03bs3200.jpg/960px-Osaka_Castle_03bs3200.jpg",
 'hok1':"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/SapporoFestival8.JPG/960px-SapporoFestival8.JPG",
 'hok2':"https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/%E5%A7%BF%E8%A6%8B%E3%83%8E%E6%B1%A0%E3%81%8B%E3%82%89%E3%81%AE%E6%97%AD%E5%B2%B3.jpg/960px-%E5%A7%BF%E8%A6%8B%E3%83%8E%E6%B1%A0%E3%81%8B%E3%82%89%E3%81%AE%E6%97%AD%E5%B2%B3.jpg",
 'hok3':"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Lavender_fields%2C_Furano_%2848254611081%29.jpg/960px-Lavender_fields%2C_Furano_%2848254611081%29.jpg",
 'hok4':"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Otaru_Canal_HDR1.jpg/960px-Otaru_Canal_HDR1.jpg",
 'hok5':"https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Jigokudani_%28Hell_Valley%29%2C_Noboribetsu_Onsen%2C_Hokkaido%2C_April_2023_14.jpg/960px-Jigokudani_%28Hell_Valley%29%2C_Noboribetsu_Onsen%2C_Hokkaido%2C_April_2023_14.jpg",
 'alp1':"https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Lake_Kawaguchiko_Sakura_Mount_Fuji_4.JPG/960px-Lake_Kawaguchiko_Sakura_Mount_Fuji_4.JPG",
 'alp2':"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/View_of_Mount_Fuji_from_Lake_Ashi.jpg/960px-View_of_Mount_Fuji_from_Lake_Ashi.jpg",
 'alp3':"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Takayama%27s_Early_Winter_Welcome_%28NE%29.jpg/960px-Takayama%27s_Early_Winter_Welcome_%28NE%29.jpg",
 'alp4':"https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Triplets_Gassho-zukuri_houses_%28Shirakawa-go%29_Gifu_%2849908188231%29.jpg/960px-Triplets_Gassho-zukuri_houses_%28Shirakawa-go%29_Gifu_%2849908188231%29.jpg",
 'alp5':"https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Stone_lantern_Kenrokuen.jpg/960px-Stone_lantern_Kenrokuen.jpg",
 'ou1':"https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Genbaku_Dome04-r.JPG/960px-Genbaku_Dome04-r.JPG",
 'ou2':"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Itsukushima_Shrine_Torii_Gate_%2813890465459%29.jpg/960px-Itsukushima_Shrine_Torii_Gate_%2813890465459%29.jpg",
 'ou3':"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Beachside_Torii%2C_Naoshima.jpg/960px-Beachside_Torii%2C_Naoshima.jpg",
 'ou4':"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Himeji_castle_in_may_2015.jpg/960px-Himeji_castle_in_may_2015.jpg",
 'ou5':"https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/250505_Korakuen_Okayama_Japan06s3.jpg/960px-250505_Korakuen_Okayama_Japan06s3.jpg",
 'oki1':"https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Miyakojima_sky_view.jpg/960px-Miyakojima_sky_view.jpg",
 'oki2':"https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Naha_Okinawa_Japan_Shuri-Castle-01.jpg/960px-Naha_Okinawa_Japan_Shuri-Castle-01.jpg",
 'oki3':"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Okinawa_kerama_islands.jpg/960px-Okinawa_kerama_islands.jpg",
 'oki4':"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Churaumi_Aquarium_main_tank_%27Kuroshio_Sea%27.jpg/960px-Churaumi_Aquarium_main_tank_%27Kuroshio_Sea%27.jpg",
 'oki5':"https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Walk_in_Taketomi_Island_10.jpg/960px-Walk_in_Taketomi_Island_10.jpg",
 'dish_sushi':"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Sushi_platter.jpg/960px-Sushi_platter.jpg",
 'dish_ramen':"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Shoyu_Ramen%EF%BC%88Tokyo_Ramen%EF%BC%89_-_01.jpg/960px-Shoyu_Ramen%EF%BC%88Tokyo_Ramen%EF%BC%89_-_01.jpg",
 'dish_tempura':"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Tempura_01.jpg/960px-Tempura_01.jpg",
 'dish_okonomiyaki':"https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Okonomiyaki_001.jpg/960px-Okonomiyaki_001.jpg",
 'dish_yakitori':"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Cooking_yakitori.jpg/960px-Cooking_yakitori.jpg",
 'dish_soba':"https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Zaru_soba_by_spinachdip.jpg/960px-Zaru_soba_by_spinachdip.jpg",
 'dish_sukiyaki':"https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Sukiyaki_01.jpg/960px-Sukiyaki_01.jpg",
 'dish_matcha':"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Matcha_Scoop.jpg/960px-Matcha_Scoop.jpg",
}

def esc(s): return s.replace('&','&amp;')

# REGIONS: key -> (titre, label_defaut, intro, [ (imgkey, head, label, desc) x5 ])
REGIONS = [
 ('tokyo','Tokyo &amp; le Kantō','Tokyo · aire urbaine de 37 M',
  "Capitale tentaculaire et futuriste, Tokyo juxtapose néons étourdissants, temples séculaires et quartiers d'une élégance feutrée. Cœur battant du Japon moderne, elle s'étend sur l'immense plaine du Kantō.",
  [('tokyo1','Le carrefour de Shibuya','Shibuya','Le passage piéton le plus fréquenté du monde, où des milliers de personnes traversent à chaque feu sous une cascade d\'écrans géants.'),
   ('tokyo2','Sensō-ji &amp; Asakusa','Asakusa','Le plus ancien temple de Tokyo, précédé de la porte Kaminarimon et de sa lanterne rouge géante, au cœur du vieux quartier d\'Asakusa.'),
   ('tokyo3','Shinjuku &amp; ses gratte-ciel','Shinjuku','Quartier électrique des tours, de la gare la plus fréquentée du monde et des ruelles à izakayas du Golden Gai.'),
   ('tokyo4','Sanctuaire Meiji','Meiji-jingū','Havre de paix shintō niché dans une forêt de 100 000 arbres en plein centre, dédié à l\'empereur Meiji.'),
   ('tokyo5','Kamakura &amp; le Grand Bouddha','Kamakura','À une heure de Tokyo, l\'ancienne capitale médiévale et son Bouddha de bronze de 13 mètres en plein air (Daibutsu).')]),
 ('kansai','Kyoto &amp; le Kansai','Kyoto · 1 200 ans d\'histoire',
  "Berceau de la culture japonaise, le Kansai concentre mille ans d'histoire impériale : Kyoto et ses temples, Nara et ses daims, Osaka et sa gastronomie débridée.",
  [('kansai1','Fushimi Inari-taisha','Fushimi Inari','Le sanctuaire aux milliers de torii vermillon serpentant à flanc de montagne, dédié à Inari, divinité du riz.'),
   ('kansai2','Kinkaku-ji, le Pavillon d\'Or','Kinkaku-ji','Pavillon recouvert de feuilles d\'or se reflétant dans un étang miroir — l\'image la plus emblématique de Kyoto.'),
   ('kansai3','Arashiyama &amp; la bambouseraie','Arashiyama','Quartier de l\'ouest de Kyoto célèbre pour sa forêt de bambous géants et ses temples au pied des montagnes.'),
   ('kansai4','Nara &amp; le Tōdai-ji','Nara','Première capitale du Japon, où des daims en liberté côtoient le Tōdai-ji et son immense Bouddha de bronze.'),
   ('kansai5','Osaka &amp; son château','Osaka','Métropole de la bonne chère (takoyaki, okonomiyaki) dominée par son château et le quartier néon de Dōtonbori.')]),
 ('hokkaido','Hokkaidō','Hokkaidō · l\'île du Nord',
  "L'île du Nord, sauvage et spacieuse, offre volcans, champs de fleurs, onsen fumants et les meilleures neiges du monde. Une autre facette du Japon, plus nature.",
  [('hok1','Sapporo &amp; le festival de neige','Sapporo','La grande ville du Nord, sa bière, ses ramen au miso et son festival de sculptures de glace géantes en février.'),
   ('hok2','Parc national de Daisetsuzan','Daisetsuzan','Le plus vaste parc du Japon, royaume de volcans, de sources chaudes et des premières couleurs d\'automne de l\'archipel.'),
   ('hok3','Furano &amp; ses champs de lavande','Furano','Collines ondulant sous des bandes de fleurs multicolores en été — lavande, coquelicots et tournesols à perte de vue.'),
   ('hok4','Otaru &amp; son canal','Otaru','Charmante ville portuaire au canal bordé d\'entrepôts en brique et de réverbères à gaz, réputée pour ses ateliers de verre.'),
   ('hok5','Onsen de Noboribetsu','Noboribetsu','La plus célèbre station thermale d\'Hokkaidō, dominée par la « Vallée de l\'Enfer » (Jigokudani) aux vapeurs sulfureuses.')]),
 ('alpes','Le Mont Fuji &amp; les Alpes','Mont Fuji · 3 776 m',
  "Au centre de Honshū se dressent le Mont Fuji et les Alpes japonaises : sommets enneigés, villages traditionnels, onsen et jardins parmi les plus beaux du pays.",
  [('alp1','Le Mont Fuji','Fuji-san','Volcan sacré de 3 776 m, cône parfait couronné de neige, plus haut sommet et symbole éternel du Japon.'),
   ('alp2','Hakone &amp; ses onsen','Hakone','Station thermale au pied du Fuji : bains chauds, lac Ashi et téléphérique survolant des vallées volcaniques fumantes.'),
   ('alp3','Takayama, la vieille ville','Takayama','Cité de montagne aux ruelles d\'Edo préservées, maisons de bois, brasseries de saké et marchés matinaux.'),
   ('alp4','Shirakawa-gō','Shirakawa-gō','Village classé à l\'UNESCO pour ses fermes gasshō-zukuri aux toits de chaume pentus, magiques sous la neige.'),
   ('alp5','Kanazawa &amp; le Kenroku-en','Kenroku-en','Ville de la feuille d\'or abritant le Kenroku-en, l\'un des trois plus beaux jardins paysagers du Japon.')]),
 ('ouest','Hiroshima &amp; l\'Ouest','Mer de Seto · l\'Ouest paisible',
  "L'ouest de Honshū, baigné par la paisible mer intérieure de Seto, mêle mémoire de la paix, sanctuaires flottants, châteaux immaculés et îles d'art contemporain.",
  [('ou1','Mémorial de la paix d\'Hiroshima','Hiroshima','Le Dôme de Genbaku, seul bâtiment resté debout sous la bombe de 1945, et son parc dédié à la paix mondiale.'),
   ('ou2','Miyajima &amp; le torii flottant','Miyajima','L\'île sacrée d\'Itsukushima et son grand torii vermillon qui semble flotter sur la mer à marée haute.'),
   ('ou3','Naoshima, l\'île de l\'art','Naoshima','Île de la mer intérieure muée en musée à ciel ouvert, parsemée de musées signés Tadao Andō et d\'œuvres contemporaines.'),
   ('ou4','Le château de Himeji','Himeji','Le plus beau château féodal du Japon, surnommé le « Héron blanc » pour ses murs immaculés, classé à l\'UNESCO.'),
   ('ou5','Okayama &amp; le Kōraku-en','Okayama','Autre membre du trio des grands jardins, vaste promenade paysagère face au château noir d\'Okayama.')]),
 ('okinawa','Okinawa','Okinawa · les tropiques japonais',
  "À l'extrême sud, l'archipel subtropical d'Okinawa déroule lagons turquoise, récifs coralliens et une culture ryūkyū singulière, héritée d'un ancien royaume insulaire.",
  [('oki1','Miyako-jima &amp; ses plages','Miyako-jima','Île aux eaux parmi les plus transparentes du Japon, réputée pour la plage de Yonaha Maehama et ses ponts spectaculaires.'),
   ('oki2','Le château de Shuri (Naha)','Shuri','Ancien palais des rois Ryūkyū à Naha, rouge et or, si différent des châteaux japonais (en reconstruction depuis l\'incendie de 2019).'),
   ('oki3','Les îles Kerama','Kerama','Petit archipel au large de Naha, célèbre pour son « bleu Kerama », ses tortues marines et ses spots de plongée.'),
   ('oki4','Aquarium Churaumi','Churaumi','L\'un des plus grands aquariums du monde, dont l\'immense bassin Kuroshio abrite requins-baleines et raies manta.'),
   ('oki5','Ishigaki &amp; Taketomi','Taketomi','Aux confins sud, l\'île de Taketomi et son village aux toits de tuiles rouges, parcouru en char à buffles.')]),
]

# carte: positions des repères (label affiché, x%, y%, region key)
PINS = [('Hokkaidō',71,15,'hokkaido'),('Tokyo',61,45,'tokyo'),('Fuji',54,49,'alpes'),
        ('Kyoto',44,53,'kansai'),('Hiroshima',33,60,'ouest'),('Okinawa',15,86,'okinawa')]

DISHES = [
 ('dish_sushi','Sushi','Emblème national','Riz vinaigré et poisson cru d\'une fraîcheur absolue. Du comptoir de quartier au maître étoilé, l\'art de l\'essentiel.'),
 ('dish_ramen','Ramen','Nouilles','Bouillon mijoté (miso, shōyu, tonkotsu) et nouilles de blé, garni de porc chashu, œuf mollet et oignons verts. Réconfort absolu.'),
 ('dish_tempura','Tempura','Friture légère','Légumes et fruits de mer enrobés d\'une pâte aérienne et frits minute. Croustillant, délicat, jamais gras.'),
 ('dish_okonomiyaki','Okonomiyaki','Osaka &amp; Hiroshima','« Crêpe » salée au chou nappée de sauce, mayonnaise et bonite séchée dansante. Cuite devant vous sur la plaque.'),
 ('dish_yakitori','Yakitori','Izakaya','Brochettes de poulet grillées au charbon, salées ou laquées à la sauce tare. L\'âme des bars à brochettes du soir.'),
 ('dish_soba','Soba','Nouilles de sarrasin','Fines nouilles de sarrasin servies chaudes en bouillon ou froides (zaru) avec une sauce à tremper. Rafraîchissant en été.'),
 ('dish_sukiyaki','Sukiyaki','Marmite conviviale','Fines tranches de bœuf wagyū mijotées à table dans une sauce sucrée-salée, trempées dans l\'œuf cru battu. Festif.'),
 ('dish_matcha','Matcha','Thé &amp; douceurs','Thé vert en poudre fouetté, intense et végétal, au cœur de la cérémonie du thé et d\'innombrables wagashi.'),
]

# saisons: key -> (classe, label, texte)
SAISONS_BAR = [('jan','hiver','Jan'),('fev','hiver','Fév'),('mar','printemps','Mar'),('avr','printemps','Avr'),
 ('mai','printemps','Mai'),('jun','ete','Juin'),('jul','ete','Juil'),('aou','ete','Août'),
 ('sep','automne','Sep'),('oct','automne','Oct'),('nov','automne','Nov'),('dec','hiver','Déc')]
SAISONS = {
 'jan':('Janvier — Hiver vif ❄️ Neige &amp; onsen','Froid sec et ensoleillé à Tokyo, neige abondante au nord et dans les Alpes. Saison idéale pour le ski, les onsen et les paysages enneigés.'),
 'fev':('Février — Cœur de l\'hiver ❄️','Mois le plus froid, neiges parfaites à Hokkaidō, festival de neige de Sapporo. Premiers pruniers (ume) en fleurs dans le sud.'),
 'mar':('Mars — Premiers cerisiers 🌸','Le mercure remonte ; les premières floraisons de sakura apparaissent fin mars à Tokyo et Kyoto. La période magique s\'annonce.'),
 'avr':('Avril — Pleine floraison 🌸 Idéal','L\'apogée des cerisiers dans tout le pays (hanami). Climat doux et lumineux — la période la plus prisée, réservez très tôt.'),
 'mai':('Mai — Verdure &amp; douceur 🌿 Idéal','Températures parfaites, ciel clair, nature éclatante après les cerisiers. L\'un des meilleurs mois, avant les pluies.'),
 'jun':('Juin — Tsuyu, saison des pluies 🌧️','La mousson (tsuyu) gagne la majeure partie du pays (sauf Hokkaidō). Hortensias en fleurs ; affluence et prix en baisse.'),
 'jul':('Juillet — Chaud et humide ☀️','Fin des pluies, début de la chaleur moite. Saison des festivals (matsuri) et des feux d\'artifice. Lavande en fleur à Hokkaidō.'),
 'aou':('Août — Pic de chaleur 🥵','Mois le plus chaud et humide (30-35°C, lourd). Idéal pour Hokkaidō et la montagne. Obon : grande période de voyages au Japon.'),
 'sep':('Septembre — Fin d\'été 🍃 Typhons','La chaleur faiblit mais c\'est la saison des typhons. La fin du mois est plus agréable ; premières couleurs au nord.'),
 'oct':('Octobre — Couleurs d\'automne 🍁 Idéal','Climat sec et doux, ciels limpides. Le kōyō (feuillages rouges et or) embrase peu à peu le pays. Excellente période.'),
 'nov':('Novembre — Apogée du kōyō 🍁 Idéal','Les érables flamboient à Kyoto et dans les montagnes — l\'automne japonais à son sommet. Frais et lumineux.'),
 'dec':('Décembre — Début de l\'hiver ❄️','Froid sec et ensoleillé sur le Pacifique, neige sur la mer du Japon. Illuminations urbaines féeriques ; peu de touristes.'),
}

ESSENTIALS = [
 ('🏙️','Capitale','Tokyo, près de 14 millions d\'habitants (37 dans l\'aire urbaine) : la plus grande mégalopole du monde, à la fois hyper-moderne et profondément traditionnelle.'),
 ('🗣️','Langue','Le japonais, écrit avec trois systèmes (kanji, hiragana, katakana). L\'anglais reste limité hors des zones touristiques — un traducteur d\'appoint est précieux.'),
 ('💴','Monnaie','Le yen (JPY). Pays sûr et de grande qualité, plus abordable qu\'on ne l\'imagine. Pensez aux espèces et à la carte IC pour le quotidien.'),
 ('⛩️','Religion','Shintoïsme et bouddhisme coexistent et se mêlent. Sanctuaires (jinja, torii rouges) et temples (-ji) rythment villes et campagnes.'),
 ('⚡','Électricité','100 V / 50–60 Hz. Prises de type A/B (comme aux USA). Un adaptateur est nécessaire depuis la France ; vérifiez le voltage de vos appareils.'),
 ('🕐','Décalage horaire','UTC+9. Par rapport à la France : +7h en été, +8h en hiver. Aucun changement d\'heure au Japon.'),
]
PRATIQUE = [
 ('🛂 Visa','Les Français bénéficient d\'une exemption de visa pour les séjours touristiques jusqu\'à 90 jours. Passeport valable toute la durée du séjour.'),
 ('💴 Argent','Le yen (JPY). Le Japon reste attaché aux espèces — retirez aux distributeurs des konbini (7-Eleven). La carte IC (Suica/Pasmo) règle transports et petits achats.'),
 ('🚄 Transports','Le train est roi : Shinkansen ultra-ponctuels, métros denses. Le Japan Rail Pass peut être rentable sur de longues distances. Conduite à gauche.'),
 ('🏯 Hébergement','De la capsule au ryokan traditionnel avec tatami, futon et onsen. Offrez-vous au moins une nuit en ryokan, idéalement avec repas kaiseki.'),
 ('🙇 Étiquette','On se déchausse à l\'entrée. Pas de pourboire. On ne mange pas en marchant. Silence dans les trains. Le salut (ojigi) remplace la poignée de main.'),
 ('📶 Connectivité','Louez un Pocket WiFi ou une eSIM à l\'arrivée. Le wifi public est inégal. Applis utiles : Google Maps, Japan Travel, un traducteur.'),
 ('♨️ Onsen','Bains chauds, nus et non mixtes. Se laver soigneusement avant d\'entrer. Les tatouages peuvent être refusés dans certains établissements — renseignez-vous.'),
 ('🌸 Saison','Évitez si possible la Golden Week (fin avril–début mai) et Obon (mi-août) : tout le pays voyage, prix et foules au sommet.'),
]

def verify():
    bad=[]
    for k,u in IMG.items():
        try:
            req=urllib.request.Request(u, method='HEAD', headers={'User-Agent':'le-savoir-site/1.0 (sebastien.laneres@icloud.com)'})
            code=urllib.request.urlopen(req, timeout=30).status
            if code!=200: bad.append((k,code,u))
        except Exception as e:
            bad.append((k,str(e),u))
        time.sleep(0.6)
    return bad

def region_tab(i, reg):
    key,titre,deflabel,intro,items=reg
    active=' active' if i==0 else ''
    lis=[]
    for imgk,head,lab,desc in items:
        lis.append(f'          <li data-img="{IMG[imgk]}" data-label="{lab}"><span class="li-head">{head}</span><span class="li-desc">{desc}</span></li>')
    lis='\n'.join(lis)
    return f'''    <div id="tab-{key}" class="tab-content{active}">
      <div class="region-text">
        <h3>{titre}</h3>
        <p>{intro}</p>
        <ul class="highlights">
{lis}
        </ul>
      </div>
      <div class="region-visual" data-label="{deflabel}">
        <img loading="lazy" decoding="async" src="{IMG['def_'+key]}" alt="{titre}" onload="this.classList.add('loaded')">
        <span class="region-photo-credit">Wikimedia Commons</span>
      </div>
    </div>'''

def build():
    tabs_btn=[]
    for i,(key,titre,_,_,_) in enumerate(REGIONS):
        lab=titre.split(' &amp;')[0].split(' —')[0]
        act=' active' if i==0 else ''
        tabs_btn.append(f'      <button class="tab-btn{act}" data-tab="{key}" onclick="showTab(\'{key}\', this)">{lab}</button>')
    tabs_btn='\n'.join(tabs_btn)
    pins=[]
    for lab,x,y,key in PINS:
        pins.append(f'      <button class="map-pin" style="left:{x}%;top:{y}%" onclick="showTab(\'{key}\')" aria-label="Région {lab}"><span class="map-pin-dot"></span><span class="map-pin-label">{lab}</span></button>')
    pins='\n'.join(pins)
    tabs_content='\n\n'.join(region_tab(i,r) for i,r in enumerate(REGIONS))

    strip=f'''      <div class="photo-strip-item">
        <img loading="lazy" decoding="async" src="{IMG['strip_temples']}" alt="Temples et torii" onload="this.classList.add('loaded')">
        <span class="strip-label">Temples &amp; torii</span>
      </div>
      <div class="photo-strip-item">
        <img loading="lazy" decoding="async" src="{IMG['strip_villes']}" alt="Métropoles japonaises" onload="this.classList.add('loaded')">
        <span class="strip-label">Métropoles</span>
      </div>
      <div class="photo-strip-item">
        <img loading="lazy" decoding="async" src="{IMG['strip_nature']}" alt="Nature et Mont Fuji" onload="this.classList.add('loaded')">
        <span class="strip-label">Nature &amp; saisons</span>
      </div>'''

    ess='\n'.join(f'''      <div class="card">
        <div class="card-icon">{ic}</div>
        <h3>{t}</h3>
        <p>{esc(p) if "&amp;" not in p else p}</p>
      </div>''' for ic,t,p in ESSENTIALS)

    dishes='\n'.join(f'''      <div class="dish-card">
        <img loading="lazy" decoding="async" class="dish-photo" src="{IMG[k]}" alt="{name}" onload="this.classList.add('loaded')">
        <div class="dish-overlay"></div>
        <div class="dish-content">
          <h4>{name}</h4>
          <div class="origin">{origin}</div>
          <p>{desc}</p>
        </div>
      </div>''' for k,name,origin,desc in DISHES)

    bar='\n'.join(f'      <div class="mois saison-{cls}{(" active" if m=="avr" else "")}" onclick="showMois(this,\'{m}\')">{lab}</div>' for m,cls,lab in SAISONS_BAR)
    av=SAISONS['avr']
    saison_js=',\n'.join(f"    {m}: {{ label: \"{SAISONS[m][0]}\", text: \"{SAISONS[m][1]}\" }}" for m,_,_ in SAISONS_BAR)
    prat='\n'.join(f'''      <div class="pratique-item">
        <h4>{t}</h4>
        <p>{p}</p>
      </div>''' for t,p in PRATIQUE)

    repl={'%HERO%':IMG['hero'],'%STRIP%':strip,'%ESS%':ess,'%TABS_BTN%':tabs_btn,'%PINS%':pins,
        '%TABS_CONTENT%':tabs_content,'%DISHES%':dishes,'%BAR%':bar,'%AV_LABEL%':av[0],'%AV_TEXT%':av[1],
        '%SAISON_JS%':saison_js,'%PRAT%':prat}
    html=TEMPLATE
    for k,v in repl.items(): html=html.replace(k,v)
    open('japan.html','w').write(html)
    print('japan.html écrit,', len(html), 'octets')

TEMPLATE = r'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Japon — Le Pays du Soleil Levant</title>
<meta name="description" content="Guide de voyage interactif sur le Japon : régions, cuisine, saisons et informations pratiques pour préparer son séjour.">
<meta property="og:title" content="Japon — Le Pays du Soleil Levant">
<meta property="og:description" content="Guide de voyage interactif : régions, cuisine, saisons et conseils pratiques.">
<meta property="og:type" content="website">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Sarabun:wght@200;300;400&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --red: #BC002D; --red-light: #E4546B; --sakura: #F3B6C2;
    --indigo: #1B2440; --night: #0E1322; --deep: #0E1322;
    --text: #232733; --bg: #F7F3EC;
  }
  html { scroll-behavior: smooth; }
  body { font-family: 'Sarabun', sans-serif; background: var(--bg); color: var(--text); overflow-x: hidden; }

  /* HERO */
  .hero { height: 100vh; background: linear-gradient(160deg, #0E1322 0%, #1B2440 45%, #3A2138 74%, #BC002D 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; overflow: hidden; }
  .hero::before { content: ''; position: absolute; inset: 0; background: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23F3B6C2' fill-opacity='0.06'%3E%3Ccircle cx='20' cy='20' r='3'/%3E%3C/g%3E%3C/svg%3E"); animation: drift 40s linear infinite; }
  @keyframes drift { from { transform: translateX(0) translateY(0); } to { transform: translateX(40px) translateY(40px); } }
  .jp-flag { width: 120px; height: 80px; margin-bottom: 2rem; border-radius: 4px; background: #fff; box-shadow: 0 8px 32px rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center; animation: fadeUp 1s ease both; }
  .jp-flag .sun { width: 46px; height: 46px; border-radius: 50%; background: var(--red); }
  .hero-eyebrow { font-weight: 200; font-size: 0.75rem; letter-spacing: 0.4em; text-transform: uppercase; color: var(--sakura); margin-bottom: 1rem; animation: fadeUp 1s 0.2s ease both; opacity: 0; }
  .hero-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(3.5rem, 10vw, 8rem); font-weight: 300; color: white; text-align: center; line-height: 0.9; animation: fadeUp 1s 0.4s ease both; opacity: 0; }
  .hero-title em { color: var(--red-light); font-style: italic; }
  .hero-subtitle { font-family: 'Cormorant Garamond', serif; font-style: italic; color: var(--sakura); font-size: 1.2rem; margin-top: 1.5rem; animation: fadeUp 1s 0.6s ease both; opacity: 0; }
  .hero > .scroll-cue { position: absolute; bottom: 2rem; left: 0; right: 0; margin-inline: auto; width: max-content; display: flex; flex-direction: column; align-items: center; gap: 0.5rem; color: var(--sakura); font-size: 0.72rem; letter-spacing: 0.3em; text-transform: uppercase; text-decoration: none; cursor: pointer; animation: fadeUp 1s 1s ease both; opacity: 0; transition: color 0.3s; }
  .scroll-cue:hover { color: white; }
  .scroll-line { width: 1px; height: 32px; background: linear-gradient(to bottom, var(--sakura), transparent); animation: pulse 2s ease-in-out infinite; }
  .scroll-arrow { font-size: 1.2rem; line-height: 1; animation: bob 1.6s ease-in-out infinite; }
  @keyframes bob { 0%,100% { transform: translateY(0); } 50% { transform: translateY(6px); } }
  @keyframes pulse { 0%,100%{opacity:0.3} 50%{opacity:1} }
  @keyframes fadeUp { from{opacity:0;transform:translateY(24px)} to{opacity:1;transform:translateY(0)} }

  nav { position: sticky; top: 0; z-index: 100; background: rgba(14,19,34,0.95); backdrop-filter: blur(8px); padding: 1rem 2rem; display: flex; align-items: center; justify-content: center; gap: 2.5rem; border-bottom: 1px solid rgba(243,182,194,0.25); }
  nav a { font-size: 0.7rem; letter-spacing: 0.3em; text-transform: uppercase; color: rgba(255,255,255,0.6); text-decoration: none; transition: color 0.3s; cursor: pointer; }
  nav a:hover { color: var(--red-light); }

  section { padding: 6rem 2rem; max-width: 1200px; margin: 0 auto; }
  .section-label { font-size: 0.65rem; letter-spacing: 0.4em; text-transform: uppercase; color: var(--red); margin-bottom: 0.75rem; }
  .section-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 300; line-height: 1.1; margin-bottom: 2rem; color: var(--deep); }
  .section-title em { color: var(--red); font-style: italic; }
  .divider { width: 60px; height: 2px; background: linear-gradient(to right, var(--red), transparent); margin-bottom: 2.5rem; }

  .essentials-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 3rem; }
  .card { background: white; border: 1px solid rgba(188,0,45,0.15); padding: 2rem; border-radius: 2px; transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s; position: relative; overflow: hidden; }
  .card::before { content: ''; position: absolute; top: 0; left: 0; width: 3px; height: 0; background: var(--red); transition: height 0.4s ease; }
  .card:hover::before { height: 100%; }
  .card:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(188,0,45,0.12); border-color: var(--red); }
  .card-icon { font-size: 2rem; margin-bottom: 1rem; }
  .card h3 { font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; margin-bottom: 0.5rem; font-weight: 400; }
  .card p { font-size: 0.9rem; line-height: 1.7; color: #555a66; font-weight: 300; }

  .tabs { display: flex; gap: 0; border-bottom: 1px solid rgba(243,182,194,0.3); margin-bottom: 2.5rem; overflow-x: auto; }
  .tab-btn { padding: 0.75rem 1.5rem; background: none; border: none; cursor: pointer; font-family: 'Sarabun', sans-serif; font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: #9aa0b0; border-bottom: 2px solid transparent; margin-bottom: -1px; transition: all 0.3s; white-space: nowrap; }
  .tab-btn.active { color: var(--red-light); border-bottom-color: var(--red-light); }
  .tab-btn:hover { color: var(--red-light); }
  .tab-content { display: none; }
  .tab-content.active { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: start; animation: fadeIn 0.4s ease; }
  @keyframes fadeIn { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
  .region-text h3 { font-family: 'Cormorant Garamond', serif; font-size: 2rem; font-weight: 300; margin-bottom: 1rem; }
  .region-text p { font-size: 0.95rem; line-height: 1.9; font-weight: 300; margin-bottom: 1rem; }
  .highlights { list-style: none; margin-top: 1.5rem; }
  .highlights li { padding: 0.6rem 0; border-bottom: 1px solid rgba(243,182,194,0.2); font-size: 0.9rem; display: flex; align-items: center; gap: 0.75rem; }
  .highlights li::before { content: '—'; color: var(--sakura); font-weight: 300; }

  .region-visual { border-radius: 2px; height: 440px; position: sticky; top: 5rem; overflow: hidden; background: #0E1322; }
  .region-visual img { width: 100%; height: 100%; object-fit: cover; position: absolute; inset: 0; transition: transform 0.6s ease, opacity 0.4s ease; opacity: 0; }
  .region-visual img.loaded { opacity: 1; }
  .region-visual:hover img { transform: scale(1.06); }
  .region-visual::before { content: ''; position: absolute; inset: 0; background: linear-gradient(to top, rgba(14,19,34,0.85) 0%, rgba(14,19,34,0.1) 60%); z-index: 1; }
  .region-visual::after { content: attr(data-label); position: absolute; bottom: 1.5rem; left: 1.5rem; font-size: 0.65rem; letter-spacing: 0.3em; text-transform: uppercase; color: var(--sakura); z-index: 2; }
  .region-photo-credit { position: absolute; bottom: 1.5rem; right: 1rem; font-size: 0.55rem; color: rgba(255,255,255,0.3); z-index: 2; letter-spacing: 0.05em; }

  .dish-card { position: relative; overflow: hidden; min-height: 280px; border-radius: 2px; background: linear-gradient(135deg, #1B2440, #0E1322); }
  .dish-photo { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease, opacity 0.4s; opacity: 0; }
  .dish-photo.loaded { opacity: 1; }
  .dish-card:hover .dish-photo { transform: scale(1.08); }
  .dish-overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(8,10,18,0.95) 0%, rgba(8,10,18,0.4) 50%, rgba(8,10,18,0.1) 100%); z-index: 1; }
  .dish-content { position: absolute; bottom: 0; left: 0; right: 0; padding: 1.5rem; z-index: 2; transition: transform 0.3s ease; }
  .dish-card:hover .dish-content { transform: translateY(-4px); }
  .cuisine-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 1.5rem; margin-top: 3rem; }
  .dish-card h4 { font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 400; margin-bottom: 0.3rem; color: var(--sakura); }
  .dish-card .origin { font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(255,255,255,0.45); margin-bottom: 0.6rem; }
  .dish-card p { font-size: 0.85rem; line-height: 1.7; color: rgba(255,255,255,0.65); font-weight: 300; }

  .hero > .hero-photo-bg { position: absolute; inset: 0; z-index: 0; }
  .hero-photo-bg img { width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 1.5s ease; }
  .hero-photo-bg img.loaded { opacity: 0.28; }
  .hero > * { z-index: 1; position: relative; }

  .photo-strip { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 6px; margin-top: 3rem; height: 280px; border-radius: 2px; overflow: hidden; }
  .photo-strip-item { position: relative; overflow: hidden; background: #0E1322; }
  .photo-strip-item img { width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 0.6s ease, transform 0.5s ease; }
  .photo-strip-item img.loaded { opacity: 1; }
  .photo-strip-item:hover img { transform: scale(1.07); }
  .photo-strip-item .strip-label { position: absolute; bottom: 0.75rem; left: 0.75rem; font-size: 0.6rem; letter-spacing: 0.25em; text-transform: uppercase; color: rgba(255,255,255,0.85); background: rgba(0,0,0,0.4); padding: 0.2rem 0.5rem; border-radius: 1px; backdrop-filter: blur(4px); }
  @media (max-width: 600px) { .photo-strip { grid-template-columns: 1fr 1fr; height: 200px; } .photo-strip-item:last-child { display: none; } }

  .pratique-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1px; background: rgba(188,0,45,0.15); border: 1px solid rgba(188,0,45,0.15); margin-top: 3rem; }
  .pratique-item { background: var(--bg); padding: 2rem; }
  .pratique-item h4 { font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; font-weight: 400; margin-bottom: 0.75rem; color: var(--deep); }
  .pratique-item p { font-size: 0.88rem; line-height: 1.7; color: #555a66; font-weight: 300; }

  .saisons-bar { display: grid; grid-template-columns: repeat(12, 1fr); gap: 4px; margin-top: 2rem; margin-bottom: 1rem; }
  .mois { cursor: pointer; border-radius: 2px; padding: 0.5rem 0.25rem; text-align: center; transition: all 0.3s; font-size: 0.65rem; letter-spacing: 0.05em; text-transform: uppercase; font-weight: 300; }
  .mois.saison-printemps { background: #F0A9BC; color: #5a1230; }
  .mois.saison-ete { background: #3FA796; color: white; }
  .mois.saison-automne { background: #D9772B; color: white; }
  .mois.saison-hiver { background: #6E8DC9; color: white; }
  .mois.active { transform: scale(1.1); box-shadow: 0 4px 12px rgba(0,0,0,0.25); }
  .saison-info { background: var(--deep); color: white; padding: 1.5rem 2rem; border-radius: 2px; font-size: 0.9rem; line-height: 1.7; min-height: 80px; transition: all 0.3s; }
  .saison-info strong { color: var(--sakura); }
  .legende { display: flex; gap: 2rem; margin-top: 1rem; flex-wrap: wrap; }
  .legende-item { display: flex; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: #555a66; }
  .legende-dot { width: 12px; height: 12px; border-radius: 2px; }

  footer { background: var(--deep); padding: 3rem 2rem; text-align: center; }
  .footer-title { font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; font-weight: 300; color: white; margin-bottom: 0.5rem; }
  footer p { font-size: 0.8rem; color: rgba(255,255,255,0.35); letter-spacing: 0.2em; }

  .full-bleed { background: linear-gradient(135deg, #0E1322 0%, #1B2440 100%); padding: 5rem 2rem; }
  .full-bleed .section-title { color: white; }
  .full-bleed .region-text h3 { color: #fff; }
  .full-bleed .region-text p { color: rgba(255,255,255,0.82); }
  .full-bleed .highlights li { color: rgba(255,255,255,0.92); border-bottom-color: rgba(243,182,194,0.35); font-size: 0.95rem; cursor: pointer; flex-wrap: wrap; transition: color .25s, border-color .25s; }
  .full-bleed .highlights li::before { color: var(--sakura); align-self: flex-start; }
  .full-bleed .highlights li .li-head { flex: 1; display: flex; align-items: center; justify-content: space-between; gap: .5rem; }
  .full-bleed .highlights li .li-head::after { content: '▾'; color: var(--sakura); font-size: .75rem; opacity: .7; transition: transform .25s; }
  .full-bleed .highlights li.sel .li-head::after { transform: rotate(180deg); }
  .full-bleed .highlights li .li-desc { flex-basis: 100%; max-height: 0; overflow: hidden; opacity: 0; font-size: .82rem; line-height: 1.6; color: rgba(255,255,255,0.72); transition: max-height .3s ease, opacity .3s ease, margin-top .3s ease; }
  .full-bleed .highlights li.sel .li-desc { max-height: 160px; opacity: 1; margin-top: .5rem; }
  .full-bleed .highlights li:hover { color: #fff; border-bottom-color: var(--sakura); }
  .full-bleed .highlights li.sel { color: var(--sakura); }
  .full-bleed .highlights li.sel::before { content: '▸'; }
  .full-bleed section { max-width: 1200px; margin: 0 auto; }

  .map-caption { text-align: center; font-size: 0.72rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--sakura); margin-bottom: 1.5rem; }
  .jp-map { position: relative; width: 100%; max-width: 420px; margin: 0 auto 3.5rem; }
  .jp-map-img { width: 100%; height: auto; display: block; opacity: 0; transition: opacity 0.6s ease; filter: drop-shadow(0 0 22px rgba(188,0,45,0.4)); }
  .jp-map-img.loaded { opacity: 1; }
  .map-pin { position: absolute; transform: translate(-50%, -50%); display: flex; flex-direction: column; align-items: center; gap: 0.3rem; background: none; border: none; padding: 0; cursor: pointer; }
  .map-pin-dot { width: 13px; height: 13px; border-radius: 50%; background: #fff; border: 2px solid #0E1322; box-shadow: 0 0 0 0 rgba(255,255,255,0.6); animation: pinPulse 2.6s ease-out infinite; transition: transform 0.2s, background 0.2s; }
  .map-pin-label { font-size: 0.6rem; letter-spacing: 0.12em; text-transform: uppercase; color: #fff; white-space: nowrap; text-shadow: 0 1px 5px rgba(0,0,0,0.9), 0 0 2px rgba(0,0,0,0.9); }
  .map-pin:hover .map-pin-dot, .map-pin:focus-visible .map-pin-dot { background: var(--sakura); transform: scale(1.3); }
  .map-pin:hover .map-pin-label, .map-pin:focus-visible .map-pin-label { color: var(--sakura); }
  @keyframes pinPulse { 0% { box-shadow: 0 0 0 0 rgba(255,255,255,0.5); } 70% { box-shadow: 0 0 0 12px rgba(255,255,255,0); } 100% { box-shadow: 0 0 0 0 rgba(255,255,255,0); } }

  @media (max-width: 768px) { .tab-content.active { grid-template-columns: 1fr; } .region-visual { height: 260px; position: static; } }
  @media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; } }

  .collection-bar { position: absolute; top: 0; left: 0; right: 0; z-index: 50; display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; padding: 1.1rem 1.6rem; font-size: 0.68rem; letter-spacing: 0.18em; text-transform: uppercase; }
  .collection-bar a { text-decoration: none; }
  .cb-brand { color: #fff; font-weight: 600; text-shadow: 0 1px 6px rgba(0,0,0,0.6); }
  .cb-links a { color: rgba(255,255,255,0.72); margin-left: 1.25rem; text-shadow: 0 1px 6px rgba(0,0,0,0.6); transition: color 0.3s; }
  .cb-links a:first-child { margin-left: 0; }
  .cb-links a:hover, .cb-links a.current { color: #fff; }
  .cb-links a.current { border-bottom: 2px solid currentColor; padding-bottom: 2px; }
</style>
</head>
<body>

<div class="collection-bar">
  <a class="cb-brand" href="index.html">Le savoir est une arme</a>
  <div class="cb-links">
    <a href="thailand.html">Thaïlande</a>
    <a href="japan.html" class="current">Japon</a>
    <a href="ww1-interactive.html">1914–1918</a>
  </div>
</div>

<div class="hero">
  <div class="hero-photo-bg">
    <img src="%HERO%" alt="Mont Fuji et pagode Chureito" fetchpriority="high" decoding="async" onload="this.classList.add('loaded')">
  </div>
  <div class="jp-flag"><div class="sun"></div></div>
  <p class="hero-eyebrow">Guide de voyage interactif</p>
  <h1 class="hero-title">Ja<em>pon</em></h1>
  <p class="hero-subtitle">日本 — Le Pays du Soleil Levant</p>
  <a href="#essentials" class="scroll-cue" aria-label="Faire défiler pour découvrir le guide">
    Faites défiler pour explorer
    <div class="scroll-line"></div>
    <div class="scroll-arrow">↓</div>
  </a>
</div>

<nav>
  <a href="#essentials">Essentiels</a>
  <a href="#regions">Régions</a>
  <a href="#cuisine">Cuisine</a>
  <a href="#saisons">Saisons</a>
  <a href="#pratique">Pratique</a>
</nav>

<div id="essentials">
  <section>
    <p class="section-label">01 — En bref</p>
    <h2 class="section-title">Tradition &amp; <em>avant-garde</em></h2>
    <div class="divider"></div>
    <p style="font-size:1.05rem;line-height:1.9;color:#555a66;max-width:680px;font-weight:300;">
      Archipel de plus de 6 800 îles à l'est de l'Asie, le Japon marie comme nul autre tradition et modernité : temples millénaires et néons, cérémonie du thé et robots, cerisiers et gratte-ciel. Quatre saisons franches y rythment une nature spectaculaire et une culture d'un raffinement extrême.
    </p>
    <div class="photo-strip">
%STRIP%
    </div>
    <div class="essentials-grid">
%ESS%
    </div>
  </section>
</div>

<div class="full-bleed" id="regions">
  <section>
    <p class="section-label" style="color:var(--sakura);">02 — Géographie</p>
    <h2 class="section-title">Explorer les <em>régions</em></h2>
    <div class="divider"></div>

    <p class="map-caption">Cliquez une région sur la carte pour la découvrir</p>
    <div class="jp-map">
      <img class="jp-map-img" src="japan-map.svg?v=1" alt="Carte du Japon" loading="lazy" decoding="async" onload="this.classList.add('loaded')">
%PINS%
    </div>

    <div class="tabs">
%TABS_BTN%
    </div>

%TABS_CONTENT%
  </section>
</div>

<div id="cuisine">
  <section>
    <p class="section-label">03 — Gastronomie</p>
    <h2 class="section-title">La cuisine <em>japonaise</em></h2>
    <div class="divider"></div>
    <p style="font-size:1.05rem;line-height:1.9;color:#555a66;max-width:680px;font-weight:300;">
      Inscrite au patrimoine de l'UNESCO, la cuisine japonaise (washoku) célèbre la fraîcheur du produit, la saisonnalité et l'harmonie. Du sushi le plus pur au bol de ramen réconfortant, une quête d'équilibre et de précision.
    </p>
    <div class="cuisine-grid">
%DISHES%
    </div>
  </section>
</div>

<div id="saisons" style="background:white;padding:1px 0;">
  <section>
    <p class="section-label">04 — Météo</p>
    <h2 class="section-title">Quand <em>partir</em> ?</h2>
    <div class="divider"></div>
    <p style="font-size:1rem;line-height:1.9;color:#555a66;max-width:680px;font-weight:300;margin-bottom:2rem;">
      Le Japon vit au rythme de quatre saisons très marquées. Cliquez sur un mois pour découvrir les conditions.
    </p>
    <div class="saisons-bar">
%BAR%
    </div>
    <div class="saison-info" id="saison-info">
      <strong>%AV_LABEL%</strong><br>
      %AV_TEXT%
    </div>
    <div class="legende">
      <div class="legende-item"><div class="legende-dot" style="background:#F0A9BC;"></div> Printemps — cerisiers (idéal)</div>
      <div class="legende-item"><div class="legende-dot" style="background:#3FA796;"></div> Été — chaud &amp; humide</div>
      <div class="legende-item"><div class="legende-dot" style="background:#D9772B;"></div> Automne — kōyō (idéal)</div>
      <div class="legende-item"><div class="legende-dot" style="background:#6E8DC9;"></div> Hiver — neige &amp; onsen</div>
    </div>
  </section>
</div>

<div id="pratique" style="background:var(--bg);">
  <section>
    <p class="section-label">05 — Informations pratiques</p>
    <h2 class="section-title">Avant de <em>partir</em></h2>
    <div class="divider"></div>
    <div class="pratique-grid">
%PRAT%
    </div>
  </section>
</div>

<footer>
  <div class="footer-title">こんにちは — Konnichiwa</div>
  <p>« Au pays du soleil levant, la beauté se niche dans le moindre détail. »</p>
  <br>
  <p style="font-size:0.65rem;opacity:0.3;">Guide interactif · Japon © 2026</p>
</footer>

<script>
  function showTab(name, btn) {
    document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); });
    document.getElementById('tab-' + name).classList.add('active');
    if (!btn) btn = document.querySelector('.tab-btn[data-tab="' + name + '"]');
    if (btn) { btn.classList.add('active'); btn.setAttribute('aria-selected', 'true'); }
  }

  document.querySelectorAll('.highlights li[data-img]').forEach(li => {
    li.setAttribute('role', 'button');
    li.setAttribute('tabindex', '0');
    const show = () => {
      const alreadyOpen = li.classList.contains('sel');
      li.parentNode.querySelectorAll('li').forEach(x => x.classList.remove('sel'));
      if (alreadyOpen) return;
      const visual = li.closest('.tab-content').querySelector('.region-visual');
      const img = visual.querySelector('img');
      const credit = visual.querySelector('.region-photo-credit');
      const src = li.getAttribute('data-img');
      const label = (li.querySelector('.li-head') || li).textContent.trim();
      const pre = new Image();
      pre.onload = () => {
        img.src = src;
        img.alt = label;
        img.classList.add('loaded');
        visual.setAttribute('data-label', li.getAttribute('data-label'));
        if (credit) credit.textContent = 'Wikimedia Commons';
      };
      pre.src = src;
      li.classList.add('sel');
    };
    li.addEventListener('click', show);
    li.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); show(); } });
  });

  document.querySelectorAll('.tab-btn').forEach(b => b.setAttribute('aria-selected', b.classList.contains('active') ? 'true' : 'false'));
  document.querySelectorAll('.mois').forEach(m => {
    m.setAttribute('role', 'button'); m.setAttribute('tabindex', '0');
    m.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); m.click(); } });
  });

  const saisonData = {
%SAISON_JS%
  };
  function showMois(el, key) {
    document.querySelectorAll('.mois').forEach(m => m.classList.remove('active'));
    el.classList.add('active');
    const d = saisonData[key];
    const info = document.getElementById('saison-info');
    info.style.opacity = 0;
    setTimeout(() => { info.innerHTML = '<strong>' + d.label + '</strong><br>' + d.text; info.style.opacity = 1; }, 200);
    info.style.transition = 'opacity 0.2s';
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.style.animation = 'fadeUp 0.6s ease both'; });
  }, { threshold: 0.1 });
  document.querySelectorAll('.card, .dish-card, .pratique-item').forEach(el => { el.style.opacity = 0; observer.observe(el); });
</script>
</body>
</html>'''

if __name__=='__main__':
    if '--verify' in sys.argv:
        bad=verify()
        if bad:
            print('IMAGES KO:')
            for k,c,u in bad: print(' ',k,c,u)
        else:
            print('Toutes les images OK (200)')
    else:
        build()
