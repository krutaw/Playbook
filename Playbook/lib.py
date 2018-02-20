from django.views.generic.list import ListView as DjangoListView

class ListView(DjangoListView):
    '''
    Enhanced ListView which also includes the ``model`` in the context data,
    so that the template has access to its model class.
    '''

    def get_context_data(self):
        '''
        Adds the model to the context data.
        '''
        context          = super(ListView, self).get_context_data()
        context['model'] = self.model
        return context
