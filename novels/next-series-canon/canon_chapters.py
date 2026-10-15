"""
canon_chapters.py - chapter plan for Proof of Home (PART 2: chapters 1-8).
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
Part 3 (to add): chapters 9-32.
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
]
