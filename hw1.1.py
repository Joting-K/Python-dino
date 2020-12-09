# 買 x1 張全票與 x2 張學生票，而一張全票的售價是 p1 元，一張學生票則是 p2 元。
# 若你拿出 t 元鈔票給櫃臺，請問是否足夠，以及若足夠，櫃臺會找你多少錢？
# 判斷 t 是否足夠支付票價，如果不夠則印出一個 −1；夠則先印出一個錢字號「$」，再印出櫃台找錢的金額，中間不可以有任何其他字元（包括空白字元）。

adult_ticket_quantity = int(input())
adult_ticket_price = int(input())
student_ticket_quantity = int(input())
student_ticket_price = int(input())
money = int(input())
cost = adult_ticket_quantity*adult_ticket_price \
       + student_ticket_quantity*student_ticket_price

if money >= cost:
    print("$"+str(money-cost))
else:
    print("-1")
哈豁
