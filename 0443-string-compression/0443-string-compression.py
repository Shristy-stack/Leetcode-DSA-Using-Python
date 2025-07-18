class Solution:
    def compress(self, chars: List[str]) -> int:
        idx=0
        i=0
        while i< len(chars):
            ch=chars[i]
            count=0
            while (i< len(chars)) and (chars[i]==ch):
                count+=1
                i+=1
            chars[idx]=ch
            idx+=1
            if count>1:
                count_str=str(count)
                for s in count_str:
                    chars[idx]=s
                    idx+=1
        return idx