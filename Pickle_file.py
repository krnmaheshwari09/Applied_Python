import pickle as pk

ordering = {"First": 1, "Second": 2, "Third": 3}
pk.dump(ordering, open("new.pkl", "wb"))
reading_pickle = pk.load(open("new.pkl", "rb"))
print(reading_pickle)
