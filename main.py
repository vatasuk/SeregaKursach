import pandas as pd
def recomendation():
    genres = {1:'Фантастика',2:'Фентези',3:'Роман'}
    authors = {1:'Айзек Азимов',2:'Лавкрафт',3:'Пушкин'}
    genre = get_user_input('Введите жанр', genres)
    author = get_user_input('Введите автора', authors)
    lenght = float(input('Введите длину'))
    rating = float(input('Введите рейтинг'))
    recomendations = pd.DataFrame()
    df = pd.read_excel('test.xlsx', sheet_name='Лист1')
    df = df.set_index('Объект').T
    df['Желание'] = [genre,author,lenght, rating]
    df.to_excel('DataSet.xlsx')
    df=pd.read_excel('DataSet.xlsx',index_col=0)
    recList=list()
    for row in df:
        k = 0
        corrMatr=df.corrwith(df[row])
        corrMatr=pd.DataFrame(corrMatr)
        tempMatr=corrMatr
        tempMatr=tempMatr.drop([row],axis=0)
        while k != 6:
            name = tempMatr.idxmax().item()
            value = tempMatr[0][tempMatr.idxmax().item()]
            recList.append([row,name,value])
            tempMatr=tempMatr.drop([tempMatr.idxmax().item()],axis=0)
            k += 1
    recomendations=recomendations._append(recList, ignore_index=True)
    recomendations.to_excel('result.xlsx')
    df2 = pd.read_excel("result.xlsx")
    df2_c = df2[df2[0] == "Желание"]
    row = 0
    arr = []
    while row != 6:
        if df2_c[2].values[row] > 0.75:
            arr.append(df2_c[1].values[row])
        row+=1
    df3 = pd.read_excel('test.xlsx')
    df3_c = df3[df3['Жанр'] == genre]
    df3_c = df3_c[df3_c['Автор'] == author]
    row = 0
    while row != len(df3_c):
        for i in range(len(arr)):
           if df3_c['Объект'].values[row] == arr[i]:
               print(arr[i])
        row +=1
def get_user_input(prompt, options):
    while True:
        try:
            user_input = float(input(f"{prompt} {options}: "))
            if user_input in options:
                return user_input
            else:
                print("Некорректный ввод. Попробуйте еще раз.")
        except ValueError:
            print("Введите число.")

recomendation()