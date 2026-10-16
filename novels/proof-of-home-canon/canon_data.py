"""
canon_data.py - single source of truth for the novel "Proof of Home"
(slow-burn small-town cozy fantasy romance). FULL REDO, version 3.

THE BOOK IS ONE THING: two people who want each other and cannot yet touch.
No votes, counts, ledgers, money plot or council business. Every chapter raises
the ache by one notch. The first kiss lands in chapter 27 of 32.

TIME: no dates, no weekdays, no ages in digits, no "three days later". Time is
shown only by a season marker, light, weather and the bread.

RULES
- Everything is data. Edit this file, never the generated files.
- Text fields are in-world facts only. Never write: Book N, the series,
  protagonist, sub-beat, Wound:, Competence:, [End of Chapter.

STATUS: DRAFT. Pen name, genre and all proposals are NOT yet approved by Zia.
"""

SERIES_SLUG = "larkmere"
BOOK_TITLE = "Proof of Home"
PEN_NAME = "Elif Kessler"   # proposal only; canon does not depend on it
TOWN = "Larkmere"           # working name; fictional lakeside town
LAKE = "Larkmere Water"     # working name of the lake
CHAPTER_COUNT = 32
WORDS_MIN, WORDS_MAX = 2300, 2700
KISS_CHAPTER = 27           # 27 of 32 = 84 percent, inside the 80-85 window

SEASONS = [
    "early spring", "spring", "late spring", "early summer", "midsummer",
    "high summer", "late summer", "early autumn", "autumn", "last of autumn",
]

# ---------- Cast (ages are fixed phrases, never computed) ----------
CAST = {
    "Sarah Quill": {
        "role": "baker, heroine, point of view in odd chapters",
        "age": "early thirties",
        "desc": "Runs the bakery on Lantern Street. Came back to Larkmere when her great-aunt Fenna Quill died and left her the shop. Her bread carries whatever she feels while shaping it. She promised herself one season, then she would decide whether to stay.",
    },
    "Jack Mercer": {
        "role": "ferryman, hero, point of view in even chapters",
        "age": "mid thirties",
        "desc": "Pilots the ferry Heron across Larkmere Water. Quiet, dry humor, steady hands. Believes the ferry is the only place he is allowed to be sure of himself. Notices what people carry and never says it first.",
    },
    "Odalys Pike": {
        "role": "innkeeper, Sarah's friend",
        "age": "late thirties",
        "desc": "Runs the Lamplight Inn, reads faces, teases Sarah without mercy. Wants her friend happy and cannot keep that to herself.",
    },
    "Wren Mercer": {
        "role": "Jack's niece, deckhand",
        "age": "sixteen",
        "desc": "Works the lines on the ferry. Sharp, loyal, sees everything between her uncle and the baker long before either admits it. Only ever meddles, never anywhere near the intimate moments.",
    },
    "Gideon Teague": {
        "role": "old townsman, lantern keeper",
        "age": "past seventy",
        "desc": "Lights the harbor lanterns each dusk. Knew Fenna Quill for fifty years. Speaks little, and what he says tends to matter.",
    },
    "Fenna Quill": {
        "role": "Sarah's great-aunt, deceased before the story opens",
        "age": "died in her eighties",
        "desc": "Baked in the shop for sixty years. Her recipes are written in a margin language of small marks that Sarah is slowly learning to read.",
    },
}

# ---------- World rules (the engine of the ache) ----------
WORLD_RULES = [
    "Sarah's bread carries the feeling she has while shaping it. Calm hands make calm bread. Longing makes bread that makes whoever eats it ache and look toward the water.",
    "A kiss given in love sets a loaf's feeling for good. Sarah fears that if she kisses Jack, every loaf she bakes will say it aloud to the whole town, and she will have lost the choice of when and how to tell anyone.",
    "Jack believes the ferry keeps its people. Fenna loved a ferryman once, and he left on the last run of a season. Jack will not ask Sarah to stay because he thinks wanting her to stay is the same as trapping her.",
    "The Heron will not carry a lie across the water. It drifts slow and sulks when anyone aboard hides what they feel. The more they hide, the later the crossing.",
    "Harbor lanterns are lit at dusk. Whoever stands at the same lantern when it catches is said to be thinking of the same person.",
]

# ---------- Touch ladder ----------
TOUCH_LADDER = {
    0: "no touch, only awareness",
    1: "a look held one second too long",
    2: "fingers brush during a handover",
    3: "a deliberate small touch: flour wiped from a cheek, a collar fixed",
    4: "a steadying grip, or bodies forced together in a tight space",
    5: "a shared coat or crowd, bodies pressed along their length",
    6: "held hands, or sitting wrapped together",
    7: "foreheads together, breath shared, no kiss",
    8: "the almost-kiss, interrupted by feeling and never by business",
    9: "the first kiss",
    10: "the aftermath: lovers who finally get to touch, and the question of staying",
}

# ---------- Chapter plan ----------
# pov: S = Sarah, J = Jack.  rung: highest touch rung reached.
# reason: why they cannot act, one of public / magic / alone / weather.
# "alone" is the cruelest: nobody stops them and they hold back anyway.
# bread: what Sarah's bread does, so the magic shows every chapter.
CHAPTERS = [
    {"n": 1, "pov": "S", "season": "early spring", "rung": 0, "reason": "public",
     "ache": "a stranger noticed her",
     "beat": "Sarah reopens Fenna's bakery and sends the first loaf across on the Heron. Jack takes it from her hands without a word. From the dock she watches him eat it on the deck, still, as if the loaf had named a loneliness he knew.",
     "space": "dock gangway", "contact": "none, only the weight of the loaf passing hands",
     "restraint": "she keeps her hands very still around the cloth; he keeps his eyes on the bread",
     "bread": "the first loaf carries her loneliness"},
    {"n": 2, "pov": "J", "season": "early spring", "rung": 0, "reason": "alone",
     "ache": "he is curious against his will",
     "beat": "Jack cannot get the taste out of his head. He starts timing his crossings to pass Lantern Street. Wren notices and says nothing, loudly.",
     "space": "wheelhouse alone", "contact": "none, only the memory of the taste",
     "restraint": "he grips the wheel and tells himself it is only bread",
     "bread": "the taste of her loneliness follows him across the water"},
    {"n": 3, "pov": "S", "season": "early spring", "rung": 1, "reason": "public",
     "ache": "first spark, denied",
     "beat": "Sarah brings a standing order to the dock and Jack looks at her until she has to look away. She goes home and bakes a loaf so distracted it comes out warm and lopsided. Odalys eats a slice at the window and sighs.",
     "space": "crowded dock", "contact": "none, a held look",
     "restraint": "she smiles at the planks and walks away before it shows",
     "bread": "a warm, lopsided loaf that makes Odalys sigh"},
    {"n": 4, "pov": "J", "season": "spring", "rung": 1, "reason": "magic",
     "ache": "he wants a longer crossing",
     "beat": "Jack carries Sarah across as a passenger for the first time. She sits near the rail with a loaf in her lap and the Heron slows for no reason he can name. He catches himself wishing the lake were wider.",
     "space": "ferry rail on a quiet crossing", "contact": "none, her hair lifts toward him in the wind",
     "restraint": "he keeps both hands on the tiller and counts the strokes",
     "bread": "the loaf in her lap hushes the other passengers"},
    {"n": 5, "pov": "S", "season": "spring", "rung": 2, "reason": "public",
     "ache": "one second of skin",
     "beat": "A crate of flour is too heavy for one pair of hands, so they lift it together up the gangplank. Their fingers brush under the edge. She spends the evening not thinking about it and bakes a very honest loaf. Odalys eats it and goes quiet.",
     "space": "gangplank, a crate between them", "contact": "fingers brush under the crate edge",
     "restraint": "she holds on a second longer than needed, then lets go",
     "bread": "an honest loaf that quiets Odalys"},
    {"n": 6, "pov": "J", "season": "spring", "rung": 2, "reason": "alone",
     "ache": "he rehearses and fails",
     "beat": "Jack replays the brush of her fingers all night and takes the long way round the island on the morning run. He rehearses a sentence for Sarah and loses it the moment he sees her at the shop door.",
     "space": "empty deck at dawn, then the shop doorway", "contact": "none, only the memory of her fingers",
     "restraint": "he scrubs the deck until his arms ache to wear the thought down",
     "bread": "a heel of her crust on his bench that he cannot finish"},
    {"n": 7, "pov": "S", "season": "spring", "rung": 1, "reason": "alone",
     "ache": "a shadow behind the sweetness",
     "beat": "Sarah finds a note of Fenna's about a ferryman, written in the margin language. She cannot read all of it. She is startled to find she hopes he is not anyone of Jack's family.",
     "space": "the loft over the shop", "contact": "none, only Fenna's paper under her palm",
     "restraint": "she presses her hand flat to the page to keep it from trembling",
     "bread": "the loaf that morning is bittersweet and no one finishes it"},
    {"n": 8, "pov": "J", "season": "late spring", "rung": 3, "reason": "alone",
     "ache": "the first deliberate touch",
     "beat": "Jack drops the evening order at the shop's back door in the narrow alley. There is flour on her cheek. He wipes it with his thumb before he can think. They both freeze, her lips parted, his hand still raised. She says thank you too quietly.",
     "space": "the narrow back alley behind the shop", "contact": "his thumb on her cheek",
     "restraint": "he withdraws the hand and shoves it in his pocket; she stands motionless, breathing carefully",
     "bread": "the loaf in her hands warms as he touches her"},
    {"n": 9, "pov": "S", "season": "late spring", "rung": 3, "reason": "alone",
     "ache": "night hunger",
     "beat": "Sarah cannot sleep and shapes dough at midnight. Jack, sleepless too, sees the oven glow from the street. She lets him in for one minute. They stand shoulder to shoulder at the oven door for its warmth, neither speaking. The minute turns into an hour.",
     "space": "bakery at midnight, a narrow strip of floor by the oven door", "contact": "shoulder to shoulder at the oven's heat",
     "restraint": "she kneads harder; he studies the fire; neither turns their head",
     "bread": "loaves too hot to hold, scorched with feeling"},
    {"n": 10, "pov": "J", "season": "late spring", "rung": 2, "reason": "magic",
     "ache": "he tries to retreat and cannot",
     "beat": "Jack stays away from the bakery for three days and the Heron sulks without reason. Wren finally tells him what he already knows and sends him with a delivery nobody ordered.",
     "space": "the sulking ferry wheelhouse", "contact": "none, absence is the ache",
     "restraint": "he stays at the wheel and pretends the delivery is nothing",
     "bread": "a loaf she sent over days ago still sits uneaten on his shelf"},
    {"n": 11, "pov": "S", "season": "late spring", "rung": 2, "reason": "alone",
     "ache": "easy, then suddenly not easy",
     "beat": "The delivery turns out to be nothing, and they both know it. They talk in the empty shop for an hour with the counter between them and the lamp low. When he leaves she realizes she has been smiling the whole time.",
     "space": "empty shop, one counter between them", "contact": "none, both their hands near on the counter edge",
     "restraint": "they lean on opposite sides and neither closes the gap",
     "bread": "easy bread that rises tall overnight"},
    {"n": 12, "pov": "J", "season": "late spring", "rung": 3, "reason": "weather",
     "ache": "almost invited in",
     "beat": "A storm keeps the ferry docked. Jack walks Sarah home through a lane so narrow they cannot walk anything but close, the hem of her coat caught round his wrist. He leaves her at her door without a word and walks back soaked and happy.",
     "space": "narrow lane in the rain", "contact": "arm against arm all the way, her coat hem tangled on his wrist",
     "restraint": "he stops on her step and does not say what he wants to say",
     "bread": "the loaf she carries stays warm in the rain"},
    {"n": 13, "pov": "S", "season": "early summer", "rung": 3, "reason": "public",
     "ache": "she touched him on purpose",
     "beat": "In the queue for the morning crossing Sarah fixes his collar while he is talking to a fisherman. Her knuckles brush his throat. He stops mid-sentence. She walks away fast and bakes three loaves in a row that make Odalys cry and laugh at once.",
     "space": "the ferry queue, passengers close behind them", "contact": "her knuckles at his throat",
     "restraint": "he forgets to breathe; she leaves before her hands start shaking",
     "bread": "three loaves in a row that make Odalys cry and laugh"},
    {"n": 14, "pov": "J", "season": "early summer", "rung": 4, "reason": "weather",
     "ache": "held, and neither lets go first",
     "beat": "Wind catches the Heron and Sarah stumbles on the deck. Jack's hand closes round her forearm and he holds her upright well past steady, his chest at her shoulder. She looks at his mouth. The boat drifts.",
     "space": "pitching deck, one rail to hold", "contact": "his hand round her forearm, his chest at her shoulder",
     "restraint": "he holds her upright and neither says let go",
     "bread": "the loaf she carried is crushed between them and neither mentions it"},
    {"n": 15, "pov": "S", "season": "early summer", "rung": 4, "reason": "alone",
     "ache": "the want gets a name",
     "beat": "Jack carries flour sacks through the narrow back passage while Sarah squeezes by with a hot tray held high. They stick fast, hips pressed, her arms raised and unable to move. Neither says a word until the tray begins to cool.",
     "space": "bakery back passage between the ovens and the flour racks", "contact": "hips and shoulders pressed, a hot tray held high between them",
     "restraint": "he stops with his back to the rack and does not breathe; she turns sideways and waits",
     "bread": "the tray's loaves all rise at once"},
    {"n": 16, "pov": "J", "season": "early summer", "rung": 3, "reason": "alone",
     "ache": "fear arrives in the middle of happiness",
     "beat": "Jack sits on Gideon's lantern steps and asks about Fenna and the old ferryman. Gideon tells him only part of it, enough to frighten him. Jack decides, quietly, that he will never ask Sarah to stay.",
     "space": "the lantern keeper's steps at dusk", "contact": "none, only Gideon's story between them",
     "restraint": "he sits with his hands locked between his knees",
     "bread": "Gideon shares a heel of Fenna's old recipe, and it tastes of leaving"},
    {"n": 17, "pov": "S", "season": "midsummer", "rung": 3, "reason": "public",
     "ache": "both thinking of the same person",
     "beat": "Midsummer lantern evening. Sarah and Jack stand at the same lantern when it catches and both understand the old custom at once. They say nothing. They stand half a step apart through the whole lighting, and the crowd shifts and presses their shoulders together.",
     "space": "the harbor lantern crowd", "contact": "half a step apart, then shoulders touching as the crowd shifts",
     "restraint": "neither closes the half step",
     "bread": "her lantern buns make every couple in the lane stand closer"},
    {"n": 18, "pov": "J", "season": "high summer", "rung": 4, "reason": "public",
     "ache": "cold after warmth",
     "beat": "Jack grows stiff and careful with her. On a crowded market-day crossing the passengers jam together and Sarah is shoved against his arm for the whole lake. He talks about the weather. She stays pressed against him and says nothing. That night her loaves come out dense and grey. Wren tells him he is an idiot.",
     "space": "a packed market-day ferry", "contact": "her shoulder hard against his arm the whole crossing",
     "restraint": "he talks about the weather and does not look down",
     "bread": "dense grey loaves he cannot eat"},
    {"n": 19, "pov": "S", "season": "high summer", "rung": 2, "reason": "public",
     "ache": "the first real hurt",
     "beat": "Sarah faces him on the dock, not with blame but with one honest sentence about missing him. He answers badly. She leaves. He stands holding a loaf that tastes of nothing he can name and everything he wants.",
     "space": "the dock, fishermen coiling lines nearby", "contact": "none, her hand stops an inch from his sleeve",
     "restraint": "she lowers the hand and walks away without looking back",
     "bread": "a loaf that tastes of nothing, held in his hands"},
    {"n": 20, "pov": "J", "season": "high summer", "rung": 4, "reason": "alone",
     "ache": "one inch of air",
     "beat": "Jack comes to the bakery at closing and says the true sentence: he cannot make her stay and he is afraid of wanting it. She tells him to stop deciding for her. The lamp gutters on the narrow cellar stairs. They end up close enough to feel each other breathe, and do not touch.",
     "space": "the narrow back stairs to the flour cellar, one dim lamp", "contact": "close enough to feel each other breathe, no touch",
     "restraint": "his fists at his sides; her fingers locked behind her back",
     "bread": "the cellar smells of yeast and warm wood and nothing is said about it"},
    {"n": 21, "pov": "S", "season": "high summer", "rung": 5, "reason": "weather",
     "ache": "heat through wet fabric",
     "beat": "A summer downpour catches them on the way to the harbor and they share her one coat, hips and shoulders pressed. The walk is slow because neither wants it to end. At her door she says goodnight to his chin.",
     "space": "one coat in the rain", "contact": "shoulders and hips pressed side by side the whole walk",
     "restraint": "they slow the pace and say nothing, both feeling every step",
     "bread": "the bread in her basket stays dry and warm beneath the coat"},
    {"n": 22, "pov": "J", "season": "late summer", "rung": 5, "reason": "public",
     "ache": "closeness as torment",
     "beat": "Late-summer lantern night. The whole town packs the harbor lanes and Wren steers them into the narrowest one. Sarah is pressed against Jack's front for the whole slow walk to the pier. Neither speaks. He grips the rail until his knuckles ache and counts the lanterns to stay upright. Her breath comes short and she does not move away.",
     "space": "the narrowest lantern lane, crowd packed tight", "contact": "her back against his front, hips joined, for the whole slow walk",
     "restraint": "he grips the rail and counts lanterns; she keeps her eyes ahead and her breath short, and neither turns",
     "bread": "next morning her bread gives her away to Odalys at the first bite"},
    {"n": 23, "pov": "S", "season": "late summer", "rung": 6, "reason": "magic",
     "ache": "hands, and then not hands",
     "beat": "On the long dusk crossing he takes her hand and she lets him. They hold hands across the whole width of the lake with their eyes fixed forward, and the Heron goes slow. At the far dock he lets go and she misses his palm like a lost limb.",
     "space": "the stern bench at dusk", "contact": "hands joined, thighs together",
     "restraint": "eyes fixed forward; he lets go at the far dock and curls his empty hand",
     "bread": "the loaf on her knee grows warm and then, when he lets go, cools"},
    {"n": 24, "pov": "J", "season": "late summer", "rung": 6, "reason": "magic",
     "ache": "marooned and happy",
     "beat": "The Heron stops mid-lake after dark and will not move until dawn. Jack and Sarah wait it out in the cramped wheelhouse under one blanket, shoulder to shoulder, hands joined. Neither sleeps. He feels every breath she takes. At dawn the Heron starts as if nothing happened.",
     "space": "the cramped wheelhouse mid-lake, one blanket", "contact": "shoulders, hips and thighs along each other's length, hands joined",
     "restraint": "he stares at the black water and says her name once, softly; she does not answer, only tightens her hold",
     "bread": "the loaf they share goes cold and neither cares"},
    {"n": 25, "pov": "S", "season": "early autumn", "rung": 7, "reason": "alone",
     "ache": "an inch from the mouth",
     "beat": "Sarah reads the last of Fenna's margin note and learns the old ferryman left because he thought it was kind. She brings the truth to Jack in the dark bakery. He rests his forehead against hers and they breathe the same air for a long time. He does not kiss her and she does not ask him to.",
     "space": "the dark bakery, the narrow back passage again", "contact": "foreheads together, bodies a breath apart",
     "restraint": "he keeps his eyes closed and does not cross the last inch; she lets him",
     "bread": "Fenna's last loaf, found wrapped in the cupboard, tastes of a goodbye she wished she had refused"},
    {"n": 26, "pov": "J", "season": "early autumn", "rung": 8, "reason": "magic",
     "ache": "the almost-kiss, ruined by a knock",
     "beat": "Sarah's birthday has just passed and Jack arrives with a loaf he baked himself, badly. They laugh at the brick of it until they are close enough to kiss, knees together under the loft table. Her breath catches, his catches, and a lantern gutters outside. Wren knocks. They pull apart, shaking.",
     "space": "the loft table, knees touching", "contact": "knees against knees, faces close enough to kiss",
     "restraint": "Wren's knock saves them; both pull back shaking",
     "bread": "his terrible loaf tastes of nothing but love"},
    {"n": 27, "pov": "S", "season": "autumn", "rung": 9, "reason": "alone",
     "ache": "release, finally",
     "beat": "The first kiss. Dusk on the Heron mid-lake, no one aboard, the lanterns catching one by one on the shore. Sarah says out loud what she wants and he answers by crossing the last inch. The Heron sails true for the first time all season. In the morning her bread tastes of nothing but joy.",
     "space": "the mid-lake deck at dusk", "contact": "the first kiss, then arms around each other",
     "restraint": "the hold-back becomes the held breath before it",
     "bread": "the morning loaf tastes of joy and the whole lake can tell"},
    {"n": 28, "pov": "J", "season": "autumn", "rung": 10, "reason": "public",
     "ache": "sweetness with a shadow of the end",
     "beat": "The day after is soft and a little shy. The whole town tastes her bread and knows. Jack cannot stop touching her hand in public. Odalys cheers from the inn steps. He realizes he still does not know how to say stay, and loves her too much to try.",
     "space": "the inn steps, then the dock", "contact": "hand in hand in public, her head against his shoulder",
     "restraint": "shy after the kiss; he steps back to let her breathe",
     "bread": "her loaves sing across the lake and every neighbor smiles"},
    {"n": 29, "pov": "S", "season": "autumn", "rung": 10, "reason": "alone",
     "ache": "gentle, honest, unfinished",
     "beat": "Sarah spends a night at his cottage by the water. They hold each other by the stove and kiss slowly and talk until dawn. They choose closeness over more, and wait together. She admits she has not decided about winter and he admits he is afraid of the answer.",
     "space": "his cottage by the water", "contact": "held through the night, kissing slowly by the stove",
     "restraint": "now it is a choice: they wait on purpose, wrapped together",
     "bread": "the loaf she leaves on his table tastes of tenderness and a little fear"},
    {"n": 30, "pov": "J", "season": "last of autumn", "rung": 10, "reason": "alone",
     "ache": "the thing he must say",
     "beat": "The last weeks of the season. Gideon hands Jack the letter Fenna left for whoever loved the ferryman. It says the old ferryman should have asked. Jack goes quiet and takes the Heron out alone. Sarah feels him pull away and her palm on his back stiffens him. The Heron sulks again.",
     "space": "the wheelhouse, alone, then together", "contact": "her palm flat against his back at the wheel",
     "restraint": "he keeps the crossing slow and cannot find the words yet",
     "bread": "her bread tastes of waiting"},
    {"n": 31, "pov": "S", "season": "last of autumn", "rung": 10, "reason": "alone",
     "ache": "chosen, not trapped",
     "beat": "Sarah makes one loaf the night before the last run with every feeling she has in it. She says she is not leaving, and she says it before he can ask. He has to sit down on the dock. She sits beside him.",
     "space": "the dock the night before the last run", "contact": "sitting side by side, his shoulder against hers",
     "restraint": "he stays quiet so she can say it first",
     "bread": "the loaf carries everything and the Heron rocks softly at the dock"},
    {"n": 32, "pov": "J", "season": "last of autumn", "rung": 10, "reason": "public",
     "ache": "home, together, in plain light",
     "beat": "The last ferry run of the season. Jack asks her to stay in plain words. She was already staying. They stand at the lantern together as it catches, no longer half a step apart.",
     "space": "the last lantern at the harbor", "contact": "standing together, no half step between them",
     "restraint": "none left to hold back",
     "bread": "she hands the town a loaf that tastes of home and nobody needs to ask"},
]

# ---------- Hidden-fact schedule (secrets of the heart only) ----------
HIDDEN_FACTS = [
    {"id": "fenna_ferryman", "seed": 7, "reveal": 25,
     "fact": "Fenna's great love was the ferryman before Jack's grandfather. He left on a last run because he thought wanting her to stay was selfish."},
    {"id": "jack_fear", "seed": 2, "reveal": 20,
     "fact": "Jack never asks anyone to stay. His mother left on this ferry when he was a boy."},
    {"id": "sarah_reason", "seed": 1, "reveal": 29,
     "fact": "Sarah left her last city quietly after a long relationship where she had to shrink. She came to Larkmere hoping to be allowed to take up room."},
    {"id": "wren_knows", "seed": 3, "reveal": 22,
     "fact": "Wren has known since the start and has been quietly steering the Heron to put the baker aboard."},
    {"id": "gideon_letter", "seed": 9, "reveal": 30,
     "fact": "Fenna left a letter for whoever fell in love with the ferryman. Gideon has kept it, waiting for the right moment."},
]

# ---------- Romance rules (sent to the writing model) ----------
ROMANCE_RULES = [
    "The love story is the book. Every chapter raises the ache by one notch.",
    "Desire lives in small physical detail: the weight of a hand, the distance between two shoulders, breath on a collar, the pause before a sentence, the effort of staying still.",
    "Pressed closeness (rungs 4 and up) is built from restraint. Show what the body does to hold back: a locked grip, a held breath, eyes fixed on a point, a word not said. Sensual, never explicit.",
    "Never let the obstacle be a meeting, a ruling, a debt, a count or any procedure. Interruptions come from feeling, weather, magic, or a person who loves them.",
    "No dates, weekdays, ages in digits or phrases like three days later. Time is season, light, weather and the bread.",
    "Show the bread magic in every chapter, small and specific.",
    "Do not kiss before chapter 27. Do not let the reader forget they want to.",
    "After the kiss the tension turns to tenderness and the question of staying, never to plot machinery.",
    "Wren never appears in any intimate beat. She only meddles around the edges.",
    "No em dashes. Avoid tidy summary sentences at chapter ends. Let the last image carry the feeling.",
]

# ---------- Self-checks ----------
import re
assert len(CHAPTERS) == CHAPTER_COUNT
assert [c["n"] for c in CHAPTERS] == list(range(1, CHAPTER_COUNT + 1))
assert 0.80 <= KISS_CHAPTER / CHAPTER_COUNT <= 0.85
assert max(c["rung"] for c in CHAPTERS if c["n"] < KISS_CHAPTER) <= 8
assert CHAPTERS[KISS_CHAPTER - 1]["rung"] == 9
assert all(c["season"] in SEASONS for c in CHAPTERS)
order = [SEASONS.index(c["season"]) for c in CHAPTERS]
assert order == sorted(order), "seasons must not go backwards"
assert all(c["reason"] in {"public", "magic", "alone", "weather"} for c in CHAPTERS)
assert sum(1 for c in CHAPTERS if c["n"] >= 8 and c["contact"].startswith("none")) <= 4
_banned = re.compile(r"\b(19|20)\d\d\b|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|days later|\u2014|\bsome(thing|one|where|how)\b|particular|the specific|the kind of|one beat too long")
for c in CHAPTERS:
    for k in ("beat", "ache", "space", "contact", "restraint", "bread"):
        assert not _banned.search(c[k]), (c["n"], k)
