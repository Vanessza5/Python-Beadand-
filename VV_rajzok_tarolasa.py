class VV_Rajz:
    def __init__(self, nev, rajz):
        self.nev = nev
        self.rajz = rajz

    def megjelenit(self):
        return self.rajz

class AllatRajz(VV_Rajz):
    def __init__(self, nev, rajz):
        super().__init__(nev, rajz)

class ViragRajz(VV_Rajz):
    def __init__(self, nev, rajz):
        super().__init__(nev, rajz)

# Állatok és virágok definiálása osztályokkal
allatok = {
    "kutya": AllatRajz("kutya", r"""
  / \__
 (    @\___
 /         O
/   (_____/
/_____/   U
"""),
    "cica": AllatRajz("cica", r"""
 _
( \
 ) )  _...._  A.-.A
( (  .      \/ , , \
 \ \/       =;  t  /=
  \   \        .--
   \   |...._  / 
   / //     | ||
  /_,))     |_,))
"""),
    "elefánt": AllatRajz("elefánt", r"""
          ___     ___
         /   \~~~/   \
   ,----(     . .     )
  /      \___     ___/
 /|          (\  |(
^  \    /___\  \_|
    |__|     |__|
""")
}

viragok = {
    "rózsa": ViragRajz("rózsa", r"""
         _______
        /_     _\
       /   ----  \
      /      /    \
     /      /      \ 
     \      \      /
      \____  \____/
           \ \
           -\ \
             \ \    ______
              \ \  /     /
       _____   \ \/_____/
       \    \ -/ /
        \____\/ /-
            -/ /
             \ \
             / /
            / /-    
         - / /
          / /
          \ \
           \ \ 
"""),
    "pitypang": ViragRajz("pitypang", r"""
    \\|//
     |
     :            \\|//
                    |
                    :
        \\|//                ||/_
          |                   /--
          :        _\||      /
                   --\
                      \
                            _\||       
                            --\
                               \
                                    "  "  "
                                  " \  |  / "
                                 *  --(:)--  *
		                  " /  |  \ "
                                    .. | ..
                                  |\   |   /|
                                  /_ \ | / _\
                                    /_\|/_\
"""),
    "napraforgó": ViragRajz("napraforgó", r"""
                     -       -
            -  -   -   -   -   -    -
           -     - -     *     - -   -
            -       \    |    /      -
          - ------   \   |   /     ----- -
         -        -   \  |  /    -        -
         -         - .:::::::. -         -
           -         :::::::::         -
            >--------:::::::::--------<
          -         -:::::::::-        - 
         -        -  ':::::::'  -        -   
          - -----     /  |  \     ------ -
            -        /   |   \      -
           -        /    |    \      -
            -      -     *     -     -
              -  -  -   - -   -  -  -
                      -     -

""")
}

def VV_rajz_valasztas(choice_type, choice):
    if choice_type == "állatokat":
        rajz = allatok.get(choice)
        if rajz:
            return rajz.megjelenit()
        else:
            return "Nincs ilyen állat az adatbázisban."
    elif choice_type == "virágokat":
        rajz = viragok.get(choice)
        if rajz:
            return rajz.megjelenit()
        else:
            return "Nincs ilyen virág az adatbázisban."
    else:
        return "Érvénytelen választás."

# Új lista a véletlenszerű kiválasztáshoz
allatok_lista = list(allatok.keys())
viragok_lista = list(viragok.keys())