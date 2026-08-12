class MyHashMap:
    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for maps in self.hashmap:
            if maps[0] == key:
                maps[1] = value
                break
        else:
            self.hashmap.append([key, value])
        

    def get(self, key: int) -> int:
        for maps in self.hashmap:
            if maps[0] == key:
                return maps[1]
        else:
            return - 1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap.pop(i)
                break

        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)