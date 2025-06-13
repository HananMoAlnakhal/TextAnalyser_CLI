import random
from TEXTstyling import *
#=========================================================-MAIN-CLASS-==========================================================
class SmartTextAnalyzer():
    stopWords=['dr', 'dra', 'mr', 'ms', 'a', "a's", 'able', 'about', 'above', 'according', 'accordingly', 'across', 'actually', 'after', 'afterwards', 'again', 'against', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'b', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'c', "c'mon", "c's", 'came', 'can', "can't", 'cannot', 'cant', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', 'currently', 'd', 'definitely', 'described', 'despite', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', "don't", 'done', 'down', 'downwards', 'during', 'e', 'each', 'edu', 'eg', 'eight', 'either', 'else', 'elsewhere', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'f', 'far', 'few', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'four', 'from', 'further', 'furthermore', 'g', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'h', 'had', "hadn't", 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he's", 'hello', 'help', 'hence', 'her', 'here', "here's", 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'i', "i'd", "i'll", "i'm", "i've", 'ie', 'if', 'ignored', 'immediate', 'in', 'inasmuch', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", "it's", 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'knows', 'known', 'l', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'little', 'look', 'looking', 'looks', 'ltd', 'm', 'mainly', 'many', 'may', 'maybe', 'me', 'mean', 'meanwhile', 'merely', 'might', 'more', 'moreover', 'most', 'mostly', 'much', 'must', 'my', 'myself', 'n', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'normally', 'not', 'nothing', 'novel', 'now', 'nowhere', 'o', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'p', 'particular', 'particularly', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provides', 'q', 'que', 'quite', 'qv', 'r', 'rather', 'rd', 're', 'really', 'reasonably', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'she', 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 't', "t's", 'take', 'taken', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that's", 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', "there's", 'thereafter', 'thereby', 'therefore', 'therein', 'theres', 'thereupon', 'these', 'they', "they'd", "they'll", "they're", "they've", 'think', 'third', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlikely', 'until', 'unto', 'up', 'upon', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'uucp', 'v', 'value', 'various', 'very', 'via', 'viz', 'vs', 'w', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", "we'll", "we're", "we've", 'welcome', 'well', 'went', 'were', "weren't", 'what', "what's", 'whatever', 'when', 'whence', 'whenever', 'where', "where's", 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', "who's", 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', "won't", 'wonder', 'would', 'would', "wouldn't", 'x', 'y', 'yes', 'yet', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'z', 'zero']
    punctuation="!@#$%^&*()/|\\,._--=+><?'\"}{[:;؛ّ~`]â€"

    def __init__(self,TextInput=""):
        self.text=TextInput
        self.sentences=[]
        self.words=[]
        if self.text!="":
            self.sentences=self.getSentences()
            self.words=self.getWords()

    def getSentences(self):
        for paragraph in self.text.strip().split("\n"):
            for sentence in paragraph.strip().split(","):
                if sentence !='':
                    self.sentences.append(sentence.lower())
        return self.sentences
    
    @classmethod
    def __increment(cls,Dic,key):
        if Dic.get(key) :
            Dic[key]+=1
        else:
            Dic[key]=1

    def getWords(self):
        self.wordsCounts={}
        self.totalWords=0
        self.uniqueCount =0
        self.uniqueWords={}
        self.CharacterCount=0
        self.CharacterOccurrence={}
        words=[]
        for sentence in self.sentences:
            wordsInSentence=[]
            for word in sentence.split():
                processed=""
                for letter in word:
                    if letter!=" ":
                        self.CharacterCount+=1
                        __class__.__increment(self.CharacterOccurrence,letter)
                    if letter in __class__.punctuation:
                        continue
                    processed+=letter
                if processed.isalpha() :
                    wordsInSentence.append(processed)
                    self.totalWords+=1
                    __class__.__increment(self.wordsCounts,processed)
                    if not(processed in __class__.stopWords):
                        __class__.__increment(self.uniqueWords,processed)
            words.append(wordsInSentence)

        self.uniqueCount=sum(self.uniqueWords.values())
        return words
    
    def MostFrequentWords(self,n=5,KeyWords=False):
        Target=self.uniqueWords if KeyWords else self.wordsCounts
        Sorted=sorted(Target.items(),key=lambda x:x[1], reverse=True)
        if n==0 or n>=len(Sorted):
            n=len(Sorted)
        return Sorted[:n]
    
    def WordCloud(self,n=5,KeyWords=False,Vis=False):
        W=self.MostFrequentWords(n,KeyWords)
        WodWMostCount=W[0][1]
        Words=[(x,y/WodWMostCount) for x,y in W]
        if Vis:
            for ind,(w,f) in enumerate(Words):
                x="="
                color=random.choice([GREEN,ORANGE,BLUE,RED,YELLOW,SkyBlue,GRASS,BROWN,PINK,PURPLE,CYAN,sysBLUE])
                print(BlackBG(w.ljust(25)),BlackBG(color(x*(round(7*f)*10))),BlackBG(color(" %.2f | %2.2f"%(W[ind][1],f*100)+"% ")),sep="")
        return Words

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
        for sentence_num,sentence in enumerate(self.words):
            s=" ".join(sentence)
            pos=s.find(Target)
            wordIndx=-1
            while pos!=-1:
                textWithTarget=Target.split()[0]
                for word in sentence[wordIndx+1:len(sentence)]:
                    if textWithTarget in word:
                        textWithTarget= word
                        break
                wordIndx+=sentence[wordIndx+1:len(sentence)].index(textWithTarget)+1
                SearchResult.append(((sentence_num,wordIndx),s,pos,pos+len(Target)))
                pos=s.find(Target,pos+1)
        
        if len(SearchResult)==0:
            if not replacing:
                print(f"there is no results found, that matches: \x1b[3m\x1b[1m{Target}\x1b[0m\x1b[0m") 
            return None
        
        return(SearchResult)
    
    def _displaySearch(self,searchResult):
        if searchResult==None:
            print("\33[38;5;202mthere is no results to print!\33[0m")
            return
        print("\x1b[1mResults Count: ",len(searchResult),"\n","="*50,"\x1b[0m",sep="",end="\n")
        for X in searchResult:
            print(f'{ITALIC("Sentence Index:")} {BOLD(X[0][0])}\t| {ITALIC("Word Index:")} {BOLD(X[0][1])}\n"{X[1][0:X[2]]}{GREEN(ITALIC(UNDERLINED(X[1][X[2]:X[3]])))}{X[1][X[3]:len(X[1])]}"')
            print("-"*25)
        
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



if __name__=="__main__":
    file=open("SpaceIpsum.txt").read()
    Report=SmartTextAnalyzer(file)
    Report.WordCloud(8,True,Vis=True)

