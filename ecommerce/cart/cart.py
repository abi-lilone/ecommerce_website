
class Cart ():

    def __init__(self, request):
       
        # return or get existing session

        self.session = request.session
    
        cart = self.session.get('session_key')

        # make a new session for new user

        if 'session_key' not in request.session:

            cart = self.session['session_key'] = {}
        
        self.cart = cart