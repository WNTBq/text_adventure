from Event import Event


events = {}
events[1] = """
Unterwegs im Golf von Mexiko gerät dein Schiff in einen furchtbaren Sturm.
In deiner Kabine suchst Du Schutz vor der Gicht, doch plötzlich gibt es einen Wassereinbruch ..
Du wachst am nächsten morgen an einem Strand auf.
Die Sonne brennt und du hast durst, dein Mund ist trocken, - dein Kleidung zerfetzt.
Hinter Dir töst die Brandung.
"""

events[27] = '''
Du hörst in der Ferne ein rythmisches Trommelgeräusch und gehst dem nach und beobachtest die Situation hinter einen Felsvorsprung.
Auf der Ostseite der Insel landen Bote an. Vor deinen Augen wird ein junger Mann niedergestreckt und von hinten erdolcht. 
Sie zerteilen die Leiche und verteilen die Stücke untereinander!
Es sind Kanibalen !
'''



random_events = { 
    'w' : 
    [
        Event('Autsch!  Du wurdest von einer schlange gebissen (-5)','subtractLifeEnergy',{'value':-5},0.2),
        Event('Du findest rote Beeren. Möchtest Du Sie essen?','decision',{'value':-10,'message:':'Oh die waren giftig !!'},0.2),
        Event('Du findest gelbe Beeren. Möchtest Du Sie essen?','decision',{'value':5,'message:':'Lecker'},0.2),
        Event('Du findest gelbe Pilze. Möchtest Du Sie essen?','decision',{'value':5, 'message:':'Der Hunger treibt es rein'},0.2)
    ],
    'b' :
    [
        Event('Autsch!  Du bist auf einen See-Igel getretten (-3)','subtractLifeEnergy',{'value':-3},0.2),
    ]
        
    }




