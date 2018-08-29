import random
import time

class page:
    def __init__(self, data=None, init_cycle=None):
        self.data = data
        self.init_cycle = init_cycle

class lru_cache:
    # Instantiate cache with empty pages
    def __init__(self, size):
        self.__cache = []
        self.__free_keys = []
        for block_id in range(size+1):
            self.__cache.append(page())
            self.__free_keys.append(block_id)

    def dump_cache(self):
        for page in self.__cache:
            if page.data != None:
                page.data = None
                self.__free_keys.append(self.__cache.index(page))

    # Find the first least recently used page and evict it
    def __evict_page(self):
        # Init by setting the first block of the cache
        evictable_key = 0
        least_recent = self.__cache[0].init_cycle
        #print "Least recent is initially", least_recent


        # Loop through and find which page had been least recently assigned
        for page in self.__cache:
            if page.init_cycle < least_recent:
                evictable_key = self.__cache.index(page)
                least_recent = page.init_cycle
                #print "Least recent is now", least_recent

        # Evict that page and return it to free key pool
        print "Evicting key", evictable_key, "; was written at", least_recent
        self.__cache[evictable_key].data = None
        self.__free_keys.append(evictable_key)

    def insert_page(self, value, clock_cycle):
        try:
            key = self.__free_keys.pop()
        except IndexError:
            print "Cache full, evicting page..."
            self.__evict_page()
            key = self.__free_keys.pop()

        self.__cache[key].data = value
        self.__cache[key].init_cycle = clock_cycle
        print value,"inserted at page", key, "on clock cycle", clock_cycle
        return key

    def free_page(self, key):
        self.__cache[key].data = None

if __name__ == '__main__':
    # Create a cache and start filling it
    lru = lru_cache(10)
    clock_cycle = 0
    while True:
        lru.insert_page(random.randint(1,1000000), clock_cycle)
        clock_cycle += 1
        time.sleep(1)
        # Randomly dump pages to jumble the ordering
        if random.randint(1,5) == 1:
            print "Randomly freeing two pages"
            lru.free_page(random.randint(0,10))
            lru.free_page(random.randint(0,10))
