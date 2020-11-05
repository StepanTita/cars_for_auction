import json
import pandas as pd

from django.shortcuts import render

# Create your views here.
import numpy as np
from rest_framework import views, response, renderers, status

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
        data = prepare.prepare_data(pd.DataFrame(dict(serializer.data.items()), index=range(len(serializer.data.items()))))
        result = np.exp(model.predict(data))  # do not forget to take exp (because we used log)

        return response.Response({"price": result})
