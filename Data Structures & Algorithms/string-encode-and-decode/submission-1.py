class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        if not strs:
            return ""
        for st in strs:
            res.append(str(len(st)))
            res.append('#')
            res.append(st)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        dec, i = [] , 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            size = int(s[i:j])
            a = j + 1
            b = a + size
            dec.append(s[a:b])
            i=b
        return dec

            


                    



