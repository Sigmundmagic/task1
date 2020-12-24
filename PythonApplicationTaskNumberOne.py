class rangeForChromosome(): # класс диапазон для хромосомы
    #реализация класса
    def setNumberChromosome(self,numberChromosome):#обрезаем строку, чтобы оставить только номер
        assert type(numberChromosome) is str and numberChromosome is not '' and numberChromosome is not None and numberChromosome.find('chr') is not -1 #проверка на то что переменная не равна пустоте, не равна пустой строке и имеет 'chr'
        numberChromosome = numberChromosome[numberChromosome.find('chr') + 3:]# здесь удаляется 'chr' из строки
        self.numberChromosome = numberChromosome # присваиваем переменной класса значение
    def __init__(self,numberChromosome,beginRead,endRead): # конструктор класса принимает в качестве входных параметров numberChromosome,beginRead,endRead 
        self.setNumberChromosome(numberChromosome)
        self.beginRead = beginRead
        self.endRead = endRead
    def __init__(self,string):
        self.string = string
        self.setNumberChromosome(string.split('\t')[0].strip())
        self.beginRead = int(string.split('\t')[1].strip())
        self.endRead =int(string.split('\t')[2].strip())

    def inRange(self,value):
        assert type(value) is int
        if value >= self.beginRead and value <= self.endRead:
            return True
        else:
            return False

class strFormVCF():
    def __init__(self,string):
        self.string = string
        self.CHROM = string.split('\t')[0].strip()
        self.POS = string.split('\t')[1].strip()


listForResult = []
def findStrInVCF(item):
    global listForResult.append(item)



findStrInVCF('lol')
print(listForResult)

#f = open('1.bed','r')
#line = f.readline()
#itemRange = rangeForChromosome(line.split('\t')[0].strip(),int(line.split('\t')[1].strip()),int(line.split('\t')[2].strip()))
#while line is not '':
    
#f.close()
