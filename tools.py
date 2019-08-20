import numpy as np

def get_scoreboard(pth):
    result = list()
    result.append('Numery graczy, którzy do tej pory uzyskali najlepsze wyniki: \n')
    with open(pth,'r') as txt:
        txt = txt.read().split('\n')
        scr = dict()
        for n in [n for n in txt if n != '']:
            tmp = n.split(',')
            scr[tmp[1][4:]]=tmp[0][4:]
        bests = list(scr.keys())
        bests.sort()
        for n in range(10):
            chunk = '{} miejsce: gracz {}'.format(n+1,scr[bests[n]])
            result.append(chunk)
    return '\n'.join(result)

def save_score(pth,nsub,score):
    with open(pth,'a') as txt:
        txt.write('\nSub {},scr {}'.format(nsub,np.round(score,4)))
