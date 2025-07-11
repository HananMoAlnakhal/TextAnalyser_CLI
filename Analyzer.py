import shutil
import math
import os
import platform
from TEXTstyling import *
from predictor import *
from lang_models import *
from TextEditor import *
#=========================================================-MAIN-CLASS-==========================================================
class SmartTextAnalyzer():
    stopWords={'dr', 'dra', 'mr', 'ms', 'a', "a's", 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again', 'against', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'b', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'c', "c'mon", "c's", 'came', 'can', "can't", 'cannot', 'cant', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', 'currently', 'd', 'definitely', 'described', 'despite', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', "don't", 'done', 'down', 'downwards', 'during', 'e', 'each', 'edu', 'eg', 'eight', 'either', 'else', 'elsewhere', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'far', 'few', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'four', 'from', 'further', 'furthermore', 'g', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'h', 'had', "hadn't", 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he's", 'hello', 'help', 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'i', "i'd", "i'll", "i'm", "i've", 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", "it's", 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'knows', 'known', 'l', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'little', 'look', 'looking', 'looks', 'ltd', 'm', 'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might', 'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my', 'myself', 'n', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'o', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'p', 'particular', 'particularly', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'q', 'que', 'quite', 'qv', 'r', 'rather', 'rd', 're', 'really', 'reasonably', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'she', 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 't', "t's", 'take', 'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that's", 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', "there's", 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'think', 'third', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'uucp', 'v', 'value', 'various', 'very', 'via', 'viz', 'vs', 'w', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", "we'll", "we're", "we've", 'welcome', 'well', 'went', 'were', "weren't", 'what', "what's", 'whatever', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', "who's", 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', "won't", 'wonder', 'would', 'would', "wouldn't", 'x', 'y', 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'z', 'zero'}
    punctuation="!@#$%^&*()/|\\,._--=+><?'\"}{[:;؛ّ~`]â€"
    contractions = {"ain't": "is not","aren't": "are not","can't": "cannot","couldn't": "could not","didn't": "did not","doesn't": "does not","don't": "do not","hadn't": "had not","hasn't": "has not","haven't": "have not","isn't": "is not","mightn't": "might not","mustn't": "must not","needn't": "need not","shan't": "shall not","shouldn't": "should not","wasn't": "was not","weren't": "were not","won't": "will not","wouldn't": "would not"}
    other_contractions = {"i'm": "i am","you're": "you are","he's": "he is","she's": "she is","it's": "it is","we're": "we are","they're": "they are","i've": "i have","you've": "you have","we've": "we have","they've": "they have","who's": "who is","what's": "what is","where's": "where is","when's": "when is","why's": "why is","how's": "how is","i'd": "i would","you'd": "you would","he'd": "he would","she'd": "she would","we'd": "we would","they'd": "they would","i'll": "i will","you'll": "you will","he'll": "he will","she'll": "she will","we'll": "we will","they'll": "they will","there's": "there is","here's": "here is","let's": "let us","that's": "that is","who'd": "who would","who'll": "who will","who've": "who have","y'all": "you all"}
    all_contractions = {**contractions, **other_contractions}
    negates={"never","not","no","neither","hardly","barely","nor","nothing","nowhere","noone","none","not","rarely","scarcely","seldom"}

    def __init__(self,TextInput=""):
        self.text=TextInput
        self.sentences=[]
        self.words=[]
        self.NextWordPred=Text_Predictor()
        if self.text!="":
            self.sentences=self.getSentences()
            self.words=self.getWords()

#---------------------------------------------------
# Helper functions 
#---------------------------------------------------

    def _ClearTerminal(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    @classmethod
    def __increment(cls,Dic,key):
        if Dic.get(key) :
            Dic[key]+=1
        else:
            Dic[key]=1
########################################################################################
#      Splitting the text into sentences
#---------------------------------------------------------------------------------------
    def getSentences(self,text=""):
        if text :
            text=text
        else:text=self.text
        for paragraph in self.text.strip().split("\n"):
            for sentence in paragraph.strip().split(","):
                if sentence !='':
                    self.sentences.append(sentence.lower())
        return self.sentences
    
########################################################################################
#      Getting and counting the words from each sentence
#---------------------------------------------------------------------------------------
    def getWords(self):
        self.wordsCounts={}
        self.totalWords=0
        self.uniqueCount =0
        self.uniqueWords={}
        self.CharacterCount=0
        self.CharacterOccurrence={}
        self.sentiment_by_sentence=[]
        self.sentiment={"pos":0,"neg":0}
        words=[]
        for sentence in self.sentences:
            sentiment=0
            expanded_sentence = self.expand_contractions(sentence)
            wordsInSentence = []
            for ind,word in enumerate(expanded_sentence.split()):
                processed = ""
                for letter in word:
                    if letter != " ":
                        self.CharacterCount += 1
                        __class__.__increment(self.CharacterOccurrence, letter)
                    if letter in __class__.punctuation:
                        continue
                    processed += letter
                # Added my sentiment function 
                if processed in POSITIVE_LEX or processed in NEGATIVE_LEX:
                    PRIME=1 if processed in POSITIVE_LEX else-1
                    if ind>0:
                        isnegate=expanded_sentence.split()[ind-1]
                        if isnegate in __class__.negates:
                            PRIME=PRIME*-1
                        real="neg" if PRIME<0 else "pos"
                        self.sentiment[real]+=1
                        sentiment+=PRIME
                    else:
                        real="neg" if PRIME<0 else "pos"
                        self.sentiment[real]+=1
                        sentiment+=PRIME

                if processed.isalpha():
                    wordsInSentence.append(processed)
                    self.totalWords += 1
                    __class__.__increment(self.wordsCounts, processed)
                    if processed not in __class__.stopWords:
                        __class__.__increment(self.uniqueWords, processed)
            self.sentiment_by_sentence.append(sentiment)
            self.NextWordPred.add_ngram(wordsInSentence)
            words.append(wordsInSentence)

        self.uniqueCount = sum(self.uniqueWords.values())
        return words

    def expand_contractions(self,sentence):
        contractions_dict=__class__.all_contractions
        words = sentence.split()
        expanded_words = []
        for word in words:
            lower_word = word.lower()
            if lower_word in contractions_dict:
                expanded_words.extend(contractions_dict[lower_word].split())
            else:
                found = False
                for suffix, replacement in contractions_dict.items():
                    if word.lower().endswith(suffix):
                        base = word[:-len(suffix)]
                        if base:
                            expanded_words.append(base)
                        expanded_words.extend(replacement.split())
                        found = True
                        break
                if not found:
                    expanded_words.append(word)
        return ' '.join(expanded_words)
########################################################################################
#      Search the Text
#---------------------------------------------------------------------------------------
    def searchText(self,Target,replacing=False):
        '''This wil return the search result in this format \n
        [((Sentence number,word number in the sentence),"sentence",TargetIndex,TargetIndex+len(Target) )]'''
        SearchResult=[]
        Target=Target.lower()
        clean=''
        for letter in Target:
            if letter in __class__.punctuation:
                continue
            clean=clean+letter.lower()
        Target=clean
        for sentence_num,sentence in enumerate(self.sentences):
            s=sentence
            pos=s.lower().find(Target)
            wordIndx=-1
            while pos!=-1:
                textWithTarget=Target.split()[0]
                for word in sentence[wordIndx+1:len(sentence)]:
                    if textWithTarget in word.lower():
                        textWithTarget= word
                        break
                wordIndx+=sentence[wordIndx+1:len(sentence)].find(textWithTarget)+1
                print(wordIndx)
                SearchResult.append(((sentence_num,wordIndx),s,pos,pos+len(Target)))
                pos=s.find(Target,pos+1)
        
        if len(SearchResult)==0:
            if not replacing:
                print(f"there is no results found, that matches: \x1b[3m\x1b[1m{Target}\x1b[0m\x1b[0m") 
            return None
        
        return(SearchResult)
#---------------------------------------------------
# display the search results clearly
#--------------------------------------------------
    def _displaySearch(self,searchResult):
        if searchResult==None:
            print("\33[38;5;202mthere is no results to print!\33[0m")
            return
        print("\x1b[1mResults Count: ",len(searchResult),"\n","="*50,"\x1b[0m",sep="",end="\n")
        for X in searchResult:
            print(f'{ITALIC("Sentence Index:")} {BOLD(X[0][0])}\t, {ITALIC("Word Index:")} {BOLD(X[0][1])}\n"{X[1][0:X[2]]}{GREEN(ITALIC(UNDERLINED(X[1][X[2]:X[3]])))}{X[1][X[3]:len(X[1])]}"')
            print("-"*25)
########################################################################################
#      Replacing Words/subStr
#---------------------------------------------------------------------------------------
    def replaceWords(self,OldVal,NewVal):
        OLdPos=self.searchText(OldVal,True)
        if OLdPos==None:
            print(BlackBG("THERE IS NO SUCH A VALUE "+YELLOW(OldVal)+" to replace it with "+YELLOW(NewVal)))
            return None
        else:
            oldNewDic={}
            for INX,((SenIndx,WordIndx),s,Bpos,Epos) in enumerate(OLdPos):
                if s==OLdPos[INX-1][1]:#if it is the same as previous edited sentence then edit on the edited version not the original
                    Bpos+=len(oldNewDic[s])-len(s)
                    Epos+=len(oldNewDic[s])-len(s)
                    s=oldNewDic[s]
                print(BOLD("sentence "+str(INX+1)+"Before replacing :\n")+s[0:Bpos]+ORANGE(s[Bpos:Epos])+s[Epos:len(s)])
                NewSentence=s[0:Bpos]+NewVal+s[Epos:len(s)]
                print("would be replaced to:\n"+s[0:Bpos]+GREEN(NewSentence[Bpos:len(NewVal)+Bpos])+NewSentence[len(NewVal)+Bpos:len(NewSentence)])
                self.sentences[SenIndx]=NewSentence
                oldNewDic[s]=NewSentence
            self.words=self.getWords()
            print(BLUE(BOLD("_"*25+"Done replacing all Values"+"_"*50)))
            return
#---------------------------------------------------------------------------------------
#       Getting the most frequent word/Keyword _sorted
#---------------------------------------------------------------------------------------
    def MostFrequentWords(self,n=5,KeyWords=False):
        Target=self.uniqueWords if KeyWords else self.wordsCounts
        Sorted=sorted(Target.items(),key=lambda x:x[1], reverse=True)
        if n==0 or n>=len(Sorted):
            n=len(Sorted)
        return Sorted[:n]
    
#################################################################################################
#       Word Cloud
#------------------------------------------------------------------------------------------------
    def WordCloud(self,n=5,KeyWords=False,Bar=False, Vis=False):
        self._ClearTerminal()
        W=self.MostFrequentWords(n,KeyWords)
        WodWMostCount=W[0][1]
        Words=[(x,y/WodWMostCount) for x,y in W]
        if Bar:
            for ind,(w,f) in enumerate(Words):
                x="="
                color=allColors.GetColor(reverse=True)
                print(BlackBG(w.ljust(25)+color(x*(round(7*f)*10)))+BlackBG(color(" %.2f , %2.2f"%(W[ind][1],f*100)+"% ")))
        if Vis:
            TakenPOS=self.generate_compact_positions(max_positions=len(Words))
            for ind in range(len(TakenPOS)):
                self._Print_square(TakenPOS[ind],allColors.GetColor(reverse=True),int(round(Words[0:len(TakenPOS)][ind][1]*10)),Words[0:len(TakenPOS)][ind][0])
                print(f"\033[0H")
#---------------------------------------------------
# prints the squares based on the size a

    def _Print_square(self,pos,COLOR=PINK,a=9,word="TEXT"):
        lines,col=pos
        for line in range(int(a)):
            print(f"\033[{(lines-a//2)+line};{col-round((a*3)//2)}H"+COLOR(" "*round(a*3),BG=True))
        print(f"\033[{(lines)};{col-(len(word))//2}H"+BOLD(COLOR(word)))

#---------------------------------------------------
# helps Generating poses for the words

    def generate_compact_positions(self, max_positions=15):
        """
        Generate organized positions for compact word cloud design
        Returns a list of (row, col) positions that work with your existing code"""
        size = shutil.get_terminal_size()
        middle_line = size.lines // 2
        middle_col = size.columns // 2
        
        positions = []
        
        positions.append((middle_line, middle_col))
        
        added_positions = 1
        ring = 1
        
        while added_positions < max_positions and ring <= 8:
            ring_positions = []
            if ring == 1:
                ring_positions = [(middle_line, middle_col - 30),    (middle_line, middle_col + 25),  (middle_line - 6, middle_col),   (middle_line + 6, middle_col),     (middle_line - 4, middle_col - 18), (middle_line - 4, middle_col + 18), (middle_line + 4, middle_col - 18), (middle_line + 4, middle_col + 18), ]
            elif ring == 2:
                ring_positions = [(middle_line, middle_col - 45),    (middle_line, middle_col + 50),     (middle_line - 12, middle_col),  (middle_line + 12, middle_col),  (middle_line - 8, middle_col - 30), (middle_line - 8, middle_col + 30), (middle_line + 8, middle_col - 30), (middle_line + 8, middle_col + 30), ]
            elif ring == 3:
                ring_positions = [(middle_line - 18, middle_col - 15),(middle_line - 18, middle_col + 15),(middle_line + 18, middle_col - 15),(middle_line + 18, middle_col + 15),(middle_line - 2, middle_col - 60),(middle_line + 2, middle_col - 60), (middle_line - 2, middle_col + 60),  (middle_line + 2, middle_col + 60),  ]
            else:
                angle_step = 360 // (ring * 4)  
                radius_row = min(ring * 6, (size.lines // 2) - 2)
                radius_col = min(ring * 20, (size.columns // 2) - 10)
                for angle in range(0, 360, angle_step):
                    rad = math.radians(angle)
                    row = int(middle_line + radius_row * math.sin(rad))
                    col = int(middle_col + radius_col * math.cos(rad))
                    ring_positions.append((row, col))
            for row, col in ring_positions:
                if added_positions >= max_positions:
                    break
                margin =5
                if (margin <= row <= size.lines - margin and 
                    margin <= col <= size.columns - margin):
                    positions.append((row, col))
                    added_positions += 1
            ring += 1
        return positions[:max_positions]




if __name__=="__main__":
    SmartTextEditor()
    # print(TRIE.auto_complete("app"))
