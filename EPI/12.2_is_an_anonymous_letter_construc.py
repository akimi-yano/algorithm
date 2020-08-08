#  12.2  is an anonymous letter constructible ? 

# letter 
# magazine 

import collections

def constructible(letter,magazine):
    l_d = {}
    m_d = {}
    for l in letter:
        if l not  in l_d:
            l_d[l]=1
        else:
            l_d[l]+=1
    for m in magazine:
        if m not in m_d:
            m_d[m]=1
        else:
            m_d[m]+=1
    for k,v in l_d.items():
        if k in m_d and v<=m_d[k]:
            pass
        else:
            return False
    return True
print(constructible("aaabbbccc","aaabbccc"))

# optimization  
def is_letter_constructible_from_magazine(letter_text,magazine_text):
    char_frequency_for_letter =  collections.Counter(letter_text)
    
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c]-=1
            if char_frequency_for_letter[c]==0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    return True
    return not char_frequency_for_letter




# shorter pythonic solution
def is_letter_constructible_from_magazine_pythonic(letter_text,magazine_text):
    return (not collections.Counter(letter_text)-collections.Counter(magazine_text))

print(is_letter_constructible_from_magazine_pythonic("aaabbbccc","aaabbbccc"))