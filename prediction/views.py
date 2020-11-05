# Create your views here.
import numpy as np
import pandas as pd
from rest_framework import views, response, renderers, status
from rest_framework.reverse import reverse

from cars_from_auction import settings
from prediction import serializers, context, prepare
from prediction.serializers import PredictionSerializer

ctx = context.Context()


class PredictView(views.APIView):
    serializer_class = serializers.PredictionSerializer
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]

    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        if not serializer.is_valid():
            response.Response(status=status.HTTP_400_BAD_REQUEST)

        model = ctx.get_model()
        df = pd.DataFrame(dict(serializer.data.items()), index=range(1))
        data = prepare.prepare_data(df)
        result = np.exp(model.predict(data))  # do not forget to take exp (because we used log)

        return response.Response({"price": result})
        # return redirect(reverse('price-view'), request=request)


class PriceView(views.APIView):
    serializer_class = serializers.PriceSerializer
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]

    def get(self, request, *args, **kwargs):
        return response.Response({
            "prediction": request.build_absolute_uri(reverse('prediction-view')),
            "version": request.build_absolute_uri(reverse('version-view')),
        })


class VersionView(views.APIView):
    renderer_classes = [renderers.BrowsableAPIRenderer, renderers.JSONRenderer]

    def get(self, *args, **kwargs):
        return response.Response({'model': settings.MODEL, 'version': settings.VERSION})
