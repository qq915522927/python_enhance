import gc

def querset_iterator(queryset, chucksize=10000):
    pk = 0
    last_pk = queryset.order_by('-pk')[0]
    queryset.order_by('pk')
    while pk < last_pk:
        for row in queryset.filter(pk__gt=pk)[:chucksize]:
            # 每次读入内存的行数最大为chucksize
            yield row
            pk = row.id
        gc.collect()
        # gc垃圾回收
