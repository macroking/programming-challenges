class BSearch(object):
    def __init__(self, slist):
        self.slist = slist

    def rsearch(self, list, idx0, idxn, val):
        '''
            Recursive approach
        '''

        if (idxn < idx0):
                return None
        else:
            midval = idx0 + ((idxn - idx0) // 2)
    # Compare the search item with middle most value
            print idx0, idxn, midval

            if list[midval] > val:
                return self.rsearch(list, idx0, midval-1,val)
            elif list[midval] < val:
                return self.rsearch(list, midval+1, idxn, val)
            else:
                return midval


    def search(self, data):
        lsize = len(self.slist) - 1
        idx = 0

        while idx <= lsize:
            midval = (idx + lsize) // 2
            print idx, lsize, midval
            if self.slist[midval] == data:
                return midval, data

            if data > self.slist[midval]:
                idx = midval + 1
            else:
                lsize = midval - 1
        if idx > lsize:
            return 'Not Present', data

lst = [2,7,19,34,53,72]
b = BSearch(lst)
ind, dat = b.search(34)
print 'Search data {} is at index {}'.format(dat, ind)
print b.rsearch(lst, 0, len(lst)-1, 34)