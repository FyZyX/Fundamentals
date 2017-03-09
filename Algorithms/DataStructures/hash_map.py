class HashMap:
    def __init__(self):
        self.size = 64
        self.map = [[]] * self.size

    def _pre_hash(self, key):
        hash_key = 0
        for char in str(key):
            hash_key += ord(char)
        return hash_key % self.size

    def __setitem__(self, key, value):
        hash_key = self._pre_hash(key)
        item = (key, value)

        if not self.map[hash_key]:
            self.map[hash_key] = [item]
            return True
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[hash_key].append(item)
            return True

    def __getitem__(self, key):
        hash_key = self._pre_hash(key)

        if self.map[hash_key]:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None

    def __delitem__(self, key):
        hash_key = self._pre_hash(key)

        if not self.map[hash_key]:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True

    def print(self):
        [print(*item) for item in self.map if item]

my_dict = HashMap()
my_dict['tim'] = 12
my_dict['kim'] = 13
my_dict['joe'] = 46
my_dict['sarah'] = 30
print(my_dict['kim'])
my_dict.print()
del my_dict['joe']
my_dict.print()
