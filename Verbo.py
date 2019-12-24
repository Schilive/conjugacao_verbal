class Verbo:
    __regular = True
    __part = 0
    __verbo = str()
    __rad = str()  # Radical
    __term = 0  # Terminação (End)
    __conj = [[[['o', 'o', 'o', 'ponho'], ['as', 'es', 'es', 'pões'], ['a', 'e', 'e', 'põe'], ['amos', 'emos', 'imos', 'pomos'], ['ais', 'eis', 'is', 'pondes'], ['am', 'em', 'em', 'põem']],
            [['ara', 'era', 'ira', 'pusera'], ['aras', 'eras', 'iras', 'puseras'], ['ara', 'era', 'ira', 'pusera'], ['áramos', 'êramos', 'íramos', 'puséramos'], ['áreis', 'êreis', 'íreis', 'puséreis'], ['aram', 'eram', 'iram', 'puseram']],
            [['ei', 'i', 'i', 'pus'], ['aste', 'este', 'iste', 'puseste'], ['ou', 'eu', 'iu', 'pôs'], ['ámos', 'emos', 'imos', 'pusemos'], ['astes', 'estes', 'istes', 'pusestes'], ['aram', 'eram', 'iram', 'puseram']],
            [['ava', 'ia', 'ia', 'punha'], ['avas', 'ias', 'ias', 'punhas'], ['ava', 'ia', 'ia', 'punha'], ['ávamos', 'íamos', 'íamos', 'púnhamos'], ['áveis', 'íeis', 'íeis', 'púnheis'], ['avam', 'iam', 'iam', 'punham']],
            [['arei', 'erei', 'irei', 'porei'], ['arás', 'erás', 'irás', 'porás'], ['ará', 'erá', 'irá', 'porá'], ['aremos', 'eremos', 'iremos', 'poremos'], ['areis', 'ereis', 'ireis', 'poreis'], ['arão', 'erão', 'irão', 'porão']],
            [['aria', 'eria', 'iria', 'poria'], ['arias', 'erias', 'irias', 'porias'], ['aria', 'eria', 'iria', 'poria'], ['aríamos', 'eríamos', 'iríamos', 'poríamos'], ['aríeis', 'eríeis', 'iríeis', 'poríeis'], ['ariam', 'eriam', 'iriam', 'poriam']],
             ['indicativo', 'pretérito-imperfeito'],
             ['indicativo', 'presente'],
             ['indicativo', 'futuro-do-presente'],
             ['indicativo', 'futuro-do-pretérito']],  # INDICATIVO
            [[['e', 'a', 'a', 'ponha'], ['es', 'as', 'as', 'ponhas'], ['e', 'a', 'a', 'ponha'], ['emos', 'amos', 'amos', 'ponhamos'], ['eis', 'ais', 'ais', 'ponhais'], ['em', 'am', 'am', 'ponham']],
             [['asse', 'esse', 'isse', 'pusesse'], ['asses', 'esses', 'isses', 'pusesses'], ['asse', 'esse', 'isse', 'pusesse'], ['ássemos', 'êssemos', 'íssemos', 'puséssemos'], ['ásseis', 'êsseis', 'ísseis', 'pusésseis'], ['assem', 'essem', 'issem', 'pusessem']],
             [['ar', 'er', 'ir', 'puser'], ['ares', 'eres', 'ires', 'puseres'], ['ar', 'er', 'ir', 'puser'], ['armos', 'ermos', 'irmos', 'pusermos'], ['ardes', 'erdes', 'irdes', 'puserdes'], ['arem', 'erem', 'irem', 'puserem']],
             ['subjuntivo', 'pretérito-imperfeito'],
             ['subjuntivo', 'presente'],
             ['subjuntivo', 'futuro']], # SUBJUNTIVO
            [[[None, None, None], ['a', 'e', 'e', 'põe'], ['e', 'a', 'a', 'ponha'], ['emos', 'amos', 'amos', 'ponhamos'], ['ai', 'ei', 'i', 'ponde'], ['em', 'am', 'am', 'ponham']],
             [[None, None, None], ['es', 'as', 'as', 'ponhas'], ['e', 'a', 'a', 'ponha'], ['emos', 'amos', 'amos', 'ponhamos'], ['eis', 'ais', 'ais', 'ponhais'], ['em', 'am', 'am', 'ponham']]],  # IMPERATIVO
            ['ando', 'endo', 'indo', 'pondo'],  # GERÚNDIO
            [['ar', 'er', 'ir'], ['', 'es', '', 'mos', 'des', 'em']]]  # INFINITIVO
    __modolist = ['indicativo', 'subjuntivo', 'imperativo', 'gerúndio', 'infinitivo', "particípio"]
    __nomelist = ['presente', 'pretérito-mais-que-perfeito', 'pretérito-perfeito', 'pretérito-imperfeito', 'futuro-do-presente',
                'futuro-do-pretérito', 'pretérito-mais-que-perfeito-composto', 'pretérito-perfeito-composto',
                'futuro-do-presente-composto', 'futuro-do-pretérito-composto', 'positivo', 'negativo', 'pessoal', 'immpessoal', 'futuro-composto', 'futuro']
    __nomelistsubj = ['presente', 'pretérito-imperfeito', 'futuro', 'pretérito-mais-que-perfeito-composto', 'pretérito-perfeito-composto', 'futuro-composto']
    __ppoalist = ['me', 'te', 'o', 'a', 'se', 'lhe', 'nos', 'vos', 'os', 'as', 'lhes', 'mo', 'ma', 'mos', 'mas',
                  'to', 'ta', 'tos', 'tas', 'lho', 'lha', 'lhos', 'lhas', 'no-lo', 'no-la', 'no-los', 'no-las', 'vo-lo',
                  'vo-la', 'vo-los', 'vo-las', 'lhe-lo', 'lhe-la', 'lhe-los', 'lhe-las']
    __oaosaslist = ['o', 'a', 'os', 'as']

    def __init__(self, verbo):
        if str(verbo[-3:]).lower() == 'ear':
            self.__conj = [[[['io', 'io', 'io'], ['ias', 'ies', 'ies'], ['ia', 'ie', 'ie'], ['amos', 'emos', 'imos'], ['ais', 'eis', 'is'], ['iam', 'iem', 'iem']],
            [['ara', 'era', 'ira'], ['aras', 'eras', 'iras'], ['ara', 'era', 'ira'], ['áramos', 'êramos', 'íramos'], ['áreis', 'êreis', 'íreis'], ['aram', 'eram', 'iram']],
            [['ei', 'i', 'i'], ['aste', 'este', 'iste'], ['ou', 'eu', 'iu'], ['ámos', 'emos', 'imos'], ['astes', 'estes', 'istes'], ['aram', 'eram', 'iram']],
            [['ava', 'ia', 'ia'], ['avas', 'ias', 'ias'], ['ava', 'ia', 'ia'], ['ávamos', 'íamos', 'íamos'], ['áveis', 'íeis', 'íeis'], ['avam', 'iam', 'iam']],
            [['arei', 'erei', 'irei'], ['arás', 'erás', 'irás'], ['ará', 'erá', 'irá'], ['aremos', 'eremos', 'iremos'], ['areis', 'ereis', 'ireis'], ['arão', 'erão', 'irão']],
            [['aria', 'eria', 'iria'], ['arias', 'erias', 'irias'], ['aria', 'eria', 'iria'], ['aríamos', 'eríamos', 'iríamos'], ['aríeis', 'eríeis', 'iríeis'], ['ariam', 'eriam', 'iriam']],
             ['indicativo', 'pretérito-imperfeito'],
             ['indicativo', 'presente'],
             ['indicativo', 'futuro-do-presente'],
             ['indicativo', 'futuro-do-pretérito']],  # INDICATIVO
            [[['ie', 'ia', 'ia'], ['ies', 'ias', 'ias'], ['ie', 'ia', 'ia'], ['emos', 'amos', 'amos'], ['eis', 'ais', 'ais'], ['iem', 'iam', 'iam']],
             [['asse', 'esse', 'isse'], ['asses', 'esses', 'isses'], ['asse', 'esse', 'isse'], ['ássemos', 'êssemos', 'íssemos'], ['ásseis', 'êsseis', 'ísseis'], ['assem', 'essem', 'issem']],
             [['ar', 'er', 'ir'], ['ares', 'eres', 'ires'], ['ar', 'er', 'ir'], ['armos', 'ermos', 'irmos'], ['ardes', 'erdes', 'irdes'], ['arem', 'erem', 'irem']],
             ['subjuntivo', 'pretérito-imperfeito'],
             ['subjuntivo', 'presente'],
             ['subjuntivo', 'futuro']], # SUBJUNTIVO
            [[[None, None, None], ['ia', 'ie', 'e'], ['ie', 'ia', 'ia'], ['emos', 'amos', 'amos'], ['ai', 'ei', 'i'], ['iem', 'iam', 'iam']],
             [[None, None, None], ['es', 'as', 'as'], ['e', 'a', 'a'], ['emos', 'amos', 'amos'], ['eis', 'ais', 'ais'], ['em', 'am', 'am']]],  # IMPERATIVO
            ['ando', 'endo', 'indo'],  # GERÚNDIO
            [['ar', 'er', 'ir'], ['', 'es', '', 'mos', 'des', 'em']]]  # INFINITIVO

        from Verboirre import listirrverb
        if str(verbo).lower() in listirrverb:
            if listirrverb[listirrverb.index(str(verbo)) + 1] == 1:
                self.__conj = listirrverb[listirrverb.index(str(verbo)) + 2]
                self.__part = listirrverb[listirrverb.index(str(verbo)) + 3]
                self.__regular = False
            elif listirrverb[listirrverb.index(str(verbo)) + 1] == 0:
                self.__part = listirrverb[listirrverb.index(str(verbo)) + 2]

        if str(verbo).isalpha(): self.__verbo = str(verbo).lower()
        else: raise ValueError('Variable VERB must be string')
        if self.__regular:
            term = (self.__verbo[-2:]).lower()
            if term == "ar":
                self.__term = 0
            elif term == "er":
                self.__term = 1
            elif term == "ir":
                self.__term = 2
            elif str(self.__verbo[-3:]).lower() == "por" or str(self.__verbo[-3:]).lower() == "pôr":
                self.__term = 3
            else:
                raise ValueError('Variable VERBO must end -ar, -er, -ir or -por')
            self.__rad = str(self.__verbo[0:-2]).lower()
        if self.__part == 0:
            if self.__term == 1:
                self.__part = self.__rad + 'ido'
            elif self.__term == 0 or self.__term == 2:
                self.__part = str(self.__verbo[:-1] + 'do')
            else:
                self.__part = self.__rad + 'posto'
        if self.__term == 3:
            self.__regular = False
            self.__rad = self.__verbo[:-3]
            self.__part = self.__rad + 'posto'

    def conjugar(self, modo, nome, num):
        # Averiguação de variáveis (Variables checking)
        conjgd = str()
        if not str(modo).lower() in self.__modolist:
            raise ValueError('Variable MODO must be: indicativo, subjuntivo, imperativo, gerúndio, infinitivo or particípio')
        modonum = self.__modolist.index(modo)
        if modonum == 3 or modonum == 4: # 3: Gerúndio. 4: Infinitivo
            if modonum == 3:
                if not self.__regular and self.__term != 3:
                    return self.__conj[3][0]
                elif not self.__regular and self.__term == 3:
                    return self.__rad + self.__conj[3][3]
                return str(self.__rad + str(self.__conj[3][self.__term]))
            else:
                if str(nome).lower() == 'impessoal':
                    return str(self.__verbo).lower()
                else:
                    if not self.__regular and self.__term != 3:
                        return self.__conj[4][1][num]
                    if str(self.__verbo).lower() == 'pôr' and not (num == 0 or num == 2):
                        return 'por' + str(self.__conj[4][1][num])
                    return self.__verbo + str(self.__conj[4][1][num])
        if not num <= 5 and num >= 0:
            raise ValueError('Variable NUM must be between 0 and 5')
        if modonum == 5:
            if num == 0:
                return self.__part
            elif num == 1:
                return self.__part[:-1] + 'a'
            elif num == 2:
                return self.__part + 's'
            elif num == 3:
                return self.__part[:-1] + 'as'
            else:
                raise ValueError("The variable NUM must be between 0 and 3")
        if not str(nome).lower() in self.__nomelist:
            raise ValueError('The variable NOME must exist in NOMELIST')
        # Conjugação (conjugation)
        modonum = self.__modolist.index(modo)
        nomenum = self.__nomelist.index(nome)
        if modonum == 1:
            nomenum = self.__nomelistsubj.index(nome)
        elif modonum == 2:
            if str(nome).lower() == 'positivo':
                nomenum = 0
            elif str(nome).lower() == 'negativo':
                nomenum = 1

        if modonum == 2 and num == 0:
            return ''
        elif not self.__regular and self.__term == 3: # Verbos terminados em -por
            if not str(nome)[-8:] == 'composto':
                return self.__rad + str(self.__conj[modonum][nomenum][num][3])
            else:
                conjter = Verbo('ter').conjugar(self.__conj[modonum][nomenum][0], self.__conj[modonum][nomenum][1], num)
                conjgd = conjter + ' ' + self.__part
        elif str(nome)[-8:] == 'composto':
            conjter = Verbo('ter').conjugar(self.__conj[modonum][nomenum][0], self.__conj[modonum][nomenum][1], num)
            conjgd = conjter + ' ' + self.__part
        elif self.__regular and self.__term != 3 and modonum == 0:
            conjgd = self.__rad + self.__conj[modonum][nomenum][num][self.__term]
        elif self.__regular and self.__term != 3 and modonum == 1:
            conjgd = self.__rad + str(self.__conj[1][nomenum][num][self.__term])
        elif self.__regular and self.__term != 3 and modonum == 2:
            if str(nome).lower() == 'positivo':
                conjgd = self.__rad + str(self.__conj[2][0][num][self.__term])
            else:
                conjgd = self.__rad + str(self.__conj[2][1][num][self.__term])
        elif not self.__regular and self.__term != 3:
            conjgd = str(self.__conj[modonum][nomenum][num])
        else:
            raise ValueError('The system has a bug')
        if self.__regular and (self.__rad[-1] == 'c' or self.__rad[-1] == 'g' or self.__rad[-1] == 'ç') and conjgd[len(self.__rad)] == 'e' and self.__term == 0:
            if self.__rad[-1] == 'c':
                conjgd = self.__rad[:-1] + 'qu' + conjgd[len(self.__rad):]
            elif self.__rad[-1] == 'g':
                conjgd = self.__rad[:-1] + 'gu' + conjgd[len(self.__rad):]
            else:
                conjgd = self.__rad[:-1] + 'c' + conjgd[len(self.__rad):]
        elif self.__regular and (self.__rad[-1] == 'c' or self.__rad[-1] == 'g' or (self.__rad[-2] == 'g' and self.__rad[-1] == 'u')) and (conjgd[len(self.__rad)] == 'o' or conjgd[len(self.__rad)] == 'a') and (self.__term == 1 or self.__term == 2):
            if self.__rad[-1] == 'c':
                conjgd = self.__rad[:-1] + 'ç' + conjgd[len(self.__rad):]
            elif self.__rad[-1] == 'g':
                conjgd = self.__rad[:-1] + 'j' + conjgd[len(self.__rad):]
            else:
                conjgd = self.__rad[:-2] + 'g' + conjgd[len(self.__rad):]

        return conjgd

    def posppoa(self, conj, ppoa, posicao):  # Posicionar pronome pessoal oblíquo átono
        if str(ppoa).lower() in self.__ppoalist:
            poscnd = 0
            ppoa = str(ppoa).lower()
            posicao = str(posicao).lower()
            oaosas = False
            if ppoa in self.__oaosaslist:
                oaosas = True

            if posicao == 'próclise':
                try:
                    conj =  str(self.conjugar(conj[0], conj[1], conj[2])).lower()
                except:
                    raise ValueError('The variable CONJ must be a list, being its order: \'modo\', \'nome\', \'número\'')
                poscnd = ppoa + ' ' + conj
            elif posicao == 'ênclise':
                try:
                    conj = str(self.conjugar(conj[0], conj[1], conj[2])).lower()
                except:
                    raise ValueError('The variable CONJ must be a list, being its order: \'modo\', \'nome\', \'número\'')
                if (conj[-1:] == 'm' or conj[-2:] == 'ão' or conj[-2:] == 'õe') and oaosas:
                    poscnd = conj + '-n' + ppoa
                elif (conj[-1:] == 'r' or conj[-1:] == 's' or conj[-1:] == 'z') and oaosas:
                    if conj[-2] == 'a':
                        poscnd = conj[:-2] + 'á-l' + ppoa
                    elif conj[-2] == 'e':
                        poscnd = conj[:-2] + 'ê-l' + ppoa
                    elif conj[-2] == 'o':
                        poscnd = conj[:-2] + 'ô-l' + ppoa
                    else:
                        poscnd = conj[:-1] + '-l' + ppoa
                elif conj[-3:] == 'mos' and (ppoa == 'nos' or ppoa == 'vos'):
                    poscnd = conj[:-1] + '-' + ppoa
                else:
                    poscnd = conj + '-' + ppoa
            elif posicao == 'mesóclise':
                if not ((str(conj[0]).lower() + str(conj[1]).lower()) == 'indicativofuturo-do-presente' or (str(conj[0]) + str(conj[1])) == 'indicativofuturo-do-pretérito'):
                    raise ValueError('Mesóclise can only be used if the verb\'s conjugation is Futuro do Indicativo or Futuro do Pretérito do Indicativo')

                try:
                    conj = self.conjugar(conj[0], conj[1], conj[2])
                except:
                    raise ValueError('The variable CONJ must be a list, being its order: \'modo\', \'nome\', \'número\'')
                if not oaosas:
                    poscnd = conj[:len(self.__verbo)] + '-' + ppoa + '-' + conj[len(self.__verbo):]
                else:
                    if self.__verbo[-2] == 'a':
                        poscnd = self.__verbo[:-2] + 'á-l' + ppoa + '-' + conj[len(self.__verbo):]
                    elif self.__verbo[-2] == 'e':
                        poscnd = self.__verbo[:-2] + 'ê-l' + ppoa + '-' + conj[len(self.__verbo):]
                    elif self.__verbo[-2] == 'o':
                        poscnd = self.__verbo[:-2] + 'ô-l' + ppoa + '-' + conj[len(self.__verbo):]
                    else:
                        poscnd = self.__verbo[:-1] + '-l' + ppoa + '-' + conj[len(self.__verbo):]
        else:
            raise ValueError('Variable PPOA must be a \'pronome pessoal oblíquo átono\'. And variable POSICAO must be: '
                             'próclise (before), ênclise (after) or mesóclise (middle).')
        return poscnd

    def getStatus(self):
        return [self.__verbo, self.__rad, self.__term, self.__part]




