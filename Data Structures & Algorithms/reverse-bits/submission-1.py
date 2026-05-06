class Solution:
    def reverseBits(self, n: int) -> int:
        # b=bin(n)[2:]
        # b=b.zfill(32)
        # rev=b[::-1]
        # return int(rev,2)
        
        res=0
        for i in range(32):
            bit=n & 1
            res=(res << 1) | bit
            n=n>>1
        return res
        