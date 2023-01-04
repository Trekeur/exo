def miroir(mot): 
    m=list(mot)
    m.reverse()
    return ''.join(m)

print(miroir('bonjour  '))