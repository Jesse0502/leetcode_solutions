def ValidAnagram(t,s):
    if len(t) != len(s):
        return False
    return str(sorted(t.lower())) == str(sorted(s.lower()))

print(ValidAnagram("anagram", "ANAGRAM"))