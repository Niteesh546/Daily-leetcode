class Solution(object):
    def isValid(self, s):
        hashmap ={
            ')':'(',
            '}':'{',
            ']':'['
        }
        st = [ ]

        for c in s:
            if c not in hashmap:
                st.append(c)
            else:
                if not st :
                    return False
                else:
                    popped = st.pop()
                    if popped != hashmap[c]:
                        return False
        return not st




            



        
        