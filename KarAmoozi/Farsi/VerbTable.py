class VTable:
    def __init__(self, verbs, allwords, excepts, operators):
        'verbs is a dictionary of {verb(root): (past, present found, present root),...}'
        self.verbs = verbs
        self.allwords = allwords
        self.exc = excepts
        self.ops = operators
        self.ngpast={}
        self.prefixv = []
        self.compounds = []
        self.incompleteComp = []
        self.pastgroup = []
        self.presentGroup = []
        self.presentsimple = []
        self.removal = []
        
        self.verbcopy = self.verbs.copy()
        

    def start(self):
        for verb in self.verbs:
            self.extractNegatives(verb)
        self.remove()
        for verb in self.verbs:
            self.extractPrefix(verb)
        for verb in self.verbs:
            self.extractCompounds(verb)
        self.remove()
        self.createPastGroup()
        self.createPresentGroup()


    def extractNegatives(self, verb):
        newv=self.createNegList(verb)
        ngs = []
        for nv in newv:
            if nv in self.verbs:
                ngs += [nv]
        if len(ngs) > 0:
            self.removal += ngs
            self.ngpast[verb] = ngs
            self.presentsimple += [self.verbs[verb][1]]

    def remove(self):
        for verb in self.removal:
            if verb in self.verbs:
                del self.verbs[verb]
        
    def createNegList(self, verb):
        if verb[0] == self.ops['alef']:
            newv = [self.ops['nia'] + verb[1:]]
        elif verb[0] == self.ops['aa']:
            newv = [self.ops['nia']+verb[1:], self.ops['ni']+verb[1:], self.ops['na']+verb[1:]]
        else:
            newv = [self.ops['noon'] + verb]
        return newv

    def getPositive(self, nverb):
        index = nverb.find(self.ops['nia'], 0, len(self.ops['nia']))
        if index != -1:
            return [self.ops['alef']+nverb[3:], self.ops['aa']+nverb[3:]]
        index = nverb.find(self.ops['ni'], 0, len(self.ops['ni']))
        if index != -1:
            return [self.ops['aa']+nverb[2:]]
        index = nverb.find(self.ops['na'], 0, len(self.ops['na']))
        if index != -1:
            return [self.ops['aa']+nverb[2:]]
        index = nverb.find(self.ops['noon'], 0, len(self.ops['noon']))
        if index != -1:
            return [nverb[1:]]
        return []

            

    def getVerbPrefixes(self):
        return [self.ops['bar'], self.ops['dar'], self.ops['foroo'], self.ops['faraa']
                , self.ops['baaz'], self.ops['var'], self.ops['va']
                ]
    
    def extractPrefix(self, verb):
        prefixes = self.getVerbPrefixes()
        ngl = self.createNegList(verb)
        flag = 0
        for prefix in prefixes:
            pv = prefix + verb
            if pv in self.verbs:
                flag = 1
                self.prefixv += [(pv, verb, prefix, self.verbs[verb][1], 'p')]
                self.removal += [pv]
            for nv in ngl:
                pnv = prefix + nv
                if pnv in self.verbs:
                    flag = 1
                    self.prefixv += [(prefix+verb, verb, prefix, self.verbs[verb][1], 'n')]
                    self.removal += [pnv]
            
    def extractCompounds(self, verb):
        ngl=self.createNegList(verb)
        flag = 0
        for sv in self.verbs:
            if len(sv) > len(verb):
                index = sv.rfind(verb, len(sv)-len(verb))
                if index != -1:
                    flag = 1
                    if index == 1:
                        self.incompleteComp.append((sv, verb))
                    else:
                        self.compounds.append((sv, verb, sv[:index], self.verbs[verb][1]))
                        self.removal += [sv]
                        
            for nv in ngl:
                if len(sv) > len(nv):
                    index = sv.rfind(nv, len(sv)-len(nv))
                    if index != -1:
                        flag = 1
                        ls = [sv] + self.getPositive(nv)
                        ls.append(sv[:index])
                        ls.append(self.verbs[verb][1])
                        if index == 1:
                            self.incompleteComp.append(tuple(ls))
                        else:
                            self.compounds.append(tuple(ls))
                            self.removal += [sv]

    def createPastGroup(self):
        for verb in self.ngpast:
            past = verb[:-1]
            npast = [pv[:-1] for pv in self.ngpast[verb]]
            rec = {}
            rec['ppast'] = past
            rec['npast'] = npast
            rec['cpast'] = [self.ops['mi'] + past,self.ops['mi'][:-1] + past]
            rec['ncpast'] = [self.ops['nami'] + past, self.ops['nami'][:-1] + past]
            self.pastgroup.append(rec)
        for vgr in self.prefixv:
            verb = vgr[1][:-1]  #the simple past tense
            pref = vgr[2]       #the prefix
            rec = {}
            rec['ppast'] = vgr[0][:-1]
            rec['npast'] = [pref+nv for nv in self.createNegList(verb)]
            rec['cpast'] = [pref + self.ops['mi'] + verb, pref + self.ops['mi'][:-1] + verb]
            rec['ncpast'] = [pref + self.ops['nami'] + verb, pref + self.ops['nami'][:-1] + verb]
            self.pastgroup.append(rec)
        for comv in self.compounds:
            verb = comv[1][:-1]
            prepart = comv[-1]
            rec = {}
            rec['ppast'] = prepart + verb
            rec['npast'] = [prepart+nv for nv in self.createNegList(verb)]
            rec['cpast'] = [prepart + self.ops['mi'] + verb, prepart + self.ops['mi'][:-1] + verb]
            rec['ncpast'] = [prepart + self.ops['nami'] + verb, prepart + self.ops['nami'][:-1] + verb]
            self.pastgroup.append(rec)
        for verb in self.verbs:
            v = verb[:-1]
            rec = {}
            rec['ppast'] = v
            rec['npast'] = [nv for nv in self.createNegList(v)]
            rec['cpast'] = [self.ops['mi'] + v, self.ops['mi'][:-1] + v]
            rec['ncpast'] = [self.ops['nami'] + v, self.ops['nami'][:-1] + v]
            self.pastgroup.append(rec)
            
            
    def createPresentGroup(self):
        for verb in self.presentsimple:
            rec = {}
            rec['ppresent'] = verb
            rec['amr'] = self.ops['beh']+rec['ppresent']
            rec['nahy'] = self.createNegList(rec['ppresent'])
            rec['cpresent'] = [self.ops['mi']+rec['ppresent'], self.ops['mi'][:-1]+rec['ppresent']]
            rec['cnpresent'] = [self.ops['nami']+rec['ppresent'], self.ops['nami'][:-1]+rec['ppresent']]
            self.presentGroup.append(rec)
        for elem in self.prefixv:
            rec = {}
            rec['ppresent'] = elem[2]+elem[3]
            rec['amr'] = elem[2] + self.ops['beh'] + elem[3]
            rec['nahy'] = [elem[2] + nv for nv in self.createNegList(elem[3])]
            rec['cpresent'] = [elem[2]+self.ops['mi']+elem[3], elem[2]+self.ops['mi'][:-1]+elem[3]]
            rec['cnpresent'] = [elem[2]+self.ops['nami']+elem[3], elem[2]+self.ops['nami'][:-1]+elem[3]]
            self.presentGroup.append(rec)    
            
        for elem in self.compounds:
            rec = {}
            rec['ppresent'] = elem[-1]
            rec['amr'] = elem[-2] + self.ops['beh'] + elem[-1]
            rec['nahy'] = [elem[-2] + nv for nv in self.createNegList(elem[-1])]
            rec['cpresent'] = [elem[-2]+self.ops['mi']+elem[-1], elem[-2]+self.ops['mi'][:-1]+elem[-1]]
            rec['cnpresent'] = [elem[-2]+self.ops['nami']+elem[-1], elem[-2]+self.ops['nami'][:-1]+elem[-1]]
            self.presentGroup += [rec]
        vs = self.verbs
        for verb in vs:
            rec = {}
            vp = vs[verb][1]
            rec['ppresent'] = vp
            rec['amr'] = self.ops['beh']+vp
            rec['nahy'] = [nv for nv in self.createNegList(vp)]
            rec['cpresent'] = [self.ops['mi']+vp, self.ops['mi'][:-1]+ vp]
            rec['cnpresent'] = [self.ops['nami']+vp, self.ops['nami'][:-1]+vp]
            self.presentGroup += [rec]
           
