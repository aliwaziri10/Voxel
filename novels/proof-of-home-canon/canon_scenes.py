"""
canon_scenes.py - the scenes of "Proof of Home", chapter by chapter.

Part of the canon, next to canon_data.py (same rules: edit here, never the generated
files, then run build_bible.py). Kept in its own file so canon_data.py stays small.
"""
import re

import canon_data as c

# ---------- Scenes (added 2026-10-16) ----------
# Each chapter is 3 or 4 real scenes, in order. The "beat" above is only the
# summary of them. A chapter reached the word floor only when it had enough real
# scenes to dramatize; one summary paragraph gave the writer one or two scenes
# and chapters came out 850 to 1500 words. These scenes are story events, not
# padding: each one has its own place, action and turn.
SCENES = {
    1: [
        "Before dawn Sarah wakes the starter and shapes the first loaf in Fenna's kitchen, reading the margin marks on the recipe cards one slowly learned mark at a time. Her loneliness goes into the dough without her meaning it to.",
        "She unlocks the shop for the first time since the funeral and sells a few rolls to the first customers. From the doorway she watches the Heron wait at the gangway and the ferryman who never turns his head.",
        "She carries the first loaf down to the dock and puts it in Jack's hands. He says nothing. From the gangway she watches him eat it on the deck, and the Heron pulls away.",
        "Gideon comes down the steps with his lantern pole and tells her the bread has told the ferryman what he was waiting to hear. She answers that she promised herself one season.",
    ],
    2: [
        "On the morning run Jack cannot lose the taste of her bread. He takes the Heron across with both hands hard on the wheel and the taste still on his tongue.",
        "He starts shortening and lengthening his crossings so the Heron passes the end of Lantern Street when the bakery door opens, and tells himself it is for the tide.",
        "Nell watches him look at the harbor clock a third time. She coils the rope too neatly and hums one note and says nothing, loudly.",
        "That night alone in the wheelhouse he finds the last crumb of crust in his jacket pocket and cannot make himself throw it away.",
    ],
    3: [
        "Sarah brings a standing order to the crowded dock. Jack looks at her until she has to look away at the planks, and she smiles at the planks and walks off before it shows.",
        "She goes home with her face hot and shapes the evening loaf with her mind on the dock. It comes out warm and lopsided.",
        "Odalys eats a slice at the inn window and sighs without knowing why. She teases Sarah about the mood of the loaf, and Sarah will not say what the mood is.",
    ],
    4: [
        "Sarah buys a passage for the first time and boards with a loaf in her lap. Jack takes her fare and finds he cannot say the words he says to everyone.",
        "Mid-lake the Heron slows for no reason he can name. The other passengers go quiet around the loaf, and Sarah tells him it is the first time she has crossed the water since she was a girl.",
        "He steers the long way round the shoal to give the crossing more lake, and catches himself wishing the water were wider.",
        "At the landing she thanks him. He watches her walk up Lantern Street until a cart blocks her from view.",
    ],
    5: [
        "A flour delivery arrives and one crate is too heavy for her. Jack sets down his lines and takes the other end without being asked.",
        "They carry it up the gangplank together and their fingers brush under the edge. She holds on one second longer than the crate needs.",
        "That evening she tries not to think about it, kneads too hard, and then rests her hands and shapes a very honest loaf.",
        "Odalys eats it, goes quiet, and for once does not tease.",
    ],
    6: [
        "Jack lies awake replaying the brush of her fingers, and on the morning run he takes the long way round the island.",
        "At the dock he scrubs the deck until his arms ache, rehearsing one sentence for Sarah over and over.",
        "He walks to the shop door with the sentence ready. The moment she looks up it is gone, and he buys a loaf and talks about the tide instead.",
        "Later a heel of her crust sits on his bench and he cannot finish it.",
    ],
    7: [
        "Clearing the loft over the shop, Sarah finds an old tin with a note in Fenna's margin language, and the note is about a ferryman.",
        "She sits on the floor matching the marks to recipe cards. She can read the first half of the note and not the rest.",
        "She realizes she is hoping the ferryman was nobody of Jack's family, and is startled by how much she hopes it.",
        "The next morning's loaf is bittersweet. Customers buy it and nobody finishes theirs.",
    ],
    8: [
        "An ordinary evening. Jack carries the inn's order to the shop's back door in the narrow alley, as he has twice before.",
        "There is flour on her cheek. He wipes it away with his thumb before he can think, and both of them freeze.",
        "She says thank you too quietly. He pushes his hand into his pocket, says the order is paid, and goes.",
        "He walks the quay with his thumb still warm and cannot find the line he meant to steer by.",
    ],
    9: [
        "Sarah cannot sleep and goes down to shape dough at midnight, and the oven glows through the front window.",
        "Jack, sleepless too, sees the glow from the street and stops at her door. She lets him in for one minute.",
        "They stand shoulder to shoulder at the oven door for its warmth and neither speaks. The minute becomes an hour.",
        "Near dawn the loaves are scorched. She cuts one and they eat in silence, and he leaves before the town wakes.",
    ],
    10: [
        "Jack stays away from the bakery. The first day he takes the long way round to avoid Lantern Street and the Heron drags through the water.",
        "By the third day the Heron sulks outright and stalls mid-lake with an empty deck. A loaf she sent over days ago sits uneaten on his shelf.",
        "Nell finally tells him what he already knows, plainly, and loads a delivery nobody ordered into his arms.",
        "He climbs Lantern Street with the box, pretending it is nothing.",
    ],
    11: [
        "Jack arrives with the delivery nobody ordered. They both look at the box and both know.",
        "They talk in the empty shop for an hour with the counter between them and the lamp low, about Fenna, the ferry, the lake in winter.",
        "She laughs properly for the first time since she came to Larkmere, and he nearly does.",
        "After he leaves she realizes she has been smiling the whole time, and the dough she shapes rises tall overnight.",
    ],
    12: [
        "A storm keeps the Heron docked. Jack doubles the lines with Nell and sees the lamp still burning in the bakery window.",
        "He walks Sarah home through a lane so narrow they cannot walk anything but close, the hem of her coat caught round his wrist.",
        "At her door he stops on the step and does not say what he wants to say. She says goodnight.",
        "He walks back through the rain soaked and happy, and the Heron knocks softly against the pilings when he returns.",
    ],
    13: [
        "In the queue for the morning crossing Sarah delivers an order and sees his collar turned wrong while he talks to a fisherman.",
        "She fixes it without thinking. Her knuckles brush his throat and he stops mid-sentence.",
        "She walks away fast. The fisherman grins at Jack and she hides her shaking hands in her apron.",
        "Back at the shop she bakes three loaves in a row, and Odalys eats all three and cries and laughs.",
    ],
    14: [
        "A gusting wind on the afternoon crossing. Jack fights the tiller while Sarah rides as a passenger with a loaf on her arm.",
        "A gust shoves the deck and she stumbles. His hand closes round her forearm and holds her upright well past steady.",
        "She looks at his mouth. The Heron drifts off its line and neither of them says let go.",
        "When the wind drops the loaf is crushed between them and neither mentions it. He brings the Heron back on course.",
    ],
    15: [
        "A busy morning. Jack carries flour sacks in through the narrow back passage while Sarah is drawing the first tray from the oven.",
        "They meet in the passage. She holds the hot tray high and they stick fast, hips pressed, her arms raised and unable to move.",
        "Neither says a word until the tray begins to cool, and the loaves all rise at once.",
        "After he goes she admits to herself, plainly, that she wants him.",
    ],
    16: [
        "At dusk Jack sits on Gideon's lantern steps while the old man trims the wicks.",
        "He asks about Fenna and the old ferryman. Gideon tells him only part of it, enough to frighten him.",
        "Gideon shares a heel of Fenna's old recipe and it tastes of leaving.",
        "Jack walks back along the water and decides, quietly, that he will never ask her to stay.",
    ],
    17: [
        "Midsummer lantern evening. The harbor fills and Sarah sells lantern buns from a tray at the shop door.",
        "She walks down to the water and finds a lantern to stand at, and Jack is standing at the same one.",
        "The lantern catches and both understand the old custom at once. They stand half a step apart through the whole lighting while the crowd shifts and presses their shoulders together.",
        "Afterward the couples in the lane stand closer, and she walks home alone with the taste of sugar on her tongue.",
    ],
    18: [
        "Jack grows stiff and careful. After Gideon's story he talks to her only about the weather and the tide.",
        "On a crowded market-day crossing the passengers jam together and Sarah is shoved against his arm for the whole lake. He talks about the weather and does not look down.",
        "That night her loaves come out dense and grey. He buys one and cannot eat it.",
        "Nell tells him he is an idiot.",
    ],
    19: [
        "A week of grey bread and no talk. Sarah decides to say one honest thing.",
        "On the dock, with fishermen coiling lines nearby, she tells him she misses him. Her hand stops an inch from his sleeve.",
        "He answers badly, with a remark about the Heron keeping a schedule. She lowers her hand and leaves without looking back.",
        "From the top of Lantern Street she sees him still standing on the dock with the loaf in his hands.",
    ],
    20: [
        "Jack comes to the bakery at closing after the last crossing.",
        "He says the true sentence: he cannot make her stay and he is afraid of wanting it. She tells him to stop deciding for her.",
        "The lamp gutters on the narrow cellar stairs. They stand close enough to feel each other breathe, and do not touch.",
        "He tells her his mother left on this ferry when he was a boy, then walks home with the cellar smell of yeast on his coat.",
    ],
    21: [
        "A summer downpour catches them at the harbor after a delivery, and they share her one coat.",
        "The walk back is slow, shoulders and hips pressed, because neither wants it to end. They take the long way.",
        "At her door she says goodnight to his chin. He nods and goes.",
        "She finds the bread in her basket stayed dry and warm under the coat, and sits on the stairs a long time.",
    ],
    22: [
        "Late-summer lantern night. The whole town packs the harbor lanes.",
        "Nell steers them into the narrowest lane, and Jack understands that she has been steering them since the beginning. Sarah is pressed against his front for the whole slow walk to the pier.",
        "He grips the rail until his knuckles ache and counts the lanterns to stay upright. Her breath comes short and she does not move away.",
        "Next morning Odalys tastes Sarah's bread at the inn steps and looks from the baker to the ferryman and laughs, and Jack hears it from the deck.",
    ],
    23: [
        "A dusk crossing with few passengers. Sarah sits on the stern bench with a loaf on her knee.",
        "He takes her hand and she lets him. They hold hands across the whole width of the lake with their eyes fixed forward, and the Heron goes slow.",
        "At the far dock he lets go and she misses his palm like a lost limb.",
        "Walking home the loaf cools in her arms and she presses the empty hand flat against her coat.",
    ],
    24: [
        "After dark the Heron stops mid-lake and will not move. Nell was sent ashore at the last landing.",
        "Jack and Sarah wait it out in the cramped wheelhouse under one blanket, shoulder to shoulder, hands joined.",
        "Neither sleeps. He feels every breath she takes and says her name once, softly.",
        "At dawn the Heron starts as if nothing had happened. The loaf they shared lies cold on the bench.",
    ],
    25: [
        "Sarah finds the rest of Fenna's margin note and learns the old ferryman left because he thought it was kind. In the cupboard she finds Fenna's last loaf wrapped in cloth.",
        "She sends word for Jack and he comes to the shop after dark. She tells him the truth standing in the dark bakery.",
        "He rests his forehead against hers and they breathe the same air for a long time. He does not kiss her and she does not ask him to.",
        "After he leaves she eats a piece of Fenna's last loaf. It tastes of a goodbye she wished she had refused.",
    ],
    26: [
        "At dawn in his cottage Jack tries to bake. The loaf comes out a brick.",
        "He brings it to Sarah's loft table and they laugh until they cannot stop.",
        "Knees together under the table, close enough to kiss, both of them go still. Her breath catches and so does his.",
        "A lantern gutters outside and Nell knocks. They pull apart, shaking.",
    ],
    27: [
        "At dusk Sarah asks Jack to take her across with no one else aboard.",
        "Mid-lake she says out loud what she wants. He answers by crossing the last inch, and they kiss.",
        "The Heron sails true for the first time all season while the lanterns catch one by one along the shore.",
        "In the morning her bread tastes of joy and of a deeper want, and she knows one kiss has not ended anything.",
    ],
    28: [
        "The day after is soft and a little shy. The whole town tastes her bread and knows, and Odalys cheers from the inn steps.",
        "Every doorway has a neighbor in it. Jack cannot stop touching her hand and lets go whenever the dock fills.",
        "They steal one kiss on the narrow cellar stairs, and it only makes the wanting worse.",
        "At night alone he counts the hours and still does not know how to say stay.",
    ],
    29: [
        "Evening at his cottage by the water. He lights the stove and they eat supper on the narrow bench.",
        "They kiss by the stove until neither can think. Then she stops it herself and tells him why, and he says he will wait as long as it takes, his voice rough.",
        "They lie wrapped together on the bench and talk until dawn. She admits she has not decided about winter and he admits he is afraid of the answer. She tells him why she left her last city.",
        "At dawn she leaves a loaf on his table and walks home along the water.",
    ],
    30: [
        "The last weeks of the season. The Heron sulks and Gideon hands Jack the letter Fenna left for whoever loved the ferryman.",
        "The letter says the old ferryman should have asked. Jack goes quiet and takes the Heron out alone.",
        "Sarah finds him on the dock at dusk. They kiss desperately, her hands fisted in his coat, and then he steps back shaking.",
        "She grips the lantern post and does not follow. He stands at the dock post while the lanterns catch one by one.",
    ],
    31: [
        "The night before the last run, Sarah makes one loaf with every feeling she has in it.",
        "She finds him on the dock and says she is not leaving, before he can ask. He has to sit down.",
        "She sits beside him and they hold each other under one coat, kissing and stopping, because the last of the wanting belongs to the morning and both of them know it.",
    ],
    32: [
        "The last crossing of the season. The Heron runs true all day and the passengers are quiet.",
        "At the landing at dusk Jack asks her to stay in plain words, and she tells him she was already staying.",
        "At the last lantern, with the whole town watching, it catches. He kisses her in plain light and she kisses him back with every season of wanting in it.",
        "The Heron sails true. The book ends on that image.",
    ],
}

# ---------- Checks ----------
assert sorted(SCENES) == list(range(1, c.CHAPTER_COUNT + 1))
assert all(3 <= len(v) <= 4 for v in SCENES.values())
_banned = re.compile(
    r"\b(19|20)\d\d\b|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|days later|—"
    r"|\bsome(thing|one|where|how)\b|particular|the specific|the kind of|one beat too long"
    r"|\barc\b|\bseries\b|Book \d|protagonist|sub-beat"
)
for _n, _scenes in SCENES.items():
    for _i, _t in enumerate(_scenes, 1):
        assert not _banned.search(_t), (_n, _i, _banned.search(_t).group(0))
        assert len(_t.split()) >= 6, (_n, _i)
