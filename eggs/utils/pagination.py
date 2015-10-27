from string import uppercase
import simplejson


class Serialization(object):
    """ handle to post pagination in html, data from mongo"""
    def __init__(self, page_object, model_class):
        self._page_object = page_object
        self._model_class = model_class
        self._paginator = self._page_object.paginator

    def _model_keys(self):
        # in generally,`models` module that yourself define,
        # database table fields is lower
        no_fields = uppercase + '_'
        attrs = self._model_class.__dict__
        return [k for k in attrs.keys() if not k[0] in no_fields and k != 'objects']

    def current_page_number(self):
        return self._page_object.number

    def has_next(self):
        return self._page_object.has_next()

    def has_previous(self):
        return self._page_object.has_previous()

    def start_index(self):
        return self._page_object.start_index()

    def page_range(self):
        return self._paginator.page_range

    def flatten(self, objects):
        iterable = (dict, list, tuple)
        json_type = (int, long, float, bool, basestring, type(None))

        for i, key_or_obj in enumerate(objects):
            if isinstance(objects, dict):
                k = key_or_obj
                v = objects[key_or_obj]
            else:
                k = i
                v = key_or_obj

            if not isinstance(v, iterable):
                if not isinstance(v, json_type):
                    objects[k] = str(v)
            else:
                self.flatten(v)

    def data(self):
        instance_data = []
        keys = self._model_keys()

        for k, item in enumerate(self._page_object.object_list):
            objs = {k: item[k] for k in keys}
            self.flatten(objs)
            instance_data.append(objs)
        return instance_data

    def dumps(self):
        data = {
            'data': self.data(),
            'current_page_number': self.current_page_number(),
            'has_previous': self.has_previous(),
            'has_next': self.has_next(),
            'page_range': self.page_range(),
            'start_index': self.start_index()
        }

        return simplejson.dumps(data)
