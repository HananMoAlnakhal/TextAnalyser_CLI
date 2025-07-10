import pickle
import os

base=os.path.dirname(__file__)
#_________loading predefined objects_______________________

#   Trie for autocomplete and spilling check
with open(os.path.join(base,"WordsTrie.pkl"), "rb") as f:
    TRIE = pickle.load(f)
#    nGrams
with open(os.path.join(base,"3Grams.pkl"), "rb") as f:
    Pred3Gram = pickle.load(f)

with open(os.path.join(base,"2Grams.pkl"), "rb") as f:
    Pred2Gram = pickle.load(f)

with open(os.path.join(base,"positive_lex.pkl"), "rb") as f:
    POSITIVE_LEX = pickle.load(f)

with open(os.path.join(base,"negative_lex.pkl"), "rb") as f:
    NEGATIVE_LEX = pickle.load(f)
