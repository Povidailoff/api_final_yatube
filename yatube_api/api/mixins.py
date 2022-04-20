from rest_framework import mixins, viewsets


class FollowCreateListSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    pass
