class Solution(object):
    def __init__(self):
        # max=2,147,483,647
        self.wd = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion",
        }
        self.bases = [10**9, 10**6, 10**3, 10**2, 10]

    def rec(self, num, ans):
        if num < 100:
            if num in self.wd:
                ans += " {}".format(self.wd[num])
            else:
                mod = num%10
                ans += " {} {}".format(self.wd[num-mod], self.wd[mod])
        else:
            for i in xrange(len(self.bases)-1):
                if self.bases[i+1] <= num < self.bases[i]:
                    ans = self.rec(num / self.bases[i+1], ans)
                    ans += " {}".format(self.wd[self.bases[i+1]])
                    mod = num % self.bases[i+1]
                    if mod > 0:
                        ans = self.rec(mod, ans)
                    break
        return ans

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return self.wd[num]

        ans = ""
        if num >= self.bases[0]:
            ans = "{} {}".format(self.wd[num/self.bases[0]], self.wd[self.bases[0]])
            num %= self.bases[0]

        if num == 0:
            return ans

        return self.rec(num, ans).strip()
        
