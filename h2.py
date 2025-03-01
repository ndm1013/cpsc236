#Question 3
def sales_tax(sum):
    tax = 0.06
    s_tax = sum * tax
    return s_tax

def total_cost(pretax_total, sales_tax):
    total = pretax_total + sales_tax
    return total

