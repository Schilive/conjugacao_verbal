# Local que possui os verbos irregulares ou com particípios irregulares

terconj = [[['tenho', 'tens', 'tem', 'temos', 'tendes', 'têm'],
             ['tivera', 'tiveras', 'tivera', 'tivéramos', 'tivéreis', 'tiveram'],
             ['tive', 'tiveste', 'teve', 'tivemos', 'tivestes', 'tiveram'],
             ['tinha', 'tinhas', 'tinha', 'tínhamos', 'tínheis', 'tinham'],
             ['terei', 'terás', 'terá', 'teremos', 'tereis', 'terão'],
             ['teria', 'terias', 'teria', 'teríamos', 'teríeis', 'teriam'],
            ['indicativo', 'pretérito-imperfeito'],
            ['indicativo', 'presente'],
            ['indicativo', 'futuro-do-presente'],
            ['indicativo', 'futuro-do-pretérito']], # Indicativo
           [['tenha', 'tenhas', 'tenha', 'tenhamos', 'tenhais', 'tenham'],
            ['tivesse', 'tivesses', 'tivesse', 'tivéssemos', 'tivésseis', 'tivessem'],
            ['tiver', 'tiveres', 'tiver', 'tivermos', 'tiverdes', 'tiveram'],
            ['subjuntivo', 'pretérito-imperfeito'],
            ['subjuntivo', 'presente'],
            ['subjuntivo', 'futuro']], # Subjuntivo
            [[None, 'tem', 'tenha', 'tenhamos', 'tende', 'tenham'], [None, 'tenhas', 'tenha', 'tenhamos', 'tenhais', 'tenham']], # Imperativo
            ['tendo'], # Gerundio
            [['ter'], ['ter', 'teres', 'ter', 'termos', 'terdes', 'terem']]]
terpart = ['tido', "tida", "tidos", "tidas"]

abrirpart = ['aberto', 'aberta', 'abertos', 'abertas']

haverconj = [[['hei', 'hás', 'há', 'havemos', 'haveis', 'hão'],
             ['houvera', 'houveras', 'houvera', 'houvéramos', 'houvéreis', 'houveram'],
             ['houve', 'houveste', 'houve', 'houvemos', 'houvestes', 'houveram'],
             ['havia', 'havias', 'havia', 'havíamos', 'havíeis', 'haviam'],
             ['haverei', 'haverás', 'haverá', 'haveremos', 'havereis', 'haverão'],
             ['haveria', 'haverias', 'haveria', 'haveríamos', 'haveríeis', 'haveriam'],
            ['indicativo', 'pretérito-imperfeito'],
            ['indicativo', 'presente'],
            ['indicativo', 'futuro-do-presente'],
            ['indicativo', 'futuro-do-pretérito']],
           [['haja', 'hajas', 'haja', 'hajamos', 'hajais', 'hajam'],
            ['houvesse', 'houvesses', 'houvesse', 'houvéssemos', 'houvésseis', 'houvessem'],
            ['houver', 'houveres', 'houver', 'houvermos', 'houverdes', 'houverem'],
            ['subjuntivo', 'pretérito-imperfeito'],
            ['subjuntivo', 'presente'],
            ['subjuntivo', 'futuro']],
            [[None, 'há', 'haja', 'hajamos', 'havei', 'hajam'], [None, 'hajas', 'haja', 'hajamos', 'hajais', 'hajam']],
            ['havendo'],
            [['haver'], ['haver', 'haveres', 'haver', 'havermos', 'haverdes', 'haverem']]]
haverpart = ["havido", "havida", "havidos", "havidas"]

porconj = [[['ponho', 'pões', 'põe', 'pomos', 'pondes', 'põem'],
             ['pusera', 'puseras', 'pusera', 'puséramos', 'puséreis', 'puseram'],
             ['pus', 'puseste', 'pôs', 'pusemos', 'pusestes', 'puseram'],
             ['punha', 'punhas', 'punha', 'púnhamos', 'púnheis', 'punham'],
             ['porei', 'porás', 'porá', 'poremos', 'poreis', 'porão'],
             ['poria', 'porias', 'poria', 'poríamos', 'poríeis', 'poriam'],
            ['indicativo', 'pretérito-imperfeito'],
            ['indicativo', 'presente'],
            ['indicativo', 'futuro-do-presente'],
            ['indicativo', 'futuro-do-pretérito']],
           [['ponha', 'ponhas', 'ponha', 'ponhamos', 'ponhais', 'ponham'],
            ['pusesse', 'pusesses', 'pusesse', 'puséssemos', 'pusésseis', 'pusessem'],
            ['puser', 'puseres', 'puser', 'pusermos', 'puserdes', 'puseram'],
            ['subjuntivo', 'pretérito-imperfeito'],
            ['subjuntivo', 'presente'],
            ['subjuntivo', 'futuro']],
            [[None, 'põe', 'ponha', 'ponhamos', 'ponde', 'ponham'], [None, 'ponhas', 'ponha', 'ponhamos', 'ponhais', 'ponham']],
            ['tendo'],
            [['pondo'], ['pôr', 'pores', 'pôr', 'pormos', 'pordes', 'porem']]]
porpart = ["posto", "posta", "postos", "postas"]

listirrverb = ['ter', 1, terconj, terpart, 'abrir', 0, abrirpart, "haver", 1, haverconj, haverpart, "pôr", 1, porconj, porpart]
# List de verbos irregulares (irregular verbs list)
