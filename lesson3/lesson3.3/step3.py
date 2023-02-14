class Model:
    def query(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)

    def __str__(self):
        ans = 'Model'
        fields = []
        for field, value in self.__dict__.items():
            fields.append(f'{field} = {value}')
        if fields:
            return  ans + ': ' + ', '.join(fields)
        return ans
model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)