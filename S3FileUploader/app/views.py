# myapp/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import UploadedFile

@csrf_exempt
def read_excel_data(request, file_name):
    try:
        # Retrieve the UploadedFile object using the file name
        uploaded_file = UploadedFile.objects.get(name=file_name)
        file_url = uploaded_file.file.url

        # Read Excel data using pandas
        df = pd.read_csv(file_url)

        # Convert DataFrame to a list of dictionaries
        data = df.to_dict(orient='records')

        return JsonResponse({'success': True, 'data': data})
    except UploadedFile.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'File not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
