
girls = ['alice', 'allie', 'bernice', 'brenda', 'clarice', 'cilly']
boys = ['chris', 'christopher', 'arald', 'arnold', 'bob']

# the bad way, quadratic time:
bad_way_pairs = [b+'+'+g for b in boys for g in girls if b[0] == g[0]]
print("the bad way:\n{}".format(bad_way_pairs))

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)

good_way_pairs = [b+'+'+g for b in boys for g in letterGirls[b[0]]]
#print("letterGirls dict: {}".format(letterGirls))
print("the good way:\n{}\nusing girls dict: {}".format(good_way_pairs, letterGirls))
