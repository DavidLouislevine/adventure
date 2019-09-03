from adventure.location import Location
from cia.cia_verb import go

def GoBuilding(game, *args, **kwargs):
    if game.state.location==game.world.locations['ON A BUSY STREET']:
        game.GoTo('LOBBY')
        if not game.Has('BADGE'):
            game.GoTo('LOBBY')
            return ""
        else:
            m = game.Look()
            m += '\nTHE DOOR MAN LOOKS AT MY BADGE AND THEN THROWS ME OUT.\n'
            game.GoTo('STREET')
            m += game.Look()
            return m

locations = (
    Location('STREET', 'ON A BUSY STREET', (0, 0, 0, 0)),
    Location('VISITOR', 'IN A VISITOR\'S ROOM', (0,  0,  'LOBBY',  0)),
    Location('LOBBY', 'IN THE LOBBY OF THE BUILDING', ('STREET', 0, 'ANTEROOM', 'VISITOR'), go(ifHas='BADGE', goTo='STREET', message="THE DOOR MAN LOOKS AT MY BADGE AND THEN THROWS ME OUT.")),
    Location('ANTEROOM', 'IN A DINGY ANTE ROOM', (0, 0, 0, 'LOBBY')),
    Location('CEO', 'IN THE COMPANY PRESIDENT\'S OFFICE', (0, 0, 0, 'ANTEROOM')),
    Location('CUBICLE', 'IN A SMALL SOUND PROOFED CUBICLE', (0, 'PLAIN', 0, 0)),
    Location('SECURITY', 'IN A SECURITY OFFICE', (0, 0, 'HALLWAY', 0)),
    Location('HALLWAY', 'IN A SMALL HALLWAY', (0, 'CAFETERIA', 'ELEVATOR', 'SECURITY')),
    Location('ELEVATOR', 'IN A SMALL ROOM', ('LOBBY', 0, 0, 0)),
    Location('CORRIDOR', 'IN A SHORT CORRIDOR', (0, 'SIDE', 0, 'ELEVATOR'), go(ifNotHas='CARD', goTo='ELEVATOR', message="THE GUARD LOOKS AT ME SUSPICIOUSLY, THEN THROWS ME BACK.")),
    Location('METAL', 'IN A HALLWAY MADE OF METAL', (0, 0, 'PLAIN', 'CORRIDOR')),
    Location('PLAIN', 'IN A SMALL PLAIN ROOM', ('CUBICLE', 0, 0, 'METAL')),
    Location('CLOSET', 'IN A MAINTENANCE CLOSET', (0, 0, 'CAFETERIA', 0)),
    Location('CAFETERIA', 'IN A CAFETERIA', ('HALLWAY', 0, 0, 0)),
    Location('SIDE', 'IN A SIDE CORRIDOR', ('CORRIDOR', 0, 'GENERATOR', 0)),
    Location('GENERATOR', 'IN A POWER GENERATOR ROOM', (0, 0, 0, 'SIDE')),
    Location('BASEMENT', 'IN A BASEMENT BELOW THE CHUTE', (0, 0, 'COMPLEX', 0)),
    Location('COMPLEX', 'IN THE ENTRANCE TO THE SECRET COMPLEX', (0, 'LEDGE', 'MONITORING', 'BASEMENT')),
    Location('MONITORING', 'IN A SECRET MONITORING ROOM', (0, 0, 0, 'COMPLEX')),
    Location('LEDGE', 'ON A LEDGE IN FRONT OF A METAL PIT 1000\'S OF FEET DEEP', ('COMPLEX', 0, 0, 0)),
    Location('PIT', 'ON THE OTHER SIDE OF THE PIT', ( 0, 0, 'LONG', 0)),
    Location('LONG', 'IN A LONG CORRIDOR', (0, 'NARROW', 'ROOM', 'PIT')),
    Location('ROOM', 'IN A LARGE ROOM', (0, 'EXAM', 0, 'LONG')),
    Location('LAB', 'IN A SECRET LABORATORY', (0, 0, 'NARROW', 0)),
    Location('NARROW', 'IN A NARROW CROSS CORRIDOR', ('LONG', 0, 0, 'LAB')),
    Location('EXAM', 'IN A CROSS EXAMINATION ROOM', ('LARGE', 'CHIEF', 0, 0)),
    Location('BATHROOM', 'IN A SMALL BATHROOM', (0, 0, 'CHIEF', 0)),
    Location('CHIEF', 'IN THE OFFICE OF THE CHIEF OF CHAOS', ('EXAM', 'END', 0, 'BATHROOM')),
    Location('CONTROL', 'IN THE CHAOS CONTROL ROOM', (0, 0, 'END', 0)),
    Location('END', 'NEAR THE END OF THE COMPLEX', ('CHIEF', 0, 0, 'CONTROL'))
)
