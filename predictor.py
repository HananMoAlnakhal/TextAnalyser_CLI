########################################################################################
#       predict next word class
#---------------------------------------------------------------------------------------
class Text_Predictor():
    def __init__(self,nGram=3):
        self.n=nGram
        self.ngram = {}

    def predict_next_top(self,context_words, k=3):
        dic=self.ngram
        context_words = " ".join(context_words.split()[(-self.N +1):])
        for i in range(len(context_words), 0, -1):
            context = context_words[-i:]
            if context in dic:
                next_words = dic[context]
                sorted_words = sorted(next_words.items(), key=lambda item: item[1], reverse=True)
                return sorted_words
        return []
    
    def add_ngram(self,wordsInSentence):
        dic=self.ngram
        for n in [3,2]:
            for i in range(1,len(wordsInSentence) - n + 1):
                context = tuple(wordsInSentence[i:i + n - 1])
                next_word = wordsInSentence[i + n - 1]
                if context not in dic:
                    dic[context] = {}
                if next_word not in dic[context]:
                    dic[context][next_word] = 0
                dic[context][next_word] += 1

########################################################################################
#       Word Autocomplete Class
#---------------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, freq=1):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += freq 

    def auto_complete(self, prefix):
        def dfs(node, path, results):
            if node.is_end_of_word:
                results.append(("".join(path), node.frequency))
            for char, child in node.children.items():
                dfs(child, path + [char], results)

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        dfs(node, list(prefix), results)
        results.sort(key=lambda x: -x[1])
        return [word for word, freq in results]