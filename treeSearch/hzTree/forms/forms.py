from django import forms
from django.forms import NumberInput, TextInput, Select, CheckboxSelectMultiple

BLOOM_COLOR_CONDITION_CHOICES = (
    ('白', '白色'),
    ('红', '红色'),
    ('黄', '黄色'),
    ('紫', '紫色'),
    ('绿', '绿色'),
)

FRUIT_COLOR_CONDITION_CHOICES = (
    ('白', '白色'),
    ('黄', '黄色'),
    ('红', '红色'),
    ('紫', '紫色'),
)

LEAF_COLOR_CONDITION_CHOICES = (
    ('绿', '绿色'),
    ('黄', '黄色'),
    ('红', '红色'),
    ('紫', '紫色'),
    ('橙', '橙色'),
)

MONTHS_CHOICES = (
    ('任意', '任意'),
    ('1月', '1月'),
    ('2月', '2月'),
    ('3月', '3月'),
    ('4月', '4月'),
    ('5月', '5月'),
    ('6月', '6月'),
    ('7月', '7月'),
    ('8月', '8月'),
    ('9月', '9月'),
    ('10月', '10月'),
    ('11月', '11月'),
    ('12月', '12月'),
)

TREE_TYPE_CHOICES = (
    ('乔木','乔木'),
    ('小乔木','小乔木'),
    ('灌木','灌木'),
)

LEAF_TYPE_CHOICES = (
    ('常绿或落叶', '常绿或落叶'),
    ('落叶', '落叶'),
    ('常绿', '常绿'),
)

VALUE_CHOICES = (
    ('观花', '观花'),
    ('观叶', '观叶'),   
    ('观果', '观果'),
    ('观树形', '观树形'),
    ('观树干', '观枝干'),
    ('观树根', '观树根'),
)

SHAPE_CHOICES = (
    ('卵', '(广)卵形'),
    ('塔', '尖塔形'),
    ('锥', '圆锥形'),
    ('伞', '伞形'),
    ('柱','圆柱形'),
    ('球','圆球形'),
)

SOIL_CHOICES = (
    ('任意土质','任意土质'),
    ('酸','酸性土'),
    ('中','中性土'),
    ('碱','碱性土'),
)

POLLUTION_CHOICES = (
    ('烟尘','烟尘大'),
    ('有害气体','气体污染大'),
    # ('风','风大'),
)
class QueryUserForm(forms.Form):
    queryContent = forms.CharField(
        required=False,
        widget=forms.TextInput)

    tree_type_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TREE_TYPE_CHOICES)
    
    leaf_type_condition = forms.ChoiceField(
        choices=LEAF_TYPE_CHOICES,
        widget=forms.Select)

    tree_value_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=VALUE_CHOICES,)

    tree_shape_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=SHAPE_CHOICES)
    
    soil_condition = forms.ChoiceField(
        widget=forms.Select,
        choices=SOIL_CHOICES)

    pollution_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=POLLUTION_CHOICES)

    bloom_color_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=BLOOM_COLOR_CONDITION_CHOICES)

    fruit_color_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FRUIT_COLOR_CONDITION_CHOICES)

    bloom_date_condition = forms.ChoiceField(
        widget=forms.Select,
        choices=MONTHS_CHOICES)
    
    fruit_date_condition = forms.ChoiceField(
        widget=forms.Select,
        choices=MONTHS_CHOICES)

    leaf_color_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=LEAF_COLOR_CONDITION_CHOICES)