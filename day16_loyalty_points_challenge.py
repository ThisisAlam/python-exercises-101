# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
def earn_points(price):
    pts= int(price) * 3
    return pts
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
def tier_label(points):
    if points < 100:
        return "Bronze"
    elif points >= 100 and points <= 499:
        return "Silver"
    else:
        return "Gold"
# 3. Given the hard-coded list `purchases`,
purchases = [3.75, 7.20, 15.99, 9.50, 12.30] 
total_points= 0
#    loop through it, call earn_points() for each amount,
for purchase_price in purchases:
#    and add the result to total_points.
    total_points += earn_points(purchase_price)
# 4. After the loop, call tier_label(total_points)
final_tier = tier_label(int(total_points))
# 5. Print 'Loyalty Summary':
print('Loyalty Summary:')
#       • Total dollars spent
print(f"Total dollars spent: ${sum(purchases)}")
#       • Total points earned
print(f"Total points earned: {total_points}pts")
#       • Final tier
print(f"Final tier: {final_tier}")