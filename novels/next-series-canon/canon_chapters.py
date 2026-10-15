"""
canon_chapters.py - chapter plan for Proof of Home (PART 2: chapters 1-16).
Imports everything from canon_data so tools can use one module.

Chapter fields:
  n, date (ISO), pov ("T" Tamsin odd chapters, "M" Matteo even chapters),
  ferry (True if the ferry is part of the day: never Monday),
  shop_open (True if the bakery trades that day: Tuesday-Saturday, on or
  after opening), must (strings the written chapter must contain),
  beats (2-4 typed sub-beats; ONLY these reach the model, so every fact the
  chapter needs is written inside them).
Placeholders: {date} {weekday} {opening} {vote} {threshold} {counted}
{final_total} {fare} {loaf_price} {crossing} {fenna_death} {opening_loaves}
{age_tamsin} {age_matteo} {age_gideon} {age_ines} {age_bertrand} {age_salma}
{age_milo} {age_lotte}. Dates and numbers always come from placeholders.
Part 3 (to add): chapters 17-32.
"""
from canon_data import *  # noqa: F401,F403

HIDDEN = {
    "ferry_cash_box": {
        "tokens": ["cash box"],
        "forbidden_chapters": list(range(1, 26)),
        "note": "Loaves sold on the ferry and not in the shop ledger. First mentioned in chapter 26.",
    },
    "lease_source": {
        "tokens": ["lobbied", "Fisk asked"],
        "forbidden_chapters": list(range(1, 20)),
        "note": "Who proposed the loaf-count condition. First revealed in chapter 20.",
    },
    "matteo_knack_unknown_to_tamsin": {
        "tokens": ["unspoken worry"],
        "forbidden_chapters": [1, 3, 5, 7, 9, 11, 13],
        "note": "Tamsin does not know Matteo's knack until chapter 14. Only Matteo's chapters may state it.",
    },
}

CHAPTERS = [
    {"n": 1, "date": "2027-03-26", "pov": "T", "ferry": True, "shop_open": False,
     "must": ["Tamsin", "Matteo", "Heron", "Reedbank", "Fenna"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, Tamsin Quill, age {age_tamsin}, arrives at Reedbank and crosses Larkmere Water on the ferry Heron to Heron Landing. The crossing takes {crossing} minutes. She pays the fare of {fare}. Matteo Garrick, age {age_matteo}, pilots the ferry and Milo Sutter, age {age_milo}, handles the ropes. She has come to take over the bakery lease left to her by her great-aunt Fenna Quill, who died on {fenna_death}."),
         ("relationship_micro_beat", "Matteo says very little. At the dock he hands her bag across the gap. They exchange names and nothing more. She notices he looks at her a moment longer than a stranger would, and she does not know why."),
         ("plot_beat", "She walks up Lantern Street to Quill's Bakery and unlocks it. Inside are the front counter, one oven, and a back room with a flour bin. She finds a stack of Fenna's recipe cards and does not read them yet."),
         ("interior_beat", "The lake is the same and Tamsin is not. She is afraid of failing Fenna's shop. She says so to no one."),
     ]},
    {"n": 2, "date": "2027-03-26", "pov": "M", "ferry": True, "shop_open": False,
     "must": ["Matteo", "Milo", "Heron"],
     "beats": [
         ("plot_beat", "That evening Matteo Garrick ties the Heron up at Heron Landing for the night. Milo Sutter asks about the woman with the one bag. Matteo says she is Fenna Quill's great-niece, come for the bakery."),
         ("interior_beat", "During the crossing Matteo felt that Tamsin was carrying an unspoken worry. His knack tells him only that a worry exists, never what it is or who it concerns, and only aboard the Heron. He decides not to ask."),
         ("callback_beat", "He remembers handing her bag across the gap at the dock, and that she thanked him without looking up."),
     ]},
    {"n": 3, "date": "2027-03-29", "pov": "T", "ferry": False, "shop_open": False,
     "must": ["Ines", "Gideon", "1,500"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, Tamsin goes to Council Hall at the top of Lantern Street. Ines Okafor, the town clerk, age {age_ines}, tells her the exact time without looking at a clock, and hands her the lease papers."),
         ("stakes_beat", "Gideon Teague, council chair, age {age_gideon}, explains the terms. The council votes on {vote} on whether to renew the lease. Renewal needs at least {threshold} whole loaves sold, counted from the bakery's own sales ledger, from the opening day through the last Saturday before the vote. Write the number as the digits {threshold}. Gideon writes the terms in ink and the ink stays dry. Tamsin is not told who proposed the condition."),
         ("interior_beat", "Tamsin feels the number as a wall. She decides to open the bakery on {opening}."),
     ]},
    {"n": 4, "date": "2027-03-30", "pov": "M", "ferry": True, "shop_open": False,
     "must": ["Matteo", "Tamsin", "Quill's Bakery"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, the Heron brings flour sacks from Reedbank for Quill's Bakery. Milo Sutter ties them down with knots that hold until he chooses to undo them. Matteo carries the last sack up Lantern Street to the bakery door himself."),
         ("relationship_micro_beat", "Tamsin asks Matteo what kind of man Gideon Teague is. Matteo says Gideon is careful with rules and fair. She thanks him for the sack."),
         ("interior_beat", "Ashore Matteo senses nothing about people. He can read Tamsin only by her face, and he finds that harder."),
     ]},
    {"n": 5, "date": "2027-03-31", "pov": "T", "ferry": False, "shop_open": False,
     "must": ["Salma", "Lotte", "Tamsin"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, Tamsin scrubs the bakery, lights the oven and bakes a first test batch. The bakery is not yet open to customers."),
         ("relationship_micro_beat", "Salma Haddad, age {age_salma}, comes in from Haddad Books next door. Salma is loud and bad at secrets: she blurts that the whole street is watching to see whether the bakery survives."),
         ("stakes_beat", "Lotte Teague, age {age_lotte}, arrives after school and eats the heel of a test loaf. Tamsin was nervous while shaping it, so Lotte feels fluttery and does not know why. Salma laughs. The feeling is mild and lasts that day only. Tamsin did not aim it at anyone."),
     ]},
    {"n": 6, "date": "2027-04-01", "pov": "M", "ferry": True, "shop_open": False,
     "must": ["Gideon", "Matteo", "Heron"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, Gideon Teague rides the Heron to Reedbank and back and pays the fare of {fare} each way."),
         ("relationship_micro_beat", "Gideon asks Matteo politely whether he has been up Lantern Street lately. Matteo says he carried a flour sack there. Gideon says it is a good beginning."),
         ("interior_beat", "Matteo feels that Gideon is carrying an unspoken worry. He learns only that it exists, never what it is. He decides to say nothing about it to anyone, Tamsin included."),
     ]},
    {"n": 7, "date": "2027-04-02", "pov": "T", "ferry": False, "shop_open": False,
     "must": ["Fisk", "Tamsin", "Quay Road"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, Bertrand Fisk, age {age_bertrand}, visits the bakery. He is friendly. He offers to stock her bread at Fisk Provisions on Quay Road from the first day."),
         ("stakes_beat", "Tamsin declines. The lease counts only loaves in the bakery's own sales ledger, so she wants every loaf sold at her own counter. Fisk smiles and says the offer stands."),
         ("interior_beat", "She feels uneasy about how easy his friendliness is, and cannot say why. She goes back to shaping dough for tomorrow."),
     ]},
    {"n": 8, "date": "2027-04-03", "pov": "M", "ferry": True, "shop_open": True,
     "must": ["Matteo", "Tamsin", "40"],
     "beats": [
         ("plot_beat", "Opening day, {weekday}, {date}. Matteo ties the Heron up at Heron Landing, walks up Lantern Street and buys the first loaf at {loaf_price}. Tamsin writes every sale in the ledger by hand."),
         ("relationship_micro_beat", "Salma comes out of Haddad Books to cheer. Lotte Teague asks Matteo whether he is Tamsin's friend. He says he carried her flour, and Lotte decides that counts."),
         ("stakes_beat", "At the end of the day the ledger shows {opening_loaves} loaves sold. Write the count as the digits {opening_loaves}. Tamsin writes the figure at the top of a new page. The target is {threshold}."),
         ("callback_beat", "Matteo thinks of handing her bag across the gap on the day she arrived."),
     ]},

    {"n": 9, "date": "2027-04-04", "pov": "T", "ferry": False, "shop_open": False,
     "must": ["Tamsin", "Fenna", "Salma"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, the bakery is closed. Tamsin Quill sits in the back room by the flour bin and reads Fenna Quill's recipe cards for the first time, one at a time. Fenna's handwriting is small and square. The ledger page from opening day sits beside her, showing {opening_loaves} loaves."),
         ("relationship_micro_beat", "Salma Haddad knocks on the back door from Haddad Books with two mugs of tea. She asks what Tamsin plans to do about the {threshold}. Tamsin says she plans to bake. Salma says that is a sensible answer and a terrible plan, and stays anyway."),
         ("interior_beat", "Tamsin finds that she misses Fenna more while reading the cards than she did at any time since arriving. She decides to bake from the cards one at a time, starting Tuesday."),
     ]},
    {"n": 10, "date": "2027-04-06", "pov": "M", "ferry": True, "shop_open": True,
     "must": ["Matteo", "Milo", "Quill's Bakery"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, the first full trading week begins. Matteo Garrick walks up Lantern Street before the first crossing and buys a loaf at Quill's Bakery for {loaf_price}. Milo Sutter has asked him to bring one back for the Heron, and Matteo does."),
         ("relationship_micro_beat", "Tamsin tells Matteo she is baking from Fenna's cards now. He asks which card. She tells him it is the one with the plainest crust, and he says he will report on it by evening."),
         ("interior_beat", "On the crossing Matteo feels that a passenger is carrying an unspoken worry. He learns only that it exists. He does not look to see who it is, and he does not tell Milo."),
     ]},
    {"n": 11, "date": "2027-04-08", "pov": "T", "ferry": False, "shop_open": True,
     "must": ["Anselm Rudd", "Tamsin", "Fisk"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, Tamsin opens the bakery at the usual hour. Anselm Rudd, who owns the hardware store, buys a loaf and eats the heel standing at the counter."),
         ("stakes_beat", "Tamsin was calm while shaping that batch. Anselm Rudd feels calm for the rest of the afternoon and says so. The echo is mild and lasts that day only. Tamsin did not aim it at him."),
         ("relationship_micro_beat", "Salma reports that Bertrand Fisk has put a hand-lettered sign over the packaged bread at Fisk Provisions saying it stays fresh all week. Tamsin says her bread is only meant to last a day. Salma says that is the whole charm."),
     ]},
    {"n": 12, "date": "2027-04-09", "pov": "M", "ferry": True, "shop_open": True,
     "must": ["Matteo", "Tamsin", "Heron Landing"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, the Heron brings the flour order across before dawn. Tamsin comes down to Heron Landing herself to meet it, with Milo Sutter tying the sacks down."),
         ("relationship_micro_beat", "Standing on the dock, Tamsin tells Matteo the number {threshold} and what it means. Matteo says nothing wise and carries a sack up Lantern Street. She laughs, once, and does not explain why."),
         ("interior_beat", "Ashore Matteo senses nothing about people, so he can only watch her face. He realizes he has wished to be aboard the Heron with her, because aboard he would know more. He decides he does not want to learn it that way."),
     ]},
    {"n": 13, "date": "2027-04-10", "pov": "T", "ferry": False, "shop_open": True,
     "must": ["Tamsin", "Salma", "Lotte"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, the first full trading week ends with a busy Saturday. Tamsin works the counter and shapes dough in between customers."),
         ("relationship_micro_beat", "Earlier that week Tamsin shaped a batch while thinking of Matteo handing her bag across the gap at the dock, and she felt warm. Salma eats a roll from that batch and grins and says Tamsin looks like someone with news. Tamsin says she has no news."),
         ("stakes_beat", "Lotte Teague, age {age_lotte}, comes in after Salma and asks Tamsin directly why the bread makes her feel like it is already Saturday. Tamsin says it is only bread. Lotte says it is a good one."),
         ("interior_beat", "Tamsin decides she should keep her knack quiet from the whole street. She wonders for the first time who in Larkmere might guess it."),
     ]},
    {"n": 14, "date": "2027-04-11", "pov": "M", "ferry": True, "shop_open": False,
     "must": ["Matteo", "Tamsin", "Heron"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, the bakery is closed. Tamsin takes the Heron to Reedbank and back on her day off to see the far shore, and pays the fare of {fare} each way."),
         ("interior_beat", "Aboard, Matteo feels Tamsin's unspoken worry again, the same one as the day she arrived. He learns only that it exists. He decides he will tell her the truth about it, because lying by silence has begun to feel like lying."),
         ("relationship_micro_beat", "At the rail, Matteo tells Tamsin his knack: aboard the Heron he knows when someone is carrying a worry they have not said aloud, never what it is. She goes quiet, then tells him about her bread. Neither of them says it is strange."),
         ("callback_beat", "He tells her that on the day she arrived he felt her worry before she had said a word, and that he handed her bag across the gap partly to give her something to hold."),
     ]},
    {"n": 15, "date": "2027-04-13", "pov": "T", "ferry": False, "shop_open": True,
     "must": ["Tamsin", "Matteo", "Ines"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, Tamsin opens the bakery thinking about what Matteo told her. Ines Okafor comes in at what she says is exactly the minute the doors open, buys a loaf and says the town has noticed the bakery's windows are clean again."),
         ("relationship_micro_beat", "Matteo comes in as a customer, buys a loaf and says nothing about the worry. He asks only what is in the day's batch. Tamsin finds she is grateful that he does not ask more."),
         ("interior_beat", "Tamsin decides she will not ride the Heron again until she knows what her worry is, because Matteo will feel it and she does not want to be known before she has said it herself."),
     ]},
    {"n": 16, "date": "2027-04-16", "pov": "M", "ferry": True, "shop_open": True,
     "must": ["Matteo", "Perpetua Ostrow", "Fisk"],
     "beats": [
         ("plot_beat", "On {weekday}, {date}, Bertrand Fisk rides the Heron to Reedbank to collect a delivery for Fisk Provisions and pays the fare of {fare}. Perpetua Ostrow, the retired schoolteacher, rides the same crossing to visit a friend."),
         ("interior_beat", "Matteo feels that Fisk is carrying an unspoken worry. He learns only that it exists, not what it is or who it concerns. He tells no one."),
         ("relationship_micro_beat", "Perpetua Ostrow tells Matteo that Tamsin's bread made her think of her classroom in the first weeks of the year. Matteo says he has noticed the same. Milo ties off the stern line and, without being asked, says Tamsin is nice."),
     ]},
]
