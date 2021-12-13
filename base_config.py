
x = 38
y = 15
#x = 0
#y = 0


runde = 1
inventar = ['Taschentuch']
lebens_energie = 100

legende = {'~': 'Wasser', 'X': 'Du'}


optionen = {'n': "gehe nach Norden", 'o': "gehe nach Osten",
            's': "gehe nach Süden", 'w': "gehe nach Westen", 'z': 'zeige Inventar', 'q': "aufgeben"}

inventar_optionen = {'bx': 'benutze x',
                     'ex': 'entferne x', 'bxmy': 'benutze x mit y'}

random_event_probability = 0.2 # 1/5


topographic_map = '''
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww_.,-'=_.-'-..wwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww._.-'             '-._wwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww_.-':_.-'                      '-._wwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwww_.-'                                   '-._.'-._wwww
wwwwwwwwwwwwwwwwwwww.-'.-,'                                                '-.w
wwwwwwwwwwwwwwwwwwww'-._                       /\   /\                    _.-'w
wwwwwwwwwwwwwwwwwwwwwwww'-.           (*)(*)  /  \ /  \                ._'wwwww
wwwwwwwwwwwwwwwwwwwwwwwwwww'-._         ((      /\ /           _.'-._,-'wwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'-._            /  \ /      _.-'wwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww.-'               /     .'wwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww.-'                 /    '-._.,.wwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'-._               /           '-._wwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'-._          /                '.wwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww .'          /                '-._wwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww_.-'           /  (*)(*)           _.'wwwwww
wwwwwwww<WRACK>wwwwwwwwwwwwwwwwwww'-._           /    (  )           '-._-'-.ww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'-._      /                        _.-'ww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww '-.    / /\            _.-"._,'wwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww_.'   / /\ /\         '.wwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww_.-'-._.-'     / /  \  \          '-._._wwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwww_.-'              /                         '-.wwww
wwwwwwwwwwwwwwwwwwwwwwwww.-'              .-'-'-._                        '-.ww
wwwwwwwwwwwwwwwwwwwwwww_.'         _.-'-.-'wwwwww '.             _.'-.-'._ .'ww
wwwwwwwwwwwwww.-'=_.'-'         .-'wwwwwwwwwwwww.-'          _.-'wwwwwwwww'.'ww
wwwwwwwwwww_.-'                 '-._,.-'._.----'            '_wwwwwwwwwwwwwwwww
wwwwwwwww.'                                                    '-._wwwwwwwwwwww
wwwwwwwww'-.- = .-'.                                               '=..wwwwwwww
wwwwwwwwwwwwwwwwwww'._                                                 '-.wwwww
wwwwwwwwwwwwwwwwwwwwww:_                                            _.-'.-'wwww
wwwwwwwwwwwwwwwwwwwwwww "._,-'.-'._    .-`-._;'-._.='._          .-'wwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'-_."wwwwwwwwwwwwww '-._:'=__.'wwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
'''

visual_map = '''
x                    ~        ~          ~            ~        ~              x
          ~                                  _.,-'=_.-'-._  ~        ~         
                  ~     ~           ~   ._.-'             '-._   ~             
                               _.-':_.-'                      '-._   ~     ~   
                           _.-'                                   '-._.'-._    
            ~       .-'.-,'                                                '-. 
                    '-._                       /\   /\                    _.-' 
          ~             '-.           (*)(*)  /  \ /  \                ._'     
                    ~      '-._         ((      /\ (           _.'-._,-'       
                               '-._            /  \ )      _.-'                
                           ~     .-'               (     .'              ~     
                                .-'                 )    '-._.,.            ~  
                ~               '-._               /           '-._  ~         
                                    '-._          (                '.   ~      
              ~                 ~      .'          )                '-._       
                                   _.-'           /  (*)(*)           _.'   ~  
        <WRACK>       Δ   ~       '-._           /    (  )           '-._-'-.  
                                      '-._      (                        _.-'  
           ~          ~ ~           ~     '-.    ) /\            _.-"._,'      
                           ~              _.'   / /\ /\         '.  ~          
                                _.-'-._.-'     / /  \  \          '-._._       
                   ~        _.-'              /                         '-. ~  
                         .-'              .-'-'-._                        '-.  
          ~            _.'         _.-'-.-'~   ~  '.             _.'-.-'._ .'  
              .-'=_.'-'         .-'  ~   ~   _ _.-'          _.-'     ~   '.'  
           _.-'                 '-._,.-'._.-'               '_   ~       ~     
         .'                                                    '-._   ~    ~   
         '-.- = .-'.                                               '=._        
                   '._                                                 '-.     
                 ~    :_                                            _.-'.-' ~  
              ~     ~   "._,-'.-'._    .-`-._;'-._.='._          .-'  ~        
                             ~     '-_."      ~    ~   '-._:'=__.'       ~     
x                   ~     ~      ~        ~     ~        ~          ~    ~    x
'''
