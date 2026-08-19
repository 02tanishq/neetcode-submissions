
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def insert(self, word) :
        node = self
        for ch in word :
            if ch not in node.children :
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.insert(w)

        rows = len(board) 
        col= len(board[0])
        path = set()
        res = set()

        def dfs(r,c,word , node):
            if (r <0 or c<0 or  
               r >= rows or c >= col or 
               (r,c) in path or 
               board[r][c] not in node.children ):
                return 

            path.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            dfs(r+1 ,c ,word , node) 
            dfs(r-1 ,c ,word , node) 
            dfs(r ,c +1,word , node) 
            dfs(r ,c-1,word , node) 
            path.remove((r,c))


        for r in range(rows):
            for c in range(col) :
                dfs(r,c,"",root)

        return list(res)


        
            
