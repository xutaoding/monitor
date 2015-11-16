from datetime import datetime
from mongoengine import *
from django.utils.encoding import smart_unicode


class BaseBlockTrade(Document):
    secu = StringField(max_length=12)
    y = StringField(max_length=10)
    typ = StringField()
    uuid = StringField()
    price = StringField()
    volu = StringField()
    amou = StringField()
    bid = StringField()
    c = DictField(default={'szh': '', 'en': '', 'cd': ''})
    sale = StringField(default='')
    buy = StringField(default='')
    stat = IntField(default=2)
    ratio = StringField(default='')
    disc = StringField(default='')
    crt = DateTimeField(default=datetime.now())
    s = StringField()

    def __unicode__(self):
        return smart_unicode(self.sale)

    def update(self, **kwargs):
        print 'he update:', self.pk
        super(BaseBlockTrade, self).update(**kwargs)


