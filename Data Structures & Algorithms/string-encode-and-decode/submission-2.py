class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res

    def decode(self, s: str) -> List[str]:

        dec , i = [] , 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = s[i:j]
            a = j + 1 
            b = a + int(length)
            dec.append(s[a:b])
            i = b 
        return dec 


            


                    



