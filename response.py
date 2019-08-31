from state import State

class Response:
    def __init__(self, iVerb, f, *args, **kwargs):
        self.iVerb = iVerb
        self.f = f
        self.args = args
        self.kwargs = kwargs
        self.travelTo = None

    def Arg(self, arg):
        return None if arg not in self.kwargs else self.kwargs[arg]

    def ArgStr(self, arg):
        return "" if self.Arg(arg) is None else self.Arg(arg)

    @staticmethod
    def Respond(responses, iVerb, game):
        if type(responses) is Response:
            responses = (responses,)
        for response in responses:
            if response.iVerb == iVerb:
                if response.Arg('condition') is None or response.Arg('condition')(game):
                    m = ""
                    if response.Arg('travelTo') is not None:
                        game.TravelTo(response.ArgStr('travelTo'))
                    if response.Arg('setState') is not None:
                        setStates = response.Arg('setState')
                        if type (setStates[0]) is not tuple:
                            setStates = (setStates, )
                        for setState in setStates:
                            game.state[setState[0]] = setState[1]
                    m += response.ArgStr('message')
                    if response.f is not None:
                        if m != "":
                            m += '\n'
                        m += response.f(game, response.args, response.kwargs)
                    return m

    @staticmethod
    def HasResponse(responses, iVerb):
        if type(responses) is Response:
            responses = (responses,)
        for response in responses:
            if response.iVerb == iVerb and response.f is not None:
                return True

        return False