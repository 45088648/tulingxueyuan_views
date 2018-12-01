from django.db import models

class ToolingInfo(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID")
    info = models.CharField(max_length=1024,verbose_name="刀具加工信息")
    params = models.CharField(max_length=1024, verbose_name="切削参数")
    data_time = models.DateTimeField(verbose_name="数据时间")
    input_time = models.DateTimeField(verbose_name="数据保存时间")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tooling_info'  # 自定义表名称
        verbose_name = '刀具加工信息表'  # 指定在admin管理界面中显示的名称