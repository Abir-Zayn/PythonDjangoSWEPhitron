from django import forms
from first_app.models import studentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = '__all__'
        labels = {
            'name': ' Student Name',
            'roll' : 'Student Roll',
        }
        widgets = {
            'name' : forms.TextInput(),
        }
        help_texts ={
            'name' : "Write your full name",
            
        }
        error_messages= {
            'name': {'required': 'Your name is required'}
        }

# Show the forms fields in the frontend . If show specific fields then declared in fields =['s1','s2'] or else fields = '__all__'
# Label is simillar of HTML Label. To show label match with the modelObject variable and assigning with the name you want to show. Eg 
# labels = {
            # 'name': ' Student Name',
            # 'roll' : 'Student Roll',
        #   }
# 
# 
# 
# 
# 