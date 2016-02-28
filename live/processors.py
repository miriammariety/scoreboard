from live.models import Cluster


def cluster_processor(request):
    return {'clusters': Cluster.objects.all()}