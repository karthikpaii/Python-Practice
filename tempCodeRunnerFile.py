if(len(s1)!=len(s2)):
            return False
        elif (len(set(s1))!=len(set(s2))):
            return False
        else:
            return True