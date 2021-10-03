from databace import Database
import re
import string

class AutoCompleteData:
    database = Database()

    def __init__(self, input):
        self.completed_sentence = input
        self.source_text = ""
        self.offset = 0
        self.score = 0
        self.sentence=[]
        self.all_sentence=[]

    def check_all_sentence(self, sentence):
        for i in range(len(self.completed_sentence)):
            tmp_sentences = re.sub('[!@#$%^&*().,;:/?><"\']', "", sentence[0].lower())
            new_name = re.sub('[!@#$%^&*().,;:/?><"\']', "", self.completed_sentence[i])
            if new_name not in tmp_sentences:
                return False
            if i != len(self.completed_sentence) - 1:
                if tmp_sentences.find(
                        re.sub('[!@#$%^&*().,;:/?><"\']', "", self.completed_sentence[i + 1])) != (
                tmp_sentences).find(
                        new_name) + len(new_name) + 1:
                    return False
        return True


    def find_string(self):
        try:
            for i in AutoCompleteData.database.get(re.sub('[!@#$%^&*().,;:/?><"\']', "", self.completed_sentence[0])):
                if self.check_all_sentence(i):
                    self.sentence.append((i[0],0))
        except:
            pass
        if len(self.sentence)>=5:
            for i in range(len(self.sentence[:5])):
                print(str(i+1)+": "+ str(self.sentence[i][0])+ "score:"+ str(self.sentence[i][1]))
        else:
            self.add_char()
            self.delete_char()
            self.change_char()
            self.sentence.sort(key=lambda tup: tup[1])
            for i in range(len(self.sentence[:5])):
                print(str(i + 1) + " " + str(self.sentence[i][0]) + "score: " + str(self.sentence[i][1]))



    def add_char(self):
        score={0:10,1:8,2:6,3:4}
        a = []
        for index_word in range(len(self.completed_sentence)):
            b=[]
            for index_char in range(len(self.completed_sentence[index_word])):
                try:
                    score_to_decrese=score[index_char]
                except:
                    score_to_decrese=1
                b.append((self.completed_sentence[index_word][:index_char]+self.completed_sentence[index_word][index_char+1:],score_to_decrese))
            b.append((self.completed_sentence[index_word],0))
            a.append(b)
        self.general(a)



    def delete_char(self):
        score={0:10,1:8,2:6,3:4}
        a = []
        for index_word in range(len(self.completed_sentence)):
            b=[]
            for i in range(len(self.completed_sentence[index_word])+1):
                try:
                    score_to_decrese=score[i]
                except:
                    score_to_decrese=1
                for char in string.ascii_lowercase:
                    b.append((self.completed_sentence[index_word][:i]+char+self.completed_sentence[index_word][i:],score_to_decrese))
            b.append((self.completed_sentence[index_word],0))
            a.append(b)
        self.general(a)


    def change_char(self):
        a = []
        score={0:5,1:4,2:3,3:2,4:1}
        for index_word in range(len(self.completed_sentence)):
            b = []
            for i in range(len(self.completed_sentence[index_word])):
                try:
                    score_to_decrese=score[i]
                except:
                    score_to_decrese=1
                for char in string.ascii_lowercase:
                    b.append((self.completed_sentence[index_word][:i]+char+self.completed_sentence[index_word][i+1:],score_to_decrese))
            b.append((self.completed_sentence[index_word],0))
            a.append(b)
        self.general(a)


    def general(self,a):
        for l in range(len(a)):
            for j in range(len(a[l])):
                b=a[l][j][1]
                self.completed_sentence[l] = a[l][j][0]
                try:
                    for i in AutoCompleteData.database.get(
                            re.sub('[!@#$%^&*().,;:/?><"\']', "", self.completed_sentence[0])):
                        if self.check_all_sentence(i) and i[0] not in [j[0] for j in self.sentence]:
                            self.sentence.append((i[0],b))
                except:
                    pass

