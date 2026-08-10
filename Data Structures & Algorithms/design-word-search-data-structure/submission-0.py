class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word :
            if ch not in node.children :
                node.children[ch] =  WordDictionary()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        node = self
        def dfs(node , index):
            if index == len(word):
                return node.end

            ch = word[index]
            if ch == ".":
                for child in node.children.values():
                    if dfs(child , index +1):
                        return True
                return False
            if ch not in node.children :
                return False
            return dfs(node.children[ch] , index+1 )

        return dfs(self,0)
        
        
