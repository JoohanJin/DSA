class TrieNode:
    def __init__(self):
        self.children: list[TrieNode] = [None] * 26 # 26 alphabet
        self.isDone = False # flag indicating the end of each word


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr: TrieNode = self.root
        for char in word:
            i: int = ord(char) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode() # make one more instance
            curr = curr.children[i]
        curr.isDone = True

    def search(self, word: str) -> bool:
        curr: TrieNode = self.root

        for char in word:
            i: int = ord(char) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.isDone
        

    def startsWith(self, prefix: str) -> bool:
        curr: TrieNode = self.root
        for char in prefix:
            i: int = ord(char) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True
