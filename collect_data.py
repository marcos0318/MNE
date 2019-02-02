from os import listdir
from os.path import isfile, join

my_path = "/home/data/corpora/Multi-Relational-Word-Embeddings-for-Selectional-Preference-Acquisition/relation_text/"
only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
amod_files = [f for f in only_files if "amod" in f]
nsubj_files = [f for f in only_files if "nsubj" in f]
dobj_files = [f for f in only_files if "dobj" in f]


num_example = 10
with open("data/small_example.txt", "w") as fout:
    for i in range(num_example):
        amod_file = amod_files[i]
        dobj_file = dobj_files[i]
        nsubj_file = nsubj_files[i]

        with open(join(my_path, amod_file), "r") as fin:
            contents = fin.readlines()
            new_contents = ["amod " + line for line in contents]
            for line in new_contents:
                fout.write(line)

        with open(join(my_path, nsubj_file), "r") as fin:
            contents = fin.readlines()
            new_contents = ["nsubj " + line for line in contents]
            for line in new_contents:
                fout.write(line)

        with open(join(my_path, dobj_file), "r") as fin:
            contents = fin.readlines()
            new_contents = ["dobj " + line for line in contents]
            for line in new_contents:
                fout.write(line)




