def longestCommonPrefix(strs):
    if not strs:
        return ""  

    first_str = strs[0]  
    
    for i in range(len(first_str)):  
        char = first_str[i] 
        for word in strs[1:]:  
            if i >= len(word) or word[i] != char:  
                return first_str[:i]  
    return first_str  


