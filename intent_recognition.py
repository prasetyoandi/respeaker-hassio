from sentences import sentences

def getIntent(spell) :
    for sentence in sentences :
        for phrase in sentence['phrase'] :
            count = 0
            for word in spell.split(' ') :
                if word in phrase :
                    count = count + 1
            if(count == len(phrase)) :
                return(sentence['event'])
    return None