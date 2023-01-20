class Arithmetics:
    def __init__(self, data) -> None:
        self.data = data
    def avg(self):
        return sum(self.data)/len(self.data)
    def mean(self):
        return self.avg()
    def median(self):
        le = len(self.data)
        if(le%2==0):
            return (sorted(self.data)[le//2] + sorted(self.data)[le//2-1]) / 2
        else:
            return sorted(self.data)[le//2]
    def mode(self):
        dict = {}
        for i in self.data:
            if i in dict:
                dict[i]+=1
            else:
                dict[i] = 1
        return [k for k,v in dict.items() if v==max(dict.values())]
numbers = [3,7,3,4,5,6,7,8,9]
calculate = Arithmetics(numbers)
print("Average:","%.2f" %calculate.avg())
print("Mean:","%.2f"%calculate.mean())
print("Median:",calculate.median())
print("Mode:",calculate.mode())