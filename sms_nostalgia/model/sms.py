import logging
log = logging.getLogger(__name__)



class Sms(object):


    def __init__(self, sender, content, type, display_name=None):

        self.sender = sender
        self.content = content
        self.type = type
        self.display_name = display_name

    def as_text(self):
        if self.display_name:
            return '%s: %s; %s' % (self.type, self.display_name, self.content)
        else:
            return '%s: %s; %s' % (self.type, self.sender, self.content)

